00:04:59 - Patrick Chouinard
Hi, Marc.

00:05:06 - Marc Juretus
What's up, Patrick?

00:05:08 - Marc Juretus
What did you say?

00:05:12 - Patrick Chouinard
Just managed to get back from work in time for the call this week, finally.

00:05:19 - Marc Juretus
Thought of you yesterday, my boss wants to start considering using Copilot.

00:05:25 - Marc Juretus
So I had to kind of explain that there's a Microsoft Copilot where it's the regular one as opposed to the GitHub, even though I heard that that's owned by Microsoft as well.

00:05:35 - Patrick Chouinard
Yeah.

00:05:37 - Patrick Chouinard
They're both Microsoft products.

00:05:39 - Patrick Chouinard
It's Copilot and GitHub Copilot.

00:05:42 - Marc Juretus
The naming convention is extremely confusing.

00:05:46 - Marc Juretus
Beyond.

00:05:47 - Marc Juretus
I was using it, though.

00:05:49 - Marc Juretus
Like to ask, what is it?

00:05:51 - Marc Juretus
What is it?

00:05:51 - Marc Juretus
Ask, edit, and what is it?

00:05:54 - Marc Juretus
Agent mode.

00:05:54 - Marc Juretus
So it's interesting.

00:05:55 - Marc Juretus
I'm using IntelliJ, so we've got to, like, tell them how they come.

00:06:00 - Marc Juretus
Can apply it to their day-to-day.

00:06:01 - Marc Juretus
So it works pretty good for the most part.

00:06:04 - Patrick Chouinard
Yeah, actually, I wouldn't develop huge application using it, but for day-to-day stuff and as an accelerator, yeah, it does a job.

00:06:15 - Patrick Chouinard
Actually, if you couple it with a spec kit from GitHub, it gains a whole lot of capabilities.

00:06:24 - Marc Juretus
Nice.

00:06:25 - Marc Juretus
Yeah, I was playing around with how you can highlight and chat against your code and it's interesting.

00:06:32 - Marc Juretus
So I'll see what I can spin up.

00:06:35 - Patrick Chouinard
Yeah, actually, that's going to be part of stuff I'm going to share tonight.

00:06:40 - Patrick Chouinard
The idea that I'm, because last week I mentioned how I wanted to, or wanted, had to automate some of the admin stuff surrounding development, like all of the issues, the pull requests, the commit, that most VibeCoder have no idea how to do.

00:06:58 - Patrick Chouinard
And now we're going

00:07:00 - Patrick Chouinard
We have a whole bunch of Vibe Coder doing those, so if we don't want to get in Shadow ID hell, we have to find a way to automate those things.

00:07:08 - Patrick Chouinard
So I'm thinking about extending SpecKit so it manages that part as well, not just the specifications.

00:07:19 - Paul Miller
Hey, Patrick, were you talking about your workplace that's gone Vibe crazy?

00:07:26 - Paul Miller
Well, I really, I couldn't imagine, like it's a really exciting, cool thing, but I can see the stress in having a whole user group playing around with those tools.

00:07:39 - Paul Miller
How's your sanity?

00:07:42 - Patrick Chouinard
And let's just say that stress level is not low, but there's a whole lot of opportunity though.

00:07:48 - Marc Juretus
I'm sure you hear a lot of, oh, that's cool.

00:07:51 - Marc Juretus
Hey, no, let's not do that's cool  before you get into some trouble here.

00:07:55 - Marc Juretus
I was telling Patrick, my boss is like, let's start using.

00:08:00 - Marc Juretus
Github Co-Pilot at my job, but the first hurdle is we have Microsoft Co-Pilot, but we don't have the Github version of Microsoft.

00:08:08 - Marc Juretus
So I had to explain that's not Code Assistant, that's for day-to-day PowerPoint slides, rewrite your email, this, that, and the other.

00:08:18 - Marc Juretus
So I was playing around with it, and I was creating some Spring Boot apps and some Next.js stuff.

00:08:24 - Marc Juretus
So it writes it pretty well for the most part.

00:08:27 - Marc Juretus
It's just another tool.

00:08:30 - Patrick Chouinard
When you create an office suite, an AI assistant, an AI development, and all gave it the name Co-Pilot, don't be surprised when customers are like, what hell is that?

00:08:42 - Marc Juretus
I mean, the one cool thing it does do, though, is like I said, I can see a usage where, with the regular Co-Pilot, where you can create an agent and have like a rag against like a 20-page document and say, okay, for my area, this is how we handle PTO, downtime, disaster recovery.

00:08:59 - Marc Juretus
in the a lot next.

00:08:59 - Marc Juretus
next.

00:08:59 - Marc Juretus
lot a I can a

00:09:00 - Marc Juretus
Ask the agent, and then you can assign it to a specific user's ID, and only they have access to it.

00:09:05 - Marc Juretus
So I could see a very good use case for that part of Microsoft Copilot, but it's not the full-blown one that I think they think it is.

00:09:14 - Paul Miller
Yeah, yeah, no, it's a good point, because within a corporate environment, you kind of don't want them, you want guardrails that are quite tight about what they can do, what they can't do, how can they access their corporate email without blowing it apart and missharing it?

00:09:32 - Paul Miller
It's a lot harder and more complicated than they think, and these are naive users that a little knowledge is dangerous, it sends a lot of scary thinking.

00:09:46 - Marc Juretus
The funny thing I've noticed is what they think they know about AI, from what I've learned, is not truly AI.

00:09:54 - Marc Juretus
Like, just some of the stuff, yeah, no, it doesn't really work that way, you know?

00:10:00 - Marc Juretus
Believe me, I'm giving, like, basic, advanced and expert training on prompt engineering.

00:10:06 - Patrick Chouinard
The number of people that gets into the advanced force saying, oh, I already know the basic stuff, and they have no clue whatsoever is impressive.

00:10:16 - Paul Miller
Yeah.

00:10:17 - Marc Juretus
Yeah.

00:10:18 - Tom Welsh
Right.

00:10:20 - Marc Juretus
Oh, my God.

00:10:22 - Paul Miller
Look, I used to do a lot of work being a CIO and being other senior IT roles in corporates, and that side I don't really miss.

00:10:37 - Paul Miller
Everyone thinks they can do that role, but it's blooming hard.

00:10:41 - Paul Miller
Managing expectation, keeping the environment stable, moving the enterprise forward, this is tough stuff.

00:10:49 - Patrick Chouinard
You want to know what the scariest sentence actually is?

00:10:52 - Patrick Chouinard
I heard it last week.

00:10:54 - Patrick Chouinard
It's a C-level individual telling you, oh, we have to do...

00:11:00 - Patrick Chouinard
Do more Vibe Coding.

00:11:01 - Patrick Chouinard
I actually Vibe Coded a CRM in three hours yesterday.

00:11:06 - Paul Miller
Yeah, right.

00:11:09 - Paul Miller
Well, we should move the whole corporation onto that platform.

00:11:13 - Al Cole
Excellent.

00:11:13 - Al Cole
Ship it.

00:11:14 - Al Cole
No, ship it.

00:11:15 - Marc Juretus
Absolutely.

00:11:16 - Marc Juretus
it in, put it on.

00:11:16 - Marc Juretus
it out, yeah.

00:11:17 - Marc Juretus
Absolutely.

00:11:17 - Al Cole
it out.

00:11:20 - Patrick Chouinard
I'm going to ship that thing under one condition if you guarantee that I'm going to get paid to fix the problem afterward.

00:11:33 - Patrick Chouinard
So, yeah, bringing those people back into reality of where do you actually create stuff?

00:11:40 - Patrick Chouinard
How do you do that safely, let's say?

00:11:44 - Marc Juretus
My favorites are always the ones that are like, oh, yeah, no.

00:11:47 - Marc Juretus
No, you just asked me that and I just showed you that.

00:11:50 - Marc Juretus
So the saying I know, you don't really know.

00:11:53 - Marc Juretus
I don't know why.

00:11:54 - Marc Juretus
That just irks me.

00:11:55 - Marc Juretus
Oh, yeah, I didn't know.

00:11:56 - Jake Maymar
Then why did you ask me?

00:11:58 - Marc Juretus
That genie is out of the portal.

00:12:00 - Paul Miller
Now, and you're not putting it back, Patrick, it's dangerous.

00:12:06 - Patrick Chouinard
So now, like you do in the chain of thought, you have to separate problem into individual chunks, so now I'm taking care of one very individual chunk, and that's how do you get VibeCoders to actually do issues, commit, pull requests correctly without having to teach them as DLC?

00:12:26 - Al Cole
Now, I think we're into the LLM hallucinations area.

00:12:30 - Al Cole
I'm not sure how well that's going to go for you.

00:12:34 - Patrick Chouinard
Well, I'm thinking, I'm playing with SpecKit and actually thinking of extending it, because what SpecKit is, is basically you give an intent and it starts creating specification.

00:12:51 - Patrick Chouinard
Well, why not actually define the number of issues in which it should be split?

00:12:59 - Patrick Chouinard
SpecKit and...

00:12:59 - Patrick Chouinard
and...

00:12:59 - Patrick Chouinard
SpecKit

00:13:00 - Patrick Chouinard
Provided with templates for either Jarrett tickets or GitHub issues or things like that.

00:13:07 - Patrick Chouinard
You could get, my idea is not to get them perfectly as if they were a software engineer, but if I can get them like 50% there, it's already a whole lot better than the no percent there they are right now creating code that has to be managed somehow.

00:13:26 - Al Cole
Got it.

00:13:26 - Al Cole
Okay.

00:13:27 - Marc Juretus
What is it writing?

00:13:28 - Marc Juretus
It's writing.

00:13:29 - Marc Juretus
much waterfall.

00:13:32 - Patrick Chouinard
Isn't spec kit too much waterfall?

00:13:36 - Patrick Chouinard
It depends.

00:13:37 - Patrick Chouinard
It is waterfall for implementation of the specification that you create, but if you create it small enough and you split it into enough parts, it can be pretty agile actually.

00:13:55 - Brandon Hancock
Guys, I gotta hop in.

00:13:56 - Brandon Hancock
Today is going to be a shorter call.

00:13:59 - Brandon Hancock
call.

00:14:00 - Brandon Hancock
Um, I have so much work to do that I have to, you know, have to make sure still have plenty of time to, to, to work for you guys.

00:14:09 - Brandon Hancock
So what I was hoping to do today is normally we go round robin, uh, ask questions, then go round robin.

00:14:16 - Brandon Hancock
But what I would love to do today is kind of make today more question based.

00:14:20 - Brandon Hancock
And then if you guys want to keep going, uh, after all questions are answered, would love for you guys to keep going.

00:14:26 - Brandon Hancock
Um, it's just, um, we are in the, the home sprint for, uh, for ship kit.

00:14:30 - Brandon Hancock
So absolutely, uh, this is the most stressful time.

00:14:34 - Brandon Hancock
I can't tell you how excited I am for literally the two, two seconds after it's launched.

00:14:40 - Brandon Hancock
So, uh, I'm going to take a, I'm going to go into a small coma for, for, for, 12 hours and then I will, will bounce back.

00:14:46 - Brandon Hancock
So, um, yeah, really looking forward to it.

00:14:50 - Brandon Hancock
Um, yeah.

00:14:51 - Brandon Hancock
So what we'll do today, quick heads up.

00:14:52 - Brandon Hancock
I think the best thing to do today is to just drop questions in chat.

00:14:56 - Brandon Hancock
That way I can make sure everyone gets their questions answered.

00:15:00 - Brandon Hancock
And then, like I said, I can definitely stay until 7 today, and then we'll go round robin, but just at, we'll say 7.05, I gotta hop off, just because I have to get back to coding.

00:15:09 - Brandon Hancock
But you guys can keep the party going.

00:15:13 - Brandon Hancock
But Ty, I did see you had a hand up real fast, so if you want to go ahead first.

00:15:18 - Ty Wells
Yeah, really, I was asking, my question is about cloning a Supabase instance.

00:15:27 - Ty Wells
Supabase has a point-in-time recovery option, but that's schema.

00:15:33 - Ty Wells
You can get data as well.

00:15:35 - Ty Wells
But what you cannot get is edge functions or users.

00:15:42 - Ty Wells
I think those are really the only two.

00:15:44 - Ty Wells
So I went through a process scripting out to gather, to pull all of that data, but then you've got UUID issues with.

00:15:54 - Ty Wells
So I'm trying to see if anybody has any thought on that.

00:15:58 - Ty Wells
I'm in the process.

00:16:00 - Ty Wells
Ross is writing an agent to do what I did, except I still have to match that data back to the users.

00:16:05 - Ty Wells
So, you know, some sort of cross-mapping table.

00:16:08 - Ty Wells
I wonder if anybody's been there.

00:16:10 - Ty Wells
Switch to Firebase.

00:16:12 - Ty Wells
Love it.

00:16:14 - Brandon Hancock
No, I'd love to dive into this because, yeah, this is one of the hardest, like, where most people get is they're like, cool, I built a local app on my computer.

00:16:24 - Brandon Hancock
Cool, I deployed it to the cloud.

00:16:26 - Brandon Hancock
Ta-da, I'm done.

00:16:27 - Brandon Hancock
And that's the start of your real-world journey as building a production application because you really need to create a staging environment and a production environment.

00:16:40 - Brandon Hancock
So, let me just share my screen really fast.

00:16:44 - Brandon Hancock
And I'll just show, I don't want to show anything I'm not supposed to.

00:16:49 - Brandon Hancock
Okay, cool.

00:16:51 - Brandon Hancock
You're supposed to show everything.

00:16:53 - Ty Wells
There are no secrets.

00:16:55 - Brandon Hancock
I'm worried I'm going to leak someone's something that I'm not supposed to.

00:16:58 - Brandon Hancock
So, it's got to be.

00:17:00 - Brandon Hancock
Got to be careful.

00:17:01 - Brandon Hancock
But OK, so like when using Supabase, the main thing that you want to do is in just to put everyone else on context with where you're at in this process is when building a real world application, you really want to have a production environment that is safe and stable for your customers and clients.

00:17:20 - Brandon Hancock
OK, now the second thing that you want to do is create basically like a staging development environment where you can completely destroy, mess up, and it does not impact your users.

00:17:31 - Brandon Hancock
So the issue that Ty is running into is as you were building out your main application, a lot of, and correct me if I'm wrong, Ty, but a lot of everything that probably got set up was related to staging.

00:17:45 - Brandon Hancock
And now that you're working on main, it's like, do I copy data over?

00:17:49 - Brandon Hancock
Do I clean everything up?

00:17:50 - Brandon Hancock
Do I delete it?

00:17:52 - Brandon Hancock
So that's the hard part, right?

00:17:54 - Brandon Hancock
That's where you're at?

00:17:57 - Ty Wells
Yeah, yeah.

00:17:58 - Ty Wells
So, yeah, that's where I'm at.

00:17:59 - Ty Wells
ahead.

00:17:59 - Ty Wells
we okay.

00:17:59 - Ty Wells
...

00:17:59 - Ty Wells
you never you sure.

00:18:00 - Ty Wells
Obviously, you don't want to touch production.

00:18:01 - Ty Wells
I have branches set up, and yes, exactly where we're at here in terms of, but more so my edge functions of the issues, because, you know, can't make those changes on production.

00:18:14 - Ty Wells
It's not going to end well.

00:18:17 - Ty Wells
So I'm just looking at a good way to clone it, because now I want to create another branch for feature, a feature branch.

00:18:24 - Brandon Hancock
Okay.

00:18:25 - Brandon Hancock
Let me show you one other thing real fast that would hopefully be super helpful.

00:18:28 - Brandon Hancock
So the way I have it is I will usually make setup scripts, like, let me make sure I'm not doing anything bad again.

00:18:37 - Brandon Hancock
Okay, this is pretty good.

00:18:39 - Brandon Hancock
So what I do is I create a collection of setup scripts, like this is just, you know, like from the chat and rag application and ship kit, but what you end up doing is you codify everything so that you manually don't have to, like, recreate buckets, and you don't have to manually recreate all of the different permissions for bugs.

00:19:00 - Brandon Hancock
Buckets, you just spin up a few setup scripts, and that way whenever you start working in a new environment, even if you have to blow everything away, you just literally run like three commands, npm run, db migrate, pool, your new database matches your current schema, then you run a few setup scripts, create all your buckets, deploy your edge functions, and then you would want to run like npm, a db seed to seed your database with some fake data.

00:19:28 - Brandon Hancock
So I think you're already doing that, but I think you're already, you're just in the hard part now where it's like, what do I do with my data?

00:19:34 - Brandon Hancock
How do I actually like, I guess, clean it for the two different environments?

00:19:38 - Ty Wells
Well, really port it over so that I could use it, you know, for, to be able to use that real data, because there's, I mean, there's real data in there, and I don't want to, I know that data is cleaned already, so I want to make sure.

00:19:54 - Ty Wells
So, okay, just, just checking to see, that's the path I've been on, I was just hoping.

00:20:00 - Ty Wells
I there was an easier way, but apparently there's not.

00:20:05 - Brandon Hancock
Yeah.

00:20:05 - Brandon Hancock
Keep me posted.

00:20:06 - Brandon Hancock
I'd be curious to see what you find.

00:20:08 - Brandon Hancock
There are some scripts you can make that you can copy data from one to the other, but yeah, you just have to do a bunch of checks to make sure it's what you want.

00:20:18 - Brandon Hancock
So that is the hard part with working in two different environments.

00:20:21 - Ty Wells
Yep.

00:20:21 - Ty Wells
All right.

00:20:21 - Ty Wells
Thanks.

00:20:22 - Brandon Hancock
Perfect.

00:20:23 - Brandon Hancock
All right.

00:20:24 - Brandon Hancock
We'll keep cruising.

00:20:29 - Brandon Hancock
All right.

00:20:29 - Brandon Hancock
So, Paul, how are you going to manage the support and follow-up wave?

00:20:34 - Brandon Hancock
Dude, I'm just going to send them to you, man.

00:20:36 - Brandon Hancock
Just direct all questions to Paul.

00:20:40 - Paul Miller
Here's his email, phone number.

00:20:43 - Paul Miller
Here's his mailing address.

00:20:45 - Brandon Hancock
No, that's funny.

00:20:50 - Brandon Hancock
Yeah.

00:20:50 - Brandon Hancock
So a few things that I've done.

00:20:54 - Brandon Hancock
So I'll just show you guys real fast.

00:20:56 - Brandon Hancock
So one second, let me click the right page.

00:21:01 - Brandon Hancock
Yeah, so a few things.

00:21:02 - Brandon Hancock
So one of the main things I want to do with ShipKit is provide as much support as possible.

00:21:07 - Brandon Hancock
So we are going to have the weekly coaching calls.

00:21:10 - Brandon Hancock
And for the first six weeks, I think we're doing three a week just because I want everyone to hit the ground, absolutely crush it, see what you guys are stuck on, and just keep recording modules and prove it just to make literally ShipKit the best project that's ever existed.

00:21:23 - Brandon Hancock
But there's a few other ways for support that I'm planning on doing.

00:21:27 - Brandon Hancock
So one is just like general AI chatting.

00:21:31 - Brandon Hancock
So like, you know, coming in here and just asking any module of like, hey, what does Brandon say to do for deploying?

00:21:39 - Brandon Hancock
Like, like what Ty was just talking about, like how to deploy your, your bucket.

00:21:44 - Brandon Hancock
Okay, well, cool.

00:21:45 - Brandon Hancock
It would point you to the right course.

00:21:46 - Brandon Hancock
Or if you're on a specific page.

00:21:48 - Brandon Hancock
Let's see, I just changed so much stuff.

00:21:51 - Brandon Hancock
I ran into some issues with video streaming speeds.

00:21:55 - Brandon Hancock
So I had to switch to Vimeo.

00:21:57 - Brandon Hancock
So I think I'm gonna have to

00:22:00 - Brandon Hancock
The video might not show up right now because it's connected to Vimeo.

00:22:06 - Brandon Hancock
So I'm in the middle of fixing it.

00:22:07 - Brandon Hancock
That's why I got to work tonight.

00:22:08 - Brandon Hancock
But you can also, if you're in a specific module, you can always chat with that specific module to be like, what did Brandon say to do?

00:22:15 - Brandon Hancock
So you can always, once again, chat with a specific page.

00:22:19 - Brandon Hancock
And also, like to help you guys as well, I feel like if one person has a question on a certain page, other people have another question on a certain page.

00:22:26 - Brandon Hancock
So they're just like, you can have a discussion about anything.

00:22:38 - Brandon Hancock
Um, yeah, um, um, um, here..

00:22:59 - Paul Miller
um, so, and also.

00:22:59 - Paul Miller
can get

00:23:00 - Paul Miller
As part of the subscription?

00:23:04 - Brandon Hancock
Well, right now, everything is done through just Git, meaning like when you Git a project, it already has like all the AI docs, all the prompt templates and everything.

00:23:15 - Brandon Hancock
I've not looked at setting up an MCP server to do anything with MCP yet.

00:23:21 - Brandon Hancock
Is there like a concrete example that you were thinking of for MCP?

00:23:25 - Paul Miller
Well, I just think some of the tool sets that I work with, the best alignment that you've kind of got is if you can add an MCP into the MCP path.

00:23:38 - Paul Miller
And so as you dynamically update questions and answers and best practice, then that's constantly linked using the MCP path.

00:23:49 - Brandon Hancock
So you're saying from Cursor, allow people to do queries against the course?

00:23:58 - Brandon Hancock
I really like that.

00:23:59 - Brandon Hancock
That's pretty cool.

00:24:01 - Brandon Hancock
Yeah.

00:24:02 - Brandon Hancock
Okay.

00:24:03 - Brandon Hancock
No.

00:24:04 - Brandon Hancock
Yeah, definitely don't have that yet, but that would be a really cool project and something to add on.

00:24:08 - Brandon Hancock
So thanks for the awesome ideas.

00:24:12 - Paul Miller
The other part of the question is, so the Google, you might already have an answer for this, but a lot of us, when you say, oh, we'll just put it in the Google Cloud, we'll do all the Google thing.

00:24:25 - Paul Miller
How do we get comfort that it's not going to, oh, my God, we're going to get hit with bill shock?

00:24:31 - Paul Miller
It's predictable.

00:24:33 - Paul Miller
It's because if you're going to resell it to other people, you're going to stick your credit card thing on there.

00:24:38 - Paul Miller
Yeah.

00:24:39 - Brandon Hancock
How are you covering for that?

00:24:41 - Brandon Hancock
Yeah.

00:24:41 - Brandon Hancock
So, I mean, the main ways to just avoid sticker shock is, like, I literally will be doing an email on this on Thursday to cover this exact question.

00:24:53 - Brandon Hancock
But let me, I was actually going to pull up Google Cloud so I could show you guys, like, cost and everything.

00:24:59 - Brandon Hancock
But the main...

00:25:00 - Brandon Hancock
Same thing I wanted to call out is like when it does come to Google Cloud, I think it really comes down to usage.

00:25:06 - Brandon Hancock
For example, if you upload a gigabyte file and put it through RAG, I think it costs anywhere from 60 to 80 cent to process that.

00:25:16 - Brandon Hancock
So like, you know, so like obviously if someone puts in a terabyte, like they're going to get a higher bill than someone who does a 20 second, 20 megabyte, you know, project.

00:25:26 - Brandon Hancock
So that's like the hard part about like, you know, it really is like, it depends.

00:25:30 - Brandon Hancock
But I will say a few other things, the way we have designed everything, and I'll explain this more on Thursday, but we've designed everything to auto scale to zero.

00:25:38 - Brandon Hancock
Because that's one of the biggest ways to add cost.

00:25:41 - Brandon Hancock
Like, for example, running some of these Google Cloud instances, if you do it 24 seven, it's 50, $60 a day.

00:25:49 - Brandon Hancock
You do that for a month.

00:25:50 - Brandon Hancock
Oh my God, you just accidentally had a thousand dollar bill.

00:25:54 - Brandon Hancock
And that's awful.

00:25:55 - Brandon Hancock
No one wants a thousand dollar bill.

00:25:57 - Brandon Hancock
So everything auto scales to zero, which means.

00:26:00 - Brandon Hancock
Since the application, yes, when you upload something to the RAG processor, it's going to take an additional 30 seconds to kick on, but that's just the way to save you guys, you know, hundreds of dollars.

00:26:11 - Brandon Hancock
So 30 seconds or $100, I think you guys would pick 30 seconds.

00:26:14 - Brandon Hancock
So that's what I, that's the way everything has been designed.

00:26:17 - Brandon Hancock
So I'm trying to pull up ShipKit so I can actually, like, show you guys some prices on my side.

00:26:25 - Brandon Hancock
But yeah, I'll go deeper into that, Paul, just because I do want to answer that question.

00:26:30 - Brandon Hancock
The other usage may vary question as well is whenever it comes to, like, token usage, like, there's multiple strategies I'll cover, but, you know, some people who just want speed, they're happy to do, like, use Claude, Sonnet, Max, the whole way through.

00:26:50 - Brandon Hancock
So, like, some people can't do that.

00:26:51 - Brandon Hancock
I do that because I just wanted to go speed mode.

00:26:54 - Brandon Hancock
Yes, I paid a lot for it, but I got everything done.

00:26:57 - Brandon Hancock
But if you are very price sensitive, you know, you can't.

00:27:00 - Brandon Hancock
You use just the regular thinking models and take on smaller tasks.

00:27:03 - Brandon Hancock
It's just like, you have to play at your own, what your comfort levels are.

00:27:07 - Brandon Hancock
If you want speed and don't mind money, go for it.

00:27:09 - Brandon Hancock
If you want more, very cost sensitive, then yeah, you have to take a different approach.

00:27:14 - Brandon Hancock
So, sorry, it's fighting me.

00:27:16 - Brandon Hancock
I can't pull it up right now, but I'll need to pull it up in a second.

00:27:21 - Brandon Hancock
But yeah, great questions, Paul.

00:27:23 - Brandon Hancock
Yeah, very excited to see what you guys build with it.

00:27:27 - Brandon Hancock
Okay, cool.

00:27:28 - Brandon Hancock
I'm going just keep going down the question list, guys.

00:27:30 - Brandon Hancock
And seriously, please, please add anything in.

00:27:34 - Brandon Hancock
All right.

00:27:35 - Brandon Hancock
So, Tom had the next question.

00:27:37 - Brandon Hancock
I have an app assess...

00:27:42 - Brandon Hancock
Oh, your asset management system.

00:27:44 - Brandon Hancock
I was wondering if Shipkit can take this app as is and improve it, even though...

00:27:51 - Tom Welsh
Rules.

00:27:52 - Tom Welsh
Yeah.

00:27:54 - Brandon Hancock
Sorry, I'm like trying to piece together the different parts of the message.

00:27:58 - Tom Welsh
Yeah.

00:27:59 - Tom Welsh
Yeah.

00:28:00 - Brandon Hancock
So, I mean, one of the best, so ShipKit is really designed to do best with the, like the containers they were built in, meaning like, Webbase and Next.js.

00:28:12 - Brandon Hancock
Like, that's the way the chat application set up to work.

00:28:15 - Brandon Hancock
If you're doing the RAG application, Python, Next.js, and Google Cloud.

00:28:20 - Brandon Hancock
So, obviously, if you're going to be like, posting all those out the window and trying something completely different, you, obviously your results will completely vary because it's not designed for that.

00:28:31 - Brandon Hancock
However, one of the coolest things that I've been recommending people to do is like, if you are working with either like a different language or different backend or whatever varies, like you already have phenomenal template examples.

00:28:44 - Brandon Hancock
And what you can do is just saying like, here's the template.

00:28:48 - Brandon Hancock
It's currently designed to work with Supabase for the backend.

00:28:52 - Brandon Hancock
I'm using this as a backend.

00:28:54 - Brandon Hancock
Please update this to work for the new backend.

00:28:57 - Brandon Hancock
And then boom, you know, so you can always.

00:29:00 - Brandon Hancock
and improve your own templates to make them suited, suited to what you're doing, so.

00:29:04 - Tom Welsh
So luckily, luckily I'm using TypeScript and Superbase, so I'm happy that way.

00:29:08 - Brandon Hancock
so then yeah, you know, you're, you're golden, man.

00:29:10 - Tom Welsh
You're golden.

00:29:10 - Tom Welsh
Yeah, my, my, I suppose a bit of word to do with the question.

00:29:14 - Tom Welsh
So basically I've got AssetMS working quite happily and I want to create a new module for risk tracking and then bolt that into AssetMS.

00:29:23 - Tom Welsh
That's what I want to do, and I wonder if I can use, so I want to, I want to work out if I can get a risk, risk tracking, tracker inside my Asset thing.

00:29:31 - Tom Welsh
So basically using the base AssetMS as the start app, but build a completely new app to pull into it through Shipkit.

00:29:41 - Brandon Hancock
I guess I'm a little confused.

00:29:43 - Brandon Hancock
So you're adding like a new, new functionality in the app is like the, the core part, or?

00:29:49 - Tom Welsh
The AssetMS is the core part, and this would be a module that you could bolt into it.

00:29:54 - Tom Welsh
You flick a switch in the settings page and make, bring, turn on new functionality basically.

00:29:59 - Tom Welsh
So it'd be quick.

00:30:00 - Tom Welsh
And you also trucking up and blowing it into it.

00:30:03 - Brandon Hancock
Yeah, I don't see why it wouldn't, like, at the end the day, like, it's just updating the application, so at the end the day, I don't see why it would not be able to.

00:30:12 - Brandon Hancock
Yeah, the one thing, yeah, the one thing that you would probably want to do is just break it down into a bunch of smaller steps along the way, instead of just, like, one huge, huge task.

00:30:22 - Brandon Hancock
But no, outside of that, yeah.

00:30:23 - Brandon Hancock
And also, if you want to send me, like, a diagram of what you're thinking about doing, would be happy to, like, say exactly how I would tackle that problem.

00:30:30 - Tom Welsh
Tomorrow is diagonal, so yeah.

00:30:32 - Tom Welsh
Cool.

00:30:33 - Brandon Hancock
Okay, you know I like a good visual.

00:30:35 - Brandon Hancock
Thank you, Tom.

00:30:39 - Brandon Hancock
Okay, Al, definitely missed you last week, buddy, but I saw you said you attended Google Labs a bit in Boston.

00:30:47 - Brandon Hancock
And, oh, they had an 80K presentation?

00:30:51 - Al Cole
So this is an update from the one that I did in the fall, Brandon.

00:30:54 - Al Cole
And so this one, actually, much more mature, had multiple ages.

00:31:00 - Al Cole
And the collaborating together with the projects, so I just wanted to share it with the team, I captured all the labs, the presentation, all that stuff, and you'd need to leverage it on GCP, but it was a pretty comprehensive set of labs to showcase the functionality where they are with the maturity.

00:31:22 - Brandon Hancock
Okay, I'm trying to open it up, but it's fighting me.

00:31:25 - Brandon Hancock
Oh, here it is.

00:31:26 - Al Cole
You should see the drive.

00:31:27 - Al Cole
Oh, wow.

00:31:28 - Brandon Hancock
Yeah.

00:31:29 - Al Cole
Oh, they share a ton of stuff.

00:31:34 - Brandon Hancock
Would you say any of them are more helpful than the others?

00:31:38 - Al Cole
say the overview slides would be the most helpful.

00:31:45 - Al Cole
And then what they did, if you're reading any of them, they wanted to gamify it for the group that was there.

00:31:52 - Al Cole
So this is all centered around a collection of games.

00:31:55 - Al Cole
But the keynote's going to give you an overview of the architecture.

00:31:59 - Al Cole
there's fact, about you're can't on

00:32:00 - Al Cole
And kind of the, what they set up here.

00:32:06 - Brandon Hancock
That's very cool.

00:32:07 - Al Cole
This is definitely a maturing of where we all were back in May when I first did it.

00:32:12 - Al Cole
It certainly was much further along.

00:32:14 - Al Cole
And they even have guardrails now where, with the ADK, you can completely intercept anything going between agents and be able to control.

00:32:30 - Al Cole
How you react to it.

00:32:31 - Al Cole
So, again, just a, just an improvement on the overall architecture.

00:32:38 - Brandon Hancock
Yeah, I, like, they are throwing so much effort at this.

00:32:42 - Brandon Hancock
I am so pumped, because, like, like the core, the part that I love, and how you just brought a nail on the head, like, the core agent orchestration is becoming so powerful and so simple to set up.

00:32:53 - Brandon Hancock
I am so pumped, as they continue to make changes to make it easier to add into Next.js, because right now, we

00:33:00 - Brandon Hancock
We as developers, we have to do more work on our side to get it to work properly in a real-world application, which is fine, like it works, but getting it to where it's just like, you know, a one-click button, and boom, you have your ADK agents, oh my gosh, that's going to be a game-changer.

00:33:15 - Brandon Hancock
So I feel like we're getting close, but as soon as I hear something, I'll let you guys know, because that's what my Christmas wish list is for them to make that a bit easier.

00:33:25 - Brandon Hancock
Any other, real fast, any other updates on contracts or cool work, Al?

00:33:33 - Al Cole
For me, I actually am still stuck with contracts.

00:33:38 - Al Cole
I went to a different contract.

00:33:40 - Al Cole
Oh, the thing I will tell the team is I did do a presentation last Tuesday to 18 financial service companies.

00:33:49 - Al Cole
They're all woefully behind in their AI adoption.

00:33:53 - Al Cole
Probably doesn't surprise anybody, but they are just completely behind.

00:33:58 - Al Cole
But what I wanted to highlight...

00:34:00 - Al Cole
That was my first time going through 100% AI-driven, I did a spec in Claude, asked it to generate a presentation outline of the topics I wanted to cover so that I could feed it into Gamma, and then I used Gamma to generate 40 slides, and other than maybe 20 minutes of cleanup, I had a presentation I could start rehearsing right after that.

00:34:25 - Al Cole
So that, for me, was a validation of what you could do in terms of starting with a spec and ending with something that the entire room could engage in for a couple hours.

00:34:37 - Al Cole
That's cool.

00:34:38 - Brandon Hancock
That's very cool.

00:34:40 - Brandon Hancock
I thought I saw Gamma has an API too, right?

00:34:44 - Elijah
Yeah, it wasn't leveraging in that way, but that would be another way to I saw that in the new release this past couple weeks ago.

00:34:52 - Elijah
So I think that's a really interesting loop there for learning as well.

00:35:01 - Brandon Hancock
I would say, I would love at some point any of these cool presentations you're doing.

00:35:05 - Al Cole
Dude, hey, if you ever- If the team's up for it, I'll just throw it in that same folder.

00:35:11 - Al Cole
You can grab it.

00:35:12 - Al Cole
I'm happy to share, guys.

00:35:13 - Brandon Hancock
Yeah, I was gonna say, I just think it's cool.

00:35:15 - Brandon Hancock
Like, I know last week, I think Adam was talking about doing a presentation for his local community.

00:35:23 - Brandon Hancock
So I just shared some slides to help brainstorm, to help him with his.

00:35:27 - Brandon Hancock
But yeah, I just think it's, it's just, it's just cool to help share and help everyone else to get to do cool things in the real world.

00:35:34 - Al Cole
And then I'll put the presentation up.

00:35:36 - Al Cole
And if you guys can borrow, steal it, feel free to do so.

00:35:39 - Al Cole
All I can tell you is if you're pitching the financial service people, they're just not even close yet in their AI adoption.

00:35:47 - Brandon Hancock
Really?

00:35:48 - Brandon Hancock
Yeah, I mean, they're probably scared to put the wrong zero in the wrong spot.

00:35:53 - Brandon Hancock
And yeah, you're out a thousand, you know, thousands of dollars.

00:35:58 - Tom Welsh
well.

00:35:59 - Tom Welsh
Yeah.

00:36:00 - Brandon Hancock
Maybe, yeah.

00:36:01 - Brandon Hancock
All right, so I'll throw it up in that folder, so if you guys check there in about 10 minutes, I'll have my stuff up there.

00:36:06 - Brandon Hancock
Okay, awesome.

00:36:07 - Brandon Hancock
Thank you, Where is the folder at?

00:36:09 - Al Cole
If you go back in the chat, you'll see I mentioned Google, the ADK, and then there'll be a link to a Google Drive folder, and then I'll put my stuff up in there.

00:36:21 - Brandon Hancock
I just tagged you, Elijah, too, in it.

00:36:26 - Elijah
Thank you.

00:36:27 - Brandon Hancock
Okay, of course, buddy.

00:36:28 - Brandon Hancock
All right, we'll keep on cruising, guys.

00:36:32 - Brandon Hancock
I'm going to struggle to pronounce this one.

00:36:35 - Brandon Hancock
I'm not even going to say it.

00:36:37 - Brandon Hancock
I think I'm going to Jahangir.

00:36:39 - Brandon Hancock
I don't know how to say it.

00:36:42 - Jahangir Jadi
Jahangir.

00:36:43 - Brandon Hancock
How are you doing, buddy?

00:36:45 - Jahangir Jadi
I'm doing great, thank you.

00:36:47 - Brandon Hancock
So, quick question.

00:36:48 - Brandon Hancock
I see you are working on some agent workflows.

00:36:52 - Jahangir Jadi
Are we doing ADK, Langshan?

00:36:55 - Brandon Hancock
Okay, ADK, would you mind explain a little bit what's going on so we can...

00:36:59 - Jahangir Jadi
You

00:37:00 - Jahangir Jadi
Yeah, basically I'm creating a system where a user will enter a query, and the system is going to first identify the, if it is correct or not, means if it is complete or not.

00:37:13 - Jahangir Jadi
Secondly, it is going to extract some information from it, like the names and dates, these kind of things.

00:37:21 - Jahangir Jadi
And in the last, it is going to classify the event based on the template, which I'm going to provide.

00:37:28 - Brandon Hancock
Okay.

00:37:28 - Jahangir Jadi
So what happens is, I have created a flow, but my first agent works fine, but it doesn't go to the second agent.

00:37:36 - Jahangir Jadi
If I work like a normal flow with sub-agents, if I use the agent as tools, then it kind of works, but it is not like, it does not work with fallback.

00:37:53 - Jahangir Jadi
Like for example, if, if you can read, for example, if there is an invalid query.

00:37:59 - Jahangir Jadi
is already.

00:37:59 - Jahangir Jadi
Zoom.

00:38:00 - Jahangir Jadi
I want to stop that agent right there and ask the user to enter the query again so that the process can work fine.

00:38:10 - Brandon Hancock
Yeah, so let me show my screen.

00:38:11 - Brandon Hancock
I can help out.

00:38:13 - Brandon Hancock
So this, most of this is a prompting, prompt engineering issue with ADK.

00:38:21 - Brandon Hancock
So here's like the main agent that we have in the root of like the example project for Shipkit.

00:38:26 - Brandon Hancock
So the main suggestion I have for you is ADK loves phased approaches, loves them.

00:38:34 - Brandon Hancock
Like I cannot express it enough.

00:38:36 - Brandon Hancock
So, so you can see here, I'm basically doing the exact same thing that you're asking about, which is like phase one, gather information.

00:38:44 - Brandon Hancock
You specifically tell it what it needs to look for and, you know, and basically just say like, you know, don't proceed to the next step until you're good to go.

00:38:55 - Brandon Hancock
So, cannot express enough.

00:38:57 - Brandon Hancock
Doing phased approaches like this.

00:38:59 - Brandon Hancock
time.

00:39:00 - Brandon Hancock
It's an absolute game-changer, and yeah, if you go look at all of the example ADK samples that ADK has provided, all of them use this.

00:39:10 - Brandon Hancock
It works the best, and you can basically say like, hey, ask these questions, don't proceed until we're good to go to the next one, and so forth.

00:39:18 - Brandon Hancock
But I think that answered part of your question.

00:39:21 - Brandon Hancock
I think there was something else I was missing, though.

00:39:23 - Jahangir Jadi
Yeah, but what is the recommended way?

00:39:25 - Jahangir Jadi
Should I do it with the tools or should I do it the normal way with the sub-agents?

00:39:32 - Brandon Hancock
So, just to make sure I'm on the same page, so we have our root agent.

00:39:36 - Brandon Hancock
Your root agent's going to ask questions, and then after it asks questions, you're saying how do you start to delegate to the next agents, or I guess I'm confused on the question.

00:39:47 - Jahangir Jadi
Yeah, we have two options for doing that now.

00:39:50 - Jahangir Jadi
Either we can with sub-agents, or either we can use the agents as tools.

00:39:56 - Brandon Hancock
Right.

00:39:56 - Brandon Hancock
So, there's two options, and I'll break.

00:39:59 - Brandon Hancock
I agree.

00:39:59 - Brandon Hancock
Thank

00:40:00 - Brandon Hancock
So when you want to do each one of them, so option one is when you want to do tools, so the way tools work when working with ADK is agent as tool, what happens is your root agent will say, hey, I need help on this, it instantly, literally treats your agent like a function is the best way I can describe it, so what that means is it's going to just like pass over a query, this agent's going to do whatever it needs to do, and instantly return the results back to the agent that called it, and that's it, what's different though is in delegation land, what ends up happening is when you say, hey, I have all the information I need, now I need you, this as a sub-agent to take over the process, so that's the difference here, this agent now becomes the main controller agent, and as you continue to interface, you're talking to this sub-agent now going forward.

00:40:59 - Brandon Hancock
is, We mean, Thank you.

00:41:00 - Brandon Hancock
Unless you provide instructions to say, like, hey, delegate back if under this certain condition.

00:41:06 - Brandon Hancock
So, yeah, so it really depends what you're trying to do.

00:41:10 - Brandon Hancock
If you're trying to go, yeah, I guess I can just ask you, what are you trying to do?

00:41:14 - Brandon Hancock
And then maybe that can be a little bit more helpful.

00:41:18 - Jahangir Jadi
OK, can I show you my screen?

00:41:21 - Brandon Hancock
Yeah, of course.

00:41:21 - Brandon Hancock
Let me click a button for you real fast.

00:41:28 - Brandon Hancock
And just while he's pulling it up, just a quick heads up, guys.

00:41:30 - Brandon Hancock
I'm just going down the list in the questions.

00:41:33 - Brandon Hancock
So, Patrick, Alex, David, that's the, like, next few in the queue.

00:41:40 - Brandon Hancock
And normally, these calls are much more chill, relax.

00:41:43 - Brandon Hancock
It's just, I have so much I have to get done for the rest of the week, so I apologize.

00:41:48 - Brandon Hancock
So, starting next week, we'll be back on our normal, like, two-hour calls.

00:41:50 - Brandon Hancock
We're nice and chill.

00:41:54 - Mitch
I thought, hey, I was supposed to do everything for you, Brandon.

00:41:57 - Brandon Hancock
Dude, I thought so, too.

00:41:59 - Brandon Hancock
At this point, it's...

00:42:00 - Mitch
It's the darn recording.

00:42:01 - Mitch
It's a scam.

00:42:02 - Brandon Hancock
It is a scam.

00:42:03 - Mitch
That's I've been saying.

00:42:04 - Brandon Hancock
Forget all these AI guys, man.

00:42:08 - Brandon Hancock
But yeah, no, it's the recording and the tweaking a code and then having to rerecord.

00:42:14 - Brandon Hancock
Yeah.

00:42:15 - Brandon Hancock
AD-20 rule still applies to everything.

00:42:18 - Brandon Hancock
Yeah, it really does.

00:42:20 - Brandon Hancock
It really does.

00:42:21 - Ty Wells
Finishing touches, that's what it is.

00:42:23 - Ty Wells
When you build a house, the finishing touches take forever.

00:42:28 - Brandon Hancock
That's literally where we're at right now.

00:42:30 - Brandon Hancock
Literally where we're at.

00:42:32 - Jahangir Jadi
Yeah.

00:42:33 - Brandon Hancock
One good question.

00:42:34 - Brandon Hancock
Are you ready to share?

00:42:35 - Jahangir Jadi
Yeah, yeah.

00:42:36 - Jahangir Jadi
But there's a problem.

00:42:37 - Jahangir Jadi
I need to restart the application so we can do it later.

00:42:40 - Jahangir Jadi
I can ask it in the group.

00:42:42 - Jahangir Jadi
Just one quick question.

00:42:43 - Jahangir Jadi
If we are using tool, so can that tool call another tool?

00:42:50 - Brandon Hancock
Like tool inception?

00:42:53 - Brandon Hancock
Yeah.

00:42:53 - Jahangir Jadi
I've never done it.

00:42:54 - Jahangir Jadi
I'm using agent as a tool and that agent is calling another tool.

00:42:59 - Brandon Hancock
lot.

00:42:59 - Brandon Hancock
You're We've We're to you.

00:43:00 - Brandon Hancock
That's fine.

00:43:01 - Brandon Hancock
I've never done an, so that's fine.

00:43:03 - Brandon Hancock
Like if you have a root agent that does agent as tool, you can, that sub-agent or tool agent can do a tool request.

00:43:11 - Brandon Hancock
I just don't know if that agent can do an agent as tool request, like two levels deep.

00:43:16 - Brandon Hancock
I don't think we can do that.

00:43:18 - Brandon Hancock
But I'm not, I've never tested that out.

00:43:20 - Brandon Hancock
But just straight up tool calls, like calling a piece of code.

00:43:23 - Brandon Hancock
Yeah, it can, that agent tool can do it.

00:43:25 - Brandon Hancock
I've 100% have done that.

00:43:27 - Jahangir Jadi
Oh, okay.

00:43:29 - Brandon Hancock
Okay, cool.

00:43:30 - Brandon Hancock
All right, thank you.

00:43:31 - Brandon Hancock
We'll keep on cruising.

00:43:32 - Brandon Hancock
And good luck on all things ADK.

00:43:34 - Brandon Hancock
I'd love, next week, if we can share your screen, I'd love to see what cool, what cool stuff you're working on in any demos.

00:43:40 - Brandon Hancock
Okay, all right, we'll keep on cruising.

00:43:44 - Brandon Hancock
So Patrick, you are up next buddy.

00:43:48 - Brandon Hancock
So are you envisioning Shipkit to be mostly for indie developers?

00:43:51 - Brandon Hancock
Are you targeting more to enterprise clients?

00:43:55 - Brandon Hancock
So, I mean, my audience is like us, you know?

00:44:00 - Brandon Hancock
So we are like individuals, some of us are doing our own things, some of us work at a company, we're trying to do like side projects, so at this point, it is more for like the indie developer to like launch that production SaaS application, or for the developer who's like, I want to do freelance work, so like the RAG template, for example, I think it's, that one is like the perfect project for anyone wanting to do like real world freelancing, like it's literally a while, a few months ago, the core, a few months ago, I did a huge RAG project for a client, like 10k or so, and basically all the core lessons from that just got copied and pasted into the RAG template here, so like, you can use it for client work too, so, but like for full blown enterprise, that's where it gets a little bit more confusing, because like, you need to pick some different tools, like enterprises are not going to use Supabase, enterprises are probably going to be doing much more deep work, they have,

00:45:00 - Brandon Hancock
They their own Kubernetes cluster that they're probably running in, like there's just so much extra stuff and the audience, the target audience is so much smaller, that probably outside the scope for ShipKit.

00:45:09 - Brandon Hancock
But you being on the enterprise side, man, I think that's an awesome opportunity for you, man.

00:45:16 - Patrick Chouinard
No, that was my question.

00:45:17 - Patrick Chouinard
I mean, if a client were to buy the license, as you mentioned, you don't want it to be exposed publicly and fully understandable.

00:45:25 - Patrick Chouinard
But if they have a hundred developers that want, and they want to tweak a version for, because it's a bunch of templates.

00:45:33 - Patrick Chouinard
So there's nothing forbidding them to adapt the template to their own infrastructure and after that using it.

00:45:39 - Patrick Chouinard
So is that a one license for the enterprise or a one license per developer in the enterprise or?

00:45:46 - Brandon Hancock
Yeah, so it's really not as much like a license as it is.

00:45:49 - Brandon Hancock
It's like, like, it's more of like, hey, these are your, this is your, your code basically at this point, go forth and build your own projects with it.

00:45:59 - Brandon Hancock
The.

00:46:00 - Brandon Hancock
The main thing, I actually, I can show you guys like the, like the little license part in GitHub in just a second, but like, basically it's not like, buy ShipKit and then hand ShipKit over to a hundred friends, like that's obviously not, not cool, but, but if you build, let's say you're working on the chat application and then you build something cool with that, and then you then go to sell that, yeah, like it is your derivative work, like you, you use what ShipKit was for, like you built something with it, and then now you're selling it, like, totally, totally makes sense.

00:46:32 - Brandon Hancock
It's like if you're, like, you can't, like, like, like, can't, like, like, like, like, that's a little bit like, that's obviously a little bit.

00:46:40 - Brandon Hancock
But I don't know if I'm answering the question.

00:46:42 - Patrick Chouinard
Basically, I'm asking if a client were to be interested in buying it, would they buy one ShipKit per dev or one ShipKit for their dev department or how do you want to do that?

00:46:59 - Brandon Hancock
I that's...

00:47:00 - Brandon Hancock
is one, like, it is for individual developers, is like the best way to describe it.

00:47:04 - Patrick Chouinard
Okay.

00:47:05 - Al Cole
And that makes sense, because you've got support commitments to it, Brandon, and if you find any traction with this, you could get creative and think about an enterprise license with numbers to match that kind of discussion, so, yeah.

00:47:20 - Brandon Hancock
Yeah, good to think it out.

00:47:22 - Patrick Chouinard
That's what I was thinking about the training, because, like I said, next month I'm training 40 dev in one shot.

00:47:27 - Patrick Chouinard
So, that's something you'd be ready to take on if we say, oh, we've just bought, I don't know, 100 Shipkit.

00:47:37 - Patrick Chouinard
Yeah.

00:47:38 - Brandon Hancock
I mean, it is designed for, I mean, like, it really is designed to build real-world applications.

00:47:45 - Brandon Hancock
It's just, like, the kicker is, is like, just to set expectations of like, is Shipkit going to teach you exactly, like, here's what a use effect is.

00:47:55 - Brandon Hancock
Here is what, you know, like, you know, all the different use routes.

00:48:00 - Brandon Hancock
Like, Shipkit is, like, in the age of vibe coding, you're actually kind of moving away from needing that.

00:48:07 - Brandon Hancock
So, like, that's the paradigm shift.

00:48:08 - Brandon Hancock
As long as you have proper context, proper working projects, and a clear roadmap and templates to help you go along the way, like, you can build pretty much anything.

00:48:17 - Brandon Hancock
So that's the goal.

00:48:17 - Brandon Hancock
It's like shipping real-world projects.

00:48:19 - Brandon Hancock
But on the side of, like, teaching Next.js stuff, I'm actually going to be doing a video on that for you guys next month.

00:48:25 - Patrick Chouinard
That's my goal.

00:48:26 - Patrick Chouinard
I understood, but are you ready to teach Shipkit to a class of 100?

00:48:31 - Brandon Hancock
I mean, hey, if they, if there's a, you know, if they, at the right price of the test, man, I'm down for everything.

00:48:40 - Patrick Chouinard
I prefer to ask first than to drop that type of load without asking first.

00:48:47 - Patrick Chouinard
Yeah.

00:48:47 - Patrick Chouinard
No, seriously, if you want to DM me, Patrick Chouinard, I'd be happy to, like, learn a little bit more about, like, actually what they're looking at and would be happy to.

00:48:53 - Patrick Chouinard
Yeah.

00:48:54 - Patrick Chouinard
I'm not saying that that's going to happen.

00:48:56 - Patrick Chouinard
I'm just saying before I open my mouth at the client site, I want Would

00:49:00 - Patrick Chouinard
I want to know if it's something you're open to, let's say.

00:49:03 - Brandon Hancock
Okay.

00:49:04 - Brandon Hancock
Perfect.

00:49:04 - Brandon Hancock
Yeah.

00:49:05 - Brandon Hancock
We can talk offline.

00:49:07 - Patrick Chouinard
I think this would be a cool offline topic.

00:49:09 - Patrick Chouinard
Thank you, Patrick.

00:49:09 - Brandon Hancock
All right.

00:49:10 - Brandon Hancock
We'll keep on cruising, guys.

00:49:12 - Brandon Hancock
AlexH, so you're building on ADK framework that has multiple LLM agents working, and they're updating and maintaining a quote.

00:49:22 - Brandon Hancock
Quotes can contain up to 100 line items, and the JSON schema has multiple fields per line.

00:49:27 - Brandon Hancock
Do you recommend using ADK state to maintain this across or artifacts?

00:49:36 - Brandon Hancock
So, Alex, do you have...

00:49:37 - Brandon Hancock
Oh, wait.

00:49:39 - Brandon Hancock
I was like, it was your time to shine.

00:49:41 - Brandon Hancock
I thought you were getting up to run away.

00:49:45 - Brandon Hancock
If you want to hop on your micro fast, just to expand on a little bit more of what you're working on, I'd be happy to clear it up.

00:49:53 - AlexH
Yeah.

00:49:53 - AlexH
So, like, maybe to define it better, just...

00:49:55 - AlexH
Right now, I have, like, each agent working in isolation I've just built on.

00:50:00 - AlexH
And they're like, oh, and so they're like going from input to output, but the outputs, and now I'm trying to hook them up together and they need to like persist and be able to maintain around the status of this quote.

00:50:10 - AlexH
And that quote can be like, they're like working on a quote and it can be like a hundred line items in the quote.

00:50:15 - AlexH
And then that quote, obviously from like, if you take it like a tabular architecture, it's got like each, you know, columns with fields in it.

00:50:23 - AlexH
So I'm trying to figure out now, how do I like, how do I maintain the state around the quote?

00:50:29 - AlexH
So that each, as each agent's accessing it, there's persistent understanding of where, where the status is, basically the state of it.

00:50:38 - Brandon Hancock
Okay.

00:50:39 - Brandon Hancock
And just to dive in a little bit deeper into it.

00:50:41 - Brandon Hancock
So like in my head, like, is this like a quote of like a hundred, like, are we building a house and we have to keep track of like, okay, the doors are going to cost, we need two doors, each door is $2 or $200 or something like that?

00:50:54 - AlexH
Yeah.

00:50:55 - AlexH
It's like a, it's like a bill of materials.

00:50:57 - AlexH
So like, okay, here's your quote with, you know, each item in here.

00:51:00 - AlexH
Just how much should, you know, it should cost, but then there's like updates to those as it's going through like different reasoning.

00:51:06 - Brandon Hancock
Yeah.

00:51:06 - Brandon Hancock
So the way I like to work with state and ADK is I like to break things down into smaller manageable components.

00:51:16 - Brandon Hancock
So for example, it sounds like if there's a hundred items, I mean, the first question I would ask myself is like, is there any sub, any way we could break down a hundred different rows into like, like I said, if we're doing houses, like exterior, interior, roof, like I would do, I would look at that first to see if there's anything that we could do to like make it easier and more manageable.

00:51:39 - Brandon Hancock
Because that would, you would just break those into different objects, like state objects.

00:51:43 - Brandon Hancock
Yes.

00:51:43 - Brandon Hancock
Yeah.

00:51:44 - Brandon Hancock
That's, that's literally what I would do is like, I would have an exterior, like in state, would literally have like exterior, exterior bill of materials, bomb.

00:51:52 - Brandon Hancock
And then that would, I would have a structured output for like, Hey, everything in this list, it needs to have, you know, it sounds like a name, a quantity.

00:51:59 - Brandon Hancock
So.

00:52:01 - Brandon Hancock
And then each agent would work on just that one final part, and then towards the end, you could have like a composer agent, like a report composer agent, that would look at all of the different states and put them together in one final version.

00:52:20 - Brandon Hancock
That's one way you could do it.

00:52:23 - Brandon Hancock
Yeah, there's multiple ways we could tackle it.

00:52:26 - Brandon Hancock
One question I would have for you is where are we getting stuck right now?

00:52:29 - Brandon Hancock
Is it like, are we getting stuck in the archetype?

00:52:32 - Brandon Hancock
Like, are we getting stuck designing it?

00:52:34 - Brandon Hancock
Or are we have it, we have it running, but it's hitting a, issue or where is it, where is it at?

00:52:39 - Brandon Hancock
It's, well, it's mostly in design.

00:52:41 - AlexH
Um, it's in design because, uh, right now in design and my fear right now is like the JSON, if you look at the JSON doc that's being produced by like any given one, like in testing, I'm giving it a fraction of what it's going to have to manage, call it like 50%.

00:52:58 - Brandon Hancock
Yeah, but in 100% in production.

00:52:59 - AlexH
Yeah.

00:53:00 - AlexH
And trying to now pass those around and maintain, like, it's more in design of, like, trying to figure that out without overloading the context window of any individual LM where it's just all of a sudden going haywire.

00:53:10 - Brandon Hancock
Yeah, that's the key reason why I say break stuff down is just because, like, the second you have too many instructions back to back to back, it's going to, it will just not perform as expected.

00:53:22 - Brandon Hancock
Like, it might do, if you gave it seven instructions, it might do four.

00:53:24 - Brandon Hancock
So, anytime I'm like, it's, almost like you're doing, like, regular software development.

00:53:29 - Brandon Hancock
It's like, the second this class is getting a little too complex, we probably need to make two subclasses in the world of agents.

00:53:35 - Brandon Hancock
The second this one agent's getting a little too complex and I couldn't just do a simple checklist to check things off, I know I need to break things up.

00:53:43 - Brandon Hancock
Quick, I want to show you this real fast because this is what literally I did inside of a project recently to get my agents working.

00:53:53 - Brandon Hancock
So, I'm to show you two different screens really fast.

00:53:58 - Brandon Hancock
This is, this will be helpful, so I'm going to pull.

00:53:59 - Brandon Hancock
will be

00:54:00 - Brandon Hancock
this up.

00:54:02 - Brandon Hancock
Where is it at?

00:54:03 - Brandon Hancock
Too many screens.

00:54:10 - Brandon Hancock
Right?

00:54:11 - Brandon Hancock
Okay, cool.

00:54:13 - Brandon Hancock
Let me share screens.

00:54:20 - Brandon Hancock
Yeah, okay, so here's, I'm going to show you two screens that I, what I do whenever I'm working on agents to help, like, me brainstorm.

00:54:27 - Brandon Hancock
Okay, so I like to draw stuff out, and I am constantly thinking in different, thinking in ADK, like, that's the way I like to describe it, it's like, by thinking in ADK, I'm thinking, I need to have agents, every time I'm working on an agent, I can give that agent's tools, I can give that agent callbacks, and I have a few other tools at my disposal, such as sequential pipelines, and loop workflows, so like, once I understand all the different puzzle pieces.

00:54:59 - Brandon Hancock
guy golden springs.

00:54:59 - Brandon Hancock
We

00:55:00 - Brandon Hancock
What I usually try and do is just map out exactly what each agent wants to do.

00:55:06 - Brandon Hancock
How can I make sure each one of my agents is doing one task?

00:55:10 - Brandon Hancock
So that's how I like to break apart stuff.

00:55:12 - Brandon Hancock
So for example, I made a YouTube workflow processor that basically asked me questions in a phased approach.

00:55:22 - Brandon Hancock
From there, it starts to delegate to an agent.

00:55:26 - Brandon Hancock
This agent is going to then write a title and hook, save to state, and then automatically gets delegated to the next one.

00:55:33 - Brandon Hancock
So I try to chunk things down into as many small actionable pieces as possible and use state as my best friend.

00:55:42 - Brandon Hancock
Because the second I get good results, I instantly throw it into state.

00:55:45 - Brandon Hancock
And then I move on to the next super small task, instantly throw it into state.

00:55:50 - Brandon Hancock
And then towards the end, use it and put it all together to do whatever you want.

00:55:55 - Brandon Hancock
So like, that's how I like to try and think about it.

00:55:59 - Brandon Hancock
And that's been insane.

00:56:00 - Brandon Hancock
That's helpful for helping me build agents really quickly.

00:56:03 - Brandon Hancock
I'll show you one other thing that's going to make your life so much easier.

00:56:08 - Brandon Hancock
One second.

00:56:12 - Brandon Hancock
One other screen to show.

00:56:16 - Brandon Hancock
One thing that I really have been doing to make my life so much easier when building ADK agents is basically come up with an agent document.

00:56:26 - Brandon Hancock
And what this agent document does is it keeps track.

00:56:30 - Brandon Hancock
It's basically like a digital twin of my true agent workflow.

00:56:34 - Brandon Hancock
What I mean by that is like, if you look inside of my actual agents, you'll see that I have like one root agent.

00:56:43 - Brandon Hancock
Then I have sub-agents.

00:56:45 - Brandon Hancock
All of these sub-agents do stuff.

00:56:47 - Brandon Hancock
Well, that's awful for my actual code to understand, like whenever I'm performing a task, that's so hard for my agent, like when I'm working on programming, for it to like read through a thousand files to figure out how to

00:57:00 - Brandon Hancock
So what I really recommend when you're doing anything that is working with multiple agents, to build something like this, where you have a digital twin of your entire workflow, calls out what all the agents do, what state they read, what state they write, what models they use, and not only do you call it out for every agent, you also have like a nice little list of how everything works together.

00:57:25 - Brandon Hancock
So that when you are making a change, like this is what we show in ship kit, but like when you do make a change to state up here, it instantly knows by looking at this document, oh, if you change state for agent one, this is going to completely destroy agents three, four, and five down here.

00:57:45 - Brandon Hancock
Because if you just try doing agent development kit and building agents one at a time, dude, it's going to, the second you get to complex state management, things are just going to ripple and break.

00:57:56 - Brandon Hancock
So that's why I recommend creating one.

00:57:59 - Brandon Hancock
So that's

00:58:00 - Brandon Hancock
So for your whole project, and as you build, update the document, as you build, update the document, and that's just going to make it so much easier when you're building agents.

00:58:08 - Brandon Hancock
So this is the only way I've been able to build bigger complex agents quickly.

00:58:13 - Brandon Hancock
So hopefully that's helpful.

00:58:16 - Brandon Hancock
that MD file, sorry, this may be a dumb question, but are you doing that manually, or is that like a cursor agent writing that in the background?

00:58:23 - Brandon Hancock
Yeah, so this is part of Shipkit.

00:58:26 - Brandon Hancock
I've never written a single line for all of Shipkit.

00:58:29 - Brandon Hancock
Agents do everything.

00:58:31 - Brandon Hancock
So what I mean by that is like, yeah, so like it's kind of starts off, you take a screenshot of those wireframes that I was showing you of like, hey, I kind of want to build this.

00:58:40 - Brandon Hancock
That instantly gets turned into that roadmap that you just saw.

00:58:44 - Brandon Hancock
And then as I go into building out each agent, then constantly I'm updating that roadmap.

00:58:50 - Brandon Hancock
That way, it's a digital twin is like the best way I would describe it.

00:58:54 - AlexH
Yeah, that's smart.

00:58:56 - Brandon Hancock
Hopefully that works.

00:58:57 - Brandon Hancock
Of course, and seriously, if you have questions, as you dive I'm I'm not

00:59:00 - Brandon Hancock
If you want to do any, like, diagrams or anything next week, would love to, would love to help.

00:59:04 - Brandon Hancock
This is the, this is the fun part, is automating work with agents.

00:59:08 - Brandon Hancock
If there's nothing more satisfying when you press go and you're like, that worked, like, that is the best feeling.

00:59:14 - AlexH
So, so, we'd be happy to help if we can.

00:59:17 - AlexH
Of course, man.

00:59:20 - Brandon Hancock
All right, next up on the question list, David, you're looking for a mentor that will help with your projects and advice.

00:59:30 - Brandon Hancock
Um, I mean, hey, David, the best way to get help, I mean, right now, if you have any questions or anything that you want to hop on the call, I'm happy to, happy to help right now.

00:59:39 - Brandon Hancock
Uh, if not, I think asking super small questions in the, in school is also a really great way to get help.

00:59:45 - Brandon Hancock
We have so many smart guys here on the call.

00:59:48 - David Stamper
Yeah, no, um, definitely, I, I know you guys are smart.

00:59:52 - David Stamper
That's why I didn't come to you guys instead of just assuming.

00:59:54 - David Stamper
Uh, but I've made it a long ways on this project.

00:59:58 - David Stamper
What I'm really looking for is someone.

01:00:00 - David Stamper
That can take the time to walk through it, look at it, that I can explain my questions to because the truth of the matter is I don't even know how to ask the questions sometimes, right?

01:00:11 - David Stamper
Like, keep in mind, I'm not a programmer.

01:00:15 - David Stamper
I'm doing the best that I can, but really I'm an entrepreneur that's learning this as I go.

01:00:20 - David Stamper
And sometimes I don't even know how to word the questions.

01:00:25 - David Stamper
I would just have to show somebody what I'm going through.

01:00:28 - David Stamper
Um, yeah.

01:00:29 - David Stamper
I think part of my issue right now is that when I built out my program, I built out my orchestrating agent and then tried to build other parts of the program on top of it.

01:00:44 - David Stamper
Um, and it doesn't, it doesn't always know that those parts of the program exist now.

01:00:52 - Brandon Hancock
When you say it doesn't know, you're talking about when you're, when you're developing your application, it doesn't know?

01:00:58 - David Stamper
Yeah.

01:00:59 - David Stamper
So I'm like a fire.

01:01:00 - David Stamper
Fired it up, so this is CRM with all the marketing and everything built into it, essentially a mostly automated business, right?

01:01:09 - Brandon Hancock
Yeah.

01:01:10 - David Stamper
So I built it all out, fired it up, and then I was like, oh, I want to add this feature, and I want to add that feature.

01:01:16 - David Stamper
And as I've added these different features, my AI literally, like, I have to argue with it for, like, 15 minutes before it recognizes that it actually can do the  that I'm telling it it can.

01:01:28 - Brandon Hancock
So, and I don't know how to fix it, that's problematic.

01:01:33 - David Stamper
So, you know, I just want somebody to walk through it with me and kind of be able to say, okay, this is what I would advise you to do differently, because I'm more than willing to put in the work.

01:01:44 - David Stamper
I'm a good worker, but I'm just not as knowledgeable.

01:01:48 - David Stamper
You guys are smart.

01:01:49 - David Stamper
That's why I'm coming to you.

01:01:51 - Brandon Hancock
I gotcha.

01:01:53 - Brandon Hancock
Yeah.

01:01:54 - Brandon Hancock
I was gonna say, I know a lot of guys are on the call.

01:01:57 - Brandon Hancock
I would, I would personally probably make

01:02:02 - Brandon Hancock
I'm sure a lot of guys would be happy to do it, some for free, some paid, you know, just depending on how much time obligation this is for mentorship.

01:02:11 - Brandon Hancock
I will say just like, without fully understanding or seeing the problem, I can go ahead and tell you the root issue is, it sounds like as you're building out your application, like, the core issue is this is a context problem.

01:02:25 - Brandon Hancock
So, like, the quickest fix that I would do if I was you is I would add in either some sort of agent.md file or something that tells the agent...

01:02:37 - Brandon Hancock
That's the digital twin you were just talking about?

01:02:40 - Brandon Hancock
So, that's a little bit different.

01:02:44 - Brandon Hancock
The agent.md actually is pretty similar, though, when you bring that up, that's actually pretty good.

01:02:48 - Brandon Hancock
Let me show you.

01:02:50 - Brandon Hancock
But in agent.md, it's just like a high level overview of what your project does.

01:02:58 - Brandon Hancock
I think this is...

01:02:59 - Brandon Hancock
is...

01:03:00 - Brandon Hancock
I don't know if I pulled up right one, but yeah, it's an open source format for guiding your agents.

01:03:05 - Brandon Hancock
So basically what you can do is put in here just like a very high level overview of like, my project is this type of project.

01:03:12 - Brandon Hancock
Here are the core files in here.

01:03:15 - Brandon Hancock
Here's how things connect.

01:03:16 - Brandon Hancock
So this is what I would, like, you would need to create one of those so you don't have to, every time you start a chat, do that.

01:03:25 - Brandon Hancock
So that's what I would recommend.

01:03:27 - David Stamper
And to the gentleman before me's question about automating that, does, is there a way for me to have Cursor build out what I currently have in place?

01:03:39 - Brandon Hancock
Yeah, the core, the, the, never write another line of code is my, is my mandate, manually at least.

01:03:47 - Brandon Hancock
Yeah, the, the core, the core lesson here is find a good example of what you're looking for online and say, hey, AI, look at my project, make this, but for my project.

01:03:56 - Brandon Hancock
And it will, you know, it might not do it perfect, but it'll do it 80%.

01:04:00 - Brandon Hancock
And then you could just ask a few follow-up questions along the way and get it to hone in.

01:04:05 - Brandon Hancock
So that would be my advice.

01:04:07 - Brandon Hancock
you very much.

01:04:08 - David Stamper
Of course, appreciate you.

01:04:09 - David Stamper
And I'm really looking forward to Shipkit, so...

01:04:12 - Brandon Hancock
Thanks, man.

01:04:13 - Brandon Hancock
I am so pumped.

01:04:16 - David Stamper
Yeah, man, I know you're putting in the hours.

01:04:19 - David Stamper
I've just started my program, but there's literally been some 36-hour days already.

01:04:24 - Brandon Hancock
Yeah, dude, we're all suffering together.

01:04:29 - David Stamper
We're all putting in the work.

01:04:31 - Brandon Hancock
Awesome.

01:04:32 - Brandon Hancock
Awesome, man.

01:04:32 - David Stamper
Looking forward to your things, man.

01:04:34 - Brandon Hancock
Of course.

01:04:34 - Brandon Hancock
Please speak to me if I can help with anything else.

01:04:36 - David Stamper
Okay.

01:04:37 - Brandon Hancock
And Mitch, I saw you had your hand up for a minute now.

01:04:39 - Brandon Hancock
Sorry about that.

01:04:41 - Mitch
Not at all.

01:04:42 - Mitch
So, can you hear me?

01:04:44 - Brandon Hancock
Yes.

01:04:44 - Brandon Hancock
Yeah.

01:04:44 - Brandon Hancock
Okay, cool.

01:04:45 - Mitch
So, you know how you're saying you don't write with, like, in a code anymore.

01:04:49 - Mitch
You don't write it by manually, but you do make your Escaladraw boards manual.

01:04:55 - Mitch
Yeah, yes.

01:04:56 - Brandon Hancock
I was like...

01:04:58 - Brandon Hancock
I sometimes write on a notepad, too.

01:05:00 - Mitch
Yeah, and so I was just like, I'm supposed to be the AI guy, I'm like, what am I not doing with AI, so I was like, wait, why don't I just make a current, like, active Mermaid file, like an MD, and then just have Cursor edit that, and it's been really good.

01:05:15 - Mitch
You just quote the voice memo, edits the Markdown file, does all the changes for you, do it right in front of the client.

01:05:23 - Brandon Hancock
No, I, I have been really liking Mermaid, except, I've been liking Mermaid for when I have a ton of code, and I want to make a cool visual for that code, to break it down, to walk it through other people, but like, I guess my, like, creative process of like, I'm struggling, like, I can't even put words on what I'm trying to build sometimes, and I literally have to draw a box, and I'm like, okay, what happens next?

01:05:48 - Brandon Hancock
Next box, you know, it's like, sometimes I, like, drawing is the way I, like, get my ideas out of my head, so, but no, you're, you're totally spot on for Mermaid.

01:05:59 - Brandon Hancock
Do you have any examples?

01:06:00 - Brandon Hancock
I'd be, I'd be curious to see if you had any examples.

01:06:02 - Mitch
Um, none that I could share.

01:06:05 - Mitch
Um, but yeah, it's, it's just when you're like working with a client and like, you're like showing them like your use of AI and like, they can see it, like update live with like voice memos.

01:06:16 - Mitch
They like, they actually like strongly believe like, oh, like this guy is magical.

01:06:21 - Brandon Hancock
Like he can do what I'm thinking.

01:06:23 - Mitch
He's He's a wizard.

01:06:25 - Mitch
So just a, yeah, freebie for y'all.

01:06:29 - Mitch
Yeah.

01:06:29 - Mitch
No, I think that's awesome.

01:06:32 - Brandon Hancock
yeah, uh, two, two quick things just to add on to that.

01:06:34 - Brandon Hancock
There really is a, um, there's a cool tool in signed of, uh, um, basically cursor.

01:06:44 - Brandon Hancock
So if you go and look at your extensions, where is it at, but yeah, it's just called mermaid.

01:06:49 - Brandon Hancock
And, um, basically it's mermaid chart.

01:06:51 - Brandon Hancock
And this is the tool that will allow you to like visualize mermaid drawings inside of a cursor.

01:06:58 - Brandon Hancock
So I don't know if I have any.

01:06:59 - Brandon Hancock
Yeah.

01:07:00 - Brandon Hancock
I in here.

01:07:00 - Brandon Hancock
I think I just cleaned them out.

01:07:02 - Brandon Hancock
I just cleaned out a bunch of diagrams.

01:07:04 - Brandon Hancock
No, I think I still have some.

01:07:05 - Brandon Hancock
Yeah.

01:07:06 - Brandon Hancock
So what's cool is, like, with Mermaid, you get to do this inside of Cursor.

01:07:12 - Brandon Hancock
It's like, this is how I was describing, like, when I'm trying to break down how does this code work, it's sick.

01:07:18 - Brandon Hancock
In Mermaid, just, or literally with AI, you just say, like, hey, make a Mermaid diagram.

01:07:22 - Brandon Hancock
And at this point, it creates this, and it's so easy to explain code.

01:07:26 - Brandon Hancock
Because sometimes, like, looking at code, it's like, man, that was 12 lines of code just to say, validate this, you know?

01:07:33 - Brandon Hancock
So I cannot recommend using Mermaid enough.

01:07:38 - Brandon Hancock
You got me laughing about you're a wizard.

01:07:42 - Brandon Hancock
But no, that's an awesome idea, Mitch.

01:07:44 - Mitch
I did make it with a scar, like, somewhere here.

01:07:48 - Brandon Hancock
Right here?

01:07:49 - Mitch
With your glasses?

01:07:50 - Mitch
Yeah.

01:07:54 - Brandon Hancock
That's funny.

01:07:55 - Brandon Hancock
Next time I expect a hat on, Gryffindor, full nine yards.

01:07:59 - Brandon Hancock
All right.

01:08:02 - Brandon Hancock
That's funny, man.

01:08:04 - Brandon Hancock
Let me pop back, open the chat questions.

01:08:08 - Brandon Hancock
Where is it at?

01:08:10 - Elijah
I know I'm not in order, but per that idea, do you draw on a board as well when you're using Excel Draw?

01:08:19 - Elijah
Like a real world board?

01:08:21 - Elijah
You have like a pen there with you or you're just using your mouse?

01:08:25 - Brandon Hancock
Mouse is the main way I do it.

01:08:27 - Elijah
Okay, sorry, because you just, it looks really good, like you're drawing very accurately, so.

01:08:34 - Brandon Hancock
The one thing I will show real fast, I think the other tool that, like this, like all these arrows, that's called, that's called Presentify.

01:08:43 - Brandon Hancock
So that's, if you ever see me draw on top of something, that's Presentify.

01:08:48 - Brandon Hancock
And it's like 10 bucks, definitely recommend it.

01:08:53 - Brandon Hancock
So if you're, if you're ever trying to annotate on your stuff, it is the best tool for quickly showcasing what's happening on your screen.

01:08:59 - Brandon Hancock
time We'll bye.

01:08:59 - Brandon Hancock
Thank

01:09:01 - Brandon Hancock
Ram, he's a he's a friend of the channel.

01:09:03 - Brandon Hancock
So I definitely recommend it.

01:09:05 - Brandon Hancock
Okay.

01:09:07 - Brandon Hancock
Let's keep on going, guys.

01:09:08 - Brandon Hancock
I know we're getting a little bit close, but I want to make sure I get sure everyone's questions are met.

01:09:13 - Brandon Hancock
And like I said, we'll be back to normal schedule next week.

01:09:15 - Brandon Hancock
It's just chug more coffee and get back.

01:09:21 - Brandon Hancock
Am I?

01:09:22 - Brandon Hancock
Okay.

01:09:23 - Brandon Hancock
Have I missed any of those questions?

01:09:25 - Brandon Hancock
if y'all want to raise your hands, I haven't hit your questions, and that way I can make sure everyone's good to go.

01:09:35 - Brandon Hancock
And like I said, y'all can keep y'all can keep the party going.

01:09:37 - Brandon Hancock
I apologize.

01:09:38 - Brandon Hancock
I just have to.

01:09:41 - Brandon Hancock
I have one more if there's no other one.

01:09:43 - Brandon Hancock
Hit me.

01:09:43 - Elijah
Um, when you showed the courses for the rag, uh, chip kit software that you're, you're, you have.

01:09:53 - Brandon Hancock
Yeah.

01:09:54 - Elijah
What were the, were the courses that you're developing in there?

01:09:58 - Elijah
That is the act.

01:10:00 - Elijah
The Shipkit project, right, is basically that learning structure, that learning management system.

01:10:09 - Brandon Hancock
Yes, yes.

01:10:10 - Brandon Hancock
So, yes, so Shipkit, let me, I guess, let me just make sure I'm saying this right.

01:10:15 - Brandon Hancock
So, let me, I'll share screen.

01:10:18 - Brandon Hancock
So, like, inside of Shipkit, this, like, this right here, oops, sorry.

01:10:24 - Brandon Hancock
Like, this is where you guys will come to, like, learn the process end to end.

01:10:30 - Brandon Hancock
In addition to that, you will hook up, I think I got to work on this, but you will, you'll hook up your GitHub repository.

01:10:40 - Brandon Hancock
And this is how you'll get instant access to all the different project templates and the rest of the other examples.

01:10:47 - Brandon Hancock
And then you can download them.

01:10:49 - Brandon Hancock
then inside of each example project, that's where you'll get, let me make sure I have the right thing.

01:10:58 - Brandon Hancock
Like, I think this is one of them.

01:11:04 - Brandon Hancock
All right, it failed.

01:11:06 - Brandon Hancock
One second.

01:11:08 - Brandon Hancock
Bring this over.

01:11:09 - Brandon Hancock
Cool.

01:11:09 - Brandon Hancock
But like, and then with inside of each project, that's where you get all the AI templates and everything else.

01:11:16 - Brandon Hancock
Did I answer that?

01:11:18 - Elijah
Yeah, that first screen that you showed with all the courses, that thing that we're logging into, is that just the RAG ShipKit, or is that all of ShipKit?

01:11:31 - Elijah
Is that the whole ShipKit portal?

01:11:34 - Brandon Hancock
Yeah, so that is the ShipKit portal where you get to log in.

01:11:38 - Brandon Hancock
And I think the part that I might have been confusing you guys on is like, the RAG template, like the RAG pre-built project was used to build out the course platform.

01:11:48 - Brandon Hancock
So what I mean by that is like, all of the document chunking, embedding, and everything that you guys learn, that's the exact same pipeline I use to help you guys ask questions about the course.

01:12:00 - Brandon Hancock
And inside of the course, you'll get to see like walkthroughs and lessons for every single project type, chat, ADK, RAG, it's all in there.

01:12:09 - Brandon Hancock
And the course structure itself, that learning management structure, that software, is that included in ShipKit?

01:12:18 - Brandon Hancock
There is a walkthrough where I go from the RAG template to a minimum version of this, but yes, that's one of the other, like in the walkthrough.

01:12:27 - Brandon Hancock
You see how I go from the RAG template, how I get to like a simpler version of the AI course, and that's also in ShipKit.

01:12:34 - Brandon Hancock
Yeah.

01:12:34 - Brandon Hancock
That's one of the projects you get.

01:12:35 - Elijah
So you're not, you're not going to host your courses, if you will, on school.

01:12:40 - Elijah
They're going to be in this new platform.

01:12:44 - Brandon Hancock
Correct.

01:12:45 - Brandon Hancock
Just because school does not allow you to add comments on post, they have no AI functionality.

01:12:50 - Brandon Hancock
Like there's, it's honestly not the best for learning, which is like, which makes me sad.

01:12:54 - Brandon Hancock
It's, it's the best for very quick, like small modules.

01:12:57 - Brandon Hancock
But like, right now, if you were to watch like my last

01:13:00 - Brandon Hancock
The project that I did inside of school, if you guys watched a module and you had a question, you had to go back to the homepage to find a post, to then drop a question, to then hop back, like, it's just, it's not intuitive for learning, fortunately.

01:13:14 - Elijah
So I know you got to jump, but are you familiar with SCORM?

01:13:20 - Elijah
Okay, so SCORM is just a file format for learning management systems.

01:13:25 - Elijah
So, like, I think, I mean, I'd love, I'm, I'm very excited to see ShipKit in its entirety, everything that you're doing, um, I'd love to talk to you more as we continue to move forward, because the whole learning management space in the ed-tech world, like, that's where I come from, um, I just see a, there's a very significant opportunity for what you've built related to that piece.

01:13:51 - Elijah
And so if you can import the SCORM files, you know, I mean, there's big, big companies in that space that...

01:14:00 - Elijah
You can't do what you're doing.

01:14:01 - Elijah
So there's a pretty good opportunity there.

01:14:04 - Brandon Hancock
The whole goal of Shipkit is you guys come from all sorts of different technical backgrounds, all sorts of opportunities that I would never even think of.

01:14:11 - Brandon Hancock
So what I'm hoping is happening is give you guys the core foundation and you guys go off, take these templates and literally launch your own real world applications.

01:14:22 - Brandon Hancock
That's what I'm hoping.

01:14:23 - Brandon Hancock
So would love for, it sounds like you have a really cool opportunity or idea.

01:14:27 - Brandon Hancock
Hey, like, let's make it happen, man.

01:14:29 - Brandon Hancock
We'd love to see you build it.

01:14:31 - Elijah
Thank you.

01:14:31 - Elijah
That's the whole goal.

01:14:32 - Brandon Hancock
Of course.

01:14:33 - Elijah
No, thank you for your hard work.

01:14:35 - Brandon Hancock
Thank you.

01:14:36 - Elijah
Of course.

01:14:37 - Brandon Hancock
Alex.

01:14:39 - Alex Wilson
I don't have my camera this week.

01:14:41 - Alex Wilson
So just a real super, super quick question.

01:14:44 - Alex Wilson
I sent you a DM.

01:14:46 - Alex Wilson
I'm taking your advice and doing the LinkedIn posts.

01:14:51 - Alex Wilson
So I just wanted to make sure you were okay if I called you out in LinkedIn.

01:14:55 - Brandon Hancock
Yeah.

01:14:57 - Brandon Hancock
I'm pulling it up right now.

01:14:58 - Brandon Hancock
I'm doing it.

01:14:59 - Alex Wilson
I'm doing Uh

01:15:00 - Alex Wilson
And advertise Chipkit a little bit.

01:15:02 - Brandon Hancock
Oh, dude.

01:15:03 - Brandon Hancock
Oh, of course.

01:15:04 - Brandon Hancock
I appreciate it.

01:15:05 - Brandon Hancock
Yeah, I apologize.

01:15:06 - Brandon Hancock
I normally, yes, I normally try and respond faster.

01:15:09 - Brandon Hancock
But yeah, seriously, always feel free to say anything nice, not nice, whatever.

01:15:15 - Brandon Hancock
Just use the best policy.

01:15:17 - Brandon Hancock
So, but yeah, seriously, would be happy to, yeah, Alex Wright, happy to, oh, happy to repost it too, or anything like that.

01:15:26 - Alex Wilson
Excellent.

01:15:26 - Alex Wilson
Thank you, thank you, thank you.

01:15:27 - Alex Wilson
I just wanted to make sure it was nothing against your brand or anything like that, you know?

01:15:31 - Brandon Hancock
Yeah, no, I seriously, I appreciate it.

01:15:34 - Brandon Hancock
Yeah, and seriously, I would love to see as you do more LinkedIn posts, please keep tagging me.

01:15:41 - Brandon Hancock
I'd love to, would love to repost or do whatever I can to help.

01:15:45 - Alex Wilson
All right, I'll do that.

01:15:46 - Alex Wilson
Thank you.

01:15:47 - Brandon Hancock
Of course.

01:15:48 - Brandon Hancock
All right, I think last few things.

01:15:51 - Brandon Hancock
Patrick, to answer your comment, dude, you're spot on.

01:15:54 - Brandon Hancock
I uh, to..

01:15:56 - Brandon Hancock
you have to watch the movie Inception to understand Shipkid.

01:16:00 - Brandon Hancock
I think the second people get in and like I will turn on like I will have like a mode to where people can come in and click around they won't be able to read the content unless they like pay but I will turn that on and I think that's gonna make so much more sense the second people can actually like go in and click around but yeah if you're totally right my friends have said the same thing because I was like guys it's the coolest thing ever like the thing I built built the thing I built and they're like what are you saying and I'm like you just gotta come here and look you gotta come here and look and then it all make sense but um but yeah you're spot on the implementation of the template is the actual product yeah I mean that's one of the cool parts is yeah like that was the um was we were trying to seek uh I was trying to seek maximum leverage and proof and I was like man there's no better proof than like built the thing you're on with the thing you're getting if that makes sense so uh that's what I was um I had that revelation one night and I was like oh my god write this down before I forget

01:17:04 - Brandon Hancock
Yeah, and thank you guys as well, but yeah, all right guys, I do, I do gotta hop, I gotta go back recording everything, but seriously, I don't know if, if anyone wants to be host, I'd be happy to make someone else host if y'all wanna keep the party going, I feel like, I don't want to deny you, you're the, our AI nerd hour guys, so if anyone wants to be host, happy to set it, if not, if y wanna call it short, happy to call it short, is whatever you guys would prefer.

01:17:29 - Brandon Hancock
And I think what I'll do, Jake, will make you host, and then I will let you guys, I will let you guys pick what happens next.

01:17:38 - Brandon Hancock
So Jake, host Jake, dumped, knighted, all of it.

01:17:44 - Brandon Hancock
If you guys have any questions, we'll be back to our normal schedule next Tuesday guys, so excited, it's gonna be a fun Saturday, and yeah, cannot wait to see what you guys build, and I will be around, answer emails and anything if you have any questions, so thanks, y'all are awesome.

01:17:56 - Elijah
There's not a live release for Shipkit, is there?

01:17:59 - Brandon Hancock
A live

01:18:00 - Brandon Hancock
I'm like a video.

01:18:00 - Elijah
Like this.

01:18:02 - Elijah
You're not doing like a show or nothing with it.

01:18:05 - Elijah
You're just releasing on the 27th.

01:18:09 - Brandon Hancock
Yeah, I'm going to release on the 27th.

01:18:10 - Brandon Hancock
I might at, I don't know.

01:18:15 - Brandon Hancock
I will announce the day of.

01:18:17 - Brandon Hancock
It's happening at 6pm on Saturday.

01:18:19 - Brandon Hancock
I have the time and everything ready.

01:18:21 - Brandon Hancock
So I will, I might do like a random live.

01:18:24 - Brandon Hancock
But you'll get a notification through school.

01:18:26 - Brandon Hancock
So it's just, quick side note.

01:18:30 - Brandon Hancock
I mean, you guys, y'all, most developers.

01:18:32 - Brandon Hancock
So like, there's nothing more stressful than launch.

01:18:34 - Brandon Hancock
So that's why I'm like hesitant to say, oh yeah, we're going to have a video.

01:18:38 - Brandon Hancock
Cause like, there's a chance, like, even though I've tried this a thousand times myself, I turn it on and I go, hey guys, we're going to have a fun launch party.

01:18:46 - Brandon Hancock
Someone clicks a button that was never supposed to be clicked in that order and everything goes wrong.

01:18:51 - Brandon Hancock
Like, I don't want that recorded.

01:18:53 - Brandon Hancock
That trauma on my face.

01:18:54 - Elijah
Then you say, oh, I think it's the internet.

01:18:57 - Elijah
Your internet's not working.

01:18:58 - Elijah
I'm breaking up.

01:19:00 - Brandon Hancock
I gotta, I gotta go.

01:19:03 - Brandon Hancock
So, so that's why I'm hesitant on the live launch.

01:19:06 - Brandon Hancock
I will be at my computer, but just like, check in refreshing a thousand times to make sure everything's going well.

01:19:12 - Brandon Hancock
So that will be happening.

01:19:14 - Brandon Hancock
So, but yeah, great question.

01:19:16 - Brandon Hancock
Not at the Alex Sermozzi level where, you know, launched millions of books in a, in a, in a day.

01:19:22 - Brandon Hancock
He's, he's on a different level.

01:19:24 - Brandon Hancock
And he's not doing software.

01:19:25 - Brandon Hancock
That's the, that's the other part.

01:19:28 - Brandon Hancock
So, all right, guys.

01:19:29 - Brandon Hancock
Well, I gotta go.

01:19:30 - Brandon Hancock
Hope you have a great Tuesday, Jake, King Jake, um, for the rest of the call.

01:19:33 - Brandon Hancock
Thanks, guys.

01:19:34 - Brandon Hancock
And I'll talk to you soon.

01:19:35 - Jake Maymar
Thanks, Brendan, for your hard work.

01:19:37 - Brandon Hancock
Thanks.

01:19:40 - Jake Maymar
All right, guys.

01:19:40 - Jake Maymar
Any questions?

01:19:41 - Jake Maymar
Does anyone have any questions?

01:19:42 - Jake Maymar
Where they jump?

01:19:45 - Elijah
I had a follow up for Mitch.

01:19:50 - Elijah
Mitch, you were, you were, uh, what were you doing that was live with folks, the drawing?

01:19:58 - Mitch
Oh, yeah.

01:19:59 - Elijah
Were a mermaid?

01:19:59 - Elijah
What was

01:20:00 - Elijah
What was the thing you were showing people live and on the calls?

01:20:03 - Mitch
Yeah, so I do content automation, so I was showing him, like, different content flows we could do, like, with different agents to connect with other agents.

01:20:15 - Elijah
Like, using, like, automation platforms like in Aiden, or you code your own?

01:20:22 - Mitch
Yeah, they're all custom coded, yeah, yeah.

01:20:25 - Elijah
Okay, cool.

01:20:33 - Jake Maymar
Yeah, I can't wait to use ShipKit.

01:20:35 - Jake Maymar
I think that's going to be really exciting.

01:20:37 - Jake Maymar
I didn't realize that it was, like, basically, um, an app within an app within an app.

01:20:43 - Jake Maymar
Um, I'm actually really excited what we're going to build sort of using the tools, and then the whole thing is just going to get better and better and better.

01:20:51 - Jake Maymar
Like, uh, the first thing I want to do is, um, uh, Neo4JS on the rag.

01:20:57 - Jake Maymar
Like, that seems to be, like, I mean, I haven't seen it yet.

01:21:00 - Jake Maymar
But I mean that to me that seems like some sort of graph rag, right?

01:21:04 - Jake Maymar
Maybe not Neo4, but it could be something, right?

01:21:07 - Jake Maymar
And then we could have like an artifact side.

01:21:11 - Jake Maymar
can have all these different things, you know?

01:21:13 - Jake Maymar
And so I'm really excited.

01:21:17 - Jake Maymar
And I'm already using the templates.

01:21:19 - Jake Maymar
The templates are amazing.

01:21:22 - Jake Maymar
But anyway.

01:21:24 - Jake Maymar
So anyone have any questions?

01:21:27 - Patrick Chouinard
Well, basically, from what I understood, you have a bunch of templates.

01:21:30 - Patrick Chouinard
From the templates, he actually created some sample implementation of four different scenario.

01:21:36 - Patrick Chouinard
And he also have training material of how he implemented those four scenarios.

01:21:45 - Patrick Chouinard
So that's what he's talking about, about the product, develop the product and train on the product.

01:21:52 - Jake Maymar
It's amazing.

01:21:53 - Jake Maymar
Yeah.

01:21:53 - Jake Maymar
And the thing is, is like, I, I'm curious to see if there's going to be like, point, say, I've been Yeah.

01:22:00 - Jake Maymar
It creates a course, right, so it actually has video, that would be pretty amazing, that would actually create a structured, I mean, there's all sorts of really interesting directions you could go.

01:22:15 - Ty Wells
Well, it's like Cloud Code, right?

01:22:17 - Ty Wells
They use Cloud Code to build Cloud Code.

01:22:20 - Ty Wells
I mean, you know, so that's what he did.

01:22:23 - Ty Wells
Yeah, yeah.

01:22:24 - Ty Wells
Which is a good structure, I believe, from what I've seen.

01:22:28 - Ty Wells
The structure is good, so if you're getting in, it's a good methodology approach, his approach, but it's solid from what I've seen so far.

01:22:40 - Jake Maymar
Yeah, and like, you know, I also like Brandon referencing like real-world applications that are deployed and saying, okay, I want this component, right?

01:22:51 - Jake Maymar
And how do I basically get this component into my application?

01:22:56 - Jake Maymar
I think that's really brilliant.

01:22:58 - Jake Maymar
So So,

01:23:00 - Jake Maymar
Paul, just to kind of address what you're talking about, completely agree, like, having that grounding, you know, I want to get it to stop going off the guard, yeah, I want it to stay on the guardrails, I want it to basically, like, obey, and Bastian had some really good tips on this, but it's, you know, I wait for the day when, like, AI is deterministic, and we have it look at a file, and it says it did it, and you look, and it actually did it, right?

01:23:36 - Jake Maymar
The thing I can't figure out is why it's so hard to write files, like, if you're using Cloud Code, Cloud Desktop, Cursor, whatever, it's so hard.

01:23:47 - Jake Maymar
It just sits there, and it, like, really struggles to write the code and write the diff and everything.

01:23:52 - Jake Maymar
I just think that's kind of amazing, and that's a huge opportunity.

01:23:57 - Jake Maymar
The other side is the context window, right?

01:23:59 - Jake Maymar
okay.

01:24:00 - Jake Maymar
Like, you know, it's kind of interesting, if you're using Cloud Desktop, you don't have access, maybe you do, but having access to that million context window, that makes all the difference in the world, and it's kind of odd that it's not built in, but yeah, I kind of can't wait till, like, we actually have context windows that we could just fill up, and we're not, like, moving stuff around all the time.

01:24:31 - Mitch
Have you given Codex a try, Jake?

01:24:33 - Mitch
Do you have a preference at all, or are you still on the Cloud side?

01:24:36 - Jake Maymar
So, I've played around a little bit with Codex 2, and it's really confusing, because there's, like, ten versions of this thing, but, like, I don't know.

01:24:45 - Jake Maymar
It seems like it's version 10, but Codex 2 is really interesting.

01:24:49 - Jake Maymar
It's really, I mean, simple projects.

01:24:52 - Jake Maymar
I just tested, and I did a code review.

01:24:56 - Jake Maymar
I did, like, a PRD.

01:25:00 - Jake Maymar
I a requirements doc, and then I did some components.

01:25:06 - Jake Maymar
Mixed results.

01:25:08 - Jake Maymar
Some of it was good, some of it was okay, but it wasn't consistent.

01:25:15 - Jake Maymar
I asked it the exact same thing.

01:25:18 - Jake Maymar
I asked it to build the exact same feature, and the first time it was really good, the second time it was not good at all, and then the third time it was actually kind of good.

01:25:30 - Jake Maymar
But they were so different.

01:25:32 - Jake Maymar
And that's the other thing I'm really looking forward to is, like, some consistency.

01:25:36 - Jake Maymar
Because it's really, really hard.

01:25:38 - Jake Maymar
I was on a call with an executive, and they were actually coding, which is a really, you know, talking where Patrick was sort of talking about.

01:25:48 - Jake Maymar
They were coding.

01:25:49 - Jake Maymar
And, you know, I remember, you know, when I was doing website design, and I got on with an executive, and this is like, you know, many, many years ago.

01:25:58 - Jake Maymar
But I got on with an executive, and they were actually...

01:26:00 - Jake Maymar
They using Photoshop, they were building a whole website using Photoshop, and at first I was like, oh man, like, what's going to happen, right, you're not going to, you know, and then, you know, they were coding it using, you know, simple tools, well, now people are coding very, very sophisticated apps and not really understanding them at all, so, I don't know, I'm curious to see how quickly this matures where I don't know, I don't where you either have to understand it or we have so many templates that the systems just kind of work, you know, it reminds me of, there's a Star Trek episode, where the aliens are pointing at the ship and saying, make go, and that's all they can say, right, that's it.

01:26:50 - Jake Maymar
And I worry that we're going to get to that stage where we don't really understand.

01:26:57 - Jake Maymar
It's kind of interesting.

01:26:58 - Jake Maymar
I was on a different call.

01:27:00 - Jake Maymar
They were saying that they're going to look back at the time right before AI and think that those people did impossible tasks, you know, because I can't imagine like where we're going to be like in just a couple of years and looking back at what we, you know, what people used to do in order to create the things that we have now and we use every day.

01:27:31 - Jake Maymar
Well, this is great.

01:27:32 - Jake Maymar
Thanks for sharing this, Patrick.

01:27:36 - Jake Maymar
So on this, Patrick, do you kind of want to talk about it a little bit because this is really interesting?

01:27:41 - Patrick Chouinard
Agents.

01:27:42 - Patrick Chouinard
And so agents did...

01:27:46 - Patrick Chouinard
Sorry.

01:27:46 - Patrick Chouinard
Yeah, no, it's just the video I've pointed you to is very, very nice about context management with Cloud Code, how to maximize the amount of context that you have, how to compress, when to do it, I was...

01:28:00 - Patrick Chouinard
Remove tools, how to include tools, when to do it, how to split into multiple sub-agents.

01:28:05 - Patrick Chouinard
Always, always focusing on having enough context left for any task you want to start with.

01:28:12 - Patrick Chouinard
I love the video.

01:28:13 - Patrick Chouinard
It's a bit long, but it's extremely well-built.

01:28:17 - Jake Maymar
Oh, amazing.

01:28:19 - Jake Maymar
Thank you for sharing that.

01:28:20 - Ty Wells
Patrick, it's 29 minutes.

01:28:21 - Ty Wells
How is that long?

01:28:25 - Patrick Chouinard
Well, I guess you're right.

01:28:27 - Ty Wells
You're right.

01:28:27 - Ty Wells
I watch my videos at 2X, so that's a good one.

01:28:32 - Patrick Chouinard
Keeps me focused.

01:28:34 - Patrick Chouinard
No, it's just because it focuses on, specifically, context management.

01:28:38 - Patrick Chouinard
So, 30 minutes on context management, not how to include MCP.

01:28:44 - Ty Wells
gotcha.

01:28:44 - Ty Wells
It's really, like, how do you manage context and clog code for 30 minutes.

01:28:49 - Ty Wells
Gotcha.

01:28:49 - Ty Wells
Well, that's why I watch it at 2X, because I can't, my brain can't process anything.

01:28:54 - Ty Wells
I can only try to absorb those words, so it keeps me focused.

01:28:57 - Patrick Chouinard
Actually, what I do really often...

01:28:59 - Patrick Chouinard
you.

01:29:00 - Patrick Chouinard
Maybe I shouldn't say that, but I've took those videos, shoved them into Notebook.lm, and just listened to the Strip Down podcast coming from the transcript.

01:29:11 - Ty Wells
Yeah, I do that too.

01:29:12 - Ty Wells
Don't worry about it.

01:29:13 - Ty Wells
Everybody's doing it.

01:29:13 - Patrick Chouinard
There are no secrets out there.

01:29:16 - Jake Maymar
Well, I'll take the transcript and then I'll just ask it questions.

01:29:20 - Jake Maymar
Sometimes that's actually really helpful.

01:29:22 - Jake Maymar
That's the other thing.

01:29:23 - Jake Maymar
I wanted to get to the point when I ask it questions that it, you know, actually answers looking at the transcript.

01:29:30 - Jake Maymar
I feel like, you know, it sort of does it, but...

01:29:34 - Jake Maymar
Oh, I did want to talk about the Grok4Fast.

01:29:38 - Jake Maymar
Sebastian, have you had a chance to use that?

01:29:40 - Jake Maymar
Because that was really interesting.

01:29:41 - Jake Maymar
Where it popped up on the evals is a really unusual place.

01:29:54 - Mitch
Dang, Zoom is not liking fashion.

01:29:56 - Jake Maymar
Yeah, I know.

01:29:56 - Jake Maymar
It's like going in and out and in and out.

01:29:58 - Mitch
Look what happened.

01:29:59 - Jake Maymar
guys.

01:30:00 - Mitch
Um, but yeah, I think, I think it's someone trying to silence him.

01:30:03 - Jake Maymar
It's, uh, who's, who is it?

01:30:06 - Mitch
Uh, who's the open air guy?

01:30:09 - Mitch
He's, he's muting Bastian's bike.

01:30:11 - Mitch
Yeah, let's see.

01:30:12 - Jake Maymar
Let's see.

01:30:12 - Mitch
Oh, ask to unmute.

01:30:14 - David Stamper
Alman.

01:30:15 - Mitch
Sam Alman.

01:30:15 - Mitch
Thank you.

01:30:16 - Jake Maymar
Does that help?

01:30:17 - Jake Maymar
Did that help at all?

01:30:18 - Jake Maymar
I don't know.

01:30:20 - Jake Maymar
Sorry, Bastian.

01:30:20 - Jake Maymar
Tried to get it to work, but yeah, it just seems like it's, it's muting you.

01:30:24 - Bastian
Hello?

01:30:24 - Bastian
Can you hear me?

01:30:25 - Jake Maymar
Oh yeah, now we can hear you.

01:30:26 - Jake Maymar
Now we can hear you.

01:30:26 - Bastian
Oh, great.

01:30:27 - Bastian
Oh yeah.

01:30:27 - Bastian
Uh, so yes, I, I did try it, but, um, I only use, uh, growth code for, uh, in Corsair, but, um, in, in, in Grox app, um, they are, they bake a bunch of tools into the, into the model itself.

01:30:45 - Bastian
So it's very awesome to, to watch it kind of carry out like multi-phase tasks.

01:30:51 - Bastian
Uh, you can actually instruct the two to use multiple phases, and you can also kind of guide it on what tools it should use.

01:30:59 - Bastian
Yeah.

01:31:00 - Bastian
And it's kind of open about it, you don't need to, like, jaybreak it or anything, and all of these tools are prefixed like xai underscore tool name, and yeah, it's really awesome.

01:31:13 - Bastian
In fact, Grok3 mini was kind of incredible for its size because it was able to call a bunch of tools in its reasoning chains, and that's not something to kind of take for granted.

01:31:26 - Bastian
So, yeah, very good experience so far, and it's, like, 40 times cheaper than Grok4, much, much faster.

01:31:36 - Bastian
And even if you use it in the application, you don't need to, like, select these modes for, like, deep research, think, and all that.

01:31:42 - Bastian
It handles all of that automatically.

01:31:44 - Bastian
Really interesting, like, in the technical side.

01:31:46 - Bastian
But yeah, I would encourage you to try it out.

01:31:49 - Bastian
And maybe not, especially for, like, the research phases, it's quite good.

01:31:55 - Bastian
And it can look inside, like, x posts.

01:31:58 - Bastian
And...

01:31:59 - Bastian
And...

01:32:00 - Bastian
Also, it has some restrictions, but it's quite open anyway, and also browse the internet and it kind of like decides what's the next step.

01:32:10 - Bastian
It has a lot of adaptability like built in.

01:32:12 - Jake Maymar
It's very good.

01:32:14 - Jake Maymar
Interesting.

01:32:15 - Jake Maymar
Yeah, I'll definitely have to try that.

01:32:16 - Jake Maymar
Oh, and then, Bastian, the other thing is, did you see Chef as open source now?

01:32:21 - Jake Maymar
I thought that would be kind of interesting.

01:32:22 - Jake Maymar
Yeah, did notice that.

01:32:24 - Bastian
It's interesting, but, I mean, what they use that's like unique to Chef, as far as I can tell, in terms of connecting it to Convex.

01:32:37 - Bastian
It's like just a markdown file inside their web application.

01:32:43 - Bastian
So, when you download those projects, you can get those markdown files directly with very good instructions for how to manage your TypeScript files and all of that in your environment.

01:32:57 - Bastian
So, I think it's...

01:32:59 - Bastian
it's...

01:33:00 - Bastian
It's based on Bolt, and Bolt is open source, so it's kind of like open sourcing the derivative.

01:33:06 - Bastian
Not exactly sure, but I think it's based on Bolt, like Bolt.new.

01:33:10 - Jake Maymar
Yeah, I think you're totally right.

01:33:12 - Jake Maymar
I think Bolt DIY, like all of those sort of different branches, I think you're totally right, because I was kind of looking at the code, and it looked kind of familiar.

01:33:23 - Jake Maymar
But they're doing some pretty interesting things.

01:33:25 - Jake Maymar
I feel like I always learn from these things.

01:33:28 - Jake Maymar
But yeah.

01:33:29 - Jake Maymar
Oh, and then, Paul, you were saying about SpecKit, Patrick was doing stuff with SpecKit, which I think he might have already said something.

01:33:41 - Patrick Chouinard
Yeah.

01:33:41 - Patrick Chouinard
No, I just said I was thinking about extending it, but it's a thought I had while driving back from work today, so not ready for implementation yet.

01:33:52 - Patrick Chouinard
But I've used it quite a bit, and so far it does a very good job.

01:33:58 - Patrick Chouinard
And I wouldn't say it's...

01:34:00 - Patrick Chouinard
It's not even Shipkit-lite, it's really just managing, creating the spec, the plan, and the task, that's it, that's all.

01:34:10 - Patrick Chouinard
Shipkit is 20 times bigger than that, but the principle of the thing is really interesting, and it's multi-tool.

01:34:18 - Paul Miller
They've just done updates that take it further, so it does more steps along the way.

01:34:25 - Patrick Chouinard
It's done a little bit more, and what I was thinking is taking it in the reverse direction.

01:34:31 - Patrick Chouinard
They're going to add stuff at implementation and debugging and doing a lot more on that side.

01:34:37 - Patrick Chouinard
I was thinking about doing things upfront instead.

01:34:41 - Patrick Chouinard
All of the managing the issues, all of the pull requests, the commit, all of the administrative part of code management that nobody does in the Vibe coding world right now.

01:34:58 - Paul Miller
Basically, your daily night.

01:34:59 - Paul Miller
on Field

01:35:00 - Paul Miller
Daily work nightmare, managing that.

01:35:02 - Patrick Chouinard
Exactly, I think, even if it does half the job correctly, it's already 50% more than what's getting done today, so...

01:35:12 - Paul Miller
Then you can book that holiday that you were planning.

01:35:17 - Paul Miller
Holiday?

01:35:17 - Paul Miller
What's that?

01:35:20 - Patrick Chouinard
Yeah, exactly, it's just, I was thinking about that, I've talked about it last week, even about the fact that I want to automate that part, but I think that as an extension to spec kit, it would be really awesome because, basically, the first thing you get from the user is an intent.

01:35:37 - Patrick Chouinard
And the intent can be parsed and split into multiple features, multiple issues, multiple user stories, but then it can also be passed to the spec generation and the planning generation.

01:35:52 - Patrick Chouinard
Basically, if you take the intent earlier on in the process, you turbo charge

01:36:02 - Patrick Chouinard
So it would give better plan, better spec, better task if you were processing it earlier in the build.

01:36:10 - Patrick Chouinard
So yep, that's where I was landing.

01:36:13 - Patrick Chouinard
Cool.

01:36:16 - Paul Miller
Yeah, no, I'm looking forward to Shipkit.

01:36:19 - Paul Miller
I'm kind of just, I think, let's get it out.

01:36:24 - Paul Miller
Let's get it working.

01:36:25 - Paul Miller
Let's get a few days of other people testing it, then jump onto it.

01:36:31 - Jake Maymar
Yeah, I totally agree.

01:36:32 - Jake Maymar
I was thinking, almost doing like a friends and family kind of thing, because I know, I know he's working on it, and I bet it feels like it's never done.

01:36:40 - Jake Maymar
But yeah, I think us kicking the tires and kind of, I mean, already using the prompts, those are, those are really nice.

01:36:48 - Jake Maymar
So, you know, just kind of seeing, but yeah.

01:36:52 - Jake Maymar
I'm also still trying to figure out the costs, like how much it would actually cost to run.

01:36:57 - Jake Maymar
You know, just, it seems like it's pretty reasonable.

01:36:59 - Paul Miller
Yeah.

01:37:02 - Paul Miller
Yeah, look, I know Brandon's a big fan of the Google side, but if I think about many of the commercial opportunities I've got, and I'm sure it's probably similar with everyone else, the concept where you go to a hosting provider, they give you a fixed price monthly host, and then you do a whole lot of stuff within that fixed price, that gives me a lot more peace of mind than going to Google, who I've had bill shot before, and it cost thousands, I woke up and had a bill for $2,000, it's like, that scares the bejesus out of me, it's kind of like, give me any of those hosts where I say, alright, I'm getting a host, I'm getting four cores, I'm getting a whole lot of disk, and I'm getting a controlled access to GPU, and I have a cap, that that's kind of what you

01:38:00 - Paul Miller
I want when I'm doing an experiment and where I'm getting a an MVP out there.

01:38:06 - Jake Maymar
Yeah, no, I totally agree.

01:38:08 - Jake Maymar
And, and it's, you know, I'm curious, I, I, I'm really looking forward to sort of when we start talking about the deployments and everything, just, you know, because I saw you had the alerts, but they didn't seem like it was a way to basically restrict, like hard restrict.

01:38:25 - Paul Miller
That doesn't work, that doesn't work with Google.

01:38:28 - Paul Miller
A Google alert, you get the next day.

01:38:31 - Paul Miller
So, Wow, so there's the bill.

01:38:35 - Paul Miller
Yeah, it's not like Amazon.

01:38:38 - Paul Miller
Amazon, you get an alert, and you could set a budget limit, and it just stops, the service just stops.

01:38:44 - Jake Maymar
Right, right.

01:38:45 - Paul Miller
Google, it just keeps, it's, oh, we'll process the alerts once a night, and then the next day you get the bill and the alert.

01:38:55 - Jake Maymar
Yeah, that's, that's painful.

01:38:57 - Jake Maymar
That's very painful.

01:38:59 - Paul Miller
I'd be real.

01:39:00 - Paul Miller
be interested for you to explain, Bastian, your thoughts on, because you've had a little bit more exposure on the looking at the Shipkit stack, is it something that we can do with a host, with a different type of hosting partner other than Google?

01:39:20 - Paul Miller
Is that going to be an option with Shipkit?

01:39:28 - Bastian
I don't really know.

01:39:30 - Bastian
I wouldn't like to talk in Brandon's place, but what I can tell you is that the costs in Google Cloud are pretty, like, you can know upfront how much it will cost, at least have, like, minimums and maximums, so you can, like, have a really complete idea.

01:39:56 - Bastian
I mean, it's basically, the version I was working on.

01:40:00 - Bastian
be interested for you to explain, Bastian, your thoughts on, because you've had a little bit more exposure on the looking at the Shipkit stack, is it something that we can do with a host, with a different type of hosting partner other than Google?

01:40:20 - Bastian
Is that going to be an option with Shipkit?

01:40:28 - Bastian
I don't really know.

01:40:30 - Bastian
I wouldn't like to talk in Brandon's place, but what I can tell you is that the costs in Google Cloud are pretty, like, you can know upfront how much it will cost, at least have, like, minimums and maximums, so you can, like, have a really complete idea.

01:40:56 - Bastian
I mean, it's basically, the version I was working on.

01:41:00 - Bastian
At least, it will run in CPU, so you basically just, like Brandon mentioned, minimum instances is zero, so it scales back to zero, and so baseline costs are nothing, basically, but the costs come when you add users, and that depends on how much vCPU you have, RAM, and the maximum instances, and then you only, like, since they charge basically in time that you use the virtual machines, it's very predictable, I mean, of course, if you set, like, maximum instances to, like, 20 versus 10 or 30, then your costs will be very valuable, but it all depends on how you, like, run the queue for your users, and you can, obviously, customize that further, right?

01:42:00 - Jake Maymar
I think this has to do with your question about deploying in other clouds.

01:42:05 - Jake Maymar
In theory, you can because it's all containerized, but I don't think, if I were Brandon, I wouldn't necessarily offer support to help you set this up in Amazon, for example, because really this is the pain.

01:42:22 - Jake Maymar
It's not just like what you guys were talking about a few months ago.

01:42:27 - Jake Maymar
The real issue is the deployment and getting it to work within the constraints of this particular cloud.

01:42:33 - Jake Maymar
in spite of they all having like equivalent services, like the parameters that you will use are, even they have different names, even if they might do the same.

01:42:45 - Jake Maymar
So for example, if you're going to handle like cold starts or boost CPU and startup for the containers, like all these variables are more nuanced than minimum instances and maximum instances.

01:42:57 - Jake Maymar
But yeah, those are the key drivers.

01:42:59 - Jake Maymar
key drivers.

01:42:59 - Jake Maymar
They

01:43:01 - Jake Maymar
Yeah, that makes sense.

01:43:02 - Paul Miller
I think what's going to be interesting is we're all going to be running these systems, and so we're all going to, I mean, I'll definitely share notes on, you know, costs and what I'm doing and deployment strategies and all those things, and I definitely will have an AWS deployment, I'll probably also have an Azure deployment, I'm sure other people will have that too, so that's what I'm really excited.

01:43:25 - Paul Miller
I really feel like this is going to be a really great focus tool for the group, where we're like building these things and kind of sharing notes and kind of understanding less about the support, but more of like sharing notes, you know, okay, well, this deployment doesn't really work on this platform, you know, or it works, just make sure don't do this kind of thing.

01:43:48 - Paul Miller
Oh, no worries.

01:43:49 - Paul Miller
So guys, I don't know if you guys want to go late.

01:43:54 - Paul Miller
I actually don't know how late we go.

01:43:57 - Paul Miller
But yeah, this has been a great call.

01:43:59 - Paul Miller
time.

01:43:59 - Paul Miller
uh… Never… We Bye.

01:44:01 - Paul Miller
Does anyone have any questions or anything else you want to discuss?

01:44:05 - Paul Miller
I think just sort of one thing in closing, and this was behind the questions that I raised for Brandon, and Brandon quite rightly is focused to get the tool out there in a really critical phase, and I think we all feel for him and so look forward to the end output.

01:44:26 - Paul Miller
What I'm thinking is part of Brandon's brilliance is he's got the thinking, he's very good at showing people how to take them along the journey and be positive and enthusiastic about it, but for this to be a real success, I think, as you were saying, Jake, get the community behind it, so that's good, because all of us are kind of in a similar position that we need this capability for every individual thing that we're doing.

01:44:55 - Patrick Chouinard
That's number one.

01:44:56 - Patrick Chouinard
So it's like so on the money with what we want.

01:45:00 - Jake Maymar
The only issue I can see is, while I like the school community, we're all here because of it, it's a very poor platform for sharing a lot of that knowledge and follow-up, and I'm glad I saw when I asked Brandon about, well, how are you going to cleverly and smartly use that support, and in many ways we kind of need sub-forum discussions on, here's stuff about hosting, here's stuff about using it with cursor versus using it in another way.

01:45:30 - Jake Maymar
Or, here's, like, the best LLMs to use this week, someone's tried the Grok, the latest version of the Grok one, or they've signed up to this other one, we just need to make sure that that support's going to be there so we can help each other and help new people that come on board.

01:45:51 - Jake Maymar
Yeah, I totally agree.

01:45:52 - Jake Maymar
Oh, go ahead.

01:45:53 - Jake Maymar
Sorry.

01:45:53 - Jake Maymar
Sorry, I was going to say, why do I think that maybe we can use Shipkit to build the support site for Shipkit?

01:46:00 - Jake Maymar
That's kind of what I was thinking too, is like, it's going to have all these nice features and we're like, oh, I wish we had this feature.

01:46:06 - Jake Maymar
Then we just build that feature in, you know?

01:46:08 - Jake Maymar
And the other thing is, you're naturally going to have a new group, a ship kit group, and then the school group, you know?

01:46:17 - Mitch
And I think there's going to be some sort of migration over that he talked about.

01:46:21 - Mitch
But yeah, I totally agree with you.

01:46:24 - Paul Miller
I do think there's going to be like a friends and family group where we're like sharing stuff.

01:46:29 - Paul Miller
And like, and is the people, know, the staff with of a of And so, you know, I think all of the advice would give is with a caveat.

01:46:50 - Paul Miller
But I mean, honestly, the friends and family thing is the way I like to work, right?

01:46:54 - Paul Miller
Have authentic conversations.

01:46:56 - Paul Miller
Where does it work?

01:46:57 - Paul Miller
Where does it break?

01:46:57 - Paul Miller
What's the gaps?

01:46:59 - Paul Miller
you know, under

01:47:01 - Paul Miller
And I do love the idea of a platform where we can actually archive all of the knowledge, you know, and then update as we as we learn new things.

01:47:15 - Paul Miller
Yeah.

01:47:16 - Paul Miller
And Paul, with your question, were you asking about the usage side of like the course and like the going over usage on that end with the Google?

01:47:27 - Mitch
Well, it was more, um, so, so it builds, it builds a capability.

01:47:33 - Mitch
Like he, he used the examples with a rag where it deploys a rag.

01:47:37 - Mitch
Oh Back end.

01:47:39 - Mitch
It was more that, that deployment.

01:47:42 - Mitch
Cause I'm kind of, even though I've got that nice big credit with Google, I'm really cautious to the point.

01:47:49 - Mitch
And I don't know if everyone else does it this way.

01:47:52 - Mitch
I always start with, uh, Docker.

01:47:55 - Ty Wells
I've got a whole lot of back office hosts in Docker.

01:47:59 - Ty Wells
So I've got local Docker.

01:48:00 - Bastian
I've got my hosted Docker in DigitalOcean, and then I've got stuff I've put into Google or Amazon, and I think if you follow Kubernetes or Docker approach, surely that would have been the best practice of deployment and hosting rather than trying to code it, or is he just trying to leverage?

01:48:28 - Bastian
No, it's not hosting, it's the vector embedding part that is done through their embedding models, because they're the only ones that can do the video and the, you know, all the different types of images and, like, all the different types, so you're just doing a query to the embedding requests, right, and doing that reverse lookup, but it still ran on the Vercel app.

01:48:54 - Bastian
Right.

01:48:55 - Bastian
I don't think there's any load, there's not much load, just the initial vectorization.

01:48:59 - Bastian
Go

01:49:00 - Bastian
of whatever content, and then, yeah, you're just accessing it.

01:49:06 - Bastian
If I can comment, just a caveat.

01:49:09 - Bastian
Actually, the most demanding process is by far chunking and the OCR process.

01:49:15 - Bastian
It's not the query part or inference, if you will.

01:49:20 - Bastian
It's actually the part where you front load all these files, and you can, of course, update them afterwards.

01:49:27 - Bastian
I think that's part of what Brandon wants to do with the drag application, like to actually have it feed the course, since, in theory, he'll be able to literally upload every YouTube video, every transcript, everything.

01:49:42 - Ty Wells
I mean, not just YouTube videos, also like ShipKit exclusive videos, and you will actually be able to query all of that directly via the ShipKit course.

01:49:53 - Bastian
So, that ties up nicely to what you and Jake were saying about having this, like, community.

01:50:00 - Bastian
I support where Brandon could act or delegate the curation of the information, and then once that's approved, he just uploads it to the Rack thing inside ShipKit course, and then it will be available to everyone, and I think it will just improve and keep improving over the next few months, and it will be an awesome project.

01:50:25 - Ty Wells
The technicalities are very interesting, but everything checks, and I don't see why it wouldn't work.

01:50:32 - Ty Wells
I'm really excited about how it will be in three to six months.

01:50:37 - Ty Wells
I think it will be just nonsense.

01:50:39 - Jake Maymar
Really, really awesome.

01:50:41 - Jake Maymar
Now, come on, guys.

01:50:42 - Jake Maymar
We know that Brandon is tight, so there's no way he's spending any money or putting anything out there.

01:50:47 - Jake Maymar
It's not gonna happen.

01:50:49 - Jake Maymar
He's definitely gonna use the most efficient solution that's available.

01:50:54 - Jake Maymar
Yeah, I think you would have needed a lot of people on support.

01:50:59 - Jake Maymar
And it's

01:51:00 - Jake Maymar
It's really, like, really, really hard.

01:51:02 - Jake Maymar
I think this is the way in this day and age, like, just have our support and helping, like, scale this thing to be as automated as possible and then escalate to him or some few, fewer supporters than he would have otherwise needed.

01:51:20 - Jake Maymar
Yeah, this is really the only way to support any product that you put out there because, yeah, you just, what's the point of a billion-dollar a single company, single-person company if you've got to hire a bunch of people to support it, right?

01:51:40 - Jake Maymar
Yeah, that's interesting.

01:51:41 - Jake Maymar
They always say that the next trillion-dollar company is going to be, like, one person or whatever, but who wants that?

01:51:48 - Jake Maymar
I'd much rather have a lot of friends.

01:51:50 - Jake Maymar
I'd love to have a trillion-dollar company, but I'd definitely love to have a lot of friends to work with, right?

01:51:54 - Jake Maymar
So, yeah, I don't know.

01:51:57 - Jake Maymar
I think the next trillion is going to just be...

01:51:59 - Jake Maymar
I be...

01:52:00 - Jake Maymar
Um, a surprise, um, probably a group very much like this.

01:52:06 - Jake Maymar
I don't know, or maybe we just let AI loose and AI figures it out.

01:52:10 - Jake Maymar
It's a zero person company.

01:52:12 - Juan Torres
Yeah.

01:52:13 - Juan Torres
Oh, I heard, I heard a really interesting article about a taxi cab that hires itself, builds the entire business plan, like the whole thing.

01:52:21 - Juan Torres
And, and like, basically like gets advertised, like advertises and gets clients to basic, you know, to, to pick up and, uh, load balances to figure out, uh, maintenance costs for the car.

01:52:39 - Juan Torres
That's nuts.

01:52:41 - Juan Torres
That's totally nuts.

01:52:42 - Juan Torres
That, that, uh, like, uh, autonomous vehicles do all those things.

01:52:50 - Juan Torres
Oh, and then also cell inference.

01:52:53 - Juan Torres
Right.

01:52:53 - Juan Torres
So of course the, the system itself is the GPU.

01:52:56 - Juan Torres
So it would sell, um, its compute to people.

01:52:59 - Juan Torres
So.

01:52:59 - Juan Torres
.

01:52:59 - Juan Torres
.

01:53:01 - Juan Torres
That's wild.

01:53:03 - Juan Torres
Like, what?

01:53:05 - Juan Torres
Anyway.

01:53:06 - Juan Torres
So, Juan, you joined late.

01:53:09 - Juan Torres
Is there anything you want to discuss?

01:53:12 - Juan Torres
Juan No.

01:53:13 - Juan Torres
Well, if I may share.

01:53:17 - Juan Torres
Let's see.

01:53:18 - Juan Torres
Yes.

01:53:19 - Juan Torres
One of the things that I think it's really interesting is you can use your agentic ID for EC2 instances.

01:53:31 - Juan Torres
Juan I've been playing around with that the last couple of two weeks, just deploying LLMs or diffusion models.

01:53:42 - Juan Torres
Juan right now, it's just been to an A10 GPU, which is not very powerful in order to handle 14 billion parameter diffusion models.

01:53:54 - Juan Torres
Juan You'll be surprised that you actually need way more GPU in order to handle those.

01:53:59 - Juan Torres
Luis Chavez And those...

01:54:00 - Juan Torres
Those has been only for funds.

01:54:04 - Juan Torres
I then have to trade the A10s for financial processing information.

01:54:12 - Juan Torres
But the way I've been trying to go around it is by engaging in CPU offloading.

01:54:20 - Juan Torres
So you can basically set up the EC2 instance to use the, let's say, the A10 has 24 gigabytes of VRAM.

01:54:34 - Juan Torres
And then you have, let's say, 16 gigabytes of CPU.

01:54:39 - Juan Torres
So what you can do is start set up the environment to upload a lot of the processing power from the CUDA environment to the CPU.

01:54:50 - Juan Torres
And then what you can do, and I've been trying to do in order to maximize the environment's capacity is apparently you can come...

01:55:00 - Juan Torres
Convert some of the memory, some of the SD memory, into actual processing capacity.

01:55:07 - Juan Torres
You can recruit it to in order to handle some of the capacity to, and you can do it permanently, can, you know, if you're like dealing with 15 gigabytes, 100 gigabytes or 150, you can recruit a percentage of that memory that you will have in order to just have your files saved there.

01:55:28 - Jake Maymar
Convert basically be used for inferences.

01:55:34 - Jake Maymar
So I've just been playing around with EC2 instances for, and the reason that I give myself that flexibility is because I'm running the EC2 instances for my clients, but then a parallel personal EC2 instance, because sometimes I'm dealing with permissions issues.

01:55:54 - Jake Maymar
So I just have to know what are some of the permissions that I have to send over to my clients.

01:56:00 - Juan Torres
I had in order for him to give me the capacity to do some changes in EC2 instances, virtual private clouds, and so now, today, I'm actually going forward with the development of downloading LLMs in order to carry some tabular data inferences.

01:56:24 - Juan Torres
Nice.

01:56:25 - Juan Torres
Nice.

01:56:26 - Juan Torres
So the LLMs, are they using, like, KimiK2 or, like, what sort of...?

01:56:38 - Juan Torres
I wish I could use the...

01:56:40 - Juan Torres
Are you talking about the one trillion parameter model?

01:56:43 - Juan Torres
Well, I heard the quantized version was pretty good, and then there was, like...

01:56:47 - Juan Torres
Okay.

01:56:49 - Juan Torres
But I don't know.

01:56:50 - Juan Torres
I mean, I'm just kind of curious to see what models are using.

01:56:53 - Juan Torres
you using to do inference?

01:56:57 - Juan Torres
We're working now for...

01:57:00 - Juan Torres
The limited environment, I mean, even when I was deploying the LLMs on an 8100 GPU with 40 gigabytes of VRAM, I was deploying 8 billion parameters and it was taking up a substantial amount of the GPU capacity.

01:57:23 - Juan Torres
And then, like I was saying in the previous call, I was using the GPT OSS 20 billion parameter that it's quantized to four bits in order to carry some inferences.

01:57:35 - Juan Torres
And it was actually requiring less GPU capacity, but the thing is that it's giving out actual space for slowness, its speed is actually decreasing when it's being quantized.

01:57:49 - Ty Wells
And I know, um, what's his name?

01:57:52 - Ty Wells
There was someone that was working with Maxim.

01:57:54 - Juan Torres
He was talking about, well, when you quantize it, isn't it supposed to actually go faster?

01:58:00 - Juan Torres
And the reason that it's supposed to go faster is if it's like having an unrestrict, well, the reason that it's going slow in the first place, it's because it's actually having a very limited environment.

01:58:14 - Juan Torres
And so when you quantize it, you actually give it space in order to go at a more sustainable pace.

01:58:20 - Juan Torres
But in my case, the issue is not GPU capacity.

01:58:24 - Juan Torres
The problem is that compared to other unquantized models, it is relatively slower.

01:58:32 - Juan Torres
So that's why he was basically having this like, you know, he was perplexed by the fact that it was going slower than an 8 billion parameter model, that it's quantized to 16 bits.

01:58:47 - Juan Torres
So did he find, did he figure it out, how to resolve that, or not?

01:58:53 - Juan Torres
Well, both of them actually work pretty effectively in an 8.100 GPU.

01:58:58 - Juan Torres
you, Wim.

01:58:59 - Juan Torres
What you

01:59:00 - Juan Torres
GIGABYTE ENVIRONMENT, BUT NOW WHAT'S HAPPENING IS THAT WE'RE TRANSITIONING FROM THAT KIND OF ENVIRONMENT TO AN A10, 24 GIGABYTE ENVIRONMENT, AND I'M GOING TO CARRY SOME TEST IN ORDER TO SEE IF THE MODELS CAN RUN SUCCESSFULLY IN A MORE RESTRICTED GPU ENVIRONMENT, BECAUSE WHAT'S GOING TO HAPPEN IS IN ORDER TO MAKE IT SCALABLE, I'M GOING TO HAVE TO ENGAGE IN A SCALING GROUP OF RECRUITING SEVERAL ATANTS IN A GROUP, IN A BUNDLE OF HORIZONTAL SCALING.

01:59:41 - Bastian
IT'S CALLED HORIZONTAL SCALING BECAUSE YOU HAVE THE RECRUITING OF SEVERAL INSTANCES OF A COMPUTATIONAL UNIT ACROSS A SIMILAR, ACROSS THE SAME EC2 INSTANCE, VERSUS VERTICAL SCALING IN WHICH YOU ACTUALLY GO ON A HERARCHY OF CHECK, CHECK.

02:00:00 - Bastian
of EC2 instances, that is, of computational units that have more capacity as you go over, right?

02:00:07 - Bastian
So here, horizontal scaling, we're just recruiting the same 810 GPUs across several, you know, one or two or three of them, right?

02:00:18 - Bastian
And the reason that I'm recommending for horizontal scaling is because what we're trying to recruit here is GPU real state instead of CPU real state.

02:00:30 - Bastian
And if you go, you were to, oh, for the vertical scaling, you will be basically not maximizing the GPU real state, and you will be more or less getting more CPU capacity.

02:00:45 - Bastian
Man, Juan, that's amazing.

02:00:47 - Bastian
Oh, go ahead.

02:00:47 - Bastian
Sorry.

02:00:48 - Bastian
Juan, I was going to ask a question just to confirm.

02:00:51 - Bastian
So if I understand correctly, horizontal scaling is traditionally used in ML models.

02:00:58 - Bastian
When the model...

02:01:00 - Bastian
model doesn't fit in your, like, one instance, so you do horizontal scaling and you distribute it, right?

02:01:06 - Bastian
And I think in those cases, you might actually find a bottleneck where the CPU is not fast enough to load the model into the GPU.

02:01:16 - Bastian
And that's a bottleneck that's not trivial.

02:01:19 - Bastian
mean, it depends.

02:01:20 - Bastian
That's the only, like, when does a processor, a CPU matter for ML loads that run in GPU?

02:01:28 - Bastian
Well, it's just, like, to give it the instructions to load the model into the memory.

02:01:34 - Juan Torres
So if you are doing horizontal scaling and those instances are cold, you will pay that cost upfront for every instance you spawn.

02:01:43 - Juan Torres
And that's the difference with, like, the other kind of scaling, not horizontal.

02:01:50 - Juan Torres
I'm sorry.

02:01:50 - Juan Torres
What's it called?

02:01:51 - Juan Torres
But then the model fits and you just spawn more instances, right?

02:01:56 - Bastian
And then you don't pay that.

02:01:59 - Bastian
doesn't randomly use quite And that's why Iwhat system So...

02:01:59 - Bastian
for example,

02:02:00 - Bastian
Like, for the CPU, you pay it only once.

02:02:03 - Bastian
And the other thing that can influence this is, obviously, they have, like, this very optimized, like, racks, so to speak, but the actual cables that link the GPUs are also a factor that weighs into, and maybe more modern GPUs, I'm just supposing, they may have better link methods developed by NVIDIA and such.

02:02:26 - Bastian
Are you facing that bottleneck yourself?

02:02:31 - Bastian
Not, no, but it's part of the things I had to study when I was considering using a GPU for the chunking in ChipKit.

02:02:41 - Bastian
Oh, yeah.

02:02:42 - Bastian
Well, for the chunking, are you kind of, like, isolating the processing of the chunking and the rack into another instance, or are you doing it in the same instance in which you're going to have the inference pipeline?

02:02:57 - Bastian
I went through, like, every option.

02:02:59 - Bastian
every option.

02:03:00 - Bastian
I think the most optimal way would be to use a GPU and only have a container that basically just does the OCR and chunking, and maybe you can have, like, two variants.

02:03:12 - Bastian
It would be awesome, like, to, because processing things that require FFmpeg are actually much faster than processing OCR in a PDF, at least in the traditional ways.

02:03:23 - Bastian
So you could actually, like, route everything very smartly, so everything can run in a CPU if it's, like, video and audio and all of that, but if you're, and text and markdown, but if you have PDFs, you will need to, like, optimally, I think you would benefit more for, of using a GPU, and I think that's where you were going.

02:03:48 - Bastian
Using one bundle of GPUs, you mean?

02:03:54 - Bastian
In this case, it's not, like, as heavy as an LLM in terms of size.

02:04:00 - Bastian
So actually, any GPU should work, like GPUs, like over 16 gigabytes or maybe less, be around like eight might be enough, I don't know, but yeah, it's different than your use case, but principles still apply.

02:04:19 - Juan Torres
What's the size parameters of your models that you're trying to deploy?

02:04:24 - Juan Torres
Oh, no, it wasn't, it's just a theoretical case, that's what I mentioned.

02:04:28 - Juan Torres
And I haven't deployed LLMs in multiple instances, but I think those could be some bottlenecks, because in theory, if its size is the most, it's the most determined factor, like parameter size, and as long as that fits in your GPU memory, and it's just one model for one GPU, and you compare like 8 billion to 20 billion parameters, I see no reason why it would be faster for the, I mean,

02:05:00 - Juan Torres
I see no reason why it would be harder for a small model to produce more token speed output, unless the bottleneck is somewhere else.

02:05:14 - Juan Torres
That's a really good question, the question of if there's any additional cost of recruiting more instances, given the demands of the specific environment.

02:05:26 - Juan Torres
because the reason that I can't really rely on one 8.100 in AWS is because they don't offer one single 8.100 GPU.

02:05:39 - Bastian
They offer like an EC2 instance with like 8.10, and then 8.10 with more CPU capacity, more CPU capacity.

02:05:52 - Bastian
And then it jumps to a bundle of 8.10.

02:05:55 - Bastian
Got And then it jumps to a bundle of 8.100.

02:05:58 - Bastian
8.100.

02:06:00 - Bastian
So I actually carried the cost benefit for my clients, and that's the reason we opted for Oculus at the beginning, because they were actually offering an 8100 isolated, right?

02:06:12 - Bastian
So in the cost benefit schema, it made sense to go for that option.

02:06:17 - Bastian
The problem is that at one point there were some costs that were not perceived at the beginning, so then that's when we decided to then reorganize around an EC2 instance and then provide the option for horizontal scalability given the demands of the specific project.

02:06:40 - Bastian
Perfect.

02:06:41 - Bastian
But that's a really good interesting option.

02:06:43 - Bastian
Maybe if you took the CPU, you could see some quick wins and have sort of quickly estimated a more optimal point, because maybe if you go one step below, it's just the same.

02:06:57 - Jake Maymar
Or maybe if you go one step higher.

02:07:00 - Jake Maymar
You get like, I don't know, like 20% less latency to the first token.

02:07:06 - Bastian
I think that's what could be, I think speed, like in tokens per second, shouldn't change too much once it's loaded into the GPU or the cluster of GPUs, but the latency to the first token, I think that should be very influenced like by the CPU and traditional RAM for its capacity to load this into the GPU and how they are connected through the defense.

02:07:30 - Bastian
links.

02:07:30 - Bastian
that's where I would look if you have a problem, like from latency to first, from question to first token.

02:07:38 - Bastian
And then, yeah, the other thing I know, I really have an explanation if it's like, once it's loaded in a GPU, it's slower than a bigger model, then I don't know.

02:07:50 - Bastian
Yeah, those are really good questions.

02:07:54 - Bastian
So, Bastian, Patrick had a question about the, uh, uh, how you manage, uh, chunk.

02:08:02 - Bastian
Yeah, specifically about if you had to test with very complex PDF, especially including complex table with merge cell, because from experience, they're held to chunk properly.

02:08:15 - Bastian
Yeah, that's an important factor, and yeah, I designed different templates, PDFs, some had different domains, and some had more tables, some had more, like, graphics, even, like, simple, like, PNGs that are stuck into it.

02:08:36 - Bastian
And I had, like, this file or folder where I had, like, these different, like, types of test documents or mock documents for different types of, like, PDFs and for the multimedia things.

02:08:50 - Patrick Chouinard
And I tried to stick with, and this is what I would encourage you guys to, because you will have to tweak the parameters of whatever Brandon ends up coding for you.

02:09:00 - Patrick Chouinard
And the complexity of your documents that you are mentioning is a great factor that adds variability.

02:09:08 - Patrick Chouinard
So yeah, I would recommend that like having like some test documents and Carson can create this for you.

02:09:14 - Patrick Chouinard
Like you just described, I need like a very basic one, just one page of plain text, then five, 20 pages of pure text.

02:09:22 - Bastian
And then like a variation where you have like one table, maybe five tables.

02:09:25 - Bastian
And then you have like maybe, I don't know, like a more traditional image.

02:09:29 - Bastian
Like, for example, something even generated by a GPT for image or some of these models.

02:09:36 - Bastian
Like, yeah, like define what looks like your most typical use cases.

02:09:42 - Bastian
And of course, if you can like front load some of the processing, like pre-processing the PDFs can make sense in some cases.

02:09:52 - Bastian
Yeah, because a lot of the problem we've encountered because we're, we build our own RAG system.

02:09:58 - Bastian
And, uh, it's for a final...

02:10:00 - Bastian
And they have a lot of very complex table that have a merge column, merge rows, merge cell part of the table.

02:10:09 - Bastian
And chunking makes it almost unreadable.

02:10:12 - Bastian
It's extremely complex to chunk it in a way that the LLM will understand, oh, those two cells are actually reporting to those two rows or so.

02:10:22 - Bastian
I think it's borderline impossible for that type of document.

02:10:28 - Patrick Chouinard
I think those should be handled, like, separately.

02:10:32 - Bastian
Like, maybe, like, okay, I'm gonna, this, I have, like, this 30-page PDF, but there are, like, these four pages that are super heavy on graphics and stuff like that, and super technical.

02:10:42 - Bastian
And I think those would benefit more, like, from an LLM with very good vision capability, instead of trying to chunk it.

02:10:52 - Bastian
Like, with traditional OCR, which is what Duglin and all this stuff do, like, under the hood, they, they may have better, faster models, but it's.

02:11:01 - Bastian
So I think those that need a deeper understanding on the domain, knowledge domain, yeah, I think agents with vision is basically the way to go for those concrete pages, but then you will lose the benefit of the embedding, or you will have to handle that a bit separately.

02:11:23 - Bastian
So that's another trade-off.

02:11:26 - Bastian
Exactly, and it's not really doable in, not real-time, but while the user is waiting, basically.

02:11:32 - Bastian
Yeah, but something that you could do is, like, actually, if you have documents like this, which, yeah, they contain some hard graphics, but are mostly text, for example, a book of some domain-like business or stuff like that.

02:11:47 - Bastian
You could maybe, like, do the chunking, do the embeddings for everything text-related, and just have the model bring the images as additional context for it to analyze at inference time.

02:11:59 - Bastian
Indies.

02:11:59 - Bastian
you.

02:12:00 - Bastian
I think that could work.

02:12:02 - Bastian
Yeah, when it's image, it's not too hard because you can have a text description of what the image is and you can chunk that, but a table, it's really...

02:12:12 - Bastian
tables and graphics and stuff like that, but I'd like to have the model bring those two at inference time to analyze it and use them to improve the answer.

02:12:23 - Bastian
So, it receives, like, the rag input, the chunks it retrieves, but also, like, oh, yeah, this document has also these images.

02:12:31 - Bastian
Do you want me to add this to the analysis and have, like, some idea of where in the text they go?

02:12:38 - Jake Maymar
So, which is related to whatever topic, for example.

02:12:43 - Jake Maymar
Okay.

02:12:43 - Jake Maymar
That makes sense.

02:12:45 - Jake Maymar
Right now, we're using document intelligence, but honestly, it's not the most stable thing in the world.

02:12:50 - Jake Maymar
Yeah, think the thing that has Andreang's product, I forgot what it's called, but he's a...

02:13:00 - Jake Maymar
Like agentic rack system, it excels for like graphical complex tables and stuff like that.

02:13:07 - Jake Maymar
I've seen it used for like medical examples, even like some tissue analysis, like looking at the microscope with all of this complicated stuff and it has a very good understanding and can produce like a structure output.

02:13:22 - Bastian
So it's like, okay, the skin has three layers and in the first layer I see this and the second I see this, and I can produce a structure JSON or whatever for you, that can be a useful way to start it.

02:13:34 - Bastian
Okay, cool.

02:13:36 - Bastian
Thank you.

02:13:37 - Bastian
Yeah, sure.

02:13:39 - Bastian
Yeah, this is great, guys.

02:13:41 - Bastian
Great call.

02:13:43 - Bastian
If anyone has anything, I mean, we're a little bit past the hour.

02:13:47 - Bastian
But yeah, I'm looking forward to the next chat and looking forward to seeing what everyone builds.

02:13:54 - Bastian
It's going to be fun to see a more relaxed Brendan.

02:13:57 - Bastian
Yeah, yeah.

02:13:58 - Bastian
I mean, he deserves it, man.

02:14:00 - Jake Maymar
Guy works so hard, and it adds so much to the community, so yeah, I'm really looking forward to, like, I don't know, having him, like, having this thing kind of take on a life of its own, you know, and then building some pretty cool things, so.

