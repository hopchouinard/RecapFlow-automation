00:00:00 - Juan Torres
Man your data science stuff is pretty cool.

00:00:03 - Juan Torres
Thank you.

00:00:03 - Juan Torres
Yeah.

00:00:05 - Juan Torres
Actually, today I was planning to share an event I'm going to be presenting on the concentration of banking with the Agentics systems and the the engineering components.

00:00:17 - Juan Torres
So we're sharing it with you.

00:00:19 - Juan Torres
I'm planning to do a live stream because it's in San Diego.

00:00:23 - Juan Torres
So for folks that may want to be, you know, in the meetings.

00:00:28 - Juan Torres
I'll make the link available.

00:00:30 - Juan Torres
Yeah.

00:00:30 - Juan Torres
Yeah.

00:00:31 - Jake Maymar
cool.

00:00:32 - Jake Maymar
Very, very cool.

00:00:33 - Jake Maymar
So are you getting a lot of traction?

00:00:36 - Juan Torres
How's that going?

00:00:41 - Jake Maymar
Did it cut out?

00:00:42 - Juan Torres
Is my mic cutting out?

00:00:44 - Juan Torres
No, I just couldn't hear you.

00:00:46 - Jake Maymar
Well, what was that?

00:00:47 - Jake Maymar
Oh, did you get a lot of traction?

00:00:50 - Juan Torres
For the events?

00:00:52 - Jake Maymar
Yeah.

00:00:52 - Jake Maymar
Well, just in general, like last time I saw, I might have missed the meetings because it's been insane.

00:01:00 - Juan Torres
There was you had like a data science video.

00:01:05 - Juan Torres
Yeah.

00:01:06 - Jake Maymar
And like, I think a GitHub repo and stuff.

00:01:09 - Jake Maymar
How's that going?

00:01:11 - Juan Torres
Well, the video, it's kind of like a byproduct of the whole project and I haven't published it yet, just because I've been really busy with other projects.

00:01:21 - Juan Torres
And I was planning to continue working on the project and then Brandon made really good recommendations and annotations to the video.

00:01:31 - Juan Torres
So I'm planning to maybe, you know, redo it against and then try to integrate a lot of his constructive criticisms.

00:01:42 - Juan Torres
Yeah.

00:01:42 - Jake Maymar
He really, it's funny.

00:01:44 - Jake Maymar
He really does know, he does know really, really good points.

00:01:49 - Juan Torres
Yeah.

00:01:50 - Jake Maymar
So yeah, it's, he's also a very kind person.

00:01:55 - Jake Maymar
And, you know, he, he wouldn't tell you anything.

00:01:59 - Jake Maymar
He wouldn't tell himself.

00:02:00 - Jake Maymar
you know, and so it may sound like critical feedback, but man, you want to hear that now.

00:02:04 - Jake Maymar
You don't want to hear that like years later.

00:02:07 - Jake Maymar
You know, when you're trying to get funding, you're trying to like, you know, I don't know, whatever you're trying to do, you don't want to find out after the fact when you spend all this time perfecting and refining something.

00:02:21 - Jake Maymar
It's so nice to have it like at the very beginning.

00:02:24 - Juan Torres
Yeah, it's awesome.

00:02:25 - Juan Torres
Yeah, and I was really thinking of doing his program, but the thing is like, I have so many projects right now and it's gonna be, yeah.

00:02:36 - Jake Maymar
It's crazy.

00:02:37 - Jake Maymar
It's like, I have so much stuff.

00:02:39 - Jake Maymar
can't even.

00:02:41 - Jake Maymar
Yeah, I mean, and it just just, all it is, it's just accelerating.

00:02:46 - Jake Maymar
Everything is just accelerating.

00:02:48 - Jake Maymar
So it's like, yeah, I love the idea and I would totally be part of it, but yeah, I just, I'm a little jealous of people that are in it, but you know what I mean?

00:02:59 - Jake Maymar
It's gonna be great.

00:03:00 - Jake Maymar
And I'm happy for them to and you know they're going to just skyrocket yeah How are you what are you doing?

00:03:08 - Jake Maymar
What's what are you working on?

00:03:10 - Jake Maymar
Oh?

00:03:11 - Jake Maymar
Well, you know this assessment tool And then oh here I'll put the link in the chat.

00:03:19 - Jake Maymar
It's it's the same one though, so it's not See This is just again the one that I saw last week Pretty great.

00:03:30 - Juan Torres
Actually look pretty neat.

00:03:32 - Jake Maymar
Well, it's probably very different now I'll walk you through it kind of fun.

00:03:39 - Jake Maymar
I always like y'all just share my screen Cannot share my screen.

00:03:43 - Juan Torres
That's fine.

00:03:43 - Juan Torres
Sure.

00:03:44 - Jake Maymar
yeah, you can you can look through it.

00:03:46 - Jake Maymar
Basically It's an assessment tool where you you test yourself on some sort of increment either daily or weekly and then try and improve your You

00:04:00 - Jake Maymar
your relational, your relational communication skills.

00:04:05 - Juan Torres
So are you seeing NLP in order to assess the communication style of people and then?

00:04:15 - Jake Maymar
You know, it's kind of funny with assessments is, you know, it's just essentially a score, right?

00:04:22 - Jake Maymar
It's just essentially a a series of questions that you ask the participants.

00:04:30 - Jake Maymar
And then depending on how they answer it, then you use all of that data to create sort of historical and projections forecasting.

00:04:43 - Jake Maymar
And then also I have a rag database that's sort of taking all of the suggestions and then creating activities that will help them increase their score as well.

00:04:56 - Juan Torres
And then tracking that as well.

00:04:59 - Juan Torres
What is the.

00:05:00 - Juan Torres
difference between the RAG database and a vector database?

00:05:03 - Jake Maymar
Well, you know, RAG often is, that's a fair question.

00:05:10 - Jake Maymar
Often, when you take something and you just create a vector database out of it, you're not, you're going to get hallucinations, because you could do cosine similarity, you could do a whole bunch of different things, but you're going to basically get hallucinations.

00:05:29 - Jake Maymar
If you do RAG, vanilla RAG, you'll probably also get hallucinations as well.

00:05:34 - Jake Maymar
But if you do RAG, where then you have a re-ranker, and then you have a judge, and you have all these other things that are kind of looking at saying, don't hallucinate, don't, you know, a fairly extensive prompt saying, essentially don't hallucinate, and you're pulling directly from not only a vector database, but an actual database, to verify the content.

00:06:00 - Jake Maymar
Chances are you're going to get something that's fairly accurate.

00:06:04 - Juan Torres
So it seems that it's the database that has rail guards and parameters, kind of like if you have an agent system ready to process the data.

00:06:13 - Jake Maymar
I mean, the problem is with RAG is it's a term like it's a retrieval augmented generation.

00:06:21 - Jake Maymar
And the problem with that is it's just a term, but now the term, if you add all this stuff in has become way to sort of mitigate hallucinations, which is the biggest reason you use it.

00:06:35 - Jake Maymar
In theory, you'd be able to ask a LLM a question and then it would respond to give you the answer.

00:06:43 - Jake Maymar
You can query a database and get a response.

00:06:48 - Jake Maymar
Like if it's in that database, it's going to come back.

00:06:51 - Jake Maymar
The problem is if you query an LLM, you'll get a response, but you don't know if it's in that database and it needs you to do that cosine similarities.

00:07:00 - Jake Maymar
See, okay.

00:07:00 - Jake Maymar
Well, this response is really similar to this one, but I'm going to respond and it doesn't match either one.

00:07:07 - Jake Maymar
But in general, it matches.

00:07:11 - Jake Maymar
And the hallucinations come when that in general, it matches.

00:07:16 - Jake Maymar
Oh, means that basically, instead of saying, the sky is blue, it says the green.

00:07:27 - Jake Maymar
Now, it says the sky is blue in your in your vector database.

00:07:32 - Jake Maymar
And that's not a really great example, but for simplicity.

00:07:36 - Jake Maymar
But it says it's green.

00:07:39 - Jake Maymar
And technically, that's kind of close, because it's close to blue.

00:07:42 - Jake Maymar
But the reality is it's supposed to be blue, it's deterministic, it needs to be blue, but you get probabilistic and it's green.

00:07:51 - Jake Maymar
And it doesn't really totally matter sometimes.

00:07:55 - Jake Maymar
But other times in health care, it matters a lot.

00:07:57 - Jake Maymar
that's the part of the reason I have these rags where it's,

00:08:00 - Jake Maymar
Basically, it's drug interactions and you ask it questions and then it looks at the database and it looks at the vector database and it looks at other headers and all the things and then it comes back with the result.

00:08:15 - Jake Maymar
But I try and verify the result as best as possible, but it's still really hard.

00:08:21 - Juan Torres
Yeah.

00:08:22 - Juan Torres
How do you verify the answers for your system?

00:08:28 - Jake Maymar
Well, classic sort of like evaluations is the best.

00:08:35 - Jake Maymar
So you do a whole bunch of synthetic data and then you generate a whole bunch of in theory responses and then you run those responses along with hallucinations.

00:08:48 - Jake Maymar
you basically give it hallucinations questions that should generate hallucinations and then you tune to make sure that it doesn't keep giving you hallucinations or at least mitigates the human.

00:09:00 - Jake Maymar
hallucinations.

00:09:01 - Jake Maymar
It's a very hard to get rid of hallucinations.

00:09:03 - Jake Maymar
The reason it's so hard to get rid of hallucinations is you have prompt drift, you have model drift, and then you have system drift, right?

00:09:11 - Jake Maymar
So, right, and a lot of people don't think about that, but like, say using, I like to use foro mini, and that's a very, very hard model to use.

00:09:22 - Jake Maymar
But I'm using foro mini because it costs nothing.

00:09:26 - Jake Maymar
Oh, foro mini, yeah, okay.

00:09:27 - Jake Maymar
Right, so it's super fast.

00:09:29 - Jake Maymar
And so, I wonder if my mic is weird.

00:09:33 - Juan Torres
Is there like a lot of echo?

00:09:35 - Juan Torres
No, okay.

00:09:38 - Juan Torres
So, it's just not a system that it's not properly said, I just change from rules.

00:09:42 - Jake Maymar
probably.

00:09:43 - Jake Maymar
Yeah, no worries at all.

00:09:45 - Jake Maymar
So, yeah, so I like to use foro mini.

00:09:48 - Jake Maymar
The reason why I like to use foro mini is it's cheap and it's fairly fast.

00:09:52 - Jake Maymar
But they keep updating foro mini.

00:09:56 - Jake Maymar
So, when I started getting in, it was kind of drunk.

00:10:00 - Jake Maymar
It wasn't very good.

00:10:01 - Jake Maymar
It was kind of weird.

00:10:03 - Jake Maymar
Now it's really refined.

00:10:05 - Jake Maymar
It's very, very fast.

00:10:07 - Jake Maymar
It gets way better results than it used to.

00:10:10 - Jake Maymar
But the problem isn't all my problems and all my system worked with that drunken model.

00:10:14 - Jake Maymar
And I can't freeze that model.

00:10:18 - Jake Maymar
And then so you have that as one system.

00:10:22 - Jake Maymar
But then you have other systems on top of that.

00:10:24 - Jake Maymar
So you have the model system.

00:10:27 - Jake Maymar
If you're pulling like we're pulling pharmaceutical data, what changes from time to time?

00:10:36 - Jake Maymar
And so everything becomes dynamic.

00:10:40 - Jake Maymar
So now I'm pulling in new data.

00:10:42 - Jake Maymar
I have a new model.

00:10:46 - Jake Maymar
And then some other API calls that I'm doing, those also drift.

00:10:51 - Jake Maymar
So it's very, very hard to make sure that you have a rock salt solution when working with LLMs.

00:10:57 - Jake Maymar
So yeah, the best way to do is just email.

00:11:00 - Jake Maymar
So you have constant evals that run in the background.

00:11:02 - Jake Maymar
problem is if you're running, let's say I was running clock right running 3.7 Well, that's very expensive right So now I have to do evals and embeddings on a very expensive model.

00:11:18 - Jake Maymar
Oh, and that's the other thing unfortunately and I don't know I've been kind of talking with Sebastian and Brandon and Paul and I Forgot his name on my my maximum and maximum's really good with evals and So You have you do an eval.

00:11:47 - Jake Maymar
Oh, she works a girl with this Promptor model drift.

00:11:51 - Jake Maymar
Oh Yeah, so you basically run evals and you create All your synthetic

00:12:00 - Jake Maymar
And then you're testing that star, I was just trying to remember where I was going with this.

00:12:06 - Juan Torres
Yeah, but you're constantly testing it.

00:12:10 - Jake Maymar
That's sort of the thing is, oh right, the cost.

00:12:13 - Jake Maymar
So I was talking about cloud.

00:12:15 - Jake Maymar
So, when going back to using open AI models, the encoding, you basically, when you vectorize and tokenize everything, currently, and again, I'm always learning, but currently you have to re-vectorize everything.

00:12:37 - Jake Maymar
If you add a substantial amount to the vector database, you have to re-encode it.

00:12:45 - Jake Maymar
Now, that doesn't seem to make sense.

00:12:48 - Jake Maymar
You would think you could just append parts of it.

00:12:51 - Jake Maymar
But what happens is that appended part doesn't relate.

00:12:55 - Juan Torres
Exactly.

00:13:00 - Jake Maymar
scene process because it is indexing everything that has to figuring out the similarities.

00:13:05 - Jake Maymar
How similar is this to this?

00:13:07 - Jake Maymar
Now, if you add a you append it, well, guess what?

00:13:12 - Jake Maymar
Those things are similar to each other, but they don't have any relation.

00:13:15 - Jake Maymar
Now, that's one of these graphs, these node graphs, and all these other sort of graphical interface.

00:13:23 - Jake Maymar
I'm forgetting the name of it, but basically like Node.js is Neo4j?

00:13:33 - Jake Maymar
That's it.

00:13:35 - Jake Maymar
It's been long day.

00:13:37 - Jake Maymar
So, but basically, have to re-encoder everything.

00:13:41 - Jake Maymar
So, if you have an expensive encoder, well, now you have to pay for that, and it gets expensive.

00:13:47 - Jake Maymar
Imagine having, you know, several gigs of data you have to re-encode.

00:13:51 - Jake Maymar
And if it's dynamic, well, that becomes very brittle.

00:13:58 - Jake Maymar
So, so you can see how ragged,

00:14:00 - Jake Maymar
it's kind of imperfect right now.

00:14:03 - Jake Maymar
But for now, if you can get to a point where it's a stable data set, and that data set isn't changing that much, then then it works pretty well.

00:14:15 - Juan Torres
You will.

00:14:16 - Juan Torres
scraping your information or do you have any?

00:14:19 - Jake Maymar
Yeah, that's actually how I get it.

00:14:20 - Jake Maymar
So I'll scrape a couple different pharmaceutical companies, um, companies as well as there's, um, aggregators and just kind of, just get a big jumble and then sort through that jumble, either manually or using different automations, um, to kind of basically sort of sort through the noise, um, then from there, uh, build a pretty solid database.

00:14:52 - Jake Maymar
And then from that database, I create a rack system and factorize it.

00:14:58 - Juan Torres
I see.

00:14:59 - Jake Maymar
Because it's.

00:15:00 - Jake Maymar
Garbage in garbage out.

00:15:01 - Jake Maymar
So if you Scrape something and you have advertising or you have Extra stuff or you have just maybe their format is really weird And you're not looking at the data and it just has all this weird noise in it Well, guess what that gets encoded into your rag and that causes confusion So you really want to have really clean data in and then of course you get clean data out, right?

00:15:27 - Jake Maymar
know you understand this so Are you in AI in order to automate the web scraping process?

00:15:33 - Jake Maymar
Yes, yeah, crawl for I was using that You know Brandon had a really nice tutorial.

00:15:42 - Jake Maymar
There's a couple other ones out there There's a couple different Methods, but they're they're all kind of the same Once you look at the and you get it to mark down once it's in mark down you look for a selectors and then from the selectors you

00:16:01 - Juan Torres
Yeah, that's what I did for the Federal Reserve really because I just use old-school ETL scripting, and I just use this Yeah, I was thinking, oh, maybe there's like a module or a system that, yeah, I mean, you gave it the HTML code and then it helps you identify the table or the specific parameters within that code.

00:16:35 - Jake Maymar
Exactly.

00:16:36 - Jake Maymar
don't know if there's any other way, I mean, like the old-school methods work, right?

00:16:42 - Jake Maymar
mean, if you want to scrape LinkedIn, you just sit there and you just figure out their selectors.

00:16:47 - Jake Maymar
only process they keep updating their selectors, so every time you basically access the site, they update everything.

00:16:57 - Jake Maymar
Makes a very neat process.

00:17:00 - Juan Torres
Unfortunately, I'm working with a bureaucracy, a government bureaucracy, that it's not very innovative.

00:17:05 - Juan Torres
So they don't innovate their webpage and their data much.

00:17:10 - Juan Torres
So I have an own dynamical web scraping process.

00:17:15 - Jake Maymar
Yeah, that's fantastic.

00:17:17 - Jake Maymar
Yeah, because I can't tell you how I'm going to my scraper is no longer work.

00:17:22 - Jake Maymar
So, yeah, that's what this is what happens, I feel.

00:17:25 - Jake Maymar
But it's So what do you what do you so to see once you have your site and your video and everything, what's kind of the next steps?

00:17:34 - Juan Torres
Well, I do want to do a contracted work doing the engineering, data science and then AI development work.

00:17:46 - Juan Torres
So that's my main goal really.

00:17:49 - Jake Maymar
And is this your like main project or do you have other projects that you've already like, do you have like client projects?

00:18:00 - Jake Maymar
as well, or is this kind of your main initiative and your capstone?

00:18:05 - Juan Torres
You think the concentration of banking is this my a client-based project or just for portfolio projects?

00:18:11 - Juan Torres
Is that what you're asking?

00:18:12 - Jake Maymar
Well, I was seeing, yeah, that's pretty much what I'm asking.

00:18:17 - Juan Torres
So the concentration of banking project is really a research project out of project is more political economy, econometrics, research projects.

00:18:38 - Juan Torres
But even despite the fact that it has no monetary implications, it has been receiving a really good reception by the data science community here in San Diego and in other parts.

00:18:53 - Juan Torres
Nice.

00:18:54 - Juan Torres
Do you know Dash, Wally, the web development framework?

00:19:00 - Juan Torres
uh rings of bell dash so it's like a dash examples let me show you let send it to the web so they're in this guys plow yeah of course plow yes yes yeah yeah so they they uh they liked it so much they actually put it right there uh in their uh awesome man nice congratulations yeah thank you um let's see which one what is it is it the it's the second one that position center is yeah nice well congratulations that's not a small thing like plot see no no massive that's fantastic yeah oh yeah I remember you you shared this link before I was like oh this is cool problem is there's so many good links shared I just yeah this is amazing very nice so the only the only client I had was

00:20:00 - Juan Torres
some next employer, which was really like the benefits group of the union doing some financial analysis for them.

00:20:10 - Juan Torres
And it was a gig for like six months that I was working on.

00:20:16 - Juan Torres
But yeah, we wanted to get more clients try to do more work.

00:20:22 - Juan Torres
And yeah, because this is, I really like this.

00:20:26 - Juan Torres
think it's like very feasible.

00:20:30 - Jake Maymar
Oh, yeah, this is, this is really cool.

00:20:33 - Jake Maymar
Yeah, this is a cool thing.

00:20:35 - Jake Maymar
So what kind of clients are you looking for?

00:20:38 - Juan Torres
I, what was that?

00:20:41 - Jake Maymar
Sorry, what kind of client are you looking for?

00:20:44 - Juan Torres
I am looking for clients, particularly, I mean, I'm not, I wouldn't want to say I'm agnostic to any industry, but right now I'm

00:21:00 - Juan Torres
doing a lot of concentration of the finance, it's, I mean, generally, like, work that requires lead engineering and data science, someone that it's open to it really.

00:21:15 - Jake Maymar
Yeah, that makes sense.

00:21:17 - Jake Maymar
Yeah, and data science is in a weird place right now, encoding and development is in a weird place too, you know, and so, yeah, it's, think it's really valuable, but a lot of people think AI is solving all these solutions, and I think if you can show that, you know, you still need data science and you still need to evaluate things, I think you're going to be in great shape.

00:21:47 - Jake Maymar
So, and I think we're already doing that.

00:21:49 - Jake Maymar
Plus you're on plotly, that's pretty amazing.

00:21:52 - Juan Torres
Yeah.

00:21:53 - Juan Torres
And I feel like data specifically, data engineering,

00:22:00 - Juan Torres
is going to still be a really important component of AI development.

00:22:07 - Juan Torres
Because if you don't have really good data in order to, if your agent exists or your models, then essentially you're not going to be able to develop really high abstract analysis by AI at all.

00:22:23 - Juan Torres
So I feel like a lot of people are overseeing the necessity of engineering, because AI is like the shannier thing right now.

00:22:34 - Juan Torres
But a lot of the projects that I'm working on just, wait, I don't know if you, know, Adam Scunover, the guy who manages the Charming Data YouTube channel.

00:22:47 - Jake Maymar
So yeah, Adam, I think so.

00:22:51 - Juan Torres
It's this guy.

00:22:53 - Jake Maymar
It's so funny.

00:22:54 - Jake Maymar
It's like the name sounds familiar, but as soon as I see the video, like, oh, yeah, okay.

00:23:00 - Jake Maymar
Sometimes sometimes it's a brand new person.

00:23:02 - Jake Maymar
It's amazing.

00:23:04 - Juan Torres
Yeah, so we get together like a group of people.

00:23:10 - Juan Torres
So it's this guy and we develop the database applications.

00:23:17 - Juan Torres
And so a lot of this work, despite the fact that we integrate like agent systems or AI tools of analysis.

00:23:31 - Juan Torres
Like it's not it doesn't work if you don't have the engineering component that just feeds all that stuff into your data web application.

00:23:40 - Juan Torres
So that's why you still see the engineering is really quintessential to everything else, you know?

00:23:46 - Jake Maymar
Yeah, I totally agree.

00:23:48 - Jake Maymar
I totally agree.

00:23:49 - Jake Maymar
Um, I am.

00:23:53 - Jake Maymar
Let's see.

00:23:55 - Jake Maymar
I like this guy a lot.

00:23:59 - Jake Maymar
Let's just.

00:24:19 - Jake Maymar
I like this guy Santiago, pretty cool data science guy.

00:24:29 - Jake Maymar
And really nice guy too.

00:24:33 - Jake Maymar
I like him explaining this MCP.

00:24:38 - Juan Torres
Have you seen Santiago stuff?

00:24:41 - Jake Maymar
It's on Twitter.

00:24:42 - Jake Maymar
me see if it can get you one that's not on Twitter.

00:24:44 - Jake Maymar
Here you go.

00:24:46 - Jake Maymar
This is a YouTube link.

00:24:48 - Jake Maymar
Some people don't like Twitter.

00:24:50 - Juan Torres
I just have some social media sites blocked so I don't get distracted.

00:24:56 - Jake Maymar
Totally understand.

00:24:57 - Jake Maymar
Oh, oh, well yeah.

00:24:59 - Juan Torres
I sent you the YouTube as well.

00:25:00 - Juan Torres
Yeah, yeah, I got it here.

00:25:01 - Juan Torres
It's under fitted.

00:25:03 - Jake Maymar
Yeah.

00:25:05 - Jake Maymar
Okay, let's see.

00:25:06 - Jake Maymar
It's his name under fitted.

00:25:07 - Jake Maymar
It's Santiago.

00:25:09 - Jake Maymar
Um, what is, what is this?

00:25:12 - Jake Maymar
Um, let me see.

00:25:16 - Jake Maymar
I haven't actually gone through his YouTube.

00:25:18 - Juan Torres
Let me see what he says.

00:25:20 - Jake Maymar
yeah, under fitted.

00:25:22 - Jake Maymar
Oh, I guess he changed his name.

00:25:23 - Jake Maymar
I don't know.

00:25:24 - Jake Maymar
But yeah, it used to be Santiago.

00:25:26 - Jake Maymar
He's great though.

00:25:28 - Jake Maymar
Very, very accessible.

00:25:30 - Jake Maymar
I mean, foundational stuff, but also some really brilliant kind of, uh, I mean, what I like is practical applications, right?

00:25:40 - Jake Maymar
science.

00:25:43 - Jake Maymar
So he shows here how you can basically spin up a model using MCP and do just about anything you want to do with it.

00:25:54 - Jake Maymar
Just pretty cool.

00:25:54 - Juan Torres
Okay.

00:25:56 - Jake Maymar
So, yeah, training.

00:25:58 - Jake Maymar
Yeah, I mean,

00:26:00 - Jake Maymar
You'll totally get it when you see it.

00:26:01 - Jake Maymar
like, oh, that's cool.

00:26:02 - Jake Maymar
Well, hey, man, it's great talking with you.

00:26:05 - Jake Maymar
Look forward to sort of where you're going.

00:26:07 - Jake Maymar
I mean, it looks like you're going already pretty cool places.

00:26:12 - Jake Maymar
And I guess I will talk to you on Thursday.

00:26:15 - Juan Torres
Didn't for sure, Jake.

00:26:16 - Jake Maymar
I said it to you.

00:26:18 - Jake Maymar
Oh, definitely.

00:26:19 - Jake Maymar
Take care.

00:26:19 - Jake Maymar
Talk to you.

00:26:20 - Jake Maymar
Bye.

00:26:20 - Juan Torres
Bye.

