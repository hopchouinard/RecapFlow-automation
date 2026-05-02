00:03:21 - Paul Miller
Hey, Marc.

00:03:24 - Marc Juretus
What do say, Paul?

00:03:25 - Marc Juretus
How you doing, mate?

00:03:26 - Paul Miller
Good, good.

00:03:28 - Paul Miller
I'm just a viewer today.

00:03:30 - Paul Miller
Brandon is back.

00:03:31 - Marc Juretus
Oh, our keeper's back, huh?

00:03:33 - Paul Miller
Yeah.

00:03:34 - Paul Miller
How are you going up there?

00:03:36 - Marc Juretus
Pretty good.

00:03:37 - Marc Juretus
It's about 6 p.m.

00:03:38 - Marc Juretus
I'm in the Philly area, so I know you all show you, right?

00:03:42 - Paul Miller
In New Zealand.

00:03:43 - Paul Miller
New Zealand.

00:03:43 - Marc Juretus
No, I'm sorry.

00:03:44 - Marc Juretus
Okay.

00:03:47 - Marc Juretus
What time is it?

00:03:48 - Marc Juretus
About 9 a.m., 10 a.m.?

00:03:49 - Paul Miller
It's 10 o'clock in the morning, so my day's only just starting.

00:03:53 - Paul Miller
It's a blue sky day in the middle of winter, so, well, towards the end of winter now.

00:03:58 - Paul Miller
We're nearly in spring, so...

00:04:01 - Paul Miller
Hey, Andrew.

00:04:03 - Paul Miller
Hey, Andrew.

00:04:04 - Marc Juretus
Hey, how's it going?

00:04:07 - Andrew Nanton
Oh, Marc, was thinking about you the other day, because I remember mentioning on one of the previous chats that it looked like NAN was kind of the front runner for visual, you know, tool builder kind of stuff.

00:04:23 - Andrew Nanton
But I did see that, I think it's called FlowWise.

00:04:27 - Paul Miller
Yeah.

00:04:29 - Andrew Nanton
Which is another one that I checked out a while ago, because it ultimately produces, it's more of a Python based tool, rather than JavaScript, which it seems like most of the other tools are pretty JavaScript focused.

00:04:42 - Andrew Nanton
And I guess they very recently got bought by Workday.

00:04:48 - Andrew Nanton
Having used Workday, I'm not sure that's a great endorsement.

00:04:52 - Marc Juretus
That's what we have at my hospital.

00:04:54 - Marc Juretus
Yeah.

00:04:57 - Andrew Nanton
So, but I mean, that should give them plenty of funding.

00:04:59 - Andrew Nanton
And they...

00:04:59 - Andrew Nanton
We just released a version 3 that looks like it might be worth a look.

00:05:05 - Andrew Nanton
I guess that one's still alive.

00:05:06 - Andrew Nanton
I thought it had sort of disappeared into the background with some of these other tools, but it looks like maybe it's still alive and kicking.

00:05:13 - Marc Juretus
Well, guy in my job mentioned, if we talked about it on the call, did we talk about Opal?

00:05:19 - Marc Juretus
That's Google's version of N8N?

00:05:21 - Marc Juretus
Is that true?

00:05:23 - Marc Juretus
Okay.

00:05:24 - Marc Juretus
Somebody mentioned it and that they liked it, but I think what I recall is that they were saying it's still pretty rough around the edges, but it looked promising.

00:05:33 - Andrew Nanton
If my off-the-top-of-the-head recollection is correct, that's, for some reason, the impression that I have.

00:05:40 - Paul Miller
Yeah, it's a bit early on for Opal.

00:05:42 - Marc Juretus
Yeah, I was thinking if I did have any potential clients, if you will, for whatever real estate, this and that, it is a great idea to do the flow in N8N just for proof of concept before you get into some serious, you know, customization, if that's what doing.

00:06:00 - Paul Miller
Yeah, I'm heavily getting into N8N, so I've got my own privately hosted one, so I've stuck it on a droplet, and then I've put it alongside a MongoDB database, and then I'm building some sort of core preferred concept projects on it, but it's going really well.

00:06:28 - Paul Miller
I'm enjoying it, because I just don't have time to build out a big back end for proof of concepts, and I need to spend as much time with the client and on the front end to get them excited, and it's the way to go.

00:06:44 - Marc Juretus
Yeah, agree.

00:06:45 - Marc Juretus
One of my reasons was to learn the frameworks at its core, that I know both options.

00:06:52 - Marc Juretus
I couldn't get to ADK.

00:06:54 - Marc Juretus
had some issues with that, so I rewrote that fantasy tool now in LangFlow, so it's just about done.

00:06:59 - Marc Juretus
then.

00:07:00 - Marc Juretus
So now I'll probably go to any.

00:07:02 - Marc Juretus
And yeah, it's a back end at FastAPI with Superbase.

00:07:06 - Marc Juretus
And then the front end is Next.js.

00:07:08 - Marc Juretus
So I may pull it up today.

00:07:10 - Marc Juretus
I have it, but it's now emailing me its lineup for the season coming up.

00:07:14 - Marc Juretus
So we're just about there.

00:07:16 - Paul Miller
You're ready for the season.

00:07:18 - Marc Juretus
One thing that sucks with Langchain, though, is there's always dependency conflicts.

00:07:23 - Marc Juretus
And then you got to let Cursor, and they're so annoying, you got to let Cursor find out, okay, you need this version with this version and requirements file.

00:07:35 - Marc Juretus
Are you using UV for dependency management?

00:07:40 - Marc Juretus
No, I'm just using just the Python environment variable.

00:07:43 - Marc Juretus
I should use, I know UV, I just didn't use it in this project.

00:07:48 - Andrew Nanton
It might help.

00:07:50 - Paul Miller
Yeah, it's good suggestion, Andrew.

00:07:54 - Paul Miller
Gosh, it saved me.

00:07:56 - Paul Miller
It's so elegant, the way it deals with it.

00:07:59 - Paul Miller
I just don't get

00:08:01 - Marc Juretus
Yeah, I said I really have a lot of those issues.

00:08:05 - Marc Juretus
It's always with Langchain and dependencies.

00:08:07 - Marc Juretus
Like, for example, I can't even use Langsmith with this Langflow project I have.

00:08:11 - Marc Juretus
Every time I try to bring it in, so I'd like to see the visualization and the flow, it just chokes out.

00:08:16 - Marc Juretus
And I was like, you know what, I don't need Langsmith that bad.

00:08:19 - Marc Juretus
It's working fine, man.

00:08:21 - Paul Miller
Yeah.

00:08:25 - Andrew Nanton
And, you know, your statement made me realize I misspoke.

00:08:29 - Andrew Nanton
It is Langflow, the one you're already using, that's more Python-based.

00:08:32 - Andrew Nanton
The other one, Flow-wise, is another, like, TypeScript sort of thingy that's more, maybe a little bit more like Node.js.

00:08:42 - Andrew Nanton
But still pretty interesting.

00:08:45 - Marc Juretus
Yeah.

00:08:46 - Marc Juretus
Yeah, Langflow, you have the nodes and it goes from node to node to node.

00:08:49 - Marc Juretus
It's basically the same as Crew AI.

00:08:50 - Marc Juretus
If you have a flow, Crew AI or Langflow is the way to go.

00:08:53 - Marc Juretus
But if you're just doing a standard chat, like, you could just use Langchain.

00:08:56 - Marc Juretus
There's no reason, you don't need no complex flow at all.

00:09:04 - Andrew Nanton
He's alive.

00:09:05 - Andrew Nanton
I am alive.

00:09:07 - Brandon Hancock
All fingers, all digits.

00:09:08 - Paul Miller
They're all here.

00:09:09 - Brandon Hancock
The sharks, the fish, they didn't get them.

00:09:12 - Brandon Hancock
Feels good to feels good to be back.

00:09:14 - Brandon Hancock
I've I've missed you guys.

00:09:18 - Paul Miller
Thank you.

00:09:19 - Brandon Hancock
Also, once again, for to Paul for for holding down the fort.

00:09:24 - Brandon Hancock
Yeah, thank you.

00:09:26 - Brandon Hancock
You're that you are the man.

00:09:28 - Paul Miller
Well, you're welcome.

00:09:30 - Brandon Hancock
Um, let's see.

00:09:31 - Brandon Hancock
Let's get this all moved around and set up.

00:09:37 - Brandon Hancock
And yes.

00:09:39 - Brandon Hancock
Yeah, we'll just we'll go ahead and kick things off, guys.

00:09:41 - Brandon Hancock
I know.

00:09:42 - Brandon Hancock
I know.

00:09:44 - Brandon Hancock
I think, yeah, definitely.

00:09:45 - Brandon Hancock
I see the little I think a few are people on the call today.

00:09:49 - Brandon Hancock
Got to get back to more content.

00:09:51 - Brandon Hancock
So quick all around updates.

00:09:53 - Brandon Hancock
So hit you on diving real fast.

00:09:56 - Brandon Hancock
And then I'll go back into coding.

00:09:58 - Brandon Hancock
Diving.

00:09:58 - Brandon Hancock
Diving.

00:09:58 - Brandon Hancock
One of the coolest.

00:10:00 - Brandon Hancock
Most experiences ever.

00:10:02 - Brandon Hancock
Absolutely love it.

00:10:03 - Brandon Hancock
We did night diving, scuba diving, snorkeling, night snorkeling.

00:10:08 - Brandon Hancock
Loved every single one of them.

00:10:09 - Brandon Hancock
The only one I will never do again is night snorkeling, because you literally just walk into the ocean, and it just tripped me out.

00:10:18 - Brandon Hancock
So many big fish, and I was like, I just don't like this.

00:10:21 - Brandon Hancock
I got a good thing going.

00:10:22 - Brandon Hancock
Why am I offering myself up as fish food?

00:10:26 - Brandon Hancock
So probably won't do that one again for a very long time.

00:10:29 - Brandon Hancock
So that was a ton of fun.

00:10:32 - Brandon Hancock
A ton of updates for you guys on CodeSide.

00:10:35 - Brandon Hancock
So YouTube had a ton of videos in the pipeline, but wasn't able to get those out before leaving.

00:10:42 - Brandon Hancock
So really cool ones.

00:10:44 - Brandon Hancock
I don't know if you guys have got to check them out yet or not.

00:10:46 - Brandon Hancock
The Presentify creator, awesome guy.

00:10:49 - Brandon Hancock
It was really cool to hear exactly how he's launched multiple profitable SaaS startups, and exactly how he did it, literally step by step.

00:10:59 - Brandon Hancock
It was insane.

00:11:00 - Brandon Hancock
Sanely helpful that he just, like, didn't hold anything back.

00:11:02 - Brandon Hancock
That one was awesome.

00:11:04 - Brandon Hancock
Did an 80K video for you guys.

00:11:07 - Brandon Hancock
That one is, like, 40-plus hours of work and trying to figure out how everything works.

00:11:12 - Brandon Hancock
So, yeah, that one is definitely a huge time saver.

00:11:15 - Brandon Hancock
Other cool update for you guys.

00:11:18 - Brandon Hancock
While two updates while videos have been a little bit slow.

00:11:21 - Brandon Hancock
Update one.

00:11:22 - Brandon Hancock
Last week, I got to actually fly out to San Francisco for a Google competition.

00:11:27 - Brandon Hancock
Let me actually show this to you guys.

00:11:31 - Brandon Hancock
Fake off.

00:11:32 - Brandon Hancock
So, I will be a part.

00:11:35 - Brandon Hancock
I'll share this video in the chat.

00:11:37 - Brandon Hancock
Share.

00:11:41 - Brandon Hancock
But, yeah.

00:11:41 - Brandon Hancock
So, I got to, I think you guys can see it.

00:11:43 - Brandon Hancock
But Google does this thing called, like, an AI agent challenge.

00:11:47 - Brandon Hancock
So, you, and I'll drop a link in the chat.

00:11:49 - Brandon Hancock
But, basically, like, it's like a top chef, but for coding.

00:11:53 - Brandon Hancock
So, you go and you build with 80K.

00:11:56 - Brandon Hancock
You have five hours to build something.

00:11:58 - Brandon Hancock
real good.

00:11:59 - Brandon Hancock
Yeah.

00:11:59 - Brandon Hancock
And...

00:12:00 - Brandon Hancock
And yeah, it was, it was all around super awesome.

00:12:03 - Brandon Hancock
So can't announce what happened yet.

00:12:05 - Brandon Hancock
But just know, I went and a ton of fun.

00:12:09 - Brandon Hancock
And yeah, I mean, all around, it was just it was an awesome experience.

00:12:13 - Brandon Hancock
Coding in your bedroom or your room.

00:12:15 - Brandon Hancock
Awesome.

00:12:16 - Brandon Hancock
Coding with a camera three inches from your face, your brain just turns off.

00:12:20 - Brandon Hancock
So it was super stressful, but had a great time.

00:12:24 - Brandon Hancock
And then cool, my most important update for you guys.

00:12:28 - Brandon Hancock
Drum roll.

00:12:30 - Brandon Hancock
Okay, ShipKit.

00:12:32 - Brandon Hancock
It is, it is free launch starts tomorrow.

00:12:35 - Brandon Hancock
So pumped for this.

00:12:37 - Brandon Hancock
Went ahead and we, we've been cruising on it.

00:12:43 - Brandon Hancock
Bastian has been helping out.

00:12:44 - Brandon Hancock
A few other developers have been helping out, have made an insane amount of progress on ShipKit.

00:12:49 - Brandon Hancock
I'm happy to answer questions.

00:12:51 - Brandon Hancock
I'll have this video.

00:12:52 - Brandon Hancock
have an updated video on the landing page that'll come out late tonight, early tomorrow morning.

00:12:57 - Brandon Hancock
So yeah, it's not 100% ready.

00:13:00 - Brandon Hancock
for pre-purchase and everything or pre-order, but it will be tomorrow.

00:13:04 - Brandon Hancock
So yeah, all around have absolutely loved it.

00:13:07 - Brandon Hancock
I have a ton of, you'll see in the video on the landing page, but it walks through all the different templates, what do they do, how they work, and what's going to be included in the course.

00:13:18 - Brandon Hancock
So yeah, there's so much.

00:13:19 - Brandon Hancock
It keeps growing.

00:13:21 - Brandon Hancock
I keep adding more stuff because I'm like, man, there's just so many cool things that I want you guys to be able to do, but very, very pumped with progress on this one.

00:13:28 - Brandon Hancock
So yeah, just, just need more time, but this is what I've been focusing on a hundred percent.

00:13:33 - Brandon Hancock
And then final, final update.

00:13:35 - Brandon Hancock
I have a video coming up for you tomorrow that goes along with the, the pre-launch and just so you guys can see it.

00:13:42 - Brandon Hancock
It's already, it's been done for like two weeks.

00:13:44 - Brandon Hancock
I've just been waiting for, um, for this video to go live.

00:13:47 - Brandon Hancock
But, um, I mean, heck, if you guys want to go ahead and watch it, I'll just drop it right now.

00:13:52 - Brandon Hancock
Um, cause it is done.

00:13:53 - Brandon Hancock
But basically I walk you guys through the, like how to actually use.

00:14:00 - Brandon Hancock
So cursor and just how to code in the new agentic paradigm.

00:14:05 - Brandon Hancock
So I walk through exactly step by step how to do it.

00:14:07 - Brandon Hancock
So it doesn't have a thumbnail or anything right now.

00:14:09 - Brandon Hancock
It will tomorrow once, you know, it's coupled with a prelaunch.

00:14:12 - Brandon Hancock
So yeah, absolutely awesome.

00:14:14 - Brandon Hancock
Awesome time.

00:14:15 - Brandon Hancock
But yeah, so we'll get back to you guys, though.

00:14:19 - Brandon Hancock
So if you guys have any questions on literally anything, I guess we'll do our normal drop a question in the chat.

00:14:25 - Brandon Hancock
Happy to dive into it.

00:14:26 - Brandon Hancock
And then we'll just go around the room.

00:14:27 - Brandon Hancock
I'd love to hear all the amazing things you guys have been up to while I've been out and about.

00:14:33 - Brandon Hancock
And Paul, I think you have the first question.

00:14:36 - Brandon Hancock
So I'll definitely dive into yours first.

00:14:40 - Brandon Hancock
So do you ask all those 80 quake?

00:14:43 - Brandon Hancock
Yeah.

00:14:43 - Brandon Hancock
So asked so many questions to Google.

00:14:47 - Brandon Hancock
So a few ones, a few major ones, like I just wanted to understand what they're doing next.

00:14:53 - Brandon Hancock
And the biggest thing is just like, I complained a lot.

00:14:58 - Brandon Hancock
Unlike a lot of friction area.

00:15:00 - Brandon Hancock
That was like, it's very hard for, for example, that last video I made, it's very hard for people to use deployed agents in Next.js.

00:15:09 - Brandon Hancock
And like, right now, would I recommend people to do it?

00:15:13 - Brandon Hancock
I mean, eh, not really, because it's very hard and shared a lot of ways that they could fix it.

00:15:20 - Brandon Hancock
Like, for example, Vercel AI SDK, you just install it, boom, you're talking with AI agents or, you know, you're talking with AI.

00:15:28 - Brandon Hancock
So they literally have listened to everything.

00:15:32 - Brandon Hancock
The lead project manager, she'll actually be coming on the channel here at the very end of the month and sharing more of the roadmap with you guys.

00:15:40 - Brandon Hancock
So that'll be, that'll be pretty cool.

00:15:41 - Brandon Hancock
But yeah, I've been nothing but a complainer.

00:15:44 - Brandon Hancock
I've been like very excited, but like, I, you know, I'm going to complain because I want it to be better.

00:15:49 - Brandon Hancock
So, and also, if you guys have complaints too, please send them to me so I can pass them along because they, they want to know what we don't like.

00:15:57 - Brandon Hancock
So it's been a really cool, really cool thing.

00:16:00 - Brandon Hancock
And, yeah, Paul, can dive into ShipKit real fast.

00:16:05 - Brandon Hancock
Yeah, so let's click the button.

00:16:09 - Brandon Hancock
Okay, so, yeah, so here's exactly what comes with ShipKit.

00:16:15 - Brandon Hancock
So what I've tried to do is multiple things at the same time.

00:16:20 - Brandon Hancock
One, I've tried to aggregate what are all the most common types of AI applications that I have been asked to be, like, paid to build.

00:16:30 - Brandon Hancock
It comes down to just, like, regular chat applications, rag applications, and agent applications.

00:16:36 - Brandon Hancock
So for each one of those project types, there's a template.

00:16:40 - Brandon Hancock
There's a simple template and a SaaS template.

00:16:42 - Brandon Hancock
So what that looks like, just, like, we can just get our hands dirty real fast.

00:16:46 - Brandon Hancock
Is this the right page?

00:16:48 - Brandon Hancock
Sorry, I have too many coding windows.

00:16:51 - Brandon Hancock
I'll just open it up.

00:16:53 - Brandon Hancock
Oh, so you guys can see it.

00:16:54 - Brandon Hancock
Sorry, one second.

00:16:56 - Brandon Hancock
ShipKit.

00:16:58 - Brandon Hancock
Let me, um.

00:17:00 - Brandon Hancock
I have like 12 cursor windows open, so it's taking a second.

00:17:05 - Brandon Hancock
But yeah, so inside of ShipKit, what that looks like is there are six templates total to where there's a simple and SaaS version of everything.

00:17:17 - Brandon Hancock
The simple is like the best way to get to just play around with the technology.

00:17:20 - Brandon Hancock
The SaaS is like, oh, you're actually trying to make money on this?

00:17:23 - Brandon Hancock
Cool.

00:17:23 - Brandon Hancock
Added in all the additional features, functionalities that you need to just like instantly spin up a SaaS version of an application.

00:17:32 - Brandon Hancock
What's really cool, though, is everything is AI first.

00:17:37 - Brandon Hancock
So for example, if you wanted to, if you're trying to spin up the chat SaaS application, what you would do, I'll just actually show you guys really fast so you guys can see it in action.

00:17:50 - Brandon Hancock
We'll go back, CD, Scratch.

00:17:52 - Brandon Hancock
So what you'll be able to do going forward is you'll be able to do shipkit.ai.

00:17:58 - Brandon Hancock
There's actually a CLI.

00:18:00 - Brandon Hancock
You get to do like demo chat.

00:18:01 - Brandon Hancock
You get to pick the type of application you want.

00:18:04 - Brandon Hancock
Let's just do the simple one for ease.

00:18:06 - Brandon Hancock
And what this will do is actually locally clone the application to your computer.

00:18:10 - Brandon Hancock
You get to open it up.

00:18:13 - Brandon Hancock
We'll open it up in here.

00:18:15 - Brandon Hancock
I just want to show you guys how cool it is because we're doing everything locally.

00:18:20 - Brandon Hancock
We're using AI first for everything.

00:18:22 - Brandon Hancock
So it comes with all the MCP servers that I use for development.

00:18:25 - Brandon Hancock
And what I wanted to do is to make this the easiest application or easiest product that you guys have ever used.

00:18:33 - Brandon Hancock
So you can say, so instead of you having to like old school learning, you're reading a document and then clicking around on the other screen.

00:18:43 - Brandon Hancock
No, we have AI agents for everything.

00:18:46 - Brandon Hancock
So this is just like the quickest one.

00:18:47 - Brandon Hancock
So like set up, like to actually set up your project.

00:18:50 - Brandon Hancock
We have a setup file that will literally step-by-step walk you through everything you need to do one step at a time.

00:18:59 - Brandon Hancock
So it gives you a road.

00:19:00 - Brandon Hancock
So tells you that you're ready.

00:19:02 - Brandon Hancock
We'll say we're ready.

00:19:03 - Brandon Hancock
And this is just an example of like, instead of you manually, like you guys are all pros.

00:19:08 - Brandon Hancock
So you, this part won't affect you guys, but like setting up your environment.

00:19:12 - Brandon Hancock
That's a huge issue for a lot of people.

00:19:13 - Brandon Hancock
Well, why have you do it?

00:19:15 - Brandon Hancock
Let's just have agents actually verify your system is set up properly.

00:19:19 - Brandon Hancock
Let's make sure that all your environment variables are set up correctly.

00:19:22 - Brandon Hancock
So it's just going to check everything for you, it up.

00:19:24 - Brandon Hancock
So like you just add every step along the journey from idea to production application.

00:19:29 - Brandon Hancock
Try to incorporate templates to make it as, as easy as possible.

00:19:33 - Brandon Hancock
So yeah, agents just do the work.

00:19:35 - Brandon Hancock
You just say go and it does it for you.

00:19:37 - Brandon Hancock
So that's what's just been trying to make it as smooth and as seamless for you guys as possible.

00:19:43 - Brandon Hancock
And then when it comes to setting up your backend, it literally just tells you exactly go here, click this button, click this.

00:19:48 - Brandon Hancock
Oh, cool.

00:19:49 - Brandon Hancock
I can verify what it did for you.

00:19:51 - Brandon Hancock
So that's kind of the paradigm that we're doing for, for literally everything.

00:19:56 - Brandon Hancock
And then outside of that, we just open up.

00:20:00 - Brandon Hancock
This one as well.

00:20:02 - Brandon Hancock
So yeah, that's just the template side of thing.

00:20:04 - Brandon Hancock
The other part that I think you guys are really, really going to like is, okay, cool.

00:20:10 - Brandon Hancock
There's templates.

00:20:11 - Brandon Hancock
I understand.

00:20:11 - Brandon Hancock
Well, how do I take these templates and actually convert them over to a real-world AI application?

00:20:16 - Brandon Hancock
And that's exactly what we have all modules for that literally just help you go from coming up with your idea and then walking you step-by-step through of kicking off a template, making your idea concrete.

00:20:30 - Brandon Hancock
Then how to actually come up with your development roadmap, how we're using AI agents to actually do all the work for you to build out the application, and then a bunch of more templates at the end to help you actually like, okay, cool.

00:20:40 - Brandon Hancock
Let's set up Mailgun.

00:20:40 - Brandon Hancock
Let's set up all these other services.

00:20:43 - Brandon Hancock
it just, AI does all of it for you because it's already pre-built.

00:20:46 - Brandon Hancock
So yeah, so this was all so cool.

00:20:50 - Brandon Hancock
And then just final thing, like even the course has accompanying, let me just show you, even the templates, like every module.

00:21:00 - Brandon Hancock
Has steps in it.

00:21:01 - Brandon Hancock
like, for example, like in the beginning, when you're coming up with your master plan and like trying to figure out how everything works, well, the templates are trained on the course, so they understand what needs to be done and will help you do it.

00:21:14 - Brandon Hancock
So it's just like, at every point there could be AI, there is AI.

00:21:18 - Brandon Hancock
So I've absolutely loved getting this set up for you guys.

00:21:21 - Brandon Hancock
So, you know, still working on it.

00:21:24 - Brandon Hancock
We have all the templates, most of the templates done, which need to make some of the more simple versions.

00:21:28 - Brandon Hancock
But yeah, everything is set up.

00:21:31 - Brandon Hancock
And the cool final thing, and I'll stop talking about it, is what's coming next.

00:21:36 - Brandon Hancock
Why I'm so pumped for this is the way ShipKit is set up, it's extensible.

00:21:41 - Brandon Hancock
So what I mean by that is like, I'm, one of the big promises of it is like, as time goes on, keep adding more.

00:21:47 - Brandon Hancock
So like, voice agents, creating video, like video shorts, like AI video shorts.

00:21:52 - Brandon Hancock
So I just want to keep adding more and more in here.

00:21:54 - Brandon Hancock
So it keeps getting more and more, more valuable.

00:21:56 - Brandon Hancock
So that's kind of, you know, ShipKit in a nutshell.

00:21:58 - Brandon Hancock
So happy to.

00:22:00 - Brandon Hancock
know, happy to, like, if there's any, like, one-on-one questions you guys have, happy to clear it up.

00:22:05 - Brandon Hancock
But, yeah, I'll have more, a lot more coming out over the next month.

00:22:08 - Brandon Hancock
So that's where we're at.

00:22:09 - Brandon Hancock
So, yeah.

00:22:12 - Brandon Hancock
Amazing work.

00:22:13 - Al Cole
It looks tremendous.

00:22:14 - Al Cole
It really does.

00:22:15 - Al Cole
And I am looking forward to getting my hands on this.

00:22:18 - Al Cole
I will learn a ton.

00:22:19 - Brandon Hancock
So it looks great.

00:22:21 - Brandon Hancock
Oh, Al, you made such, you triggered a thought.

00:22:24 - Brandon Hancock
The other thing, there are even more applications, meaning, cool, there's templates.

00:22:29 - Brandon Hancock
But I actually show you guys, there's three other projects that come with it.

00:22:32 - Brandon Hancock
So I, for every type of project template, I convert it to an app.

00:22:35 - Brandon Hancock
So that way you actually get to see all in So all in all, you get nine projects, realistically.

00:22:40 - Brandon Hancock
So there's so much in there.

00:22:42 - Brandon Hancock
So that's why it takes longer, because I keep adding more.

00:22:45 - Brandon Hancock
So, yeah, it's keeping me busy and keeping me out of trouble.

00:22:50 - Brandon Hancock
So, all right, perfect.

00:22:51 - Brandon Hancock
But, yeah, we can just go round robin, guys.

00:22:54 - Brandon Hancock
We'll just go in order that people are popped up on the screen.

00:22:57 - Brandon Hancock
So excited to see what you guys have been with.

00:23:00 - Brandon Hancock
I'll drop the drop in the chat.

00:23:04 - Brandon Hancock
I do have a question, Brandon.

00:23:06 - Alex
Where do I, where do I buy it?

00:23:09 - Alex
I need it right now.

00:23:11 - Alex
I need, I need one more day.

00:23:13 - Brandon Hancock
We are, we are wrapping up a few things right now to make sure the email sequences come out properly and, and everything like that.

00:23:21 - Brandon Hancock
So we're just wrapping up, adding a few videos.

00:23:24 - Brandon Hancock
Exactly.

00:23:25 - Alex
Yeah.

00:23:25 - Alex
That was my question.

00:23:27 - Al Cole
Will it go off the school platform or are you doing it something separate?

00:23:31 - Brandon Hancock
So another thing that's going to be super cool for it is ShipKit is building ShipKit.

00:23:35 - Brandon Hancock
So what I mean by that is actually ShipKit has a rag, like there's a rag template in here.

00:23:42 - Brandon Hancock
So one of the cool things that is happening is every video module, every document, everything that goes into ShipKit will be in the vector store.

00:23:51 - Brandon Hancock
So what's nice is at some point, if you're ever like, what did Brandon say to do to spin up chat sass?

00:23:57 - Brandon Hancock
You'll be able to like chat with.

00:24:00 - Brandon Hancock
The course.

00:24:00 - Brandon Hancock
So it literally is AI in every aspect.

00:24:04 - Brandon Hancock
So, um, so yeah, so there's, there's a ton of things that go, um, that go into that.

00:24:09 - Brandon Hancock
So it will be its own separate course, but it'll be all done.

00:24:12 - Brandon Hancock
Like what's cool.

00:24:13 - Brandon Hancock
It's like the platform that you're learning how to build real world production applications was used to build a real world AI production application.

00:24:20 - Brandon Hancock
So it's kind of like full circle and social proof.

00:24:23 - Brandon Hancock
So, um, so that, yeah.

00:24:26 - Brandon Hancock
So yeah, weird thing.

00:24:27 - Brandon Hancock
You'll never hear someone say this, please don't buy it.

00:24:30 - Brandon Hancock
Today, please don't.

00:24:32 - Brandon Hancock
I may tomorrow afternoon will be good, but until tomorrow afternoon, please, please, please know it's not going anywhere.

00:24:39 - Brandon Hancock
Uh, and then yeah, fit.

00:24:41 - Brandon Hancock
Sorry.

00:24:41 - Brandon Hancock
On the email sequences, there's, uh, a few bonuses that are given out, um, on, on that.

00:24:48 - Brandon Hancock
I'll make sure you get it.

00:24:49 - Brandon Hancock
But basically you get instant access to the previous course I made, uh, the, uh, marketing, the marketing course, you get instant access to that.

00:24:58 - Brandon Hancock
So setting up that email.

00:25:00 - Brandon Hancock
Setting up that zap, there's a connection I have to make, giving instant access to most templates, most prep files, like all of that.

00:25:09 - Brandon Hancock
I just want make sure when you get it, you get instant access.

00:25:12 - Brandon Hancock
So that's the kicker.

00:25:14 - Brandon Hancock
So that's what we're fixing today and tomorrow morning.

00:25:17 - Brandon Hancock
So yeah, definitely, definitely very busy.

00:25:20 - Brandon Hancock
Yeah, Fitz, yeah, the second I get that all connected, I will make sure to manually send it over to you too.

00:25:27 - Brandon Hancock
So yeah, but yeah, that is everything on my side.

00:25:34 - Brandon Hancock
So Andrew, the floor is yours.

00:25:36 - Brandon Hancock
Love to hear all the cool things you've been up to, man.

00:25:38 - Andrew Nanton
Missing you guys.

00:25:40 - Andrew Nanton
Well, yeah, thanks.

00:25:43 - Andrew Nanton
Not a lot of updates today.

00:25:45 - Andrew Nanton
I've just still been continuing to work on playing with Lang Extract, that Google library for structured extraction for very long.

00:25:58 - Andrew Nanton
Documents.

00:25:59 - Andrew Nanton
Seems like it will probably.

00:26:00 - Andrew Nanton
It'd be really promising for my work, both for general structured extraction, but also I've been trying to play around a bit more with graph rag and extracting triplets for graph rag.

00:26:11 - Andrew Nanton
So that's what I've been up to.

00:26:14 - Andrew Nanton
Short update today, but I'll put in a link to it because if people haven't looked at it, it's worth a look.

00:26:20 - Brandon Hancock
So just link extract from Google?

00:26:23 - Brandon Hancock
Yep.

00:26:24 - Andrew Nanton
Let me look at this.

00:26:25 - Andrew Nanton
And a couple of gross, weird people who camp on empty domain names have set up fake domains for it, but yeah, it's just this GitHub one.

00:26:38 - Andrew Nanton
So it's pretty straightforward to get started with, and it does this cool HTML visualization of what you get out of it.

00:26:48 - Andrew Nanton
If you keep scrolling down, there's like an animated GIF down there to show you.

00:26:53 - Andrew Nanton
So yeah, it's extracting it here.

00:26:57 - Andrew Nanton
It'll show the character, the emotion, and the relationship.

00:27:00 - Andrew Nanton
And because they go through all of Romeo and Juliet and with just, you a couple of really simple examples and you can have it do like take a couple of passes at it.

00:27:11 - Andrew Nanton
And because it's not super complicated, this seems like one that you might actually be able to run with maybe that local GPT model because, mean, you may need to run it a couple of times to get decent accuracy.

00:27:23 - Andrew Nanton
But if you really wanted to keep everything totally local, it seems like that wouldn't be out of the question, depending on how complex your task is.

00:27:32 - Brandon Hancock
So just because like this is cool, I'm going to make sure I fully understand it.

00:27:36 - Brandon Hancock
So I'm passing in text files or PDFs and it is extracting all text from document.

00:27:45 - Brandon Hancock
And it looks like you said it was also adding in some metadata to it.

00:27:49 - Brandon Hancock
Like this came from this section, right?

00:27:52 - Brandon Hancock
Is that what's happening?

00:27:54 - Andrew Nanton
Yes.

00:27:54 - Andrew Nanton
So, and it does that by like character count.

00:27:56 - Andrew Nanton
It does not handle PDFs, only plain text, but it says, you know.

00:28:00 - Andrew Nanton
This selection starts at character X and ends at character Y.

00:28:04 - Andrew Nanton
And then if things are selected, like if you do two or three passes and it's selecting slightly different boundaries on that, it will combine all those together in a way that I still don't totally understand.

00:28:17 - Andrew Nanton
It seems to do its own chunking under the hood, which, again, I haven't really poked too much at.

00:28:23 - Andrew Nanton
But yeah, I've been pretty impressed and it's moving very quickly.

00:28:29 - Andrew Nanton
So if you do play with it, make sure you update the library often.

00:28:34 - Brandon Hancock
Oh, that's awesome.

00:28:35 - Brandon Hancock
Yeah, well, because like the main one, Dockling, I think you introduced Chunky to the group.

00:28:42 - Brandon Hancock
So it sounds like this one is best for just like an insanely long document that I guess just like, cool, this is a new tool in my tool belt.

00:28:52 - Brandon Hancock
From your experience using it, when would one use this?

00:28:56 - Brandon Hancock
I guess is my big question.

00:28:58 - Andrew Nanton
So the two things that make it...

00:29:00 - Andrew Nanton
Interesting for what I'm doing because I was between this and actually another one that you should take a look at called BAML, B-A-M-L.

00:29:08 - Andrew Nanton
There are two things that are relevant for me for this one.

00:29:11 - Andrew Nanton
BAML seems much more developer-oriented and I'm not a developer, you know, and the other two things are it's great for long documents.

00:29:26 - Andrew Nanton
Ling Extract is great for long documents and it's great for very specific citations about where this information came from.

00:29:32 - Andrew Nanton
And so those are two really key ingredients for me.

00:29:36 - Andrew Nanton
It also is super easy to get started with.

00:29:39 - Andrew Nanton
BAML, I sent Bastian a link and I'll put it in the chat.

00:29:43 - Andrew Nanton
There's a, someone wrote like a guide that Kuzu embedded database.

00:29:49 - Andrew Nanton
They have a couple of tutorials using BAML for structured extraction, specifically about building graphs, but it could be for anything.

00:29:58 - Andrew Nanton
I mean, it really is.

00:30:00 - Andrew Nanton
It's just structured extraction, but it seeks to make structured extraction a lot more predictable and straightforward.

00:30:07 - Andrew Nanton
It looks really neat.

00:30:08 - Andrew Nanton
I haven't found any use for it myself, but another one that's maybe good to know about.

00:30:13 - Brandon Hancock
This is wild that it just took it in and instantly generated its own schema, or yeah, answering this schema, and then it actually does it.

00:30:24 - Brandon Hancock
That's wild.

00:30:26 - Brandon Hancock
Huh.

00:30:27 - Brandon Hancock
That's pretty cool, man.

00:30:30 - Brandon Hancock
Yeah, that's awesome.

00:30:32 - Brandon Hancock
Yeah, like I said, I need to trap both of these just to see how they both work.

00:30:37 - Brandon Hancock
But yeah, it looks like it's doing awesome.

00:30:38 - Brandon Hancock
I would be very curious to see how it works just compared to like a Gemini, like just pass in an image and say Gemini structured output.

00:30:45 - Brandon Hancock
Like that's like one in my head, like why would I use BAML versus Gemini without a structured output?

00:30:53 - Brandon Hancock
But maybe just because like it can handle a lot more.

00:30:55 - Brandon Hancock
Maybe they're doing a lot more under the hood.

00:30:57 - Brandon Hancock
But no, both very cool finds.

00:31:00 - Brandon Hancock
Yeah, I was going to say, think BAML is based on the models that it's doing.

00:31:05 - Jusin Gibbs
So if you're going to do a thousand different receipts or a thousand receipts of the similar, Gemini might get a couple of those messed up where BAML is going to make sure it's still getting the same structure when you're importing it.

00:31:19 - Jusin Gibbs
Okay.

00:31:19 - Brandon Hancock
Okay, cool.

00:31:20 - Brandon Hancock
So they probably have like a lot more like backend stuff that's like making sure it works every time.

00:31:24 - Brandon Hancock
No, awesome.

00:31:25 - Brandon Hancock
Fine.

00:31:26 - Brandon Hancock
Awesome.

00:31:26 - Brandon Hancock
Fine.

00:31:27 - Brandon Hancock
Andrew, I swear you find the most new things and absolutely love it.

00:31:32 - Brandon Hancock
All these new tools.

00:31:34 - Brandon Hancock
Keeping us busy.

00:31:36 - Brandon Hancock
Well, I hope someone finds it useful.

00:31:38 - Andrew Nanton
Yeah.

00:31:38 - Andrew Nanton
Thanks.

00:31:38 - Andrew Nanton
Glad you're back.

00:31:40 - Andrew Nanton
No, good to be back.

00:31:41 - Brandon Hancock
Any, any other big things on the, and Andrew Lam?

00:31:45 - Andrew Nanton
No, no, I, I, um, I guess the last thing is that I've been, um, doing some more stuff with, um, like, uh, threat assessment groups.

00:31:55 - Andrew Nanton
And so I might be looking more at AI applications and.

00:32:00 - Andrew Nanton
In the threat assessment space.

00:32:01 - Andrew Nanton
so if that gets interesting, I'll keep you all posted.

00:32:06 - Brandon Hancock
And just out of curiosity, just so me, when I hear threat coming from like a DOD background, like in my head, I'm like, oh, aircraft of this type, you know, or what do you mean by threat?

00:32:18 - Andrew Nanton
But so I sit on a couple of threat assessment teams here in Oregon, and that's usually like county law enforcement, FBI, maybe like school representatives, if it's like school related stuff.

00:32:32 - Andrew Nanton
And, you know, just to sort of review different cases.

00:32:36 - Andrew Nanton
OK, this this is a situation of concern.

00:32:39 - Andrew Nanton
Here are the people who are involved.

00:32:42 - Andrew Nanton
And so it's it's very multidisciplinary, but less so than I would have thought, you know, it's only occasional that people are coming to the table with a whole boatload of data that needs to be looked at.

00:32:58 - Andrew Nanton
And I don't understand why that is.

00:33:00 - Andrew Nanton
Because, I mean, everyone's digital footprint is pretty huge these days.

00:33:04 - Andrew Nanton
I think maybe people are just catching up.

00:33:07 - Andrew Nanton
But yeah, I think it's potentially pretty useful to use something like Langextract or BAML if there are specific kinds of information that you're looking for.

00:33:17 - Andrew Nanton
You have a very large volume of information, and you need to find relevant stuff as fast as possible, where speed is as or more critical than accuracy.

00:33:28 - Andrew Nanton
You just want to, like, cast a wide net.

00:33:30 - Andrew Nanton
What are the things in here I need to be worried about?

00:33:33 - Andrew Nanton
And then you can focus your attention on that.

00:33:35 - Brandon Hancock
With all my videos and everything out there, if you could run it on me, I'd like to know if I'm a threat or not.

00:33:40 - Brandon Hancock
I'd be...

00:33:41 - Brandon Hancock
Okay, I'll let you know.

00:33:42 - Andrew Nanton
I'll let you know.

00:33:43 - Brandon Hancock
I gotta say, I'm a little concerned.

00:33:45 - Andrew Nanton
I've got the FBI on speed dial.

00:33:48 - Andrew Nanton
You'll know.

00:33:49 - Andrew Nanton
They'll knock in the Don't answer the door.

00:33:51 - Andrew Nanton
If it's a loud bang, don't answer.

00:33:52 - Andrew Nanton
We got a narc in the group.

00:33:54 - Marc Juretus
All right, that's cool.

00:33:55 - Marc Juretus
Yeah, man, I like you, Andrew.

00:33:56 - Marc Juretus
You're all right, brother.

00:33:58 - Brandon Hancock
Sorry.

00:34:00 - Marc Juretus
And you're all right by me, man.

00:34:02 - Marc Juretus
Go, Andrew.

00:34:03 - Andrew Nanton
That's funny.

00:34:04 - Brandon Hancock
All right.

00:34:05 - Brandon Hancock
Thanks, Andrew.

00:34:07 - Brandon Hancock
Mark, you're up next anyway.

00:34:09 - Brandon Hancock
What's going on?

00:34:11 - Marc Juretus
Hey, thanks for the video, by the way.

00:34:13 - Marc Juretus
That's on my consume list.

00:34:15 - Marc Juretus
So right now, what I've been working on, I pretty much, it's like 95% on the fantasy app.

00:34:20 - Marc Juretus
I guess I can show it real quick if you want.

00:34:22 - Brandon Hancock
Oh, I can't.

00:34:23 - Brandon Hancock
Let me click the button for you.

00:34:24 - Marc Juretus
screen.

00:34:25 - Marc Juretus
I don't want stay on that long.

00:34:26 - Marc Juretus
All right.

00:34:28 - Marc Juretus
What do got to do?

00:34:28 - Marc Juretus
Share.

00:34:29 - Marc Juretus
I always screw this up.

00:34:30 - Marc Juretus
It's not like I work in IT.

00:34:33 - Marc Juretus
So you guys hear me chirping about this for the longest time.

00:34:37 - Marc Juretus
But anyways, this is basically my fantasy app.

00:34:39 - Marc Juretus
So it's a front end.

00:34:41 - Marc Juretus
It's Next.js.

00:34:42 - Marc Juretus
Back end is Python with a fast API served up with Superbase.

00:34:48 - Marc Juretus
So basically, I can come in here.

00:34:50 - Marc Juretus
I can set the roster for it.

00:34:52 - Marc Juretus
So there's my players.

00:34:53 - Marc Juretus
I can search them.

00:34:54 - Marc Juretus
It has them out in groups.

00:34:56 - Marc Juretus
And then I have, you know, my starting lineup.

00:34:59 - Marc Juretus
Oh, hold on.

00:34:59 - Marc Juretus
Let me go.

00:35:00 - Marc Juretus
I can add a player.

00:35:01 - Marc Juretus
can edit a player.

00:35:02 - Marc Juretus
I can actually look at the rankings that are listed here for every player to score that it has.

00:35:09 - Marc Juretus
And I can also, you know, edit some of the players that I have in my roster.

00:35:14 - Marc Juretus
I can delete them.

00:35:15 - Marc Juretus
I can add them.

00:35:15 - Marc Juretus
I can put them to the bench.

00:35:18 - Marc Juretus
Dude, this has come so far along.

00:35:20 - Brandon Hancock
This is looking awesome.

00:35:21 - Marc Juretus
So, well, I mean, part of this process, and this is completely written in Lang Flow as well.

00:35:26 - Marc Juretus
Yeah, I switched off, you know, what you were just speaking about with ADK, man.

00:35:30 - Marc Juretus
I was like, man, I got to get this done, man.

00:35:31 - Marc Juretus
Season starts on the 4th.

00:35:33 - Marc Juretus
So, but at any rate, you know, the main piece of it is it's going to email me its lineup.

00:35:39 - Marc Juretus
So what it does is it interfaces with Supabase, takes in the rankings that it's got for that week, which you just saw, like, you know, the different rankings for each player.

00:35:48 - Marc Juretus
And it has two separate ranking points, and it gives an average score.

00:35:52 - Marc Juretus
And then whoever has the lower score, you have to start two running backs, two wide receivers, a flex, a quarterback, and a tight end.

00:35:58 - Marc Juretus
So I basically...

00:36:00 - Marc Juretus
Say, get starting lineup.

00:36:02 - Marc Juretus
And this will get kicked off by a PowerShell job.

00:36:05 - Marc Juretus
But right now it's just, I can just come in here.

00:36:08 - Marc Juretus
And now if I click on email, it'll email me.

00:36:10 - Marc Juretus
But it basically said, hey, Jalen Hurts, his base score was that.

00:36:14 - Marc Juretus
I'm basically giving them a point advantage if they're playing at home.

00:36:17 - Marc Juretus
So that takes it down to 3.5 from 4.5.

00:36:20 - Marc Juretus
So out of my two quarterbacks, it says, hey, Marc, start him.

00:36:24 - Marc Juretus
Start, you know, Derek, this and that.

00:36:26 - Marc Juretus
I know some of guys don't watch sports, so I'll make it real brief.

00:36:28 - Marc Juretus
So it tells me to start, gives me this analysis for the position, this, that, and the other.

00:36:32 - Marc Juretus
So what I'll do for an entire season is I'll put the lineup in for the team, and that'll pretty much, we'll see how it does for the year.

00:36:42 - Marc Juretus
So right now, I just have to factor in injury status, and I can't really pull that feed into its evaluation until injury status is available and relevant, which won't be for about another week.

00:36:54 - Marc Juretus
So that's where we're at.

00:36:55 - Marc Juretus
But after this, I want to consume your ADK, and...

00:36:59 - Marc Juretus
let's

00:37:00 - Marc Juretus
These guys had a great idea, like if I'm trying to go out and actually get some work, now that I know some of these frameworks and stuff, is to maybe learn N8N, that if somebody had a simple flow that they wanted to do, instead of trying to do some complex solution, I can probably spin something up.

00:37:14 - Marc Juretus
And I know JavaScript, like the back of my hands, that's what I heard it's made in.

00:37:17 - Marc Juretus
So if I can do that, you know, I can say, here, here's a mock-up of what I can do for you.

00:37:23 - Marc Juretus
But if you need something more complex, I can get in and do something like LangChing, LandFlow, and hopefully Google ADK.

00:37:29 - Brandon Hancock
Yeah, absolutely, absolutely love that.

00:37:31 - Brandon Hancock
I have two quick points for you.

00:37:33 - Brandon Hancock
I just dropped in the chat, I saw the response from the agents was in raw markdown.

00:37:39 - Brandon Hancock
Cool, cool thing, if you just, if look in the chat, there's two libraries you can use, react markdown, and then there's a plugin.

00:37:46 - Brandon Hancock
But what it'll do is, as the agent is streaming back a response, it'll automatically add in, it'll actually format it for you in real time.

00:37:55 - Brandon Hancock
So that way, when it's the agent's generating response, it looks like super clean, things are...

00:38:01 - Brandon Hancock
So if you want to add that into your, to your fantasy app, it could make the, the messages look more formatted to literally two imports and then that file.

00:38:10 - Brandon Hancock
And then second one, do you want to just mention this on ADK?

00:38:14 - Brandon Hancock
ADK for workflows, where you're doing stuff, as long as you're not streaming, I've had an insane amount of like, it is so easy to use, like the backend.

00:38:24 - Brandon Hancock
Now that I've like figured it all out, as long as you're not streaming, so easy to use.

00:38:29 - Brandon Hancock
It works perfect with Agent Engine, it works perfect with local development.

00:38:32 - Brandon Hancock
And it, yeah, it's so easy, create the session, send the message, and it just works perfectly.

00:38:36 - Brandon Hancock
It's just streaming.

00:38:38 - Brandon Hancock
Streaming is the thing, it looks cool, but it adds so much complexity and breaks.

00:38:42 - Brandon Hancock
So if you're ever thinking about just doing a straight up workflow, I still am really bullish on ADK, just not streaming right now.

00:38:49 - Brandon Hancock
So happy to dive deeper into that, if you guys have questions, but yeah, happy to, happy to share more.

00:38:55 - Marc Juretus
The app that I want to do, like if I want to try to, you know, maybe try to stir up some work is...

00:39:00 - Marc Juretus
Just a  company where you can upload the resume for opening positions and it'll like analyze your resume, let you know if you're qualified and a bunch of other things like here's a full function and phony, you know, company with a whole full functionality with AI built in for different aspects of it.

00:39:15 - Marc Juretus
So that would be my other thing to have just as like, hey, what are you doing AI here?

00:39:19 - Marc Juretus
Go play up in this phony company and you can see.

00:39:23 - Marc Juretus
That's very cool.

00:39:24 - Brandon Hancock
Yeah.

00:39:25 - Brandon Hancock
Ping me if I can help with that at all.

00:39:27 - Brandon Hancock
And heck, if next time, if you want to like, one of my favorite things is if you want to like an Excalibur, just like kind of map up current thinking, would love to just like review and drop hints and tips before you start.

00:39:40 - Brandon Hancock
I do have one question.

00:39:42 - Marc Juretus
How do you like, I've been using the Google Docs like checklist.

00:39:45 - Marc Juretus
What do you guys use?

00:39:46 - Marc Juretus
Like, okay, because what I do is I'll go on, I'll have a list of five things.

00:39:50 - Marc Juretus
Mark, you need to accomplish this this weekend.

00:39:52 - Marc Juretus
Are you using like a checkbox list?

00:39:54 - Marc Juretus
What are you using for that?

00:39:55 - Marc Juretus
Because it's always kind of annoying to do it in Word and Google Docs.

00:39:58 - Marc Juretus
Is there something even easier?

00:40:00 - Brandon Hancock
Like for just to do's like gameplay.

00:40:03 - Brandon Hancock
Yeah.

00:40:03 - Marc Juretus
Yeah.

00:40:04 - Brandon Hancock
I, if you saw my desk right now, you would be disgusted at the amount of like raw notes I have with just to do's because I have like real quick, my approach.

00:40:15 - Brandon Hancock
If it's an idea, it's a big project.

00:40:17 - Brandon Hancock
It's going into notion.

00:40:18 - Brandon Hancock
I see Andrew with his old school too.

00:40:20 - Brandon Hancock
If it's a long-term goal, like a vision, like if it's a map for the next month, I have like a huge board in front of me and I just stick high level like goals.

00:40:30 - Brandon Hancock
So I usually break stuff down from goals from up there for the month, then to daily actions on paper.

00:40:36 - Brandon Hancock
And then if it's more of a bigger project where I need to keep up with stuff long-term notion, that's my system.

00:40:43 - Brandon Hancock
It's a little gross, but if anyone else has any ideas or recommendations, happy to hear.

00:40:47 - Brandon Hancock
Oh, and then finally, if I am working with another developer, I use linear for literally everything.

00:40:53 - Brandon Hancock
I can show it to you guys real fast.

00:40:54 - Brandon Hancock
I think linear is such a cheat code when keeping up with to do's bugs, fixing.

00:41:00 - Brandon Hancock
And everything else.

00:41:01 - Brandon Hancock
So like, it's just like, it's Trello, but made for developers.

00:41:07 - Brandon Hancock
So you can always add an issue.

00:41:09 - Brandon Hancock
So like, help Marc with brainstorming, brainstorming app, you can assign it to a person, put it in any category.

00:41:19 - Brandon Hancock
When it's done, you have an issue.

00:41:22 - Brandon Hancock
What's cool is it's like also hooked up to GitHub.

00:41:25 - Brandon Hancock
So you can easily like, they work together.

00:41:28 - Brandon Hancock
So whenever you're in Codeland, and you check out this branch right here, and you make progress on it, it'll actually update the activity timeline.

00:41:38 - Brandon Hancock
So you can actually see, like, it all just works together.

00:41:40 - Brandon Hancock
So linear, awesome recommendation for keeping up with code to do's.

00:41:45 - Brandon Hancock
It's funny, we use Azure DevOps at work, and we have the whiteboard, and we have this basically looks just like that.

00:41:51 - Marc Juretus
And I actually have my own tenant, I should maybe even use that just to get used to it more as well.

00:41:55 - Marc Juretus
I'll look at that as well.

00:41:57 - Marc Juretus
Yeah, I think I'm on the free plan.

00:41:59 - Brandon Hancock
And I actually have like, Yeah,

00:42:00 - Brandon Hancock
People on the team, like I think it's a pretty good, yeah, I don't think I'm, yeah, I'm on the free plan and I've been using it for months.

00:42:06 - Brandon Hancock
So love free.

00:42:08 - Brandon Hancock
So definitely recommend checking it out as well.

00:42:10 - Brandon Hancock
And then Andrew and Patrick also have some really good ideas too.

00:42:15 - Brandon Hancock
Patrick's going down the agent to do list to keep up with stuff, which I think I should probably lean into more.

00:42:20 - Brandon Hancock
Patrick, I love that suggestion.

00:42:23 - Brandon Hancock
Yeah, that is awesome idea.

00:42:24 - Brandon Hancock
I need to do that.

00:42:25 - Brandon Hancock
Okay.

00:42:27 - Brandon Hancock
Um, cool.

00:42:29 - Brandon Hancock
And final thing, Bastian also just dropped in a cool comment for you.

00:42:32 - Brandon Hancock
I guess you get a ton of free stuff with that, uh, that link you just shared.

00:42:38 - Marc Juretus
So, Hey, that's part of it that you shared, Al.

00:42:43 - Marc Juretus
Okay.

00:42:45 - Marc Juretus
Yeah.

00:42:46 - Al Cole
So that, um, Lenny's newsletter, um, I did that.

00:42:50 - Al Cole
So for a couple hundred bucks, you get access to, something like 20 different platforms.

00:42:57 - Al Cole
Linear was on there.

00:42:58 - Al Cole
I haven't yet.

00:43:00 - Al Cole
Dove in, but now that I've seen how you've integrated it in, I'll get there.

00:43:05 - Brandon Hancock
I need to check it out, too.

00:43:08 - Brandon Hancock
Perfect.

00:43:09 - Brandon Hancock
Alex, you're up next, man.

00:43:11 - Brandon Hancock
Dude, you are clean-shaven everywhere.

00:43:15 - Alex Wilson
For the time being, I think it's about time to start growing it back.

00:43:21 - Alex Wilson
That's awesome.

00:43:21 - Alex Wilson
Well, what cool projects have been working on?

00:43:25 - Alex Wilson
Right now, I'm working on figuring out what job I'm going to do next.

00:43:28 - Alex Wilson
So I'm doing all the, I'm part of LHH for my last job and looking for work.

00:43:35 - Alex Wilson
So last week, I asked some questions about different meetings and whatnot.

00:43:39 - Alex Wilson
But I have a question for you.

00:43:41 - Alex Wilson
Saul recommended a MacBook Air.

00:43:45 - Alex Wilson
So I had my first Mac in decades.

00:43:49 - Alex Wilson
So I'm getting used to it.

00:43:50 - Alex Wilson
So I just started your course again, the course that we had in here in the classroom, just to get everything set up.

00:43:59 - Alex Wilson
So I have kind of the same.

00:44:01 - Alex Wilson
And one of the questions I had is, you're using Gemini a lot now.

00:44:06 - Alex Wilson
What are you doing for like projects that you used to do with like Claude?

00:44:12 - Brandon Hancock
So I am still mostly using Claude.

00:44:15 - Brandon Hancock
Like if I was to like map it out, it's 90% Claude.

00:44:18 - Brandon Hancock
The only time I am using Gemini is for huge context problems.

00:44:24 - Brandon Hancock
For example, that's how you saw I had that like setup process that was going to walk people through the entire process.

00:44:31 - Brandon Hancock
I use Gemini Max, like Gemini 2.5 Pro on max setting because I want to hit that million token context window.

00:44:40 - Brandon Hancock
But outside of that, I am always in Claude 4.0, Claude 4 thinking.

00:44:46 - Brandon Hancock
That's where I'm at nine hours of time.

00:44:49 - Alex Wilson
Okay.

00:44:50 - Alex Wilson
So that's what I would recommend too.

00:44:52 - Brandon Hancock
I've been playing with Gemini.

00:44:53 - Alex Wilson
I like a lot of it.

00:44:54 - Alex Wilson
It does some weird stuff for me every now and again, like just random results.

00:45:02 - Alex Wilson
So I built a screenplay tool and instead of using the projects the way you normally use them, I hooked it up to GitHub.

00:45:11 - Alex Wilson
So all of the assets that you use, like your script Bible and your character profiles and all that, I can just drop it from the editor directly into Copilot.

00:45:24 - Alex Wilson
And then as you're writing your different scenes and everything, it has access to all that, that info in Claude.

00:45:30 - Alex Wilson
So I was wondering if there was anything.

00:45:33 - Brandon Hancock
Are you doing Claude Code out of curiosity?

00:45:36 - Brandon Hancock
Not doing Claude Code yet.

00:45:38 - Brandon Hancock
Okay.

00:45:39 - Brandon Hancock
No, the, um, one of the big things I get to hope to work on next week is like making, and I'll hopefully get a video up later next week is on Claude Code subagents.

00:45:49 - Brandon Hancock
I think that is an insanely valuable, like how you just mentioned, Gemini's doing weird, doing weird things.

00:45:55 - Brandon Hancock
You'll see in the video that's coming out tomorrow, um, how I'm using.

00:46:00 - Brandon Hancock
Templates to make sure when I'm writing code, it just does exactly what I want, but you can also, sorry, but you can also, you can also achieve, you can achieve the same result with flawed code subagents.

00:46:14 - Brandon Hancock
So I'll be doing another video on that soon.

00:46:17 - Brandon Hancock
But do diving in more on the job stuff.

00:46:19 - Brandon Hancock
Are you more freelance stuff?

00:46:20 - Brandon Hancock
Is this full-time job?

00:46:21 - Brandon Hancock
What do you, what are you leaning into?

00:46:24 - Alex Wilson
I'm leaning more towards full-time.

00:46:27 - Alex Wilson
need to do probably another 10 years to have enough in my retirement to start working on the passion projects.

00:46:34 - Alex Wilson
But I don't know, I'm open.

00:46:37 - Alex Wilson
I gotcha.

00:46:38 - Brandon Hancock
A few things that I have seen just recently, just so you can see what I'm seeing job-wise.

00:46:46 - Brandon Hancock
I know you obviously have an insane amount of projects that you've built.

00:46:52 - Brandon Hancock
And at this point, I assume your portfolio is like awesome.

00:46:56 - Brandon Hancock
So like one thing that I would definitely recommend looking at.

00:47:00 - Brandon Hancock
It's like finding people who have too much work to do.

00:47:03 - Brandon Hancock
For example, Dan, Dan Martel, the one that hopped on the group, he has that incubator to where he helps out SaaS founders.

00:47:10 - Brandon Hancock
And every time SaaS founders run into an issue, they go, Dan, do you know someone?

00:47:14 - Brandon Hancock
And then from there, Dan goes, well, whoever's good in this field, I will just point to.

00:47:20 - Brandon Hancock
So like, I think it could be very helpful to, I think you had Dan's email or Instagram or whatever, but just like reach out and just say like, hey, I am this developer, here's what I'm like awesome at.

00:47:31 - Brandon Hancock
If anyone, if anyone of your teams ever need help on anything in here, I'm happy to help.

00:47:37 - Brandon Hancock
And that, that's actually led to some cool, cool things recently.

00:47:42 - Brandon Hancock
Bastian, you can talk more about that in a second if you, if you want to.

00:47:45 - Brandon Hancock
But just going to the people who have too much work, then they can keep up with.

00:47:50 - Brandon Hancock
Cause you already have an awesome resume.

00:47:51 - Brandon Hancock
And I also too, if you ever want to talk more about like building an AI personal brand, would be happy to just give you like for your situation, like a 30 minute.

00:48:00 - Brandon Hancock
Crash Course on like exactly what I would do just because like, you know, all it takes is like a little bit of posting for a little while and it just opens so many doors, you know, so happy if you ever want to have a conversation on that just because I think it's, yeah, it can be life changing.

00:48:17 - Alex Wilson
Okay, thank you.

00:48:18 - Alex Wilson
I don't know if I, I don't feel like I have the personality for it, but, you know, I'm probably more the engineer, the back room person.

00:48:28 - Brandon Hancock
Hey, dude, I was going to say, you press record and you say, hey guys, in today's video, and then boom, you just talk and just go from there, man.

00:48:39 - Brandon Hancock
But yeah, even if it's like a LinkedIn thing where it's all text, that's also 100% doable too.

00:48:45 - Brandon Hancock
just literally, the whole model is give free stuff away on the internet to show that you're the expert and it will pay dividends because people go, that was awesome.

00:48:54 - Brandon Hancock
Can you do it for me?

00:48:55 - Brandon Hancock
And then boom, it's instantly paid for itself, you know, so we'll definitely recommend that out.

00:49:00 - Brandon Hancock
And I think you watched that one YouTube video I did a while ago on the AI Authority Accelerator.

00:49:06 - Brandon Hancock
Alex, actually, that is a great sale.

00:49:09 - Alex
Like, I know that's not what you expected, but in today's video, you know, it's a new angle, fresh angle.

00:49:17 - Brandon Hancock
Yeah, seriously.

00:49:18 - Brandon Hancock
But I just dropped it in the chat.

00:49:22 - Brandon Hancock
If you want to rewatch it, and there is a final thing.

00:49:26 - Brandon Hancock
There's a Notion, like, masterclass attached to it.

00:49:30 - Brandon Hancock
And I'll link that, too.

00:49:31 - Brandon Hancock
Just because, like, seriously, I would love for every one of you guys to have your own, like, LinkedIn or YouTube.

00:49:38 - Brandon Hancock
But I will find it.

00:49:40 - Brandon Hancock
Yeah, my personal brand.

00:49:42 - Brandon Hancock
Yeah, I will find it and send it over to you.

00:49:44 - Brandon Hancock
But I think I'm super helpful.

00:49:46 - Brandon Hancock
You do?

00:49:47 - Brandon Hancock
Okay, perfect.

00:49:48 - Brandon Hancock
Yeah.

00:49:48 - Alex Wilson
Okay, cool.

00:49:49 - Brandon Hancock
I'll drop it in in case anyone else needs it as well.

00:49:54 - Brandon Hancock
I'll just have to find it.

00:49:55 - Brandon Hancock
Yeah, I will find it, and I will send it to you guys.

00:49:57 - Brandon Hancock
Send it to everyone else.

00:49:58 - Brandon Hancock
I'll just drop the public link in a second.

00:50:00 - Brandon Hancock
Yeah, perfect.

00:50:01 - Brandon Hancock
keep me posted on the job side.

00:50:04 - Brandon Hancock
And then if there's anything I can ever help with, always let me know.

00:50:07 - Brandon Hancock
Happy to help.

00:50:08 - Alex Wilson
Thank you much.

00:50:10 - Alex Wilson
Of course.

00:50:11 - Brandon Hancock
All right, Paul, co-host.

00:50:14 - Brandon Hancock
What's going on?

00:50:16 - Paul Miller
Gosh, it's a lot of work running a video and being involved in it at the same time.

00:50:23 - Paul Miller
I prefer being a participant.

00:50:28 - Paul Miller
Your head has to go a thousand directions at once.

00:50:31 - Brandon Hancock
It's different.

00:50:31 - Brandon Hancock
no, I'm happy to help.

00:50:32 - Paul Miller
Look, you give so much to your community.

00:50:35 - Paul Miller
If we can ever give back, it's always very rewarding.

00:50:40 - Paul Miller
But no, so what's going on with me?

00:50:46 - Paul Miller
Like Mark, I've actually gone down the N18 path quite a lot more because I've got so many balls in the air.

00:50:59 - Paul Miller
Yeah, got

00:51:00 - Paul Miller
The moment with different projects, I just I need to focus on what the customers want and the customers that are going to pay the money and the customers want to see they want to see tangible deliverable and then the money flows and it's kind of unlocking that whole get the deliverable right.

00:51:21 - Paul Miller
And I think, you know, while I've always been impressed in my tech life about a really good back end and really well built architecture, customers never get that.

00:51:34 - Paul Miller
They're all about the front end and seeing a demonstration that knocks it out of the park in terms of delivering what they want.

00:51:42 - Paul Miller
And so I've got really focused on that in quite a funny way, because as many of you might know, I get quite involved with politics.

00:51:53 - Paul Miller
And at the moment, we've got a local body politics election.

00:51:58 - Paul Miller
So it's for municipal.

00:52:00 - Paul Miller
So mayoral elections, councillor elections, and sure enough, I'm involved with this huge group of people, all asking very similar questions.

00:52:12 - Paul Miller
And while I won't get into the politics side, the challenge when you have a very grassroots organisation, and maybe the thing that Mark was talking about before, when you're trying to link in community, people, and a lot of discussion points, and you want people to be really focused and grounded on, well, here's the documents, or here's the approach you need to look at, linking that together with a little N8N process to say, I'm focused on this area in my city.

00:52:48 - Paul Miller
These are the top three things that people have said that they're concerned about, and these are the persona of the people that actually vote, because you can be, oh, you know, I like this.

00:53:00 - Paul Miller
This, I like that, and we should talk about this and talk about that.

00:53:03 - Paul Miller
And you forget, people that actually vote, this is all I care about.

00:53:08 - Paul Miller
So make an engine that puts that information through and guides people in a way that's not biased, that says, look, this is how people think.

00:53:19 - Paul Miller
You know, put it through there, talk with the chat bot, get your, before you do a post on social media or you go and say something stupid at press event, go through this, sense check what is core to your voter base.

00:53:37 - Paul Miller
And it doesn't have to be in politics, it could be briefing many different people doing different stuff, maybe in advisory roles.

00:53:47 - Paul Miller
That, that's kind of what I'm getting into.

00:53:49 - Paul Miller
It's, it's kind of mashing up my two worlds of politics and, and tech, and I'm quite excited about it at the moment.

00:53:56 - Brandon Hancock
So that's my thing.

00:53:57 - Brandon Hancock
I love that so much.

00:54:00 - Brandon Hancock
In my head, I instantly went to implementation of doing basically a parallel workflow to where passing the message or the speech, whatever you're about to do next, and per persona, an agent would critique, here's what I like, here's what I dislike, here's what you could have done better, and then afterwards combine all of their different reports and complaints.

00:54:22 - Brandon Hancock
Once you have that feedback, generate an updated, basically generate an updated speech that drives it home with each demographic or voter persona.

00:54:34 - Brandon Hancock
That's very cool.

00:54:35 - Brandon Hancock
They're going to be like, Paul, my God, which craft is this?

00:54:38 - Brandon Hancock
You were over there just winning elections left and right.

00:54:41 - Brandon Hancock
They didn't know you got the power of AI behind you, man.

00:54:43 - Brandon Hancock
Yeah.

00:54:45 - Paul Miller
Yeah, well, it's fun.

00:54:47 - Paul Miller
And look, I'm seeing in politics at the moment, there's a lot of people that are generating policy out of AI, but I think everyone on this call knows that...

00:55:00 - Paul Miller
There's a lot of people that use very simple chat messages with a single prompt with no grounding about the background of what they're asking.

00:55:08 - Paul Miller
They'll say, oh, I'm going to do a speech to all these people about transport or this.

00:55:14 - Paul Miller
They're not saying, well, you know, where do you stand?

00:55:16 - Paul Miller
What about the party you're representing?

00:55:18 - Paul Miller
What's core to them?

00:55:19 - Paul Miller
What's the existing policies they have?

00:55:21 - Paul Miller
All these other things that need to go in it.

00:55:24 - Paul Miller
And it's just building a solid framework around making sure that people can be grounded in what they talk about or focused in what they talk about.

00:55:36 - Paul Miller
And if you think in terms of the next steps, say if someone videos or records your presentation, you go and talk at some town hall, record that.

00:55:46 - Paul Miller
You put that back into the Google engine, you play that audio back in there, you convert it back and you give them a rating and say, you know, did you stick to the subject?

00:55:56 - Paul Miller
How well did you do?

00:55:57 - Paul Miller
You want to rate your candidates?

00:56:00 - Paul Miller
In who you're going to put forward in the next election or in more of a senior role, you can look at who's the most effective with communicating the party line.

00:56:11 - Paul Miller
I love that.

00:56:12 - Brandon Hancock
Cool thing, if I was in your shoes, I would try, is making a small platform for, you know, whichever party you're involved with, to where you could do the, like, and what would the tabs be?

00:56:25 - Brandon Hancock
Like, one would just be, like, a persona review, like, review this, and then the other one would just be, like, a general Q&A, and the third would just be, like, an upload section to where you could just always upload more and more to the, like, the party database.

00:56:38 - Brandon Hancock
So you could instantly get questions and answered, and then, boom, like, everyone in that party would have access to the platform and, you know, could spin up really fast and amplify their impact because, you know, everything's moving faster.

00:56:55 - Brandon Hancock
So I don't know, I think that's really cool.

00:56:56 - Brandon Hancock
If it works for one party, it works for all of them.

00:56:58 - Brandon Hancock
And then...

00:56:59 - Brandon Hancock
Well, completely.

00:57:00 - Brandon Hancock
So that's why I think that'd be a very cool project to dog food with your own organization first.

00:57:05 - Brandon Hancock
So, hey, we'd love to see a demo next week, man.

00:57:08 - Brandon Hancock
The idea was born.

00:57:10 - Paul Miller
Brilliant.

00:57:12 - Paul Miller
I'll get something together.

00:57:13 - Paul Miller
I'll make it very neutral because I don't want to leak out on the internet.

00:57:22 - Paul Miller
Look, it's right across the political spectrum because when you talk about local body politics, it's very different from national politics.

00:57:29 - Paul Miller
Because, you know, making sure there's a water treatment plant or a road is fixed or roundabouts done or whatever, that's very different from some of the global political issues that we've got.

00:57:42 - Paul Miller
And it's a lot more enjoyable, but you're dealing with a lot more of a base level person in terms of candidates and people getting out there and they can get a lot more off track.

00:57:52 - Paul Miller
But no, I'll get a demo.

00:57:54 - Paul Miller
All right, dude.

00:57:55 - Brandon Hancock
Absolutely love Paul.

00:57:56 - Brandon Hancock
And thank you once again for the last few weeks.

00:57:58 - Brandon Hancock
You were my hero.

00:57:59 - Brandon Hancock
Thank you.

00:58:00 - Brandon Hancock
Um, all right.

00:58:01 - Brandon Hancock
Perfect.

00:58:02 - Brandon Hancock
Uh, Sam, you're up next, man.

00:58:04 - Sam
Back to back New Zealanders.

00:58:06 - Sam
I like it.

00:58:07 - Sam
He'll teamed up.

00:58:11 - Sam
Oh, no, I just have a funny story.

00:58:13 - Sam
I think you guys will appreciate.

00:58:15 - Sam
So I, I sort of had that side hustle and I build the customer for it.

00:58:18 - Sam
And then I started watching the traces and like, like the first time I use a user that they pursue like a non use case.

00:58:30 - Sam
Like they, they put in this like query and this question.

00:58:32 - Sam
I'm like, you want to use it like that?

00:58:35 - Sam
You didn't tell me that.

00:58:38 - Sam
That's funny.

00:58:39 - Brandon Hancock
I can't remember.

00:58:40 - Brandon Hancock
There's a bunch of memes about this.

00:58:42 - Brandon Hancock
It's like, it's like, you know, if you give a chair to a, you know, if a developer makes a chair and gives it to a user, they flip it upside down and sit on it in a way that you never expected possible.

00:58:51 - Brandon Hancock
That's literally exactly what just happened with a, with what you just built.

00:58:55 - Brandon Hancock
So, which is so funny.

00:58:56 - Sam
I yeah, I was on their paper and I was like, is this something you want?

00:59:00 - Sam
And so now anyway, it's not too much work, but it's just boring stuff.

00:59:05 - Sam
So I have to spin up an API.

00:59:08 - Sam
Fortunately, New Zealand, with a lot of the council stuff, they surprisingly, they have a lot of free APIs to pull the data, which I didn't realize until I looked into it.

00:59:17 - Sam
So that's just me.

00:59:21 - Brandon Hancock
Out of curiosity, like going a little bit deep in tech stack, are you using PostHog for telemetry?

00:59:27 - Brandon Hancock
What were you using to help you spot what was going on?

00:59:31 - Sam
I'm a true believer.

00:59:32 - Sam
So I'm fully integrated with LangSmith, LangChain.

00:59:38 - Sam
Okay.

00:59:38 - Brandon Hancock
So you're literally just looking at the raw query that's coming in?

00:59:42 - Sam
No, they have, no, with their traces.

00:59:44 - Sam
So they have traces, you can store traces in there.

00:59:47 - Sam
So any interaction is pulled up in the trace.

00:59:49 - Sam
So I just pull up the traces and then see what they're saying and how the bot's working.

00:59:54 - Sam
I haven't got into evals yet, but that's all integrated in the platform.

00:59:59 - Brandon Hancock
That's cool.

00:59:59 - Brandon Hancock
That's

01:00:00 - Brandon Hancock
I mean, that's the best part about, like, building these things is, like, you kind of get to understand user behavior in ways that you never would have if you normally just gave it away.

01:00:08 - Brandon Hancock
So, yeah, tracing, so important.

01:00:11 - Sam
Yeah, no teaser, but don't be surprised when the customer's like, I'm going do this.

01:00:17 - Sam
It's like, that's fine, but you've to pay for it.

01:00:20 - Brandon Hancock
Yeah.

01:00:21 - Brandon Hancock
So is it almost done on the project?

01:00:23 - Brandon Hancock
Where are we at?

01:00:25 - Sam
I delivered what they wanted, and that works fine.

01:00:29 - Sam
But then they're like, oh, we want this as well, which is kind of what you said, is like, oh, you do one thing, and then they'll want something else.

01:00:37 - Brandon Hancock
Business-wise, I can't remember, did you end up going milestone approach?

01:00:40 - Brandon Hancock
Did you end up going milestone plus hourly, just so people can understand what's working right now in the real world?

01:00:48 - Sam
Yeah, I went hourly plus resources across as well.

01:00:53 - Sam
And then that kind of, because then it kind of set expectations, I think, for when I went on and said, and this.

01:01:00 - Sam
This is how much the subscription is going to cost, so they can kind of see that, okay, these are your resourcing, and then I have a little bit of dev time on top to say, look, this is to keep their wheels on, and then anything else you want is going to be an extra cost on top.

01:01:15 - Brandon Hancock
No, that's awesome.

01:01:16 - Brandon Hancock
That's awesome.

01:01:16 - Brandon Hancock
I know you've been working on it for a minute, so I'm glad to hear that nothing feels better than being done.

01:01:22 - Brandon Hancock
I don't feel like me.

01:01:24 - Brandon Hancock
I like new.

01:01:25 - Brandon Hancock
So getting to hop to the next new thing is always the fun part.

01:01:28 - Sam
Shiny things.

01:01:29 - Sam
Exactly.

01:01:30 - Brandon Hancock
Exactly.

01:01:31 - Brandon Hancock
Well, perfect.

01:01:32 - Brandon Hancock
Well, keep us posted, and yeah, good luck on keep adding in more and more AI, because that's once they get a taste of it, man.

01:01:39 - Brandon Hancock
We are all AI drug dealers, and once people get a taste, they're addicted.

01:01:44 - Sam
Yes.

01:01:47 - Brandon Hancock
Perfect.

01:01:48 - Brandon Hancock
Alex, you're up next, man.

01:01:51 - Alex
Hey, guys.

01:01:51 - Alex
How you doing?

01:01:52 - Alex
Thank you, Paul, for last week, and welcome back, Brandon.

01:01:57 - Alex
Hey, guys.

01:01:58 - Alex
So, well, for my end, I...

01:02:00 - Alex
I do have a lot of lined up videos for my channel.

01:02:04 - Alex
I finally contacted in a music concert.

01:02:11 - Alex
I got to know a nice editor, you know, taking your word, Brandon.

01:02:16 - Alex
So I could, yeah, he already told me, like, I need to have, like, three videos, like, in the working while he has, you know, I think that it's going to benefit a lot of the work on YouTube.

01:02:28 - Alex
But in the other side, I wanted to show you guys one project.

01:02:33 - Alex
This is a friend of mine.

01:02:35 - Alex
He just finished his master's in Canada, actually.

01:02:40 - Alex
Very cool.

01:02:41 - Alex
Yeah, so he's developed these.

01:02:44 - Alex
Maybe if I show you, I think it would be better.

01:02:49 - Brandon Hancock
Yeah, you're all going to share.

01:02:50 - Brandon Hancock
And then real quick while you're pulling that up, was it a thumbnail editor or a video editor?

01:02:54 - Alex
Video.

01:02:55 - Alex
Did you get a, do you care if I asked for hourly rate?

01:02:58 - Brandon Hancock
I just want to make sure you're getting a good deal.

01:03:00 - Alex
Yeah, actually, we're going to have a call this week regarding the package.

01:03:06 - Brandon Hancock
Quick update.

01:03:08 - Brandon Hancock
I can give you a, I owe you a document right after this, which usually I just share with video editors.

01:03:15 - Brandon Hancock
So it's just like hyper clear.

01:03:17 - Brandon Hancock
Here's expectations.

01:03:18 - Brandon Hancock
So I will send that to you after this.

01:03:21 - Brandon Hancock
It just makes it easier to tell them what you're going to give them.

01:03:25 - Brandon Hancock
How many, the rate, what hours are expected, how they need to allocate their time and the expected outputs.

01:03:32 - Brandon Hancock
So I will, I will send that to you.

01:03:35 - Alex
That'd be very useful.

01:03:36 - Alex
Yeah.

01:03:36 - Alex
Thanks a lot, man.

01:03:38 - Alex
Of course.

01:03:39 - Alex
Yeah.

01:03:40 - Alex
Okay.

01:03:40 - Alex
So he has developed these, he, these guys, like the smart type.

01:03:45 - Alex
He, he's a mathematician mainly, but he studied like computer science as well.

01:03:50 - Alex
And he's developed through a couple of years, some geo-reference algorithm.

01:03:56 - Alex
So what this, he's working.

01:03:59 - Alex
Thank you.

01:04:00 - Alex
Currently, with more of these monitoring news agencies and government.

01:04:05 - Alex
I don't know if you guys can see this Deep River page.

01:04:10 - Alex
Yeah.

01:04:10 - Brandon Hancock
Yeah, yeah.

01:04:11 - Alex
Okay, so this feed takes, it's open media.

01:04:17 - Alex
It's creamy.

01:04:18 - Alex
It's screening, I think, like every half a second.

01:04:24 - Alex
It's processing news, processing news.

01:04:26 - Alex
And the added value of this guy, like you can see here how many times this news has been mentioned, 40 times.

01:04:34 - Alex
This one, 128.

01:04:36 - Alex
This one, 251.

01:04:38 - Alex
And you could come here to this event.

01:04:42 - Alex
And here you see like the principal trends.

01:04:46 - Alex
And the same like 367 times it has been mentioned.

01:04:51 - Alex
Then you have like by topic, law and justice.

01:04:56 - Alex
We have safety.

01:04:58 - Alex
Well, hey,

01:05:00 - Alex
Security, politics, and you can keep on going.

01:05:04 - Alex
Here in the analysis section, this is where he grabs the content of the news and he georeferences it and puts it down in this map.

01:05:18 - Alex
Of course, it's focused in Mexico now.

01:05:21 - Alex
So let's say if I go to Mexico, well, this one that it's a bit more active.

01:05:27 - Alex
If I just put like events that have happened around here, and if I get a bit closer, oh no, I'm sorry, it's this one right here.

01:05:40 - Alex
Here, for instance, if I press here, I can see that there's like 59 news happening in this area.

01:05:49 - Alex
So it's pretty cool in terms of live monitoring.

01:05:55 - Alex
That's very cool.

01:05:56 - Alex
Yeah, and hearing that he has one...

01:05:59 - Alex
you.

01:05:59 - Alex
Thank

01:06:00 - Alex
Well, the report area, if you only want like a specific monitoring, you can decide how you want your report.

01:06:09 - Alex
This is just like a quick feed.

01:06:12 - Alex
Then you have a little summary.

01:06:13 - Alex
This is just by topic.

01:06:15 - Alex
You know, I can add which topic I want here, you know, like all the different types.

01:06:22 - Alex
And then I just export it as a PDF from here, you know, more of the deliverable side, you know?

01:06:28 - Alex
So I think it is pretty cool.

01:06:31 - Alex
And we had a conversation to make these, and, you know, of course, like we're trying to develop this for supply chain monitoring, you know, in Mexico.

01:06:43 - Alex
Yeah.

01:06:43 - Alex
know, given the big amount of logistic transport, you know, having one hour your bus stopped can mean a lot of, in terms of changes, especially.

01:07:00 - Alex
Especially for big companies.

01:07:01 - Alex
So when we had a conversation is like, we want to spin this because he's working already with governments and the tool, like we can tweak it to make it custom made.

01:07:11 - Alex
Like Alex Hormozzi says, like, you know, let's instead of, and that's what I told him, like, instead of just being general, like news, let's just focus on like monitoring retail for food specifics.

01:07:24 - Alex
So this is what the, where I'm going.

01:07:28 - Alex
And I don't know, maybe Al has interesting insights on how to approach the private sector, but I find the, this is like all, all, mostly made with SQL type of algorithms.

01:07:43 - Alex
So the cost is like only, he uses a call to an LLM just for the final deliverable.

01:07:51 - Alex
So it's very efficient.

01:07:53 - Alex
It's like, it costs nothing to keep, to, to, to have it operated.

01:08:00 - Alex
And we're just trying to make it special for a specific industry.

01:08:06 - Alex
And we're thinking on logistics and monitoring of logistics.

01:08:10 - Alex
Can I add a few things real fast that I think?

01:08:13 - Brandon Hancock
So I just want to share with you what I've seen people do that have been paid for applications.

01:08:21 - Brandon Hancock
So other AI developer, he was reaching out to companies for work.

01:08:27 - Brandon Hancock
And the thing that he ended up getting traction on and getting paid for was a custom AI newsletter for that organization.

01:08:36 - Brandon Hancock
Every Saturday or Friday, he would go through, do all of that research.

01:08:41 - Brandon Hancock
And every Friday, that company would get a tangible report on, in this case, if you wanted to go logistics, he would build it for them.

01:08:49 - Brandon Hancock
And so the key lesson here is like, you know, you might just want to make a demo version of it.

01:08:55 - Brandon Hancock
And then just like, it is a very straightforward playbook of going to each business and saying.

01:09:00 - Brandon Hancock
And hey, I've done this logistics at a high level, but I can tailor this to your business.

01:09:05 - Brandon Hancock
And usually you'd want to charge some upfront fee, like a pretty high customization upfront fee.

01:09:11 - Brandon Hancock
then just like, and then, yeah, you would never charge per hour for this type of project.

01:09:16 - Brandon Hancock
You would say like, I can customize it to your business needs, you know, maybe 8K, 6K, depending on what tangible outputs you can give them in the report.

01:09:24 - Brandon Hancock
And then just tell them to run it on a monthly basis, you know, depending on the size of the organization's many hundreds of dollars per month, because they get, they get to share it with all their employees.

01:09:32 - Brandon Hancock
So you could do it per seat.

01:09:34 - Brandon Hancock
You could do it.

01:09:35 - Brandon Hancock
Yeah.

01:09:35 - Brandon Hancock
There's multiple ways you could play this.

01:09:37 - Brandon Hancock
And you could do this for all organization types.

01:09:39 - Brandon Hancock
You're not just like, and it's so easy to go to the next and say, Hey, I've done this.

01:09:48 - Brandon Hancock
What can I do?

01:09:53 - Brandon Hancock
What can I I to bring you next?

01:09:57 - Brandon Hancock
What can I do to

01:10:00 - Brandon Hancock
Awesome.

01:10:05 - Brandon Hancock
Everyone wants their own unique idea that you guys, I'll take 10% ownership, but I would absolutely love if you guys did this.

01:10:11 - Brandon Hancock
Oh, sorry.

01:10:11 - Brandon Hancock
Is it cutting off?

01:10:12 - Brandon Hancock
Sorry about that.

01:10:13 - Brandon Hancock
But no, I would say I'd love to take 10% ownership.

01:10:15 - Brandon Hancock
That's the main point.

01:10:20 - Alex
That is, yeah, yeah, I'm more than happy.

01:10:24 - Brandon Hancock
Yeah.

01:10:25 - Alex
Yeah, yeah.

01:10:26 - Alex
You know, one other thought that I've been thinking is like, I think the user, you're totally right in that side of, I think that they just want their deliverable given like, I don't know, like in the morning and at night.

01:10:38 - Alex
And I don't want to deal with your, you know, like using the tool would be more like agent, like an agency, I would imagine.

01:10:48 - Brandon Hancock
Yeah, exactly.

01:10:49 - Brandon Hancock
You're a custom news agency to where you build the news they need for them, you know.

01:10:54 - Brandon Hancock
And the cool part is 90%, 80% of the core technology to do it for one company applies.

01:10:59 - Brandon Hancock
Thank very much.

01:11:00 - Brandon Hancock
To the next, you know, at that point, you're literally just shoved.

01:11:03 - Brandon Hancock
Once you have the core loops, sequences, at that point, you're just swapping out prompts for different companies.

01:11:09 - Brandon Hancock
So it's, you know, would probably be a pretty high margin business.

01:11:13 - Brandon Hancock
So only final comment, I dropped some stuff in the chat, some PDFs and some links.

01:11:19 - Brandon Hancock
You're obviously gonna have to like tweak it because it was made for a program.

01:11:23 - Brandon Hancock
was the program I was launching, but a lot of it you could steal and copy.

01:11:26 - Brandon Hancock
The key thing is I would hire a video editor between $25 and $30 an hour, anything.

01:11:33 - Brandon Hancock
And that's what I would, I'd cap it at, just so have numbers.

01:11:36 - Alex
Okay.

01:11:37 - Alex
An hour, right?

01:11:38 - Alex
Okay.

01:11:40 - Brandon Hancock
Yeah.

01:11:40 - Brandon Hancock
Editing, no?

01:11:41 - Alex
Yeah.

01:11:42 - Alex
Yeah.

01:11:42 - Alex
So, yeah.

01:11:43 - Alex
So that's, that's what it's going to keep me busy for upcoming weeks.

01:11:48 - Alex
And also I have my final class on Thursday of the, for the government.

01:11:54 - Brandon Hancock
That's awesome.

01:11:55 - Alex
That has been a cool trip and yeah, you know, hopefully get paid.

01:12:02 - Alex
Yeah.

01:12:02 - Brandon Hancock
Any other ways we could leverage that for future opportunities?

01:12:09 - Brandon Hancock
Are you thinking about doing it?

01:12:10 - Brandon Hancock
are you like, no, that was a one-time thing?

01:12:11 - Brandon Hancock
What are you feeling?

01:12:13 - Alex
Yeah, I think it is pretty cool.

01:12:15 - Alex
And now that I have these six sessions, I think there's a lot of lessons learned and kind of like a marketable product.

01:12:27 - Alex
It is very basic.

01:12:28 - Alex
So I might think on trying to go to other local governments and just offering it.

01:12:36 - Alex
I just need to get more grasp on dealing with the government.

01:12:40 - Alex
I got some good advice last week regarding payment.

01:12:47 - Alex
That's awesome.

01:12:48 - Brandon Hancock
Yeah.

01:12:49 - Alex
And then Bastian called it out right.

01:12:50 - Brandon Hancock
Yeah.

01:12:50 - Brandon Hancock
You're probably going to have like net 30, 60, 90.

01:12:52 - Brandon Hancock
Like it's going to be a minute before you get paid.

01:12:54 - Brandon Hancock
But hey, getting paid.

01:12:56 - Alex
That's the important part.

01:12:57 - Brandon Hancock
Yeah.

01:12:57 - Alex
You know, getting my hands dirty.

01:12:59 - Alex
I enjoyed it.

01:13:00 - Alex
And we're very thankful for the opportunity.

01:13:02 - Alex
And yeah, I'm open for more of these.

01:13:04 - Alex
And actually, it's very amazing to see people, how grateful they are, like saying, like, this is going to, this is amazing.

01:13:11 - Alex
Like, it's going to improve my life.

01:13:12 - Alex
And that is so nice, you know, very rewarding to see those reactions.

01:13:19 - Brandon Hancock
That's awesome.

01:13:20 - Alex
Yeah.

01:13:20 - Alex
Yeah.

01:13:20 - Alex
Dude, you're a local hero.

01:13:21 - Brandon Hancock
You're a local AI hero.

01:13:22 - Brandon Hancock
I love it.

01:13:23 - Brandon Hancock
All right.

01:13:24 - Alex
Perfect.

01:13:24 - Brandon Hancock
Well, please keep me posted.

01:13:25 - Brandon Hancock
Let me know if you have questions on the video editor stuff.

01:13:27 - Brandon Hancock
And we'd love to, you know, if y'all do go down the more news letter stuff, we'd love to hear how it goes.

01:13:32 - Brandon Hancock
Because I think that's a really cool opportunity to be in.

01:13:34 - Brandon Hancock
Yeah.

01:13:35 - Alex
Thank you very much, guys.

01:13:36 - Alex
All right.

01:13:36 - Brandon Hancock
Perfect.

01:13:37 - Brandon Hancock
Al, you're up next, Sam.

01:13:39 - Al Cole
So I am piggybacking off of what Alex just said.

01:13:43 - Al Cole
It's interesting.

01:13:43 - Al Cole
We actually have some commonality here.

01:13:46 - Al Cole
So while you were gone, I picked up a couple of gigs.

01:13:50 - Brandon Hancock
And this is me getting my feet wet.

01:13:53 - Al Cole
And so it's early on the pricing.

01:13:57 - Al Cole
What I've got for the first one, because I know I'm learning.

01:14:00 - Al Cole
So with someone I've known for a while, they run a digital agency, so they want automation and they're looking for doing initially a kind of buzz research agent.

01:14:12 - Al Cole
And the newsletter idea was a different format than I was thinking.

01:14:16 - Al Cole
So what they've done is given me access to three clients that they serve and sites where you would find information about those clients.

01:14:25 - Al Cole
So they're looking for kind of a real-time summary of, is there anything out there that as a marketing agency they should be aware of, that they could potentially be exploiting.

01:14:35 - Al Cole
And then they're also looking for crawling social sites, those kinds of things.

01:14:43 - Al Cole
So for me, the way to ease into this, it'll be NAN, I'll probably leverage that initially, and then just see how far I can get leveraging that platform, at least as a starting point.

01:15:01 - Al Cole
You still there, Brandon?

01:15:07 - Al Cole
I see him fading a bit in and out.

01:15:10 - Al Cole
then I, following the...

01:15:12 - Al Cole
I think I told him.

01:15:15 - Al Cole
Go ahead, Brandon.

01:15:16 - Al Cole
You were fading out a bit.

01:15:17 - Al Cole
I see a red there on the bandwidth.

01:15:23 - Alex
I bet there is many cursor activities in the background.

01:15:27 - Alex
Yeah.

01:15:28 - Al Cole
Someone's streaming a nice long movie in the house.

01:15:33 - Al Cole
Anyway, so I have that.

01:15:35 - Al Cole
And I actually have another opportunity that emerged again from another meetup last week.

01:15:41 - Al Cole
So I'm sharing this to the team.

01:15:43 - Al Cole
So I have been intermixing with just business leaders who are coming together just to talk about some AI topics.

01:15:53 - Al Cole
And I got yet another lead.

01:15:54 - Al Cole
I'm speaking to them first time Thursday of this week.

01:15:59 - Al Cole
So...

01:16:06 - Al Cole
Are you there, Brandon?

01:16:09 - Patrick Chouinard
I think he's just Yeah, I'm sorry.

01:16:11 - Brandon Hancock
My computer's just dying.

01:16:13 - Brandon Hancock
I'm closing out of stuff.

01:16:14 - Al Cole
I should be back now.

01:16:15 - Brandon Hancock
I apologize for that.

01:16:16 - Brandon Hancock
I'm just, I'm going to close out of everything except Zoom.

01:16:20 - Brandon Hancock
Maybe it is cursor.

01:16:21 - Brandon Hancock
I'm not even touching it.

01:16:22 - Brandon Hancock
That's wild.

01:16:22 - Brandon Hancock
Okay.

01:16:24 - Brandon Hancock
But, sorry, the area I cut off on was, it sounds like you're literally just hand-to-hand networking is what it sounds like, right?

01:16:31 - Al Cole
That's It's very organic at this point.

01:16:33 - Al Cole
And so just being at these events where we're mixing in business and some, not even strong technical.

01:16:43 - Al Cole
Most of the people that represent technical are people that do more AI strategy discussions, some training.

01:16:49 - Al Cole
There's really no builders in the places that I've been in.

01:16:53 - Al Cole
So that's opened some doors.

01:16:56 - Al Cole
I'm just sharing that that seems to be working.

01:17:00 - Brandon Hancock
So I love boots on the ground.

01:17:03 - Brandon Hancock
You're getting in there doing it yourself.

01:17:04 - Brandon Hancock
A few questions I have, because I think this would be super helpful for the group.

01:17:08 - Brandon Hancock
Are you just saying, because I think the most important thing is just like, how are you presenting yourself to people in these chats?

01:17:14 - Brandon Hancock
Is it just like, hey, I can help?

01:17:17 - Brandon Hancock
Or what do you, I guess, do you, how are you bringing up the conversation in the first place?

01:17:22 - Al Cole
Yeah.

01:17:22 - Al Cole
So I'm focusing more on the solution side.

01:17:25 - Al Cole
So when I've spoken to, so where I'll typically start when I'm in a room is I go find the organizer and I go look at myself.

01:17:34 - Al Cole
I make sure they understand my interest in the group they have and my background and what I bring.

01:17:40 - Al Cole
And the way this happened was the business owner who he describes his, it's a pretty solid marketing firm too.

01:17:49 - Al Cole
He says, I've run it for 10 years as an analog business.

01:17:53 - Al Cole
He goes, we're all old school and it's been a great business, but he knows it is the time now.

01:18:00 - Al Cole
Where he's going to start thinking about automation.

01:18:02 - Al Cole
So he literally went to the organizer while we were at this meeting and says, I need a builder.

01:18:07 - Al Cole
Organizer said, I just met him.

01:18:09 - Al Cole
Go see Al.

01:18:11 - Al Cole
And that's how it happened.

01:18:18 - Brandon Hancock
So it's working organically.

01:18:19 - Al Cole
I'm just sharing.

01:18:20 - Al Cole
Well, congrats, man.

01:18:21 - Brandon Hancock
I am a few, few other.

01:18:25 - Brandon Hancock
That's awesome.

01:18:25 - Brandon Hancock
I absolutely love that.

01:18:27 - Brandon Hancock
I mean, it is 100% scary to go into a room of people you don't know, have no idea what's going to happen next.

01:18:34 - Brandon Hancock
So, dude, take some balls.

01:18:36 - Brandon Hancock
So I absolutely love that you're getting out there and doing that.

01:18:38 - Brandon Hancock
You're doing the hard work.

01:18:39 - Brandon Hancock
So, and the coolest part is the hardest part is what you just did.

01:18:43 - Brandon Hancock
Because now you get success for the first few guys.

01:18:46 - Brandon Hancock
They tell some friends and then you get the next guys.

01:18:48 - Brandon Hancock
So it just literally is a domino at this point.

01:18:51 - Brandon Hancock
So you have done the hardest part, zero to one, hardest part, and you're absolutely crushing it.

01:18:55 - Brandon Hancock
Now we just got to build it, but you're a smart man.

01:18:57 - Brandon Hancock
I know you'll, I know you'll get it done.

01:18:58 - Al Cole
there we go.

01:18:59 - Al Cole
Right.

01:18:59 - Al Cole
So.

01:19:00 - Al Cole
And I've got the right expectations set for the first one.

01:19:04 - Al Cole
And then the second one, I've got backup.

01:19:06 - Al Cole
So the team should know I have access to some engineers that are proven.

01:19:11 - Al Cole
So if through the discovery on Thursday, I need some help, I know between this network and some people I know, I could get that help.

01:19:21 - Brandon Hancock
Absolutely.

01:19:21 - Brandon Hancock
And one other thing I just want to like project forward, like you crush this, you do this for a client or two.

01:19:28 - Brandon Hancock
What's so awesome is once you understand how these systems are built in and out, the real money value making skill in this is actually the networking and landing the deal.

01:19:38 - Brandon Hancock
So, you know, going forward, you really could potentially bring on a developer of some sort, like an N8N developer, probably 30 to 40 an hour.

01:19:46 - Brandon Hancock
And at that point, you're just overseeing and managing the contract and land deals and all the actual like this connects to this, this connects to this.

01:19:58 - Brandon Hancock
You can always do that.

01:19:59 - Brandon Hancock
So just, I mean, I'm just.

01:20:00 - Al Cole
You described it for me.

01:20:01 - Al Cole
You just described exactly the business model I'm looking for is I want to be able to front end it, but I'd like to be able to follow along as I participate in these calls with enough technical so I can at least stare at conversation properly.

01:20:14 - Al Cole
But ultimately, it would be tapping into the talents of others as this thing scales up.

01:20:18 - Al Cole
Yep.

01:20:18 - Al Cole
Yeah.

01:20:19 - Brandon Hancock
And the cool part is everybody wins in that situation, which is awesome.

01:20:22 - Brandon Hancock
So yeah, absolutely love it.

01:20:24 - Brandon Hancock
And yeah, seriously, once again, congrats on landing deals.

01:20:27 - Brandon Hancock
Nothing gets me more excited when you guys start to like bring in money through AI one way or another, like nothing gets me more excited.

01:20:33 - Brandon Hancock
So seriously, congrats, man.

01:20:35 - Al Cole
And let us know how far we can help.

01:20:36 - Al Cole
Appreciate it.

01:20:38 - Brandon Hancock
But it sounds like you're off to an awesome start.

01:20:41 - Brandon Hancock
Okay.

01:20:42 - Brandon Hancock
Perfect.

01:20:43 - Brandon Hancock
It looks like, Amal, am I pronouncing that right?

01:20:46 - Hemal Shah
Yes.

01:20:47 - Hemal Shah
Hey, Brandon.

01:20:47 - Hemal Shah
Welcome, man.

01:20:48 - Brandon Hancock
Welcome, welcome.

01:20:49 - Brandon Hancock
How can we help?

01:20:50 - Brandon Hancock
Glad to see you on the call.

01:20:50 - Hemal Shah
Yep.

01:20:51 - Hemal Shah
This is my second session.

01:20:53 - Hemal Shah
I joined last week.

01:20:55 - Hemal Shah
Paul is doing a great job hosting it.

01:20:58 - Hemal Shah
And I...

01:21:00 - Hemal Shah
And I'm enjoying it.

01:21:01 - Hemal Shah
I don't feel like I'm seeing, meeting you for all of your second time.

01:21:05 - Hemal Shah
I mean, it feels like a good, good, close knit community.

01:21:08 - Hemal Shah
So thank you again.

01:21:09 - Hemal Shah
I already feel I'm part of this, this amazing group.

01:21:13 - Hemal Shah
Glad to have you here.

01:21:15 - Brandon Hancock
And, and Brandon, I'm, I'm from Atlanta coming area.

01:21:18 - Hemal Shah
So I heard that you are also in Georgia, Atlanta area.

01:21:21 - Hemal Shah
So looking forward to meet you sometime in near future.

01:21:24 - Hemal Shah
If there are meetups or anything, um, do, do let us know if there are any, uh, meetups in Atlanta area that you recommend.

01:21:32 - Hemal Shah
Yeah.

01:21:32 - Hemal Shah
The second I'm up there for an event, I will let you, I'll, I'll do a post.

01:21:36 - Brandon Hancock
So, um, cause I would love to get to meet, meet some of you guys in real life.

01:21:39 - Brandon Hancock
So 100%, I will let you know.

01:21:41 - Hemal Shah
Yeah.

01:21:42 - Hemal Shah
Um, um, um, and I'm, I've been focusing on, so for my company, uh, they are going to open up more, um, allow AI related tools.

01:21:51 - Hemal Shah
Uh, it was like close knit.

01:21:52 - Hemal Shah
They do, they wanted to do a lot of, you know, security and, and other, uh, to research and make sure all the policies are in place.

01:22:00 - Hemal Shah
So they're going to open it up in coming weeks, and right now I'm focusing on capturing all the best practices, identifying the right framework that we'll be using to create different AI-based applications, and we are mostly GCP shop.

01:22:18 - Hemal Shah
So Google Cloud is what we are using, and that's where I was researching different Google ADK agents, and that's where I learned into your masterclass and came to know about this amazing community.

01:22:31 - Hemal Shah
So that is what I'm looking into it.

01:22:33 - Hemal Shah
I'm focusing it a bit more on end-to-end development process that I can lay down the whole path for my company, so other engineers, they can look into that.

01:22:44 - Hemal Shah
For Google ADK, evals is another thing that I'm trying to find some information around, so that is one thing on my plate to explore a little bit, how to use evals in Google ADK.

01:23:00 - Hemal Shah
So, yeah, that's what I've been focusing on.

01:23:03 - Hemal Shah
I do have a couple of questions.

01:23:04 - Hemal Shah
So you mentioned about the React Markdown earlier.

01:23:09 - Hemal Shah
And I'm wondering if there are any other similar options where I am understanding is React Markdown will, you know, provide the responses in more polished ways.

01:23:20 - Hemal Shah
But what if we want to also get some information from end user, not in a plain text, but maybe it's we are for booking a flight.

01:23:28 - Hemal Shah
User did not put in a date.

01:23:30 - Hemal Shah
So we want to date from end user, but we want to show them nice widgets, calendar widget or something.

01:23:35 - Hemal Shah
So dynamic generation form sort of thing where instead of just text, you know, I've been thinking to explore something around that.

01:23:44 - Hemal Shah
And if you have any recommendation on libraries that can give a jump start, that will appear.

01:23:49 - Hemal Shah
Yeah.

01:23:50 - Brandon Hancock
So I can go ahead and tell you high level, like what I've done recently.

01:23:54 - Brandon Hancock
So ADK is the one I've been using the most recently.

01:23:57 - Brandon Hancock
And for example...

01:24:00 - Brandon Hancock
Um, what I'm doing is a combination of structured outputs and like an author message to determine what message to show.

01:24:10 - Brandon Hancock
I can actually, I can show it in just a second.

01:24:13 - Brandon Hancock
I'm, I just hope my internet doesn't keep fighting me.

01:24:16 - Brandon Hancock
Um, I can, I'll open it up and I'll run it.

01:24:18 - Brandon Hancock
But long story short, what I do is once agents respond, I check who sent the message and I'll check, um, using some structured outputs of like what else is needed.

01:24:29 - Brandon Hancock
In your case, if it was the agent could respond with a structured output of like input field or input type, and you would just say like calendar widget, um, billing information widget, like whatever the widget is you want to show, you could just have that pop up in real time, um, and show dynamic UIs and take it beyond just a regular chat message back and forth.

01:24:51 - Brandon Hancock
So, um, if, um, cursor will run here in a second, I can, I can show an example and just a little bit of how I've used it.

01:24:59 - Brandon Hancock
choice?

01:24:59 - Brandon Hancock
Let's go.

01:25:00 - Brandon Hancock
To actually show some, in my case, I want people to be able to download PDFs.

01:25:04 - Brandon Hancock
I want people to be able to like, when agent A responds to show it in this custom format.

01:25:09 - Brandon Hancock
let me actually just, I can show it real fast.

01:25:12 - Brandon Hancock
It's spinning up and I'll show you.

01:25:14 - Brandon Hancock
Yeah.

01:25:15 - Hemal Shah
Okay, cool.

01:25:16 - Hemal Shah
Something like React JSON form and some of those libraries that can, you know, based on metadata can generate dynamic UI.

01:25:24 - Hemal Shah
But just wondering.

01:25:27 - Brandon Hancock
Yeah, I mean, the cool part is, is it really comes down to the agents are smart enough to tell you when they need information.

01:25:34 - Brandon Hancock
The input fields that you're collecting information from, it's just at the end of the day, it's context.

01:25:38 - Brandon Hancock
It's context that's going to go back into the agent in a form of a raw string.

01:25:43 - Brandon Hancock
So let me just show you what I've done.

01:25:47 - Brandon Hancock
You guys can see.

01:25:50 - Brandon Hancock
So like, for example, whenever an agent, whenever I get something back from this agent, I know I need to update the chat message to start showing a PDF.

01:25:59 - Brandon Hancock
Yeah.

01:26:00 - Brandon Hancock
The people can download a PDF.

01:26:02 - Brandon Hancock
I have an evaluator, so evaluators need to respond using a different message format.

01:26:07 - Brandon Hancock
So it's just like per author and per event, you dynamically change the message event.

01:26:14 - Brandon Hancock
And what this looks like in code, just to like go deeper really fast, let me just do it to the side.

01:26:19 - Brandon Hancock
But basically you have like a parent wrapper class.

01:26:23 - Brandon Hancock
What's that?

01:26:24 - Brandon Hancock
Control A.

01:26:24 - Brandon Hancock
So what you end up having is like a message wrapper, and you basically just do like, you know, if it is like from this author, you know, you show this component.

01:26:37 - Brandon Hancock
So you basically just wrap it and then just have a switch statement to dynamically determine what type of UI to load.

01:26:43 - Brandon Hancock
That's how I've been tackling it, and hopefully that helps.

01:26:56 - Brandon Hancock
You may have to send Brandon some money to upgrade it.

01:27:00 - Marc Juretus
56k modem, man, he's really, is that US Robotics, Brandon?

01:27:07 - Brandon Hancock
Because agents are getting, seriously, I mean, put me on dial-up, let me, let me swap over to a hot spot, I apologize, it works fine all day, I'll hop to a hot spot, I apologize for that, one second.

01:27:35 - Patrick Chouinard
That always happened in the worst possible time, always seemed to happen to me when I'm giving training, I have like 50 people on the line.

01:27:44 - Brandon Hancock
Okay, I think we're good, we're on a hot spot now, I have no idea, it's never happened on a call before, so I guess we're good, we are hot spotting, so if this time, if it goes out, it's making the internet hate me.

01:28:00 - Brandon Hancock
At this point.

01:28:00 - Brandon Hancock
So I think we should be good.

01:28:03 - Brandon Hancock
But, Hemal, was I able to answer a question?

01:28:06 - Hemal Shah
Yes, yes.

01:28:08 - Brandon Hancock
Hopefully that was enough ideas.

01:28:11 - Brandon Hancock
Yes, that's great.

01:28:16 - Brandon Hancock
Perfect.

01:28:17 - Brandon Hancock
Well, well, glad to have you back for the second time.

01:28:19 - Brandon Hancock
Sorry I missed you last week.

01:28:20 - Hemal Shah
But yeah, excited, excited to have you here.

01:28:24 - Brandon Hancock
Perfect.

01:28:25 - Brandon Hancock
All right.

01:28:26 - Brandon Hancock
I think next up was Jusin, but I think he said he had to leave.

01:28:31 - Brandon Hancock
So, Bastian, you're up next, man.

01:28:38 - Brandon Hancock
I know.

01:28:39 - Brandon Hancock
Bastian was online.

01:28:41 - Brandon Hancock
Oh, skip you.

01:28:42 - Brandon Hancock
Noisy.

01:28:43 - Brandon Hancock
Okay, cool.

01:28:45 - Brandon Hancock
After that was Matthew.

01:28:47 - Brandon Hancock
If Matthew's still here.

01:28:50 - Brandon Hancock
There's a long list.

01:28:51 - Brandon Hancock
Matthew's not here.

01:28:53 - Brandon Hancock
Tolu.

01:28:55 - Brandon Hancock
Tolu's not here.

01:28:57 - Brandon Hancock
Fitz.

01:29:00 - Brandon Hancock
I think Fitz is here.

01:29:05 - Brandon Hancock
If Fitz, if you're busy, Timoteo.

01:29:12 - Brandon Hancock
We're going to get someone.

01:29:16 - Brandon Hancock
All right.

01:29:17 - Brandon Hancock
If not, we're just going to go with people who have.

01:29:21 - Brandon Hancock
Yo, there he is.

01:29:25 - Brandon Hancock
How's it going, man?

01:29:26 - Brandon Hancock
How can we help?

01:29:29 - Temitayo Gbolahan
Yeah, I'm good.

01:29:31 - Temitayo Gbolahan
What about you?

01:29:33 - Brandon Hancock
I'm doing good.

01:29:34 - Brandon Hancock
It's funny.

01:29:34 - Brandon Hancock
Earlier today when I was coding, same thing.

01:29:37 - Brandon Hancock
Hood's up, man.

01:29:39 - Brandon Hancock
That's how I code deep mode.

01:29:41 - Brandon Hancock
I put my blinders on and it's nothing but me and the screen.

01:29:44 - Temitayo Gbolahan
So I feel you.

01:29:47 - Temitayo Gbolahan
Yeah.

01:29:48 - Temitayo Gbolahan
Okay.

01:29:48 - Temitayo Gbolahan
So last week, we launched a version two of our app, Orientee.

01:29:55 - Temitayo Gbolahan
I talked about it once in a while.

01:30:01 - Temitayo Gbolahan
It's an orientation platform for, you know, those guys getting ready to go to college, university, and they are finding it difficult to choose a career path.

01:30:15 - Temitayo Gbolahan
So they basically use AI to analyze their scores and everything, and they also give them some recommendations and they can actually continue.

01:30:25 - Temitayo Gbolahan
So we launched, we got about 80 sign-ups, we have too long going on that.

01:30:32 - Temitayo Gbolahan
Now, the funniest part about it is that we were working on production environment.

01:30:45 - Temitayo Gbolahan
So one of the leads, he wanted us to have a test environment so that we could run up some tests before we roll back to get them into production.

01:30:57 - Temitayo Gbolahan
So we had a VPS and and and

01:31:00 - Temitayo Gbolahan
Everything was going on well on CLS.

01:31:04 - Temitayo Gbolahan
Okay, so basically what happened was Did you delete something?

01:31:11 - Temitayo Gbolahan
Oh no, oh no.

01:31:15 - Temitayo Gbolahan
I had the...

01:31:18 - Temitayo Gbolahan
We had the stuff on DPS, so we used CITB to make sure everything goes on the automation well.

01:31:26 - Temitayo Gbolahan
So I just forgot one simple command, a minus T, like a hyphen T that I was to put in a joker compose.

01:31:37 - Temitayo Gbolahan
So I ran out a command for the test database, for the test environment, and everything in production, white guys.

01:31:47 - Temitayo Gbolahan
Everything.

01:31:48 - Temitayo Gbolahan
Oh no, that's the worst feeling.

01:31:53 - Temitayo Gbolahan
That's the worst.

01:31:54 - Brandon Hancock
Well, hey, how quickly did you get it back up?

01:31:56 - Brandon Hancock
That's the important part.

01:31:57 - Brandon Hancock
How long, how long did it take to recover?

01:31:59 - Temitayo Gbolahan
Yeah, was...

01:32:00 - Temitayo Gbolahan
To get to the chat box, it took us to our search for that, but we didn't record that at least we had to email so that everyone is signed up and to look up to the chat box, so what we got to the extent of my email.

01:32:16 - Brandon Hancock
Temitayo, sorry, real fast, dude, sorry, real fast, the mic, it's like really hard to hear, that might just be me, but it was just kind of hard to hear you.

01:32:30 - Temitayo Gbolahan
Okay, can you hear now?

01:32:32 - Brandon Hancock
Oh, so much better.

01:32:35 - Temitayo Gbolahan
Okay.

01:32:37 - Temitayo Gbolahan
So, we were able to, since we had the emails of everyone and we had the list of paid users too, so what we just did was send a mass email for them to sign up again, which they did.

01:32:53 - Temitayo Gbolahan
So, everything's up and I'm ready So, you like dropped a table, so you like dropped a full, like you deleted it.

01:33:00 - Temitayo Gbolahan
The whole database, everything, like, it flushed, like, with everything.

01:33:06 - Brandon Hancock
Oh, no.

01:33:08 - Brandon Hancock
Oh, no.

01:33:10 - Brandon Hancock
Dude, that is, that is biggest fear at every startup I've worked at is hitting the deploy button.

01:33:17 - Brandon Hancock
That is always my biggest fear because, like, that actually does happen.

01:33:23 - Brandon Hancock
Like, it's, and it's so easy.

01:33:24 - Brandon Hancock
You said you missed, like, a dash three or something.

01:33:26 - Brandon Hancock
That is, dude, that is, that is a nightmare.

01:33:28 - Brandon Hancock
That is, like, I have nightmares about that.

01:33:31 - Brandon Hancock
So I feel for you, man.

01:33:32 - Brandon Hancock
You're resilient, though.

01:33:33 - Brandon Hancock
You bounced back.

01:33:35 - Brandon Hancock
Quick question.

01:33:36 - Brandon Hancock
Did you have backups?

01:33:37 - Brandon Hancock
Oh, I can't remember.

01:33:38 - Brandon Hancock
Yeah, at that time, at that time, we didn't have any backup.

01:33:42 - Temitayo Gbolahan
So that was the biggest mistake we did.

01:33:44 - Temitayo Gbolahan
That was the biggest mistake.

01:33:47 - Brandon Hancock
Gotcha.

01:33:48 - Brandon Hancock
Were you, just out of curiosity, are you deploying, where is your database deployed?

01:33:51 - Brandon Hancock
What are you using, out of curiosity?

01:33:54 - Temitayo Gbolahan
Okay, okay.

01:33:55 - Temitayo Gbolahan
So we, we got a VPS on, uh, this guy's Contabo.

01:33:59 - Brandon Hancock
I think Contabo is.

01:34:01 - Brandon Hancock
Okay.

01:34:03 - Temitayo Gbolahan
So you're using like custom stuff, right?

01:34:06 - Brandon Hancock
Yeah.

01:34:06 - Brandon Hancock
So you're using, okay.

01:34:08 - Brandon Hancock
Really quick recommendation.

01:34:09 - Brandon Hancock
I mean, especially like, I don't know how many people are using the app, but like Neon or Supabase, you could get so far on the free tier and it automatically has built in backups every 24 hours.

01:34:24 - Temitayo Gbolahan
I think both of them.

01:34:25 - Brandon Hancock
So, so like, just, just if you're looking for something that is free to use, I would definitely look at both of those just because, like I said, when you're doing custom stuff, it's so easy to accidentally do that.

01:34:38 - Brandon Hancock
And, you know, and then all that progress you made, it's just hard to get back the momentum, you know?

01:34:43 - Brandon Hancock
So we definitely recommend checking out both of those if you're, if you're looking for, for other options, but it sounds like y'all have made a ton of progress and more redundant now, but yeah, those would be my two, two recommendations.

01:34:57 - Temitayo Gbolahan
Okay.

01:34:57 - Temitayo Gbolahan
Thank you very much.

01:35:00 - Brandon Hancock
Of course.

01:35:00 - Brandon Hancock
Of course.

01:35:01 - Brandon Hancock
All right, dude.

01:35:01 - Brandon Hancock
Well, awesome.

01:35:03 - Brandon Hancock
Okay.

01:35:03 - Brandon Hancock
We'll keep on, keep on cruising.

01:35:05 - Brandon Hancock
I think it is Juan, then Mitch, then Patrick.

01:35:12 - Juan Torres
Hello, folks.

01:35:13 - Juan Torres
Can you guys hear me?

01:35:15 - Brandon Hancock
Yep.

01:35:15 - Brandon Hancock
Sounds great.

01:35:17 - Juan Torres
Hey, good, good.

01:35:18 - Juan Torres
I just came from a trip to Istanbul, Turkey.

01:35:23 - Juan Torres
I'm still recovering.

01:35:25 - Juan Torres
I think I got some degree of food poisoning.

01:35:29 - Brandon Hancock
I don't know, man.

01:35:30 - Brandon Hancock
It's hard to hear that.

01:35:32 - Juan Torres
Yeah, no, it's okay.

01:35:32 - Juan Torres
But it was, it was awesome.

01:35:34 - Juan Torres
It was, it was great.

01:35:35 - Juan Torres
It was just, I got invited to present my data science, data engineering project on the concentration of banking, which is kind of like a economic, econometric modeling project.

01:35:49 - Juan Torres
And people, people really liked it.

01:35:52 - Juan Torres
So it was really awesome.

01:35:55 - Juan Torres
Then I got to explore Istanbul.

01:35:59 - Juan Torres
Actually, I'm going send you guys.

01:36:00 - Juan Torres
It's some awesome pictures from Istanbul.

01:36:02 - Juan Torres
I think you guys are going to really, really like it.

01:36:06 - Brandon Hancock
No.

01:36:07 - Brandon Hancock
I've there for a layover, and it's different.

01:36:10 - Brandon Hancock
It's different than any Western country.

01:36:13 - Brandon Hancock
I mean, it's just a different culture.

01:36:15 - Brandon Hancock
So, like, it is crazy different.

01:36:16 - Brandon Hancock
Very cool experience.

01:36:18 - Juan Torres
Yeah, yeah.

01:36:19 - Juan Torres
It was really awesome.

01:36:22 - Juan Torres
Here's the pictures I took over there.

01:36:25 - Juan Torres
And here are some of the pictures of the presentation.

01:36:30 - Juan Torres
The itself.

01:36:33 - Juan Torres
Dude, what a stud.

01:36:36 - Al Cole
Amazing.

01:36:39 - Al Cole
Wow.

01:36:41 - Al Cole
Yeah, it's so beautiful over there.

01:36:43 - Juan Torres
It is incredible.

01:36:45 - Juan Torres
It's, like I said in the message, the collective unconscious, like, really gets re-activated when you see the great Arab, Ottoman, Byzantinian archives.

01:37:01 - Juan Torres
It is truly amazing.

01:37:04 - Brandon Hancock
Did you get to try some Turkish coffee?

01:37:06 - Brandon Hancock
I hope you did.

01:37:09 - Juan Torres
I did.

01:37:10 - Juan Torres
It was great.

01:37:12 - Juan Torres
The only thing is that I brought some Turkish coffee and apparently on June there was implementation of no pottery material being imported at 300 milligrams or grams, I mean.

01:37:26 - Juan Torres
So my whole Turkish coffee was thrown away when I tried to import it from Turkey to the U.S.

01:37:33 - Brandon Hancock
Yeah.

01:37:33 - Brandon Hancock
No.

01:37:34 - Brandon Hancock
Dang.

01:37:35 - Brandon Hancock
Dang.

01:37:35 - Brandon Hancock
Dang.

01:37:36 - Brandon Hancock
Well, hey, at least you got to try it.

01:37:38 - Brandon Hancock
You got to try it once.

01:37:40 - Juan Torres
Yeah.

01:37:41 - Juan Torres
Dude, how can we help?

01:37:43 - Brandon Hancock
What else is going on?

01:37:45 - Juan Torres
So right now I have too much client work.

01:37:49 - Juan Torres
It's not good.

01:37:52 - Juan Torres
I think it's and there's this physician, surgeon, Brazilian.

01:38:00 - Juan Torres
That approached me through LinkedIn, and he wants me to help him essentially get his Rack system working.

01:38:12 - Juan Torres
He's using Chroma, he's using OpenAI, Embedded Models, and I don't think I have the time right now to be able to do.

01:38:26 - Juan Torres
I could do it by the end of the month, but I don't want to get too much work and not deliver good results for everyone.

01:38:34 - Juan Torres
So that's why I'm thinking of loading this client work, just so I can keep everybody happy.

01:38:43 - Juan Torres
Can I, real quick, pause to add to that?

01:38:45 - Brandon Hancock
I mean, kind of like what we just discussed with Al, like at this point, I mean, getting the deal, networking, landing the client, that is arguably one of the hardest parts.

01:38:58 - Brandon Hancock
So So

01:39:00 - Brandon Hancock
The typical structure that I've seen most developers do is offer some sort of to another developer like, hey, I'll take anywhere between 20 to 30 percent and you do the work and then you just charge the client, you know, high, high dollar amount.

01:39:14 - Brandon Hancock
That structure works.

01:39:15 - Brandon Hancock
Everyone's incentives are aligned.

01:39:17 - Brandon Hancock
You know, you did you got the deal.

01:39:19 - Brandon Hancock
You're probably going to do some project oversight and then you hand it to the another developer who might not be like fully doing all sorts of like networking outreach.

01:39:27 - Brandon Hancock
So everybody wins in that situation.

01:39:29 - Brandon Hancock
So we're definitely looking to that so you don't lose the client, you know.

01:39:33 - Juan Torres
Yeah, I was actually thinking of doing that also.

01:39:38 - Juan Torres
I do have a couple connections here in San Diego of people that could help me with the RAC system.

01:39:45 - Juan Torres
And the RAC problem is not from my assessment is not that big.

01:39:49 - Juan Torres
I think what he needs is context engineering to get his agentic system to really work because he's a really specialized.

01:39:57 - Juan Torres
Surgeon physician and.

01:40:00 - Juan Torres
He's having issues with retrieval because of the specificity of the medical terms that he's using.

01:40:06 - Juan Torres
So I'm telling him, my hypothesis is that he needs to create an embedding of the terminology and have a specialized agent that correlates the query of the user to the specific documents that he wants to pull.

01:40:27 - Brandon Hancock
Have you got to keep behind the curtain?

01:40:30 - Brandon Hancock
Do you know what embedding model they're using?

01:40:32 - Brandon Hancock
Do you know any of that?

01:40:35 - Juan Torres
I haven't seen his architecture.

01:40:37 - Juan Torres
In fact, I didn't even have a chance to talk to his senior developer because he couldn't make it.

01:40:45 - Juan Torres
But from the one that he was telling me, it was the OpenAI text.

01:40:52 - Juan Torres
What is it called?

01:40:59 - Juan Torres
Texted.

01:41:00 - Juan Torres
I can send it to you on the chat once I find it.

01:41:04 - Juan Torres
But the embedding model, I thought that the initial issue was that he was trying to align different models and mixing with different embedding models, but that might not seem to the issue.

01:41:18 - Juan Torres
My two hypothesis is the issue of context engineering or the fact that he's using several vector databases.

01:41:27 - Juan Torres
And so the model in the Agentex system does not know from which database it has to retrieve the documents.

01:41:37 - Brandon Hancock
I got you.

01:41:38 - Brandon Hancock
One, a few other helpful tips, think.

01:41:42 - Brandon Hancock
I think Maxim, if you are looking for a developer, I think Maxim was taking on some RAG stuff.

01:41:47 - Brandon Hancock
mean, Maxim is like the RAG expert.

01:41:50 - Brandon Hancock
So if you just wanted to hand it to competent hands, I think he was looking for just a few bit of extra work.

01:41:55 - Brandon Hancock
So I would definitely connect to him.

01:41:59 - Brandon Hancock
If it.

01:42:00 - Brandon Hancock
You just want to, like, not have to worry about it and just know someone's going to do a good job.

01:42:04 - Brandon Hancock
100% would connect with Maxim.

01:42:08 - Brandon Hancock
But yeah, RAG can be tricky because it doesn't work until it works really well.

01:42:12 - Brandon Hancock
So, yeah.

01:42:14 - Brandon Hancock
There's probably a hundred or a dozen small issues that could be going wrong.

01:42:18 - Brandon Hancock
So, yeah, this one could be tricky.

01:42:21 - Juan Torres
I feel like Maxim is being requested by everyone, though.

01:42:24 - Juan Torres
I think he's, like, in Super The Man.

01:42:29 - Brandon Hancock
Yeah, but hey, I'd reach out.

01:42:31 - Brandon Hancock
I think he had a lull recently.

01:42:33 - Brandon Hancock
So, if you're looking for a fellow AI buddy, we'd definitely reach out to him.

01:42:38 - Juan Torres
Awesome.

01:42:39 - Juan Torres
Okay.

01:42:39 - Juan Torres
Perfect.

01:42:40 - Brandon Hancock
Dude, well, please keep us posted.

01:42:41 - Brandon Hancock
And seriously, congrats for the client work.

01:42:45 - Brandon Hancock
Awesome, awesome problem to work on.

01:42:47 - Brandon Hancock
That's been super fun.

01:42:48 - Brandon Hancock
So, very, very cool.

01:42:49 - Brandon Hancock
You're getting very cool.

01:42:50 - Brandon Hancock
Very glad you're getting cool work.

01:42:51 - Brandon Hancock
This is the fun stuff.

01:42:54 - Brandon Hancock
But yeah.

01:42:54 - Brandon Hancock
Thank you, Keep us in the loop.

01:42:55 - Brandon Hancock
And if you run it into any technical issues, diving to this stuff, always happy.

01:43:00 - Brandon Hancock
The drop more, like, I would check this out or, you know, look at this kind of thing.

01:43:05 - Juan Torres
One more thing, if I may, technical-wise.

01:43:08 - Brandon Hancock
Yeah.

01:43:11 - Juan Torres
Of course.

01:43:12 - Juan Torres
So for one of my clients, I've successfully deployed a model in a server, Oculus server.

01:43:21 - Juan Torres
Now I have to go through the process of, I have two tests at hand.

01:43:25 - Juan Torres
One is testing the model, right?

01:43:29 - Juan Torres
I've downloaded some CUDA libraries in order to test the stress level I'm placing on the A100 GPU for the local server.

01:43:43 - Juan Torres
From the last attempt I tried to do a simple test, it didn't work out.

01:43:49 - Juan Torres
So I'm assuming that even the 8 billion parameter model that I deployed might not be sufficient or might be too big for the specific GPU.

01:44:00 - Juan Torres
So that's one of the things if anyone had experience in stress testing at GPU.

01:44:06 - Juan Torres
And then secondly, my clients, the people in charge of managing the data center are attempting to charge him about $15,000 to $20,000 to create an API recall tool to basically allow the AI to communicate externally.

01:44:36 - Juan Torres
to other servers.

01:44:39 - Juan Torres
So I am hypothesizing that perhaps I could help him create this networking tool without actually having to spend, you know, $15,000 to $20,000.

01:44:53 - Juan Torres
And so I'm not putting the risk on him.

01:44:55 - Juan Torres
even tell him, like, look, if this API tool that I create internally doesn't

01:45:00 - Juan Torres
Work.

01:45:01 - Juan Torres
I'm not going to charge you any money, but I don't know if anyone also had experience with that.

01:45:09 - Brandon Hancock
Not at that like bare metal level, definitely out of my wheelhouse, but if anyone else on the call does, you know, would be curious.

01:45:19 - Brandon Hancock
Also, seriously, like, you know, if you want to do a community post on that, dude, go for it.

01:45:23 - Brandon Hancock
Just because, like, there are, I mean, there's 9,000 people, like, I'm sure there's someone that has more, you know, met, like, played with the actual, like, CUDA libraries and, like, working on all that.

01:45:34 - Brandon Hancock
So I'm sure there's someone in the community.

01:45:37 - Brandon Hancock
That's not my wheelhouse, though.

01:45:41 - Brandon Hancock
Yeah, dude, you're getting work all across the spectrum.

01:45:45 - Juan Torres
Absolutely love it.

01:45:45 - Juan Torres
It's funny.

01:45:46 - Brandon Hancock
It's like when you have, like, oh, you're in software.

01:45:50 - Brandon Hancock
Can you help me with my printer?

01:45:51 - Brandon Hancock
Like, I feel like it's at that level of, like, oh, you use AI.

01:45:55 - Brandon Hancock
Cool.

01:45:55 - Brandon Hancock
Help me with everything, you know?

01:45:57 - Brandon Hancock
So, I mean, it's a good spot to be in, though.

01:46:00 - Brandon Hancock
Oh, the dollar dollar.

01:46:01 - Juan Torres
Can be my therapist?

01:46:02 - Juan Torres
Yeah, seriously.

01:46:06 - Brandon Hancock
All right, perfect.

01:46:07 - Brandon Hancock
Mitch, you're up next, man.

01:46:11 - Mitch
Juan, I know this doesn't help, but I saw a video that I was doing somewhat of what you were doing on YouTube, but it wasn't all of it, like a building API and stuff, but there's videos out there.

01:46:21 - Mitch
Maybe ask Chad Gbd to find a video for you or some videos and you might find them, but yeah.

01:46:29 - Mitch
But what's going on in Mitchlands?

01:46:33 - Mitch
Well, so basically I'm trying to figure out, I'm able to do basically the Google Cloud Functions, I'm running in local development, and I'm able to get it to mostly work.

01:46:44 - Mitch
Now I'm getting to the point where I need to have it get triggered by like a webhook, and when I'm in local Python land, right, I don't necessarily know how to hook over.

01:46:57 - Mitch
So I'm getting need webhook.

01:47:00 - Mitch
Into like the local development, I'm guessing I would use like Ngrok and something like that to build up like a kind of local development to public land.

01:47:10 - Mitch
I was just curious about any opinion on that.

01:47:14 - Brandon Hancock
Yeah, so there's, okay, so there's a few, there's a few ways we can do what you're trying to do.

01:47:19 - Brandon Hancock
So are, are you using cloud, cloud run or cloud functions?

01:47:23 - Brandon Hancock
Which one, which one are you doing?

01:47:25 - Mitch
You know, it was so confusing because they changed the name.

01:47:27 - Mitch
So there's cloud run, but you can still run it on the Docker image or you can run it on the cloud function.

01:47:34 - Mitch
So it's technically called cloud run, even if it's for Google cloud functions.

01:47:39 - Mitch
But yeah, it's cloud functions, technically speaking, but it's still on run.

01:47:44 - Brandon Hancock
Okay, that one, that's trippy.

01:47:45 - Brandon Hancock
Yeah.

01:47:47 - Brandon Hancock
So here's, here's usually how, like the split works just for everyone's, you know, awareness.

01:47:52 - Brandon Hancock
Like cloud run is usually for very long running jobs, like the worst, like you could, you basically just could have a couple.

01:48:00 - Brandon Hancock
Full-blown, like, fast API server just running and deployed and always listening forever.

01:48:06 - Brandon Hancock
Like, it's running the API forever.

01:48:10 - Brandon Hancock
Cloud functions are more like Lambda functions, if you're familiar with that, on AWS, where it's like you send in a request, and it will, like, spin up and generate a quick response and throw the answer back.

01:48:22 - Brandon Hancock
So, in your case, here's what you could do.

01:48:27 - Brandon Hancock
From my understanding, you were working on a sequence for your videos to where you make a request, and then it just goes prompt A, B, C, D, E, spits out a final result, okay?

01:48:38 - Brandon Hancock
So, there's multiple ways you could tackle this.

01:48:45 - Brandon Hancock
Option one is really just use, because I, let me, let me check timeout periods.

01:48:51 - Brandon Hancock
I just want to make sure I'm not giving you bad answers.

01:48:54 - Brandon Hancock
Okay, okay, so a cloud...

01:49:00 - Brandon Hancock
Function caps out at 60 minutes, which is way less than what I think your stuff's ever going to hit.

01:49:06 - Brandon Hancock
What are you at?

01:49:07 - Brandon Hancock
Eight minutes max?

01:49:08 - Brandon Hancock
Probably something like that.

01:49:10 - Mitch
we're using like 03, yeah.

01:49:11 - Mitch
About that, yeah.

01:49:13 - Brandon Hancock
Okay.

01:49:13 - Brandon Hancock
So, I mean, what you really could do is you'll usually want to do a few things.

01:49:19 - Brandon Hancock
You'll want to have some sort of cloud task scheduler to like, you submit, everything's Q-based.

01:49:25 - Brandon Hancock
So you would submit something to the database, A, kick off a job.

01:49:30 - Brandon Hancock
That gets added to a task.

01:49:32 - Brandon Hancock
That task then gets consumed by your cloud function, does the work, and saves it back to your database.

01:49:38 - Brandon Hancock
That is what the loop, if I was to build this, would look like.

01:49:42 - Brandon Hancock
What's nice about this is every time you submit a request, the way you're spinning things up with your Google Cloud task is it can actually like handle unlimited requests.

01:49:51 - Brandon Hancock
Every request is going to spin up its own thing and just go to work.

01:49:55 - Brandon Hancock
So that's, you could totally go down that approach.

01:49:58 - Brandon Hancock
Which, you'll probably see.

01:50:00 - Brandon Hancock
Save money doing this cloud tasks where it auto scales up and auto scales down.

01:50:05 - Brandon Hancock
Because if you were to do cloud run where you had this running like as a backend job forever in Google Cloud, I think it's like $60 a month to have like their basic version running 24 seven.

01:50:15 - Brandon Hancock
So like, you know, if you just had a backend server running constantly, like a background worker, it would be probably closer to 60 a month.

01:50:24 - Brandon Hancock
Whereas cloud functions, it's only going to spin up when it's working.

01:50:27 - Brandon Hancock
So it's probably going to be like a dollar a month.

01:50:29 - Brandon Hancock
So you're saving a lot doing this.

01:50:31 - Brandon Hancock
The kicker though is like...

01:50:32 - Mitch
2 million invocations for free a month.

01:50:36 - Mitch
Okay, perfect.

01:50:36 - Brandon Hancock
Yeah.

01:50:37 - Brandon Hancock
So, so, so yeah, the main, the main kicker is how do you trigger this?

01:50:41 - Brandon Hancock
The two options are cloud task or event arc.

01:50:46 - Brandon Hancock
Like those are the two, two main ways.

01:50:47 - Mitch
Oh, sorry.

01:50:48 - Mitch
It's a super face has their web hook tooling.

01:50:51 - Mitch
So then it would even create it.

01:50:53 - Mitch
Right.

01:50:53 - Mitch
I just don't know how to test it on local development or.

01:50:59 - Mitch
Yeah.

01:50:59 - Mitch
Stuff.

01:51:01 - Mitch
I got you.

01:51:02 - Brandon Hancock
that's the hard part about cloud versus local is like they're two completely different paradigms because like you can't locally just clone event arc like that's in Google, you know, so, so you, yeah, I would be happy to go deep in this rabbit hole.

01:51:19 - Brandon Hancock
But once you usually get to a spot like where you're at, like you're almost testing in the cloud, like testing locally is starting to become less of a thing because you're so reliant on the cloud.

01:51:31 - Brandon Hancock
The good news is though, you just spin up a production environment and a development environment, test the heck out of development until it's working, and then copy the changes to production.

01:51:40 - Brandon Hancock
That's usually what I've seen most people do in these scenarios, because you can't test anymore locally.

01:51:46 - Brandon Hancock
Like you're using cloud services that do not exist locally anymore.

01:51:50 - Brandon Hancock
So like you're, you're in the big boy leagues in the cloud.

01:51:55 - Brandon Hancock
Um, so I know I threw a lot at you.

01:51:59 - Brandon Hancock
Questions.

01:52:02 - Mitch
No, no, I don't have any questions.

01:52:04 - Mitch
It's just a lot of pain.

01:52:06 - Mitch
There's a lot of pain behind this.

01:52:09 - Brandon Hancock
What I would do, I know you have some of the ship kit templates.

01:52:13 - Brandon Hancock
What I have found super helpful is to use the diagram tool to say, like, map out my backend workflow just so you can see it.

01:52:23 - Brandon Hancock
And it also comes with an analysis to the side.

01:52:26 - Brandon Hancock
And then once it generates that analysis, just be like, is there a simpler way to do this?

01:52:30 - Brandon Hancock
Because 99% of the time, there's something simpler.

01:52:32 - Brandon Hancock
So that's, that's what I would do if I was you.

01:52:36 - Brandon Hancock
And also, like, if you want to, like, I don't if you have it ready now, we could just at the very end of the call or next week's call.

01:52:42 - Brandon Hancock
But if you do want to have that diagram spun up, we'd be happy to just critique it for you.

01:52:47 - Brandon Hancock
And we can get some, everyone could look at it.

01:52:50 - Mitch
And side question, are you using Cloud Code more than Cursor recently?

01:52:55 - Mitch
Or are you still on the Cursor lane?

01:52:58 - Brandon Hancock
Cursor, Cursor 99%.

01:53:00 - Brandon Hancock
At time.

01:53:01 - Brandon Hancock
Yeah.

01:53:02 - Brandon Hancock
And Bastian is saying the same thing.

01:53:04 - Brandon Hancock
It is advanced.

01:53:05 - Brandon Hancock
You're going to learn a ton, but like you are in the deep end, man.

01:53:09 - Brandon Hancock
Working on spinning up jobs and tasks and everything.

01:53:13 - Brandon Hancock
Oh, I think it was for Juan's task, but yeah.

01:53:17 - Mitch
Yeah.

01:53:19 - Brandon Hancock
Also, mean, Bastian did just help a ton with a lot of the cloud stuff for me.

01:53:24 - Brandon Hancock
So maybe if you also want more help too, Bastian does a fountain of knowledge.

01:53:30 - Brandon Hancock
As well.

01:53:30 - Brandon Hancock
Sorry, I didn't see the other comment.

01:53:32 - Mitch
Yeah, my bad.

01:53:33 - Mitch
I created you on something.

01:53:34 - Mitch
Anyway, yeah.

01:53:35 - Mitch
Okay.

01:53:35 - Mitch
Sounds good.

01:53:36 - Mitch
I just need to, just like a lot of time, but I feel like it's like the last, it's the final boss of the full stack dev.

01:53:43 - Brandon Hancock
So excited.

01:53:44 - Brandon Hancock
I mean, it really is.

01:53:45 - Brandon Hancock
mean, you got Next.js I've been running.

01:53:47 - Brandon Hancock
You're now in the cloud.

01:53:49 - Brandon Hancock
I mean, you're doing, you're doing it all.

01:53:51 - Brandon Hancock
So yeah, you, you're, you're absolutely crushing it.

01:53:54 - Brandon Hancock
And then I can, after this, ping, ping me tomorrow morning.

01:53:59 - Brandon Hancock
Bye.

01:54:00 - Brandon Hancock
I'm to shoot you some updated code samples because you could probably just steal some of the stuff I've already done too.

01:54:10 - Brandon Hancock
I'll save it more for tomorrow, but just ping me tomorrow morning and I can shoot you some better code samples.

01:54:15 - Brandon Hancock
Praise be.

01:54:16 - Mitch
Thank you.

01:54:18 - Brandon Hancock
Blessed to have.

01:54:19 - Brandon Hancock
All right, perfect.

01:54:20 - Brandon Hancock
Patrick, you're up next, man.

01:54:23 - Patrick Chouinard
Sure.

01:54:23 - Patrick Chouinard
So a couple of side of Dr.

01:54:27 - Patrick Chouinard
Jekyll and Mr.

01:54:27 - Patrick Chouinard
Hyde this week.

01:54:30 - Patrick Chouinard
At the job site, at my client, I started to work on a new workshop or a group project, or I don't know how to call it exactly, but basically the whole development department asked me to participate in an exercise where they are starting to investigate vibe coding inside of the business.

01:54:50 - Patrick Chouinard
Basically creating a, but not for the developer necessarily, but because they have an issue with a lot of shadow IT.

01:55:00 - Patrick Chouinard
Basically, a lot of people in the business creating tools, but they create tools left, right, and center.

01:55:05 - Patrick Chouinard
There's no standard whatsoever, and it's very complicated to maintain.

01:55:11 - Patrick Chouinard
So they want to see if they can use Vibe Coding well-integrated and well-managed because basically what I would create is a list of tools for them, list of templates, a list of prompts, list of chat modes.

01:55:27 - Patrick Chouinard
So basically everything to give them all of the context they would require to create their prototype in the business in a way that, first of all, would not create huge security hole.

01:55:42 - Patrick Chouinard
Second, would be upgradable to an enterprise product eventually.

01:55:48 - Patrick Chouinard
So basically structure their proof of concept in a way that can be inherited by a true development group to upgrade to production value.

01:56:00 - Patrick Chouinard
And that's why if I put a lot of effort in all of the documentation they're going to use to vibe code their application into existence, then we can take that same documentation and use it through the dev department to create something a little bit more production ready for them.

01:56:19 - Patrick Chouinard
So I'm going to be interested in seeing how that develops internally.

01:56:23 - Brandon Hancock
You know, so out of curiosity, because like this is like a very different approach from most of like the work we're talking about today.

01:56:32 - Brandon Hancock
So like it sounds like I mean, are you coming in as a consultant to where you're delivering plans and then practices for the group or like what's like, I guess what role?

01:56:44 - Patrick Chouinard
Basically, I basically act as an internal consultant because I am a consultant by name.

01:56:49 - Patrick Chouinard
So I work for a consulting company full time.

01:56:51 - Patrick Chouinard
It's just that and I've been at the same consulting firm for 16 years now, but this client I've been in.

01:57:00 - Patrick Chouinard
Contract with them full time for the last five years.

01:57:04 - Brandon Hancock
So, but internally, they use me almost as an internal consultant, like a, pick a number and you get hours from Patrick.

01:57:14 - Brandon Hancock
And this is the same.

01:57:16 - Patrick Chouinard
awesome.

01:57:16 - Patrick Chouinard
I mean, hey, you're in demand.

01:57:17 - Brandon Hancock
That's a good spot to be.

01:57:20 - Patrick Chouinard
Exactly.

01:57:20 - Patrick Chouinard
So that's basically what they want to do.

01:57:22 - Patrick Chouinard
So they want to implement that.

01:57:23 - Patrick Chouinard
They had no idea how to go about that.

01:57:25 - Patrick Chouinard
So they came to me, asked me what I thought, gave them a couple of pointers, and now we're developing this entire framework internally of how can we guide business, technical business people to create stuff that is relatively safe, that will not leak data left, right, and center, and that can actually be upgraded to production ready if we see an ROI possibility in whatever they develop.

01:57:52 - Patrick Chouinard
And for them, it gives them value very quickly.

01:57:55 - Patrick Chouinard
So we're going to accomplish that.

01:58:01 - Patrick Chouinard
That's awesome.

01:58:02 - Brandon Hancock
What about your internal stuff?

01:58:03 - Brandon Hancock
I know you for a little while have been creating your own repository of all your cool stuff.

01:58:08 - Brandon Hancock
How's that going?

01:58:08 - Brandon Hancock
Yeah.

01:58:10 - Patrick Chouinard
So that's the Dr.

01:58:12 - Patrick Chouinard
Jekyll part.

01:58:13 - Patrick Chouinard
So if I look at my personal project, I've actually, in the last couple of weeks, I've got a lot of encouragement from this very group.

01:58:22 - Patrick Chouinard
And as I mentioned last week, I've now reopened my YouTube channel, but fed it specifically.

01:58:30 - Patrick Chouinard
But I'm not personally on it.

01:58:34 - Patrick Chouinard
It's basically all Notebook LM created material.

01:58:37 - Patrick Chouinard
But what I decided to do is basically, since my project is all text, it's everything, it's philosophy, how to work with AI, things like that, but all text.

01:58:49 - Patrick Chouinard
So I feed that into Notebook LM for their video creation, the video overview, where they create kind of a PowerPoint presentation with a...

01:59:00 - Patrick Chouinard
An audio presentation as well.

01:59:02 - Patrick Chouinard
All of those I store in the repo and I started to push them to my YouTube channel as a playlist.

01:59:11 - Patrick Chouinard
That's called a Clara Forge playlist.

01:59:13 - Patrick Chouinard
So basically the project itself.

01:59:14 - Patrick Chouinard
I'm trying to start building a format where every project, all the documentation is presented in multimedia format.

01:59:23 - Patrick Chouinard
And one of the publishing platform is YouTube.

01:59:26 - Patrick Chouinard
The idea is not to make my YouTube channel something that has millions of viewers.

01:59:30 - Patrick Chouinard
It's just an output for people who want to understand the repo I'm working on and don't want to read through hundreds of pages of documentation.

01:59:43 - Patrick Chouinard
So easy to consume material on an easy to share platform basically.

01:59:49 - Patrick Chouinard
And this week, the big piece I've added is a personality trait.

01:59:54 - Patrick Chouinard
So I've started splitting the person.

02:00:00 - Patrick Chouinard
Personality of my agents into individual part.

02:00:04 - Patrick Chouinard
And maybe I can share that piece.

02:00:11 - Brandon Hancock
While you're pulling that up, Alex was also wondering if you could drop your channel.

02:00:16 - Patrick Chouinard
Oh, yeah, yeah, yeah.

02:00:17 - Patrick Chouinard
I'll put all of that into the chat.

02:00:21 - Patrick Chouinard
But basically, here you have the list of traits.

02:00:25 - Patrick Chouinard
So those are the ones I've already worked on.

02:00:27 - Patrick Chouinard
So I have curiosity, restraint, whimsy, skeptic, obsession, empathy, sarcasm, sass, and I'm going to be working on a list of others.

02:00:37 - Patrick Chouinard
The idea is those are completely defined, the trait, the trait philosophy, the behavioral definition, and even trait configuration for the system prompt, the linguistic style pattern, integration guidance.

02:00:53 - Patrick Chouinard
All of that is used basically as context because when I opened this project in...

02:01:00 - Patrick Chouinard
Visual Studio, I will point it to the trait I want to use, and I will integrate it, and the first personality I've rebuilt using those traits is the original, the general personality, and you have the trait configuration that I found is actually, it's not pure configuration as it would be in an application, but the LLM actually takes that into consideration while it renders the personality, and then I have the role, the core principle.

02:01:36 - Patrick Chouinard
This is basically my system prompt for that personality, and I'm going to be building a bunch of others based on the character trait I've designed.

02:01:48 - Patrick Chouinard
And that actually, quick note, with GPT-5, that is extremely sensitive to personality design, made a huge difference.

02:02:00 - Brandon Hancock
on the type of output and the quality of output I got from the model in discussion.

02:02:05 - Brandon Hancock
wow.

02:02:06 - Brandon Hancock
Yeah.

02:02:07 - Patrick Chouinard
So maybe I'll...

02:02:08 - Patrick Chouinard
Were you using...

02:02:10 - Patrick Chouinard
Yep, yep.

02:02:11 - Patrick Chouinard
Just a super quick question.

02:02:13 - Brandon Hancock
Were you using GPT-5 like regular or were you doing mini, nano?

02:02:16 - Brandon Hancock
What were you using?

02:02:19 - Patrick Chouinard
For that, I used just GPT-5 standard because I use it in a project.

02:02:24 - Patrick Chouinard
So I create a project in OpenAI and I gave it this personality as project instruction.

02:02:33 - Patrick Chouinard
And then I just have a multiple discussion and files with long-term memory.

02:02:40 - Patrick Chouinard
Basically, I've designed a system where I have three layers of memory that I work with.

02:02:47 - Patrick Chouinard
Personality is the first.

02:02:48 - Patrick Chouinard
So this is where I'm going to put all the information concerning the behavior I want from the AI assistant.

02:02:55 - Patrick Chouinard
The short-term memory.

02:02:56 - Patrick Chouinard
So basically all the chats that are within the project.

02:03:00 - Patrick Chouinard
So this is what to do, what not to do.

02:03:03 - Patrick Chouinard
And long-term memory is all the files I put in the project, because basically those are factual.

02:03:08 - Patrick Chouinard
I try to keep those as purely factual information for the model knowledge.

02:03:14 - Patrick Chouinard
The three of them together build that way.

02:03:17 - Patrick Chouinard
I have awesome amount or type of reaction from the model.

02:03:23 - Patrick Chouinard
And now I'm going to try.

02:03:25 - Patrick Chouinard
Real quick, and you're doing this all inside of, you said VS Code, right?

02:03:29 - Brandon Hancock
Like this is where you're, okay.

02:03:31 - Brandon Hancock
Quick thing just to add is what you could do, because I love the short-term memory, personality, long-term memory.

02:03:38 - Brandon Hancock
You could also add like a dynamic memory of some sort to where as the conversation is going, it just pulls out four snippets and automatically saves it to like a temp memory file of some sort.

02:03:51 - Brandon Hancock
That way, that just sessions are getting stored.

02:03:54 - Brandon Hancock
So as you're talking, it's constantly learning.

02:03:56 - Brandon Hancock
Because, I mean, that's the coolest part about talking with agents is it can just...

02:04:00 - Brandon Hancock
Just like update a file, update a file, update a file as a tool call, you know?

02:04:03 - Brandon Hancock
So you're setting up something really awesome.

02:04:06 - Patrick Chouinard
But basically, I just wanted to stay as close to pure semantic development because there's thousands of people and they are far better developers than I am.

02:04:18 - Patrick Chouinard
Most of them here to develop all of those, that memory management and RAG system behind it.

02:04:25 - Patrick Chouinard
What I'm trying to build is something that is purely semantic.

02:04:29 - Patrick Chouinard
So basically, that will work with no matter what LLM model is behind it.

02:04:34 - Patrick Chouinard
It doesn't care about the technology underpinning.

02:04:38 - Patrick Chouinard
It's just guiding your personality through prompt engineering.

02:04:42 - Patrick Chouinard
That's it.

02:04:44 - Brandon Hancock
That's awesome.

02:04:45 - Brandon Hancock
That's awesome.

02:04:46 - Brandon Hancock
Well, very cool, Patrick.

02:04:47 - Brandon Hancock
I'd love, like I said, if you could drop that channel.

02:04:50 - Brandon Hancock
Yeah, if you could drop that channel, that would be awesome.

02:04:53 - Brandon Hancock
We'd love to peek at it.

02:04:55 - Brandon Hancock
Okay, perfect.

02:04:58 - Brandon Hancock
While he's doing that, Jake.

02:04:59 - Brandon Hancock
Okay.

02:04:59 - Brandon Hancock
Okay.

02:04:59 - Brandon Hancock
Okay.

02:04:59 - Brandon Hancock
Okay.

02:05:00 - Brandon Hancock
Patrick, you're up next, man.

02:05:01 - Jake Maymar
Oh, yeah.

02:05:02 - Jake Maymar
Patrick, that's amazing.

02:05:03 - Jake Maymar
You know, it's so interesting because have you hooked it up to voice yet?

02:05:09 - Jake Maymar
We might have already mentioned that, but.

02:05:11 - Patrick Chouinard
Oh, yeah.

02:05:12 - Patrick Chouinard
All of what I do, all of the interaction is always through voice.

02:05:16 - Patrick Chouinard
Again, that's why I use ChatGPT.

02:05:18 - Patrick Chouinard
It works well with perplexity.

02:05:21 - Patrick Chouinard
It works decently with Gemini, but definitely the voice model used by ChatGPT is the best one.

02:05:29 - Jake Maymar
And how reliable are, like, so working on a use case where, sounds kind of odd, but people are crying or laughing or, like, different kinds of emotions.

02:05:44 - Jake Maymar
Do you feel like it's consistent or do you feel like it's kind of hit or miss stuff?

02:05:50 - Patrick Chouinard
What do you mean how the system will react to somebody displaying an emotion or?

02:05:56 - Jake Maymar
More of the system displaying an emotion.

02:06:01 - Patrick Chouinard
Actually, that's funny.

02:06:03 - Patrick Chouinard
I found that so far, that's why I'm a little bit scared that they say they will retire standard voice pretty soon because with this level of prompting or system prompt, I feel like standard voice is more true to the emotional tone I gave to the personality than advanced voice.

02:06:22 - Patrick Chouinard
Because advanced voice, it seems to want to put its own personality on top of it, and it flattened a lot of what I wrote in the prompt.

02:06:30 - Patrick Chouinard
It's getting better with GPT-5.

02:06:33 - Patrick Chouinard
It adheres to the prompt more, but standard voice still has an edge.

02:06:38 - Jake Maymar
Oh, that's really, really interesting.

02:06:40 - Jake Maymar
Yeah, that's really interesting.

02:06:41 - Jake Maymar
Yeah, because we were finding that it was inconsistent.

02:06:44 - Jake Maymar
It's just basically you're delivering bad news, and the person's supposed to cry, and they would cry too long, or like it's essentially a play that you're in, and we...

02:07:00 - Jake Maymar
It had to be the same for everyone, which of course, you know, these things are not deterministic.

02:07:04 - Jake Maymar
That's really, really interesting.

02:07:06 - Jake Maymar
Yeah.

02:07:06 - Jake Maymar
Thank you for sharing that.

02:07:08 - Patrick Chouinard
But honestly, I would say that when you design the personality with the trait as defined as I showed, it works a whole, because I've tried before, like, oh, you have that trait personality, you're humoristic, or you're funny, or you, that works, but it gets lost really, really quickly as you interact with the model.

02:07:29 - Patrick Chouinard
When you have very specifically defined character trait, especially with the configuration block in YAML, where I actually gave them weight, it seems to reinforce it a lot.

02:07:43 - Patrick Chouinard
Amazing.

02:07:44 - Jake Maymar
Amazing.

02:07:45 - Jake Maymar
Yeah.

02:07:45 - Jake Maymar
I'd love to, I kind of see you doing something in, like, VO or just, like, a demo of that.

02:07:52 - Patrick Chouinard
I'd be really excited to see that, for sure.

02:07:55 - Patrick Chouinard
Just a matter of time.

02:07:57 - Patrick Chouinard
If I find an agent that can give me a little bit more...

02:08:00 - Jake Maymar
We have more time in a week.

02:08:01 - Jake Maymar
Yeah, sure.

02:08:01 - Jake Maymar
Absolutely.

02:08:03 - Jake Maymar
Yeah, I feel like that.

02:08:04 - Jake Maymar
feel like AI, like the whole thing was if you use AI, then you get more time.

02:08:11 - Jake Maymar
Well, that was true until everyone started using AI.

02:08:13 - Brandon Hancock
I feel like I have no time.

02:08:15 - Brandon Hancock
No time at all.

02:08:17 - Jake Maymar
It's insane.

02:08:20 - Jake Maymar
What's going on in Jakeland?

02:08:24 - Jake Maymar
Lots of projects.

02:08:25 - Jake Maymar
I can't wait to show them.

02:08:26 - Jake Maymar
I'm under heavy NDA for a lot of them.

02:08:30 - Jake Maymar
But yeah, definitely, Brandon, I'd love to get your thoughts on these because these are making me nervous.

02:08:39 - Jake Maymar
They're just like, yeah.

02:08:42 - Jake Maymar
And so it's interesting.

02:08:46 - Jake Maymar
I think it's really just the production, like scaling this up is what makes me nervous.

02:08:55 - Jake Maymar
But yeah, I'll have more details on all those things.

02:08:58 - Jake Maymar
But in general.

02:09:00 - Jake Maymar
It's very, very exciting.

02:09:01 - Jake Maymar
Like, there's just so much work, which is amazing.

02:09:06 - Brandon Hancock
Can I dive in real fast?

02:09:07 - Brandon Hancock
So on production, is it just like where to deploy, what to deploy, or, you know, not keeping it, obviously, going from like 100 customers to 10,000 customers.

02:09:22 - Jake Maymar
And like that just is making me like not sleep at night, trying to figure out how to do that.

02:09:28 - Jake Maymar
But now, it's still a reasonable time to get to that point, but a lot can break with 10,000 customers.

02:09:38 - Jake Maymar
Yeah.

02:09:39 - Brandon Hancock
So, and it's not just that.

02:09:42 - Jake Maymar
So, you know, it's a lot of moving pieces, definitely rag, different flavors of rag, sort of light AI sort of prompts and some heavy AI prompts.

02:09:59 - Jake Maymar
Sorry for being.

02:10:00 - Jake Maymar
Vague on this, but yeah, you know, we'll just sign like an NDA and I'll just tell you the whole thing.

02:10:06 - Jake Maymar
But basically, yeah, it's, it's, it's mostly just a lot of moving pieces that makes me nervous.

02:10:14 - Jake Maymar
It's a communication tool and a lot of moving pieces.

02:10:19 - Jake Maymar
So, you know, not really workflows.

02:10:24 - Jake Maymar
So it's, it's, that's the thing I've, I've made everything super generic.

02:10:31 - Jake Maymar
And I feel really confident about that side of it.

02:10:35 - Jake Maymar
And everything, of course, can scale once we get to that point.

02:10:39 - Jake Maymar
But.

02:10:42 - Brandon Hancock
I don't know if you watched the book launch, but Alex Hermos, he released an AI version of him.

02:10:48 - Brandon Hancock
So I think that's what Mitch is referring to.

02:10:51 - Jake Maymar
I'm just joking around.

02:10:53 - Jake Maymar
Yeah, yeah, yeah.

02:10:53 - Mitch
He gained like, I think it was like 100,000 users in like two days.

02:10:57 - Mitch
I was just joking around.

02:10:58 - Mitch
Oh my God.

02:10:59 - Jake Maymar
Yeah.

02:10:59 - Jake Maymar
Yeah.

02:11:00 - Mitch
That's insane.

02:11:00 - Jake Maymar
No, I don't think it's going to be like that, but it's, it's, it's definitely a learning curve, you know?

02:11:06 - Jake Maymar
And then.

02:11:07 - Brandon Hancock
Can I drop a few hints real fast?

02:11:09 - Brandon Hancock
Okay.

02:11:10 - Brandon Hancock
So biggest, like, just as I've seen applications usually scale in the past, most, most issues around like the front end application, like, I'm not sure what platform you're deploying to, but like the front end application handling traffic, that's usually never, never the issue.

02:11:27 - Brandon Hancock
Usually most, most failures I've seen when working on things are mostly related to the database.

02:11:35 - Brandon Hancock
So what I mean by that is like queries at a scale of a hundred users become exponentially more difficult on a large application because if you're don't, if you're not doing indexing properly, well, it doesn't matter at a hundred users.

02:11:50 - Brandon Hancock
But when a 10,000 users all have 10,000, like a thousand rows, you know, you're working with like an insane amount of data.

02:11:56 - Brandon Hancock
So indexing insanely important enough.

02:12:00 - Brandon Hancock
Another big issue seen in the past is working with concurrent database connections.

02:12:07 - Brandon Hancock
So I'm not sure what, if you're using Postgres, I'm not sure what you're using or where you have your database deployed, but making sure you're using like a, I'll just point, I'll just show you really fast.

02:12:20 - Brandon Hancock
Let me show you Postgres.

02:12:22 - Brandon Hancock
So I'm using Convex.

02:12:23 - Brandon Hancock
Let's just do this one.

02:12:23 - Brandon Hancock
Superbase.

02:12:25 - Brandon Hancock
You are using Convex?

02:12:26 - Brandon Hancock
Okay.

02:12:26 - Brandon Hancock
A little out of, I know Bastion got to play with it recently.

02:12:30 - Brandon Hancock
I know Theo talks about it a lot.

02:12:32 - Brandon Hancock
You might not have to run into as many, you might not run into a lot of these issues.

02:12:37 - Jake Maymar
I'm still sorry.

02:12:39 - Brandon Hancock
I know.

02:12:40 - Brandon Hancock
Yeah.

02:12:41 - Brandon Hancock
But you usually want, there's a thing called a shared pool.

02:12:45 - Brandon Hancock
And what happens is like, instead of every client getting their own instant access to the database, it puts like a puller in front of it and it basically just makes sure that you stay under your database connection threshold.

02:12:57 - Brandon Hancock
For example, I think Superbase has around.

02:13:00 - Brandon Hancock
60.

02:13:00 - Brandon Hancock
So like, if you ever have long running jobs or anything like that, that use direct connections, you're going to destroy, you're just going to break.

02:13:08 - Brandon Hancock
And people are going to be like, and you're going to get very weird timeout errors.

02:13:11 - Brandon Hancock
So using some sort of pulled connections is super important.

02:13:15 - Brandon Hancock
And it really just comes down to theory of constraints.

02:13:17 - Brandon Hancock
And the database, there's usually one, and it has very limited resources.

02:13:21 - Brandon Hancock
And it is a thing that breaks first, 90% of the time.

02:13:24 - Brandon Hancock
And at 10,000, that's, I think, the big issue you'll probably run into.

02:13:28 - Brandon Hancock
Your front end, however you have that working, that will just work fine.

02:13:32 - Brandon Hancock
The database most likely will be the issue.

02:13:34 - Jake Maymar
Yeah, the front is just Next.js, app routers.

02:13:38 - Jake Maymar
And that's like pretty rock solid, pretty bulletproof.

02:13:42 - Jake Maymar
It's just my biggest worry is the database.

02:13:46 - Jake Maymar
And I haven't ever used Convex.

02:13:48 - Jake Maymar
So I'm trying to ramp up and Bastion was helping me on that too.

02:13:51 - Jake Maymar
I'm trying to test as much as I can, pressure test this as much as possible to get an idea, but it's very new for

02:14:00 - Jake Maymar
And then there's Blob Storage and other things, too.

02:14:04 - Al Cole
Jake, do you tend to be read-bound or write-bound with that app?

02:14:14 - Jake Maymar
It's hard to say.

02:14:15 - Brandon Hancock
It really is.

02:14:16 - Jake Maymar
I'm going assume read.

02:14:18 - Jake Maymar
I would think...

02:14:23 - Jake Maymar
Yeah, I guess read.

02:14:25 - Jake Maymar
I guess read.

02:14:29 - Jake Maymar
It's a communication tool.

02:14:32 - Jake Maymar
So you are constantly sort of posting information.

02:14:36 - Jake Maymar
Oh, never mind.

02:14:39 - Jake Maymar
So I can't talk about it because I have...

02:14:41 - Al Cole
That's okay.

02:14:42 - Al Cole
That's okay.

02:14:42 - Al Cole
So the reason I was going here, guys, is because I come from Redis.

02:14:46 - Al Cole
And Redis, this is where we would get the phone call.

02:14:50 - Al Cole
It's when the databases got absolutely hammered, fall over, and because they were rebound, Redis had a roll.

02:14:59 - Al Cole
wherever Jay!

02:14:59 - Al Cole
you have

02:15:00 - Al Cole
Play where you could leverage it and it is more than capable.

02:15:04 - Al Cole
You could go a million ops per second and you'd be okay.

02:15:09 - Jake Maymar
Yeah, yeah.

02:15:10 - Al Cole
It's an extra infrastructure component, but if that was your concern and you mostly rebound, that could be a way to ensure you offloaded it.

02:15:17 - Jake Maymar
That makes sense.

02:15:18 - Jake Maymar
I used Redis on the Reddit tool and that was just speed.

02:15:24 - Jake Maymar
It was insane.

02:15:26 - Jake Maymar
That's a really great point.

02:15:28 - Jake Maymar
It's really, really great.

02:15:30 - Jake Maymar
Yeah, it's very helpful.

02:15:32 - Jake Maymar
Thank you.

02:15:35 - Brandon Hancock
No, seriously, Jake, just let us know how we can help.

02:15:37 - Brandon Hancock
Yeah, this is, these are the fun big boy problems of like going from like vibe coding an app to being like, oh, it works for one user, myself, to like, oh, now 10,000 people are using it.

02:15:49 - Brandon Hancock
Like there's a big jump.

02:15:50 - Brandon Hancock
Two other quick points.

02:15:52 - Brandon Hancock
I would 100% look into adding some sort of metrics to track what's happening in your app.

02:16:00 - Brandon Hancock
Wow.

02:16:00 - Brandon Hancock
So PostHog, phenomenal for that.

02:16:03 - Brandon Hancock
You want to have Sentry.

02:16:04 - Brandon Hancock
So if users do have an error in the front end of the application, you know about it.

02:16:09 - Brandon Hancock
And then I also, yeah, those are probably the two I would add just because the second there's 10,000 users, you just want issues to automatically pop up for you to address and you're not having to hunt them down.

02:16:23 - Brandon Hancock
And so in real time, you can be like, oh my God, I got 50 errors.

02:16:27 - Brandon Hancock
Boom.

02:16:28 - Brandon Hancock
You get an alert on your phone and then, you know, to at least tell people something's going wrong and you're on it because the worst thing is just, it's down for 12 hours and you don't know, you know?

02:16:40 - Brandon Hancock
Yeah.

02:16:41 - Jake Maymar
So I would look those two as well.

02:16:43 - Jake Maymar
That's fantastic.

02:16:44 - Jake Maymar
Thank you.

02:16:44 - Jake Maymar
Yeah.

02:16:45 - Jake Maymar
That makes a lot of sense.

02:16:47 - Jake Maymar
Yeah.

02:16:47 - Jake Maymar
Okay.

02:16:49 - Brandon Hancock
Well, dude, well, good luck.

02:16:52 - Jake Maymar
Perfect.

02:16:52 - Brandon Hancock
Perfect.

02:16:53 - Brandon Hancock
All right.

02:16:53 - Brandon Hancock
Good luck, Jake.

02:16:54 - Brandon Hancock
Let me know if I can help.

02:16:56 - Brandon Hancock
Okay.

02:16:56 - Brandon Hancock
Next up, I think we have a John Michael.

02:17:04 - Brandon Hancock
If he is a, just a listener today, Nguyen, if you want to hop on, happy to help, help out however we can.

02:17:17 - Brandon Hancock
Let's see, give them a few seconds.

02:17:22 - Brandon Hancock
Yeah, if not, I was going to ask Brandon, do you have any more like AI trips or plans for events for the rest of the year or no?

02:17:30 - Brandon Hancock
You're staying home.

02:17:31 - Brandon Hancock
Dude, I don't want to fly anymore for a while.

02:17:35 - Brandon Hancock
Yeah.

02:17:36 - Brandon Hancock
Because like what happened is like I got back Tuesday night, unpacked the car, unpacked everything, passed out, woke up Wednesday morning, helped like, you know, Bastion, Waheed developers helping out with ShipKit, gave them as much information as I could.

02:17:50 - Brandon Hancock
And then at noon, hopped on a flight to go to travel again.

02:17:54 - Brandon Hancock
Then I got back.

02:17:55 - Brandon Hancock
So it's just been like back to back to back, which is a huge chain of scene from like.

02:18:00 - Brandon Hancock
This, where I am normally 24-7.

02:18:02 - Brandon Hancock
So I had to like recharge all Saturday and Sunday because I like, I can't, I'm so tired, you know, normally, you know, normally it's thinking all day, not talking and being like 100%.

02:18:13 - Brandon Hancock
So probably nothing, nothing in the immediate next two months, maybe, maybe more towards the end of the year.

02:18:22 - Brandon Hancock
But, but yeah, few questions for you guys.

02:18:26 - Brandon Hancock
Out of curiosity, are y'all mostly, like, are y'all mostly cursor right now?

02:18:32 - Brandon Hancock
Are y'all mostly cloud code?

02:18:33 - Brandon Hancock
Are you mostly, I would just be curious what you guys are using just because like, and the reason I'm asking is because I'm trying to figure out what to dive deeper in because most of my stuff has been around cursor tips.

02:18:44 - Brandon Hancock
Cloud code is phenomenal, but it's just a completely different flavor.

02:18:47 - Brandon Hancock
So I was just curious if you guys had one favorite or the other, because I know right now I, I use both, but I'm mostly cursor.

02:18:57 - Brandon Hancock
Okay.

02:18:58 - Brandon Hancock
So you guys mostly cursor as well.

02:19:00 - Brandon Hancock
Is there anything I could dive deeper into Cursor or just any other topics over the next few weeks that you guys would like to know more about?

02:19:07 - Brandon Hancock
You know, always looking for the Cursor CLI?

02:19:12 - Brandon Hancock
Okay.

02:19:13 - Brandon Hancock
I can look at that for you guys.

02:19:16 - Alex Wilson
I think the rules and how you set it up would be helpful, too.

02:19:22 - Brandon Hancock
It's changed.

02:19:25 - Brandon Hancock
It has changed.

02:19:26 - Brandon Hancock
And the thing, definitely, Alex, the video I just, it's going live tomorrow, so there's not like a thumbnail or title for it right now.

02:19:34 - Brandon Hancock
But if you guys want to go ahead and look at it, it does have a chapter dedicated to that if you want to peek at it.

02:19:43 - Brandon Hancock
Let's see.

02:19:44 - Brandon Hancock
Let me get you the link again.

02:19:48 - Brandon Hancock
Perfect.

02:19:50 - Brandon Hancock
Yes.

02:19:50 - Brandon Hancock
So I would definitely peek at that one.

02:19:52 - Brandon Hancock
It already has some, it already, it has, it goes a little bit into it, but if you need more, let me know.

02:19:59 - Brandon Hancock
Thank

02:20:00 - Brandon Hancock
It's like, it's so funny because at that developer competition for Google, I mean, I was the only person there talking to my computer.

02:20:10 - Brandon Hancock
I was the only one who got like a completed project just because like everyone was kind of coding like it was 2020, you know?

02:20:17 - Brandon Hancock
And I was the only one using like templates and tasks and like actually leaning into AI agents to do most of the work.

02:20:25 - Brandon Hancock
And I just, I was able to move so much faster than everyone else.

02:20:28 - Brandon Hancock
So it's just still funny to see like, you know, there's, there's, there's levels to AI development.

02:20:34 - Brandon Hancock
So I try to, as much as I can, that video share, like the paradigm has 100% changed.

02:20:40 - Brandon Hancock
Here's, here's how you can do, do it faster.

02:20:42 - Brandon Hancock
So if you want me to go deeper after that video, 100%, I'd love going into this.

02:20:46 - Brandon Hancock
I love nerding out on, on it.

02:20:48 - Brandon Hancock
Trying to think if there's any other questions.

02:20:51 - Brandon Hancock
Yeah.

02:20:52 - Brandon Hancock
I mean, seriously, if you guys think of anything that you'd like me to go deeper on, I'm always open to, to suggestions just because like, it's the coolest time alive to be a developer.

02:21:00 - Brandon Hancock
To build stuff.

02:21:01 - Brandon Hancock
Yeah, I'm so pumped.

02:21:04 - Al Cole
And just clarification, Brandon, on, sorry to interrupt, on ShipKit, you were just giving us the yellow flag, not the green flag, and you looking for a day or two for the go signal?

02:21:18 - Brandon Hancock
Yeah.

02:21:19 - Brandon Hancock
20 hours, something like that.

02:21:21 - Brandon Hancock
18 hours.

02:21:22 - Brandon Hancock
Just need to wrap up a few things tonight and first thing in the morning.

02:21:26 - Brandon Hancock
As soon as that YouTube video goes live and emails go out, it's ready.

02:21:30 - Brandon Hancock
So it'll happen tomorrow.

02:21:32 - Brandon Hancock
Just need to...

02:21:33 - Brandon Hancock
Yeah, no pressure, I just wanted to know when I could hit the buy.

02:21:36 - Al Cole
Okay.

02:21:37 - Al Cole
All right.

02:21:38 - Brandon Hancock
Okay.

02:21:39 - Brandon Hancock
I absolutely love it.

02:21:40 - Brandon Hancock
Yeah.

02:21:41 - Brandon Hancock
Coolest thing, why I'm so excited for this, just like back, like, you know, kind of see behind the curtain.

02:21:46 - Brandon Hancock
I did that full stack marketing platform.

02:21:48 - Brandon Hancock
The biggest regret on that is it was hard to continue to add value to it because it is a project, if that makes sense.

02:21:55 - Brandon Hancock
Like, it's literally called full stack marketing platform.

02:21:57 - Brandon Hancock
So why I'm pumped for this one is...

02:22:00 - Brandon Hancock
Because it's just all around building real-world AI applications.

02:22:04 - Brandon Hancock
And I'm just pumped to like, like my cycle going forward is like every six weeks, four to six weeks, depending on what you guys want, build it.

02:22:13 - Brandon Hancock
So like, I know Mark on the call, he's all in on LandGraph.

02:22:17 - Brandon Hancock
So like, would love to add a LandGraph in there, like just to build a real-world LandGraph application video.

02:22:24 - Brandon Hancock
Okay, hey, a ton of developers are building shorts that go, that they use for marketing or to make their own YouTube channels.

02:22:31 - Brandon Hancock
Here's how you can actually build out a real-world video production application.

02:22:36 - Brandon Hancock
But like, you kind of have to start using some more heavy cloud services.

02:22:39 - Brandon Hancock
So like, I'm just pumped because there's so much room to just continually add in there for you guys.

02:22:43 - Brandon Hancock
Because it's just a completely different shift at coming at building out the course and product.

02:22:49 - Brandon Hancock
So yeah, I'm just, I'm pumped.

02:22:51 - Brandon Hancock
I wish I could hit the finish everything button for you guys tomorrow, but it just takes time.

02:22:55 - Brandon Hancock
So apologize on the, on the wait.

02:22:58 - Brandon Hancock
Dude, and Mitch, it is a new.

02:23:00 - Brandon Hancock
Laptop.

02:23:00 - Brandon Hancock
That's the worst part.

02:23:01 - Brandon Hancock
I think I have no idea what went wrong.

02:23:04 - Brandon Hancock
I'm so embarrassed.

02:23:05 - Brandon Hancock
know there's a bunch of new people on the call and they're probably like, man, this Brandon guy lives, you know, he's probably has an antenna outside of his room pointing at the pointing at something.

02:23:15 - Brandon Hancock
But no, it's supposed to be good internet.

02:23:18 - Mitch
So I guess it was just down for a second.

02:23:20 - Brandon Hancock
So that's funny.

02:23:21 - Mitch
Maybe it's the recording then, like when you record these calls that take that just lags zoom or something.

02:23:27 - Mitch
Maybe I don't know.

02:23:28 - Brandon Hancock
Dude, it's like, it's like six, 700 megabits down, 400 up.

02:23:33 - Brandon Hancock
I have literally no idea what went wrong.

02:23:36 - Brandon Hancock
So, um, but, but yeah.

02:23:38 - Brandon Hancock
Um, and Jake, yeah, I'll send it to you real fast.

02:23:42 - Brandon Hancock
Like I said, not, not ready yet.

02:23:44 - Brandon Hancock
Um, but I'll go ahead and drop it.

02:23:47 - Jake Maymar
I'm so excited for this, Brandon.

02:23:52 - Brandon Hancock
Paul, you're right.

02:23:53 - Brandon Hancock
I need to have a wired connection.

02:23:54 - Brandon Hancock
Um, yeah, I think that's the, that's the, that's the move for, for, Hey, Black Friday.

02:24:00 - Brandon Hancock
Hey, I'll buy some more gear, get it all set up and going.

02:24:04 - Brandon Hancock
All right.

02:24:04 - Brandon Hancock
Perfect.

02:24:05 - Brandon Hancock
Well, thank you, guys.

02:24:06 - Brandon Hancock
It was so good to get to see all of my fellow nerds again.

02:24:09 - Brandon Hancock
I've missed you guys.

02:24:10 - Brandon Hancock
It felt good to be back.

02:24:12 - Brandon Hancock
Once again, shout out to Paul for holding down the fort while I was off being shark bait and cannot wait to see you guys next week.

02:24:19 - Brandon Hancock
And if there's seriously anything I can help with, I know you guys are working on so many cool real world projects.

02:24:23 - Brandon Hancock
Ping me.

02:24:23 - Brandon Hancock
Always happy to help.

02:24:25 - Brandon Hancock
Very slammed right now, but we'll definitely try to squeeze in like some call to keep you guys.

02:24:30 - Brandon Hancock
Not stuck and, you know, keep crushing it.

02:24:33 - Brandon Hancock
So, yeah, y'all are awesome.

02:24:35 - Brandon Hancock
Can't to see you guys next week and hope you have a great rest of your week.

02:24:37 - Brandon Hancock
Okay.

02:24:38 - Brandon Hancock
Have a good week, guys.

02:24:40 - Brandon Hancock
See you guys.

02:24:41 - Brandon Hancock
You have a great one.

02:24:41 - Brandon Hancock
Bye.

