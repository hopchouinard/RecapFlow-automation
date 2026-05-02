00:01:18 - Andrew Nanton
How's it going?

00:01:20 - alexrojas
What's Andrew?

00:01:21 - alexrojas
All good, all good?

00:01:24 - Andrew Nanton
Good.

00:01:25 - Andrew Nanton
How's your class going that you're teaching?

00:01:27 - alexrojas
Good.

00:01:29 - alexrojas
I'm actually starting next week, given that it's government.

00:01:37 - alexrojas
They need a little more extra time.

00:01:40 - Andrew Nanton
Sure, sure.

00:01:41 - Andrew Nanton
No, I work part-time in a government job.

00:01:44 - alexrojas
I know how that goes.

00:01:45 - alexrojas
Oh, yeah.

00:01:47 - alexrojas
There is a lot of changes, no?

00:01:50 - Andrew Nanton
Well, and everything moves slowly at the best of times.

00:01:57 - alexrojas
That is the fast phase, huh?

00:02:00 - Andrew Nanton
Yeah.

00:02:01 - alexrojas
Yeah.

00:02:02 - alexrojas
Hey, Andrew, actually, I was looking into the chunky library that you shared.

00:02:08 - Andrew Nanton
Yeah.

00:02:09 - alexrojas
Do you use it a lot?

00:02:12 - Andrew Nanton
I've used it some.

00:02:13 - Andrew Nanton
You know, I've found that since I have been poking into things more, I've been going more into actually sticking together larger pieces of context rather than splitting them up into smaller bits.

00:02:28 - Andrew Nanton
But I'm not doing RAG per se, right?

00:02:32 - Andrew Nanton
Like, I mean, initially, RAG was kind of relevant to my workflow because context windows were so small, but now they're so big that, like, at least for the stuff I'm doing.

00:02:43 - alexrojas
Okay.

00:02:45 - Andrew Nanton
Just also because retrieval of chunks is – like, if it were perfect, then everyone would use RAG all the time because why wouldn't you?

00:02:56 - Andrew Nanton
But it's that retrieval step, and now that context windows are bigger, at least

00:03:00 - Andrew Nanton
For the stuff that I'm doing, there's a – but it's like – it's very manual kind of work where it's, you know, look at different intermediate products and then combine them.

00:03:11 - Andrew Nanton
And so it just – for my workflow, I've been using it less.

00:03:15 - Andrew Nanton
But I have used it some and found – did you run into an issue with Chunky?

00:03:21 - alexrojas
Yeah, because I actually – I'm doing a rag application for illegal consumption of, like, laws.

00:03:28 - alexrojas
Okay.

00:03:30 - alexrojas
It's for a lawyer friend.

00:03:32 - alexrojas
So I saw in Chunky that they have a very good semantic chunking.

00:03:39 - alexrojas
And now I'm using just the fixed chunks.

00:03:44 - alexrojas
But I haven't gotten to that point where I need to do eval, let's say.

00:03:51 - alexrojas
You know, I wanted to make it – put it up and running first and then see how – use Chunky and then evaluate it versus the – just, like, 500.

00:04:03 - Andrew Nanton
So what I would say is that given how large context windows are now, including in like, you know, GPT-4.1 mini, which is great for a lot of stuff, that it might make more sense to look at the chunks that you're getting and split them semantically in some way.

00:04:29 - Andrew Nanton
You know, whether you're bringing in PDFs or HTML, but just make sure that the boundaries of the chunks seem reasonable and make sense because you have so much context window to play with.

00:04:42 - Andrew Nanton
And the consequences of shearing a chunk where you're missing context are so high that, you know, I'm definitely a big fan of, like, you should be looking at your data at every step of the workflow.

00:05:00 - Andrew Nanton
Like, is the stuff that's going in reasonable?

00:05:03 - Andrew Nanton
And if so, then you probably are going to get reasonable results.

00:05:06 - Andrew Nanton
But, like, I think fixed chunking, especially with no overlap, is – because it's so much easier.

00:05:16 - Andrew Nanton
Yeah, yeah.

00:05:16 - Andrew Nanton
Like, you probably will get substantially better performance with very little effort by just adjusting how you're chunking.

00:05:24 - alexrojas
Okay.

00:05:25 - alexrojas
Yeah.

00:05:26 - alexrojas
I'll try it out and see how it compares.

00:05:31 - Andrew Nanton
Yeah, mean, see what you get, right?

00:05:32 - Andrew Nanton
Like, maybe what I'm saying actually makes no difference.

00:05:35 - Andrew Nanton
But at least for the stuff that I'm doing, I've noticed that it tends to make a pretty big difference.

00:05:41 - alexrojas
Okay.

00:05:45 - alexrojas
I'm actually leveraging this super-based thing that you could do double-tagging.

00:05:49 - alexrojas
So I prepare SQL and embeddings.

00:05:53 - alexrojas
So, you know, they're tied together and the queries, you know, both of them.

00:06:00 - alexrojas
Mm-hmm.

00:06:00 - alexrojas
Just… Just…

00:06:00 - alexrojas
Make sure.

00:06:03 - alexrojas
Yeah, add a third, do graph rag, why not?

00:06:08 - alexrojas
Yeah, you know, I'm getting ambitious here.

00:06:14 - alexrojas
With two, I feel I'm being ambitious.

00:06:20 - Brandon Hancock
What's up, everybody?

00:06:22 - Brandon Hancock
Hope you all have an awesome Tuesday so far.

00:06:26 - Brandon Hancock
Let's do a call order.

00:06:29 - Brandon Hancock
Cool updates for you guys before we kick off the – oops, sorry, I sent that to the wrong group.

00:06:35 - Brandon Hancock
Before we kick the day off, so update one.

00:06:40 - Brandon Hancock
So I actually got sick on, like, Thursday last week, so I didn't get to do the call with Joe for Crew AI.

00:06:48 - Brandon Hancock
So that's this Friday now.

00:06:49 - Brandon Hancock
So that'll be one cool chat with you guys.

00:06:52 - Brandon Hancock
And then another one is not next Tuesday, but the following one after that will probably do –

00:07:00 - Brandon Hancock
I'm going actually pull this up so you guys can see him in case you don't know who he is.

00:07:04 - Brandon Hancock
We'll probably do a guest speaker for one of our weekly coaching calls.

00:07:11 - Brandon Hancock
I don't know if y'all have heard of Dan Martell, but he basically will probably come on and – super excited for this, actually, because he basically is doing a lot of AI project incubation.

00:07:26 - Brandon Hancock
So we're going to talk about a bunch of topics for you guys around building AI businesses and so forth.

00:07:30 - Brandon Hancock
But one of the cool things is they run like a – not like a venture – not a venture capital, but an incubator, basically, is the way I would describe it.

00:07:39 - Brandon Hancock
So they take in thousands of requests from all sorts of AI businesses.

00:07:44 - Brandon Hancock
And one of the cool things is they're just going to kind of share, like, hey, this is exactly what we have seen, high level.

00:07:51 - Brandon Hancock
Here's what makes a good AI company, bad AI company.

00:07:53 - Brandon Hancock
Here's, like, what we're looking at funding.

00:07:54 - Brandon Hancock
Here's cool projects that we recommend.

00:07:56 - Brandon Hancock
So very excited for that.

00:07:58 - Brandon Hancock
So most likely not this Tuesday.

00:08:00 - Brandon Hancock
That's right, the following Tuesday, but the one after that.

00:08:02 - Brandon Hancock
So I think it's like July 1st-ish.

00:08:04 - Brandon Hancock
So very excited for that one.

00:08:07 - Brandon Hancock
And outside of that, one final update.

00:08:10 - Brandon Hancock
Actually two, I lied.

00:08:12 - Brandon Hancock
I've been busy, man.

00:08:14 - Brandon Hancock
I've been cooped up.

00:08:15 - Brandon Hancock
I've just been sitting on the couch having to brainstorm.

00:08:17 - Brandon Hancock
So Dan, will he be wearing a shirt?

00:08:21 - Brandon Hancock
It's up to you guys.

00:08:22 - Brandon Hancock
It's going to be a poll.

00:08:23 - Brandon Hancock
If the community wants it or the community doesn't want it, it's up to you guys.

00:08:27 - Brandon Hancock
So, yeah, he's making me look bad.

00:08:29 - Brandon Hancock
I'm not even 30 yet, and he's jacked.

00:08:32 - Marc Juretus
Yeah, man.

00:08:33 - Marc Juretus
I like that dude.

00:08:34 - Marc Juretus
I've actually followed a bunch of his videos already because he likes to work out like I do.

00:08:38 - Brandon Hancock
So he's a cool dude, man.

00:08:39 - Brandon Hancock
That's odd that you have him coming on, man.

00:08:42 - Brandon Hancock
I like that.

00:08:42 - Brandon Hancock
Yeah, I'm pumped.

00:08:43 - Brandon Hancock
I'm pumped.

00:08:44 - Brandon Hancock
So, yeah, just got to meet him last week.

00:08:46 - AbdulShakur Abdullah
Are you also jacked?

00:08:48 - Marc Juretus
Huh?

00:08:49 - AbdulShakur Abdullah
I said, are you also jacked like that then?

00:08:52 - Marc Juretus
I don't think so.

00:08:53 - AbdulShakur Abdullah
Maybe a little bit.

00:08:55 - Brandon Hancock
Yeah,'all put me to shame.

00:08:56 - Brandon Hancock
Y'all put me to shame, Mark.

00:08:58 - Marc Juretus
I would.

00:08:59 - Brandon Hancock
would stop it.

00:09:00 - Brandon Hancock
That's a cool one.

00:09:00 - Marc Juretus
There's not a lot of dudes who have both the world techie and working out, so that's impressive to me.

00:09:07 - Brandon Hancock
So, I agree.

00:09:08 - Brandon Hancock
I agree.

00:09:08 - Brandon Hancock
He's an impressive guy.

00:09:10 - Brandon Hancock
So, then, let me – cool other thing.

00:09:12 - Brandon Hancock
Marc, you and I got to actually talk about this a little bit a little bit ago, but I want to show everyone else, too.

00:09:17 - Brandon Hancock
So, cool new project I'm working on next.

00:09:20 - Brandon Hancock
So, long story short is, you know, last year, I did the, like, full stack marketing platform course to teach you guys how to, like, build a full stack.

00:09:30 - Brandon Hancock
AI application, you know, full learning experience.

00:09:32 - Brandon Hancock
I learned so much about making courses.

00:09:35 - Brandon Hancock
So, what I'm doing now, a new project called Shipkit, and basically what I'm doing is templateizing the entire process of making AI applications.

00:09:45 - Brandon Hancock
chat applications, rag applications, and agentec applications.

00:09:49 - Brandon Hancock
So, there's just gonna be an insane amount of templates and prompts to, like, literally guide you from I have an idea to a production application you shipped.

00:09:58 - Brandon Hancock
So, it's all gonna be copy and paste, code.

00:10:00 - Brandon Hancock
Basically to like, cause like I don't really code that much anymore.

00:10:03 - Brandon Hancock
just use AI prompt to help me do it.

00:10:05 - Brandon Hancock
So in the middle of building this out.

00:10:07 - Brandon Hancock
So we'll definitely keep you guys posted as I make more progress.

00:10:11 - Brandon Hancock
But like I said, the whole goal is just every part of the way.

00:10:15 - Brandon Hancock
I'll just show you guys, but like, you know, I'm kind of building it all out as we speak right now, but everything is like prompt driven.

00:10:21 - Brandon Hancock
So that's one of the main takeaways from my last course is like, you kind of had to just watch me build the whole thing.

00:10:27 - Brandon Hancock
And then after you got done, you're like, cool.

00:10:29 - Brandon Hancock
Now I need to go build an application.

00:10:32 - Brandon Hancock
And this one is flipping it on its head to just like, you know, the whole goal of Shipkit is to help you launch an AI application, you know, in a week, basically.

00:10:40 - Brandon Hancock
So that's the, that's what working on.

00:10:43 - Brandon Hancock
So we'll keep you guys posted on that.

00:10:45 - Brandon Hancock
Literally coding, coding as fast as I can right now, all the different like templates and everything for the different applications.

00:10:52 - Brandon Hancock
So like things like this.

00:10:54 - Brandon Hancock
So, but yeah, kind of very excited.

00:10:56 - Brandon Hancock
Like these will be all the templates.

00:10:58 - Brandon Hancock
So this is just like one of the the starters.

00:11:00 - Brandon Hancock
So.

00:11:00 - Brandon Hancock
Building it all out as we speak.

00:11:01 - Brandon Hancock
Just got to stop getting sick so I can code more and make more courses.

00:11:05 - Brandon Hancock
So very excited.

00:11:06 - Brandon Hancock
So yeah, if you have questions on any of that, I'll be doing a post probably later in the week.

00:11:12 - Brandon Hancock
And then final, final thing, I swear, and it's you guys' turn.

00:11:16 - Brandon Hancock
Upcoming video, I want to do the – I don't know if you guys have got to watch this yet.

00:11:22 - Brandon Hancock
Let me share my screen one more time.

00:11:23 - Brandon Hancock
Definitely want to recommend this resource if you guys haven't seen it yet.

00:11:26 - Brandon Hancock
But the Interrupt series by Langchain is probably one of the biggest hidden gems, I think, on the internet right now when it comes to building out agents and agentic applications.

00:11:39 - Brandon Hancock
Sorry, let me go to the playlist.

00:11:45 - Brandon Hancock
Interrupt 2025.

00:11:46 - Brandon Hancock
Yeah, so this playlist right here, it has – I think there's 11 different videos in here.

00:11:52 - Brandon Hancock
Everything from – everything from Andrew Ng talking about it, it's how Uber is building agents, JP Morgan's building agents.

00:12:00 - Brandon Hancock
So it's like they're not holding anything back, like they literally walk you through, here's exactly how we are building agentic applications in some of the big, I mean, the world's biggest companies.

00:12:10 - Brandon Hancock
So tomorrow I'm going to work on, while this is like still pretty new, work on like breaking it down, here's what I see and reporting back to you guys.

00:12:19 - Al Cole
So, but that's probably the next thing I'm LinkedIn one, Brandon, and it was insightful.

00:12:24 - Al Cole
They were, essentially I've got a recruiting platform on top of LinkedIn.

00:12:30 - Al Cole
And so they've got an AI agent, which you just give it a prompt of what you're sourcing for your talent.

00:12:35 - Al Cole
And it just goes out and finds the best matches based on your profile.

00:12:40 - Al Cole
It was pretty compelling.

00:12:42 - Brandon Hancock
And it's, it's insane.

00:12:44 - Brandon Hancock
So yeah.

00:12:45 - Brandon Hancock
Yeah, seriously, thanks.

00:12:46 - Brandon Hancock
Thanks for, for sharing that.

00:12:47 - Brandon Hancock
So yeah, if you guys have it, I'll drop like a link in the chat.

00:12:49 - Brandon Hancock
So you guys, if you want to just, you know, watch it over here today, tomorrow, but I will definitely be making the next video on this just to like basically summarize it, simplify it.

00:12:59 - Brandon Hancock
But I just dropped it.

00:13:00 - Brandon Hancock
So those are all the updates on my side, and earlier in the chat at 6.01, I dropped in the call order I'm going to go through, so Alex, you're up first, but before we start, I just want to say, Sam, I love the chicken hat, so just want to give a shout out to Sam before we kick things off, but Alex, the floor is yours.

00:13:22 - alexrojas
Yeah, hey, looking forward for that ship, .ai, man, that would be pretty dope.

00:13:29 - Brandon Hancock
I'm pumped, I'm very excited.

00:13:31 - alexrojas
Yeah, I love Dan as well, man, I'm a big follower of his, so yeah, I'm just keep doing some YouTube editing, I think I've realized, Brandon, that you were right, I need to get an editor.

00:13:48 - alexrojas
It's become a nightmare for me, I'm like, I barely have time to code, and you know, so that it was a key realization, and also, I've been working in a RAG application for a legal assistant.

00:14:00 - alexrojas
Right?

00:14:01 - alexrojas
Sure.

00:14:01 - alexrojas
Like I told you last time, I am trying to get, like, my fingers wet and, you know, learn that way.

00:14:07 - alexrojas
So I started doing kind of, trying to grab one of your agents from a video and then modify it, and it was quite messy.

00:14:17 - alexrojas
So I decided to take a go at your video of how to develop it.

00:14:25 - alexrojas
So I went, actually, through the pumps and, you know, used Next.js and everything.

00:14:31 - alexrojas
And I had a lot of learnings.

00:14:34 - alexrojas
But my specific question is, I want to develop more ADK agents, right?

00:14:42 - alexrojas
Okay.

00:14:42 - alexrojas
And now I ended up using the stack of Superbase.

00:14:49 - alexrojas
I have, I struggled a lot with Google authentication.

00:14:55 - alexrojas
I tried to be in the Google environment, Vertex AI.

00:14:59 - alexrojas
I spent...

00:15:00 - alexrojas
way too much time with those problems.

00:15:02 - alexrojas
So I just use Next.js and Superbase.

00:15:06 - alexrojas
And based on what Paul inspired last time, I'm doing double tagging.

00:15:11 - alexrojas
So I'm doing the SQL schema and the embeddings at the same time.

00:15:16 - alexrojas
And they are tied.

00:15:18 - alexrojas
So yeah, like I wanted to make that multi-agent, but that is just easier.

00:15:23 - alexrojas
So now I finally make it everything work.

00:15:27 - Brandon Hancock
It connects.

00:15:28 - alexrojas
Yeah.

00:15:29 - alexrojas
After a long, long, long, long time.

00:15:31 - alexrojas
But now I'm facing that it's actually very simple and there is no way now I can get any ADK agents because it's like pretty basic operation, you know.

00:15:44 - alexrojas
And so, and also I see that Next.js is JavaScript and ADK is more like Python based.

00:15:52 - alexrojas
So my question now is here, before I take it any further, should should I focus on...

00:16:00 - alexrojas
on...

00:16:00 - alexrojas
What stack in order to be more ADK-friendly?

00:16:04 - Brandon Hancock
Good question.

00:16:05 - Brandon Hancock
Okay, so I would actually, before saying just like, oh, multi-agent, I mean, when it comes to doing just general, like, level one RAG queries, like, you really don't need a full-blown agent to go deep into that path.

00:16:21 - Brandon Hancock
Like, there's nothing wrong with just making a query to your vector store and just, like, getting answers back and providing it as context.

00:16:31 - Brandon Hancock
Like, that's completely fine.

00:16:33 - Brandon Hancock
Like, the main reason you want to do agents is when you want to, like, you know, plan, take action, did you get the information, come back, take other action, like, that's when you want to go more agentic.

00:16:45 - Brandon Hancock
So, I mean, there's nothing wrong with just making multiple LLN calls to get context from your vector store, putting all of that back into a prompt and saying, like, here's some additional helpful resources.

00:16:57 - Brandon Hancock
You know, does this help you answer your question?

00:17:00 - Brandon Hancock
answer question?

00:17:00 - Brandon Hancock
You does this help

00:17:00 - Brandon Hancock
And basically, the prompt usually can use that context.

00:17:03 - Brandon Hancock
Like, you don't always have to go agents, especially with RAG.

00:17:06 - Brandon Hancock
Like, there's a – you usually have to have, like, a very good reason to go from, like, single-shot LLN calls with RAG to, like, a multi-agent solution would be.

00:17:17 - Brandon Hancock
So, yeah, I would actually just stick right now to just straight-up LLN calls.

00:17:22 - Brandon Hancock
I can actually really fast share, um, something, let's see, If I wanted to make that query with voice, like, your agent that controls the calendar, then it's when an agent makes sense, right?

00:17:40 - alexrojas
With the voice command.

00:17:44 - Brandon Hancock
Even then, you could still just do a normal voice, um, you could just use, like, Gemini Live.

00:17:52 - Brandon Hancock
They're API.

00:17:53 - Brandon Hancock
You could just use that.

00:17:55 - Brandon Hancock
It's just, like, whenever you want to do, like, more dynamic tool calling, you know, because that's kind of what –

00:18:00 - Brandon Hancock
For it's a regular LLM to an agent, especially with the multiple iterations, so there's multiple ways to, you know, to tackle this one, but yeah, just, I mean, like, really fast, here's what you do to get this to work in Supabase, so long story short, like, you're going to have a fetch, so basically, you're going to have make it like a – let me just go over – well, I don't want to take too long, but basically, in Supabase, you can create functions that take action inside on your database, so in Supabase, I created a function called Match Artifact Sections, and basically, I just passed in the embedding, how many do I want to get back, yeah, that's the threshold, like, how picky am I being, how many do I want to get back, and then I added some metadata to say, like, hey, I only want to get information back for these types of artifacts, so, like, you know, I only want to get information back on product to A, or I only want to get

00:19:00 - Brandon Hancock
information back on product B.

00:19:01 - Brandon Hancock
That's basically what I've done.

00:19:03 - Brandon Hancock
And a lot of this you can steal from this YouTube video I did a while back on Supabase.

00:19:12 - Brandon Hancock
You can steal it because a lot of the same principles apply.

00:19:17 - Brandon Hancock
Yeah, this one.

00:19:18 - alexrojas
yeah.

00:19:19 - Brandon Hancock
So a lot of the same code applies one-to-one to exactly what you're doing.

00:19:25 - alexrojas
So I would definitely recommend checking that one out.

00:19:27 - alexrojas
Okay, perfect.

00:19:28 - alexrojas
Yeah, actually, I got that idea from you because Supabase allows you to do the SQ and PG vector.

00:19:35 - Brandon Hancock
Yeah.

00:19:35 - Brandon Hancock
So they've come a long way.

00:19:37 - Brandon Hancock
I'm in I'm in love with what they're working on.

00:19:39 - alexrojas
Yeah, I learned the hard way that Google Cloud, Google Run doesn't allow PG vector.

00:19:46 - alexrojas
It's such a pain.

00:19:47 - Brandon Hancock
Yeah, it's a pain.

00:19:48 - Brandon Hancock
Yeah.

00:19:49 - Brandon Hancock
So any final things I can help with?

00:19:52 - Brandon Hancock
want to make sure you're...

00:19:53 - Brandon Hancock
Oh, and real quick, I owe you...

00:19:56 - Brandon Hancock
I can send you a link after this to a good editor.

00:19:59 - Brandon Hancock
I'll send you a link

00:20:00 - Brandon Hancock
I'll connect you to a guy.

00:20:02 - Brandon Hancock
Yeah.

00:20:02 - alexrojas
Yeah, I think, actually, I would like to talk to him before I record for him to tell me what exact specs I need to give to him.

00:20:10 - Brandon Hancock
Yeah?

00:20:11 - Brandon Hancock
no, perfect.

00:20:11 - Brandon Hancock
Yeah, his name's Abdul.

00:20:13 - alexrojas
I will connect you to him.

00:20:14 - alexrojas
Perfect.

00:20:15 - Brandon Hancock
Yeah, there's multiple.

00:20:16 - Brandon Hancock
Actually, I'll send you a few.

00:20:18 - Brandon Hancock
Okay.

00:20:18 - alexrojas
Yeah, so thank you very much.

00:20:20 - alexrojas
Yeah.

00:20:20 - Brandon Hancock
All right, dude, keep cranking away.

00:20:22 - Brandon Hancock
Hopefully next week we'll see an awesome demo, but that's what we're looking for.

00:20:25 - alexrojas
Oh, yeah.

00:20:25 - alexrojas
Yeah.

00:20:26 - alexrojas
Finally, I got to the connection side, and it's beautiful.

00:20:30 - alexrojas
Perfect.

00:20:31 - alexrojas
Love it.

00:20:31 - alexrojas
As you say, it's all working with it.

00:20:33 - alexrojas
I feel like having a cursor, it's like having an intern that you can exploit.

00:20:38 - alexrojas
Amazing.

00:20:39 - alexrojas
Yeah.

00:20:39 - Brandon Hancock
No, it's insane.

00:20:40 - Brandon Hancock
I mean, it's a cheat code.

00:20:41 - Brandon Hancock
All right, perfect.

00:20:42 - Brandon Hancock
We're gonna keep on cruising.

00:20:43 - Brandon Hancock
Mitch, you're up next, man.

00:20:45 - Brandon Hancock
How is your app development going?

00:20:47 - Brandon Hancock
What are we working on?

00:20:52 - Mitch
I didn't know I was coming up so close.

00:20:55 - Brandon Hancock
What?

00:20:55 - Brandon Hancock
Dude, right out the gate, man.

00:20:58 - Brandon Hancock
What?

00:20:58 - Mitch
No.

00:20:59 - Mitch
I thought, yeah.

00:21:00 - Mitch
There was, um, yeah, we Andrew and Mark.

00:21:04 - Mitch
All right, I broke – dude, thank you.

00:21:06 - Mitch
You're holding me accountable.

00:21:07 - Brandon Hancock
I appreciate it.

00:21:08 - Brandon Hancock
Um, you were just first on my screen.

00:21:10 - Brandon Hancock
Andrew, though.

00:21:10 - Brandon Hancock
All right.

00:21:11 - Brandon Hancock
We're fixing the order.

00:21:12 - Brandon Hancock
I'm dragging you guys back around to the right spots.

00:21:18 - Brandon Hancock
Oh, you're muted, Andrew, by the way.

00:21:23 - Andrew Nanton
Thank you.

00:21:24 - Andrew Nanton
Sorry about that.

00:21:24 - Andrew Nanton
Um, so yeah, a lot of, uh, a lot of the stuff that I'm doing is, you know, because of the kinds of files that I'm working with, I'm, I'm doing a lot of working with local files on disk and almost all of the web frameworks that I've tried for that are like, there's a lot of hoops you have to jump through to work with local files.

00:21:44 - Andrew Nanton
Um, so in some of the most recent experiments that I've been doing, and I, I think this sort of reflects my, my path along doing this stuff is like, uh, really the only language I know is Python, right?

00:21:57 - Andrew Nanton
Like that, that's the only language I know.

00:21:58 - Andrew Nanton
And, and I'm not, I'm not an expert.

00:22:01 - Andrew Nanton
And so I was looking at ways to work with things locally, and I feel like more and more I'm just falling back to, as I'm developing a plan with LLM, I'm like, well, I don't know, what do you think?

00:22:15 - Andrew Nanton
Sure, we'll go with that, because if that's what you know, then you're going to be writing it anyway.

00:22:20 - Brandon Hancock
So let's do that.

00:22:22 - Andrew Nanton
And I feel like more and more, so this most recent prototype that I'm working on is Tori for the, you know, like a Rust-based electron equivalent, and TypeScript, which at least I know a little TypeScript.

00:22:40 - Andrew Nanton
You know, I can fumble my way through TypeScript.

00:22:43 - Andrew Nanton
But I just feel like more and more the workflow that I'm falling into, which it sounds a little bit like, you know, if I'm reading between the lines correctly for you, Brandon, more like what you're falling into at times, which is like, most of my work is in specification docs.

00:23:00 - Andrew Nanton
And implementation plans, I'm like, okay, update the spec, all right, what have we done?

00:23:04 - Andrew Nanton
Update the implementation plan.

00:23:06 - Andrew Nanton
Let's start a new chat, fresh context window, review these two, let's move on to the next step, write some tests.

00:23:13 - Andrew Nanton
Tests are boring and terrible, but you don't mind writing them, so write the tests.

00:23:17 - Andrew Nanton
Did you break anything?

00:23:19 - Andrew Nanton
Okay.

00:23:19 - Andrew Nanton
And I feel like this is kind of the groove that I'm settling into in a lot of the work that I'm doing.

00:23:27 - Andrew Nanton
And I'm curious if that's true for other people, too.

00:23:30 - Brandon Hancock
I mean, real quick, for me at least, I mean, 100% spot on.

00:23:33 - Brandon Hancock
mean, that is my current workflow.

00:23:35 - Brandon Hancock
I mean, the AI docs folder that I showed in that last video, I use that religiously.

00:23:41 - Brandon Hancock
Like, I cannot express to you guys enough.

00:23:44 - Brandon Hancock
Between AI docs, cursor rules, Context 7, thank you, Andrew, and I can't remember who else called that one out, but if you guys haven't started to use Context 7, insanely powerful tool, what it allows you to do is, let me just actually showcase it really.

00:24:00 - Brandon Hancock
So, let's do

00:24:01 - Brandon Hancock
Context 7, I'll just share my screen really fast so everyone can see it in case you haven't yet.

00:24:09 - Brandon Hancock
Let's go here, share, share.

00:24:12 - Brandon Hancock
Fantastic.

00:24:13 - Brandon Hancock
So basically what Context 7 does is it has all the most popular docs that you could think of, it has them actually saved as like just text files.

00:24:24 - Brandon Hancock
So what's amazing about this is you can set up and you're – let me actually go to some code so I can just show you how easy it is because it is – it's wild how easy it is.

00:24:34 - Brandon Hancock
Sorry, let put this right here for you guys.

00:24:36 - Brandon Hancock
But yeah, all you do – oh, sorry.

00:24:40 - Brandon Hancock
There you go.

00:24:40 - Brandon Hancock
So all you do is just say, you know, set up your MP server, just point to the remote URL, Context 7, and now any time you're chatting with your agents and you're like, hey, you're not really doing what Tailwind is supposed to do, here, refer back to the Tailwind documents and check out what the latest docs say on how

00:25:00 - Brandon Hancock
how you should update global variables for style, or so forth, you know, and the agent will go, okay, cool, I'm using context 7, I'm looking up the library, I found it, okay, I now understand exactly how this library works, and then it just spits out correct code.

00:25:16 - Brandon Hancock
So, and the fact that all it takes to get access to all the latest documents is this, like, one line right here is honestly stupid.

00:25:23 - Brandon Hancock
So, definitely, thank you, Andrew, and I cannot remember who else called it out, but I've been using this religiously recently, just to help me work so much faster, not spend so much time, like, no, that's not what you do in Next.js, you know better.

00:25:36 - Brandon Hancock
So, I cannot recommend that one enough.

00:25:38 - alexrojas
You keep it in the, um, Jason, so if you, if you want, you just make a list of whatever, um, I'll just drop it real It's an FCP and you set it up once, and you, you know, unless it's a really exotic library, it's in there.

00:25:55 - alexrojas
Okay.

00:25:56 - Brandon Hancock
So, I'm dropping it in chat right now, uh, just so everyone could steal it.

00:26:00 - Brandon Hancock
Yeah, you just – in your .cursor folder, you have MCP, which is where you're going to set up your – you know, all your MCP servers, and what's nice is they have a public URL to handle everything, and that's all you have to paste.

00:26:13 - Brandon Hancock
And then when you're inside a cursor, you just say, use context 7 to look up, and like I said, it had access to Next.js, Talon.

00:26:23 - Brandon Hancock
It has access to almost 19,000 libraries.

00:26:27 - Brandon Hancock
So, if you're using a – like any tool, it has 19,000 libraries, and it'll look it up, find it, and use it instantly to help provide context to help you build better and faster.

00:26:38 - Brandon Hancock
So, cannot recommend that one enough.

00:26:40 - Brandon Hancock
Cheat code, honestly.

00:26:42 - alexrojas
Thank you very much.

00:26:43 - Brandon Hancock
So, oh, I turned off my camera.

00:26:45 - AbdulShakur Abdullah
Why do you put it – why do you put it in your .cursor folder and not like the MCP server folder?

00:26:54 - AbdulShakur Abdullah
Or is that the same thing?

00:26:56 - Brandon Hancock
Yeah, same, same.

00:26:58 - AbdulShakur Abdullah
Okay.

00:26:59 - Brandon Hancock
Yeah.

00:26:59 - Brandon Hancock
So, yeah, it'll work.

00:27:00 - Brandon Hancock
So, yeah, definitely recommend it if you guys haven't tried it yet for your projects.

00:27:04 - Brandon Hancock
It will save you so much time.

00:27:06 - Brandon Hancock
But yeah, Andrew, going back, though, to what you're doing on your development journey, cannot say it enough.

00:27:12 - Brandon Hancock
I mean, at this point, I am a senior engineer who's – or whatever engineer, just looking over a bunch of other engineers, making sure they're doing the right thing.

00:27:21 - Brandon Hancock
So, yeah, definitely recommend keep going down that path.

00:27:26 - Brandon Hancock
And would love to see – whenever you get your demo ready, would love to see it.

00:27:31 - Brandon Hancock
I have not – I've seen plenty of Electron apps.

00:27:34 - Brandon Hancock
In case you guys aren't familiar, Electron allows you to build a desktop application, you know, using Pyscript, basically.

00:27:43 - Brandon Hancock
So, I guess Andrew has found an alternative with Rust.

00:27:46 - Brandon Hancock
So, I'm very excited to see that come to life.

00:27:49 - Brandon Hancock
So, you'll have to let me know what you learned.

00:27:51 - Brandon Hancock
You'll be the Rust desktop expert in the group.

00:27:55 - Andrew Nanton
Without ever having written a line of Rust.

00:27:58 - Brandon Hancock
So, we'll see how that goes.

00:28:00 - Andrew Nanton
And I guess the last question I have is, I've noticed that in Cursor, which I've been using for, I feel like Winsurf has kind of fallen off a little bit, I have – the context windows that are available in the models are a lot smaller than they are generally available through the API, and I'm curious if anybody is having much success with things like Claude Code or Codex or Jules or, you know, these other more sort of overtly agentic systems, because especially I feel like as I'm moving further and further away from editing the lines of code, probably something like that makes sense, but I just – I'm also a little nervous to kind of make the jump, because it seems like a pretty big black box.

00:28:49 - Brandon Hancock
To Central Fest, and I'd love if anyone else have any feedback.

00:28:52 - Brandon Hancock
I mean, Claude Codex is probably, I think, going to be the winner in this area, because it I'm not sure if you guys – I'm not got to use

00:29:00 - Brandon Hancock
Devin, but it reminds me so much of Devin, to where I'm just, like, spinning off jobs, like, go do this, go do this, go do this, and then it just implements them in a PR and allows me to review them.

00:29:12 - Brandon Hancock
I, my personal feedback, like, if I'm coding, I'm coding.

00:29:16 - Brandon Hancock
I'm not just, you know, I'm not just thinking of a few tasks and then running away, like, I just want to build a feature.

00:29:21 - Brandon Hancock
So, I'm always just in Cursor.

00:29:24 - Brandon Hancock
I have not truly seen, like, why would I not just use Cursor instead of Claude code?

00:29:30 - Brandon Hancock
I haven't, I have not had that lightbulb moment yet to, like, oh, I have the use case now to where I don't want to see my code, I just want to spend background jobs off.

00:29:38 - Brandon Hancock
Like, no, I would just much rather open multiple tabs and just crank out code, where I can actively see it and iterate quicker.

00:29:45 - Brandon Hancock
Because I don't want to, yeah.

00:29:46 - Brandon Hancock
So, that's my, that's my thought.

00:29:47 - Brandon Hancock
But if, I know Bastion, he had a lot of, he has a lot of experience with Codex.

00:29:52 - Brandon Hancock
I can't remember if he's on the call tonight, but if anyone else has any experience, would love to, to, you know, hear, hear what your thoughts are as well.

00:30:00 - Bastian Venegas
I have used Codex, and it's pretty good, and they also made some updates recently, the main ones being that you can now ask for multiple, you can ask for a task and ask for multiple versions, so you can later decide which one you like the most, but you always need to set up this agents.md file, that it's kind of like cursor rules, that tells the agent how to, it's additional to the readme file, because it's meant for the agents and not for the humans.

00:30:31 - Bastian Venegas
So, if you use that, you get a lot more out of Codex, and they also implemented a way for, so the agent does have access to the internet, like to download some packages that you may need, and you can also make, so you can download the packages and run your tests and all that, but also you can now like, oh, I forgot what I was saying, I will type it into the chat.

00:31:00 - Bastian Venegas
is.

00:31:00 - Bastian Venegas
Oh Live isn't else.

00:31:00 - Brandon Hancock
Thank

00:31:00 - Brandon Hancock
Andrew, you can share, by the way, I just pressed approve.

00:31:03 - Andrew Nanton
Andrew Okay, great.

00:31:06 - Andrew Nanton
Andrew So there's not much to see, but...

00:31:11 - Andrew Nanton
Andrew So, you know, you'll see here what I've gotten started.

00:31:17 - Andrew Nanton
Andrew There's a couple of steps that I've put in.

00:31:19 - Andrew Nanton
Andrew So for the back end, I went with FastAPI.

00:31:23 - Andrew Nanton
Andrew I started with FastHTML, which has a lot of FastAPI sort of stuff built into it.

00:31:28 - Andrew Nanton
Andrew I thought FastAPI would be too heavy.

00:31:32 - Andrew Nanton
Andrew But again, like, you know, these LLMs have millions of lines of FastAPI code Andrew and zero lines of FastHTML.

00:31:40 - Andrew Nanton
Andrew so even if, in theory, something lighter is a better fit, Andrew it's just easier to, you know, go with the current Andrew and let it use FastAPI because it knows it.

00:31:51 - Andrew Nanton
Andrew But yeah, watch is a local file folder.

00:31:54 - Andrew Nanton
Andrew Norton,.D.: I have it processing.

00:31:58 - Andrew Nanton
Andrew.D.: So I.

00:32:00 - Andrew Nanton
I downloaded an open library copy of Dracula because it's very similar to the documents that I get where it's like one very large document with many small sub documents inside.

00:32:12 - Andrew Nanton
I don't know if you've ever read Dracula, but it's like, you know, a series of letters and diary entries and stuff is how it's written.

00:32:18 - Andrew Nanton
And so I wanted to test the splitting that Azure Document Intelligence is using.

00:32:24 - Andrew Nanton
So how is it defining the boundaries between these different elements?

00:32:28 - Andrew Nanton
Because this is a pretty optimal version of the kind of documents that I get, and then on the back end, what I was having it do is Azure Document Intelligence chokes at 2000 pages in creating a JSON representation of the hierarchy of the document.

00:32:48 - Andrew Nanton
And so I built out on the back end that it will reassemble, you know, an arbitrary length document into one giant piece of JSON, and which is...

00:33:00 - Andrew Nanton
It's shockingly okay in memory still, even when it gets really large.

00:33:05 - Andrew Nanton
So that's what I've been working on.

00:33:07 - Brandon Hancock
That's awesome.

00:33:08 - Brandon Hancock
That's awesome.

00:33:09 - Brandon Hancock
Yeah, I'd love to – like I said, the second, it's like full end-to-end.

00:33:12 - Brandon Hancock
Like you can click through or ask questions against the documents.

00:33:14 - Brandon Hancock
I'd love to see a demo.

00:33:16 - Brandon Hancock
And if you learn any rust along the way, I'd love to hear your thoughts on it.

00:33:22 - Brandon Hancock
But yeah, seriously, very cool Andrew.

00:33:24 - Brandon Hancock
All right, we're going keep on cruising.

00:33:27 - Brandon Hancock
Let's see.

00:33:27 - Brandon Hancock
Mark, you are up next, man.

00:33:31 - Marc Juretus
What's going on, gentlemen?

00:33:33 - Marc Juretus
Can you hear me?

00:33:34 - Brandon Hancock
Yep, sounds great.

00:33:35 - Marc Juretus
Not too much going on.

00:33:37 - Marc Juretus
still – so basically I was consuming Mix.js and FastAPI and Docker containers on top of still going through my Google agent stuff that I'm doing by ADK.

00:33:48 - Marc Juretus
But I did want to tell you, I don't know if you've ever seen an influence of Migos code.

00:33:53 - Marc Juretus
So I actually – I've actually been on the phone with him a few times for some advanced Spring Boot Java stuff.

00:33:57 - Marc Juretus
But anyways, he just reached out to me like a half hour.

00:34:00 - Marc Juretus
before the phone call, and asked if I believe that AI will be replacing developers, which I know we've talked about, and I'm like, look, I'm kind of like, just got my feet in this a little bit, but I did – I put in the chat what I responded with, so you guys could debunk it all you want, but anyways, he was asking questions, but I did send him an email, and I said, hey, dude, you ought to join our community.

00:34:24 - Marc Juretus
I mentioned you in there, but anyways, I said, you ought to join our community call, because there's a lot of cool stuff that people are doing, and these guys probably can answer the question a lot better than I can, but I said he ought to – and I don't know if you want to consider maybe getting in his Discord one time to pick up some new people, so he'd probably talk to you, man, but he's – yeah, he's got one of the – to be honest with you, the stuff where I've learned and stuff, he's probably got the best channel that I've seen, so I guess he doesn't know a lot about AI at this time, but that's what I wrote.

00:34:54 - Marc Juretus
I've been – since web, I started in 98, so from what static pages to database, is to content.

00:35:00 - Marc Juretus
To management systems, to Java stuff now, but, like, some of this code that it's writing, I mean, it's kind of like my belief, like, on Tesla with the – I didn't think the autonomous vehicles would come because I thought it wouldn't be safe enough and other – I think it's going to get to a point where pseudocoders can just go in there with a few paragraphs and explain themselves and have an app that's functioning.

00:35:20 - Marc Juretus
I mean, obviously, car sales would have to be in place, but that was what I wrote, so I don't know what your thoughts are on that.

00:35:26 - Brandon Hancock
So I want to do a full-blown video on this.

00:35:30 - Brandon Hancock
don't know if you guys – don't watch David Shapiro by chance.

00:35:33 - Brandon Hancock
He has a channel on, like, post – okay, I love that we're all nerds and watch the same thing.

00:35:40 - Brandon Hancock
In real life, all my friends are like, what are you talking about?

00:35:42 - AbdulShakur Abdullah
I think because we follow you, we get a lot of suggestions of things that you're connected to.

00:35:47 - Brandon Hancock
Okay, but, no, like, a lot of his thoughts on, like, post-labor economics I find so interesting.

00:35:53 - Brandon Hancock
Like, I don't know, I might want to do something on that at some point.

00:35:55 - Brandon Hancock
But, yeah, long story short, I mean, I do get – I it don't I

00:36:00 - Brandon Hancock
I'm starting to get a little bit more worried, but I'll tell you what I'm seeing.

00:36:04 - Brandon Hancock
basic – in the past, it was just static websites.

00:36:07 - Brandon Hancock
That's what AI was.

00:36:09 - Brandon Hancock
Now, it's gone to more CRUD.

00:36:11 - Brandon Hancock
So anything that's just straight-up database operations, now that it fully understands Next.js, server action, API points, making – now that it's starting to do more, it's getting to the level of CRUD, which is like most startups are really just a chat – AI AI startups are mostly just a chat section and a CRUD operations.

00:36:32 - Brandon Hancock
that is at the end of the day what most startups are.

00:36:35 - Brandon Hancock
That's all they have inside.

00:36:37 - Brandon Hancock
So it's getting pretty darn good at that.

00:36:40 - Brandon Hancock
What's next is like the more advanced features, which is actually like setting up backend infrastructure and connecting it all.

00:36:48 - Brandon Hancock
That's where I'm starting to say, well, like it does okay at it, but it's still not insane.

00:36:52 - Brandon Hancock
So it is definitely going up the stack, but I mean, is it going to replace developers?

00:36:57 - Brandon Hancock
My main thought is

00:37:00 - Brandon Hancock
I still think no, strictly because, like, you have – just strictly for accountability.

00:37:08 - Brandon Hancock
Like, a boss, you or an employer, needs to be able to say, go do this, you know?

00:37:14 - Brandon Hancock
So, like, I don't see – I basically see teams getting smaller, but I don't see, as a whole, like, developers just not existing, you know, because there still needs to be someone to, like – that can answer questions, take action, manage all the code.

00:37:27 - Brandon Hancock
So, I think it's just strictly going to shrink.

00:37:30 - Brandon Hancock
But, yeah, that's my thoughts.

00:37:31 - Brandon Hancock
I mean, curious if what you guys have any other ones.

00:37:34 - Brandon Hancock
I haven't got to, like, dive deep into, like, exploring it, because I'm like, man, I still just want to build.

00:37:39 - Al Cole
Have you guys heard the Y Combinator interview with Michael Truel?

00:37:44 - Al Cole
He's one of the founders of Cursor AI.

00:37:47 - Al Cole
So, this is his take over the last week or two.

00:37:51 - Al Cole
He doesn't view where they are today as a professional level yet, meaning that – you're able to build the basic –

00:38:00 - Al Cole
programs, but where he wants to get to is the million-line codebase, and he does not yet have that capability in what he's building.

00:38:10 - Al Cole
That's where he wants to get to.

00:38:11 - Al Cole
So he says he's probably six months away from getting that kind of reach into the codebase, but I didn't hear anything from him saying that this thing wasn't going to progressively get better.

00:38:23 - Al Cole
So it's kind of, Marc, a bit of a timeline question is, are you asking what the next year, in the next five years?

00:38:33 - Marc Juretus
Where's your response?

00:38:34 - Marc Juretus
My response was, by the way, I posted the second email about him joining the community.

00:38:39 - Marc Juretus
I'm an idiot.

00:38:39 - Marc Juretus
I just posted what I wrote him back, but I saw, I see like two to three years, like kind of like Brandon, the way Crew AI builds the whole model for you to start up.

00:38:50 - Marc Juretus
I think it's just going to get to a point where you're going to have enough of a framework that a outlier coder could really spin up some powerful stuff.

00:38:58 - Marc Juretus
That's my opinion.

00:38:59 - Marc Juretus
And, you know, you obviously

00:39:00 - Marc Juretus
You know, tons more than I do, but that's just my – from the outside as well.

00:39:04 - Brandon Hancock
One other thought real fast, and I just dropped that video.

00:39:08 - Brandon Hancock
I just added to the playlist, too.

00:39:09 - Brandon Hancock
I have – I got to watch that.

00:39:11 - Brandon Hancock
That's going to be an awesome, awesome interview.

00:39:13 - Brandon Hancock
The one thing that I think will probably also happen – just heads up, guys – I do think there will be a lot more work and opportunity for, like, one-off developer shops is, like, one thought I've had recently of, like, hey, as development becomes cheaper because you can do so much more with AI, it takes so much less time.

00:39:31 - Brandon Hancock
I mean, I think what's going to happen is companies will do a lot more custom solutions for their own stuff.

00:39:37 - Brandon Hancock
But I think there's going to be an opportunity for just more small, one-off developer agencies to, like, almost, like, be a one-man army of, like, hey, I will build any business anything.

00:39:46 - Brandon Hancock
I'll charge you $5,000 to $10,000, which is, you know, maybe $15,000, depending on the size of the business and what they're trying to do.

00:39:53 - Brandon Hancock
And, like, you know, and you're just creating insane value for that company, but it's now becoming affordable.

00:39:57 - Brandon Hancock
Because in the past, that same solution literally…

00:40:00 - Brandon Hancock
Like, two years ago would have been closer to $80,000, $100,000 just because, like, it would have taken a front-end developer, a UI, UX, creator just to spin up the whole workflow, and it's, like, front-end, back-end, like, there's so much to that.

00:40:13 - Brandon Hancock
Like, it would have been a full startup team working on it for three months.

00:40:15 - Brandon Hancock
Though it would have blown through the budget.

00:40:17 - Brandon Hancock
It just wouldn't have been feasible.

00:40:18 - Brandon Hancock
So I do think things are going to become more custom.

00:40:20 - Brandon Hancock
The only, like, the analogy I could think of is, like, back in the day when things are super expensive to do, you had, like, three TV channels for everyone, like, back in my parents' age.

00:40:28 - Brandon Hancock
And as time has gone on, you've fractaled all the way now to where, like, TikTok, to where there's any content anywhere ever that could be possibly created, it's being created.

00:40:39 - Brandon Hancock
So I think things are just going to continually fractal down to a super, super niche, and I think which opens up opportunities for you guys, as, like, being able to come in as a one-man army and work and just crank through as many $10,000 to $20,000 projects as possible.

00:40:52 - Brandon Hancock
So that's where I think it's going as things get cheaper.

00:40:57 - Marc Juretus
If he responds to me, you're fine with him joining the channel.

00:41:00 - Marc Juretus
He's, in some way, a competitor of yours.

00:41:02 - Marc Juretus
No, I'd be happy to hop on a one-on-one call, too.

00:41:06 - Marc Juretus
Well, you don't know what it'll spit into, you know, with himself.

00:41:09 - Marc Juretus
But anyways, I did have one quick question, because I, uh, I just wanted to do a quick screen scare, I just wanted to, your opinion on something real quick.

00:41:17 - Marc Juretus
Let me make it real brief.

00:41:20 - Marc Juretus
Can you, uh, see my screen?

00:41:22 - Marc Juretus
Um, no, there goes.

00:41:25 - Marc Juretus
Alright, so here's my question.

00:41:26 - Marc Juretus
Um, is there a specific format that you can, that you have to return, uh, from a, from an agent call that, know, is able to, so basically I did, I took your advice, and I have the Chrome embeddings going, and it's returned.

00:41:41 - Marc Juretus
So, to make a long story short, uh, I basically embedded this document, which is from my Rallo port, you know, application, and I have it embedded.

00:41:49 - Marc Juretus
And anyways, let me go back to the code, um, I keep doing it, it's not the icon, alright.

00:41:54 - Marc Juretus
So anyways, it's this one here.

00:41:57 - Marc Juretus
Um, and if go here, so basically I made it.

00:42:00 - Marc Juretus
As a class, Brandon, it says embed new, and then I did the if main just to test it locally, as opposed to when the agent calls it, right?

00:42:08 - Marc Juretus
So my question to you is – let me get down here to it.

00:42:12 - Marc Juretus
Ah, come on.

00:42:13 - Marc Juretus
So anyways, if I run it here, which basically is just going to call the class, it's going to pass the information, my arcade machine won't turn on.

00:42:21 - Marc Juretus
So it's going to the Chrome embedding, and then boom, comes back, like got all this – basically the answer is right there.

00:42:30 - Marc Juretus
It pulls it from embedding as expected, right?

00:42:33 - Marc Juretus
But the problem is now when I use ADK, and I call it, and I see that it's actually calling it, is there a specific format that I have to return it in?

00:42:41 - Marc Juretus
Because when I come in here, and I actually run the actual agent, that you can see that it calls it.

00:42:48 - Marc Juretus
What do I do if my machine won't power on?

00:42:52 - Marc Juretus
And I'll show you that code real quick.

00:42:55 - Marc Juretus
It comes back and it finds nothing.

00:42:58 - Marc Juretus
And I see the tool response to the –

00:43:00 - Brandon Hancock
The tech info, tool response?

00:43:02 - Brandon Hancock
Yeah.

00:43:04 - Brandon Hancock
Okay.

00:43:05 - Brandon Hancock
So nothing's in response.

00:43:07 - Marc Juretus
Yeah.

00:43:07 - Marc Juretus
And what I wanted to show you was – so basically – it's in this one here.

00:43:12 - Marc Juretus
So here's the call, right?

00:43:13 - Marc Juretus
And just to show you, like, the agent does call it because it comes in here and says – I even put my name in there and misspelled it as Marco.

00:43:21 - Marc Juretus
And where is it at?

00:43:22 - Marc Juretus
Right?

00:43:23 - Marc Juretus
Right.

00:43:23 - Marc Juretus
Come on.

00:43:24 - Marc Juretus
Jesus Christ.

00:43:27 - Marc Juretus
But anyways, yeah, right there.

00:43:28 - Brandon Hancock
The criteria path, Marco.

00:43:30 - Marc Juretus
So it does call it, right?

00:43:32 - Marc Juretus
Yeah.

00:43:32 - Marc Juretus
here's the code for that real quick.

00:43:35 - Marc Juretus
I just did another function.

00:43:37 - Marc Juretus
It's tech info three.

00:43:40 - Marc Juretus
And it's just embedding that class that you saw.

00:43:43 - Marc Juretus
And I say, hey, use tech info three.

00:43:45 - Marc Juretus
And this is the call you make with the user data.

00:43:49 - Marc Juretus
So my question is, why is it not returning it there when I do Line 88, could you hover over it?

00:43:56 - Marc Juretus
Right here?

00:43:58 - Brandon Hancock
Yeah.

00:43:58 - Brandon Hancock
Hover over to get the next one.

00:44:00 - Brandon Hancock
GetTechInfo2.

00:44:01 - Marc Juretus
Sorry, line 88.

00:44:04 - Marc Juretus
So it's returning a string, returning a date.

00:44:07 - Brandon Hancock
Okay, so just a few things I'm noticing.

00:44:11 - Brandon Hancock
Ideally, for ADK tool calls, you need a doc string.

00:44:15 - Brandon Hancock
I'm surprised it's not complaining about that.

00:44:18 - Brandon Hancock
I would have added a doc string just to say what the tool does.

00:44:21 - Brandon Hancock
You want to return a dictionary.

00:44:25 - Brandon Hancock
If you return a string, ADK usually wraps it in to a result, but depending on what you're trying to return, it might be doing something weird.

00:44:36 - Brandon Hancock
So you always want to make sure you're returning dictionaries.

00:44:39 - Marc Juretus
So GetInfo2 should return a dictionary.

00:44:41 - Marc Juretus
And you want the doc string basically explaining what the tool does overall.

00:44:44 - Marc Juretus
That's getting confused.

00:44:46 - Brandon Hancock
Okay.

00:44:47 - Brandon Hancock
All right.

00:44:48 - Brandon Hancock
Yeah.

00:44:49 - Brandon Hancock
And then I would also GetTechInfo2.

00:44:51 - Marc Juretus
Can we go back to that class real fast?

00:44:52 - Marc Juretus
And then we'll hop out.

00:44:54 - Marc Juretus
Yeah.

00:44:55 - Brandon Hancock
So yeah, this should return a string.

00:44:57 - Brandon Hancock
It should have typings for criteria.

00:45:00 - Brandon Hancock
Yeah.

00:46:00 - Brandon Hancock
Keep on cruising, guys.

00:46:02 - Brandon Hancock
Next up, let's see, is – all right, now back to you, Mitch.

00:46:08 - Mitch
Yay.

00:46:09 - Brandon Hancock
The floor is yours.

00:46:10 - Mitch
I did not skip the line.

00:46:13 - Mitch
I do have one note with the – is AI taking over coding?

00:46:18 - Mitch
I was listening to this guy.

00:46:21 - Mitch
I don't really know his credits.

00:46:23 - Mitch
I'll add it to them.

00:46:26 - Mitch
But they call him the father of LLMs or something like that.

00:46:30 - Mitch
So I was curious about what his opinion was.

00:46:33 - Mitch
And he said just, you know, the generative text models would be a tool that, like, an actual higher level of intelligence would use.

00:46:39 - Mitch
But, like, what he designed is largely what the LLMs are using, that generative text transformation model and that stuff.

00:46:48 - Mitch
And he's like, it's going to be hard to, like, take it to another level of, like, where it's at.

00:46:54 - Mitch
And you can create tooling to, like, really funnel it.

00:46:57 - Mitch
But it's still, at the end of the day, not going to be.

00:47:00 - Mitch
Yeah.

00:47:00 - Mitch
Yeah.

00:47:00 - Mitch
He's good as what people would think, and, I mean, he's one of the people who helped pivot and get this whole industry moving forward, so that's who I trust a bit more than the people who have a financial gain, but that's just me.

00:47:14 - Brandon Hancock
No, that's interesting.

00:47:15 - Brandon Hancock
Huh.

00:47:16 - Brandon Hancock
Apparently he has a – okay.

00:47:17 - Brandon Hancock
Yeah, have you seen YouTube videos from him too?

00:47:19 - Brandon Hancock
Please share if you see any good ones.

00:47:21 - Mitch
I'd just be curious to see what he says.

00:47:22 - Mitch
Yeah, I have a video a back.

00:47:23 - Mitch
I was trying to find it, but yeah, after this I'll try to find it.

00:47:28 - Mitch
So, one thing is, I saw you using, like, a super-based edge function.

00:47:32 - Mitch
Are you using that, like, over Railway?

00:47:36 - Brandon Hancock
Yep.

00:47:37 - Brandon Hancock
So, it's actually different.

00:47:42 - Brandon Hancock
Let me just – I'll just show you exactly what it is.

00:47:44 - Brandon Hancock
I'll share my screen really fast.

00:47:45 - Mitch
Let me just go to the project.

00:47:46 - Mitch
Sorry, Dad.

00:47:47 - Brandon Hancock
Super fast.

00:47:48 - Mitch
I was just – No worse.

00:47:50 - Brandon Hancock
Hey, we're here to share some code, man.

00:47:53 - Brandon Hancock
Okay.

00:47:53 - Brandon Hancock
Let's do share.

00:47:56 - Brandon Hancock
Share.

00:47:57 - Brandon Hancock
All right.

00:47:58 - Brandon Hancock
So, this is a client project and –

00:48:00 - Brandon Hancock
And database, database functions, and then this is a public function, and then – oh, what was it?

00:48:12 - Brandon Hancock
I can't remember off the top of my head.

00:48:14 - Brandon Hancock
Match artifact.

00:48:18 - Brandon Hancock
Yeah, so you can kind of see what it does, but basically – match function, but I guess not.

00:48:26 - Brandon Hancock
This is like a database function, so there's different types inside Supabase.

00:48:34 - Brandon Hancock
So this one you can see, it's like, all right, what are the arguments for this database function?

00:48:38 - Brandon Hancock
Based on that, I'm actually going to perform a raw SQL query on the database, and then it just like returns back the artifacts that are similar, and it's only going to return the top three, order by the most similar, limit to the top number.

00:48:56 - Brandon Hancock
So this is how you do it.

00:48:58 - Brandon Hancock
And then you can actually see –

00:49:01 - Brandon Hancock
Um, just real fast, you know, one of the reasons we use Drizzle is so that we have, like, a migration history.

00:49:07 - Brandon Hancock
Let's not let me – there we go.

00:49:09 - Brandon Hancock
So you can see inside of Drizzle, we've made a function right here.

00:49:15 - Brandon Hancock
I'll actually paste this in chat, Mitch, if – I think some people will be fine.

00:49:19 - Brandon Hancock
Um, I have to – yeah.

00:49:25 - Brandon Hancock
Mitch, I'll shoot it to you in a DM.

00:49:27 - Brandon Hancock
But if anyone else wants it too, just let me know.

00:49:29 - Brandon Hancock
But this is, like, a straightforward function to basically have, you know, perform a RAG query inside of your Supabase, Supabase vector store.

00:49:38 - Brandon Hancock
And it comes – final thing is it comes with this cool little extra field I added, and this is where – how I can filter by metadata.

00:49:46 - Brandon Hancock
So in my case, I only want to, like, query a certain document.

00:49:51 - Brandon Hancock
So imagine you had a hundred documents, and I'm like, no.

00:49:53 - Brandon Hancock
The user's trying to chat with three of them.

00:49:56 - Brandon Hancock
Here are the three ideas.

00:49:58 - Brandon Hancock
That way you don't accidentally, like, bring –

00:50:00 - Brandon Hancock
And something about like cars, if they're trying to do stuff on boats, you know, so this is a, this is a little extra nuance than what you'll typically see from, from, from most demos, so, um, but yeah, so I'll actually use this too.

00:50:15 - Mitch
So, uh, if you're doing the function with SupaBase, then why, why are you still using Drizzle on top of that?

00:50:24 - Brandon Hancock
Oh, sorry, Drizzle, uh, Drizzle, so Drizzle is the ORM, um, and, you know, it's like what helps us, like, take usual code, uh, like a, like our normal schema that's in TypeScript, and converts it over to, uh, to an actual SQL table, a SQL table.

00:50:39 - Brandon Hancock
What's awesome though, is you can use Drizzle to create all sorts of migration files, and in this case, I wanted to, like, not just go into the SupaBase, you know, UI editor, and just manually create something, I like to keep everything as code, so I can always have a log of everything I've ever done, so, um,

00:51:00 - Brandon Hancock
So that's why I created a schema that I then – or I created a migration that I then applied to the Drizzle database.

00:51:07 - Brandon Hancock
When I did that, it created a new function.

00:51:10 - Brandon Hancock
So now I can always call in my code Supabase RPC.

00:51:17 - Brandon Hancock
I can't remember what it stands for off the top of my head.

00:51:19 - Brandon Hancock
I think it's a remote procedure call, but I could be butchering that if anyone knows.

00:51:24 - Brandon Hancock
But yeah, basically – Remote procedure call, yeah, that goes back to the 90s.

00:51:27 - Ty Wells
You bet.

00:51:28 - Brandon Hancock
Okay.

00:51:33 - Brandon Hancock
But yeah, so basically it can perform a remote function call.

00:51:37 - Brandon Hancock
And the function I'm calling is this with these arguments.

00:51:39 - Brandon Hancock
So yeah.

00:51:40 - Brandon Hancock
So it's a pretty cool way to actually execute raw SQL queries instead of having to do all sorts of other stuff.

00:51:47 - Brandon Hancock
Pretty nice add-in from Supabase.

00:51:50 - Brandon Hancock
Last thing, you just want to make sure you're probably calling it as an admin.

00:51:54 - Brandon Hancock
So I have like an admin client that can perform these like more advanced queries.

00:51:59 - Mitch
Gotcha.

00:52:00 - Brandon Hancock
So I – That's

00:52:00 - Brandon Hancock
I don't want have to worry about permissions when I'm doing stuff like that, so there.

00:52:04 - Brandon Hancock
So boom, there's your rag in a nutshell, man.

00:52:07 - Mitch
Yeah.

00:52:08 - Mitch
Yeah, I might have to delay this project a little bit more for you to finish some of the stuff on your end, so I'd just be like, yeah, you know what, I'll just copy and Copy and paste.

00:52:14 - Brandon Hancock
Hey, that's the goal of the thing I'm working on, all the templates, just copy and paste.

00:52:19 - Brandon Hancock
So anything else can help with on your project, man?

00:52:22 - Mitch
No, I'm just manually copying and pasting the lovable stuff, because it was like that free period, so I learned how, anyways, just copy and pasting that, adding that to a directory so that I can reference that in cursor.

00:52:36 - Brandon Hancock
Real quick, I think this is a super valuable lesson.

00:52:39 - Brandon Hancock
actually just, Mitch and I were talking about this, so I don't know if you guys saw, I don't know if you guys saw in the last video on my workflow, but here's literally what I'm doing now to help speed up the process of going from lovable, which is a vite based project to transform it to a next.

00:53:00 - Brandon Hancock
JS-based project.

00:53:01 - Brandon Hancock
So what you do is you add a sub-module to your project.

00:53:06 - Brandon Hancock
I just called mine Lovable.

00:53:08 - Brandon Hancock
This is the full-blown project that I built in Lovable, and you can see it has all my components, all my like FAQ.

00:53:17 - Brandon Hancock
It has everything in here, but it's not, you know, it's not made for Next.js.

00:53:22 - Brandon Hancock
So then what I do is like, you know, I'm making templates for this, but long story short is you can actually just call.

00:53:29 - Brandon Hancock
So you could do like, hey, you don't have to do hey, but please recreate the components in, and then you can just call it out.

00:53:39 - Brandon Hancock
So Lovable, Lovable components, and yeah, and then you can like say now recreate them inside of my Next.js project over here.

00:53:50 - Brandon Hancock
And this is what's so nice about this is you're not having to like copy and paste, and all you've done is added a git sub-module, just like this.

00:53:59 - Brandon Hancock
And now you can.

00:54:00 - Brandon Hancock
can.

00:54:00 - Brandon Hancock
You refer to it as much as you want when you're going from Lovable to Nex.js, and then when you're done, just delete the sub-module, delete Lovable, hands are clean, and you're just working on your own project.

00:54:09 - Brandon Hancock
So this is the easiest way I have found to port things over.

00:54:14 - Brandon Hancock
So hopefully that's helpful as you guys are cranking out your own projects.

00:54:19 - Brandon Hancock
And one last thing.

00:54:21 - Mitch
So like, let's say, currently I have a button that would just go to trigger a webhook to start an NNN workflow, but now that I'm kind of doing more code-heavy, would I just use Railway to do that, or do you recommend something else?

00:54:38 - Brandon Hancock
Railway to trigger NNN, or Railway to just do the job?

00:54:44 - Mitch
Just to do the job, yeah.

00:54:46 - Brandon Hancock
Railway is awesome, but if it's all, like, you could also potentially just do it as an API function, or like a, yeah, you, like, depending on what that NNN workflow is doing, you could either just do it as code if it's all TypeScript.

00:54:59 - Brandon Hancock
Like, if you can do it in TypeScript, you could

00:55:00 - Brandon Hancock
Do it in a regular API forward slash thing, whatever you're trying to do, or if you need it to be Python because you're doing some custom library stuff, yeah, you might have to do it over in real way.

00:55:10 - Mitch
like, if it's hosted on Vercel, it would be on Vercel.

00:55:13 - Brandon Hancock
Yeah, it would just run as a function, yeah.

00:55:16 - Brandon Hancock
So, yeah.

00:55:18 - Brandon Hancock
Also, I mean, always hit me up, Mitch, too.

00:55:20 - Brandon Hancock
Happy to help if anything's broken.

00:55:22 - Brandon Hancock
So, happy to help.

00:55:24 - Brandon Hancock
So, all right, we're keep on cruising.

00:55:26 - Brandon Hancock
I want to make sure everyone gets a chance.

00:55:27 - Brandon Hancock
So, Juan, you're up next, buddy.

00:55:33 - Juan Torres
So, I had the MVP for the Agentex system I was building for my client.

00:55:42 - Brandon Hancock
Hey, how's it going?

00:55:44 - Juan Torres
Good, good.

00:55:45 - Juan Torres
It works.

00:55:46 - Juan Torres
So, I have an Agentex system now that essentially goes through the description column, extracts the vendor name, and then places into another column.

00:55:57 - Juan Torres
And it's interesting.

00:55:58 - Juan Torres
I still have to improve.

00:56:00 - Juan Torres
Proof in accuracy in terms of like what identifies as the vendor name, but essentially I'm using a hybrid architecture in which part of the way identifies the vendor name is through the LLMs.

00:56:17 - Juan Torres
I'm using ChatGPT for Turbo as the models that I'm using for my Agentex system.

00:56:25 - Juan Torres
I'm using CrewAI as a sequential system in order to go through the process.

00:56:30 - Juan Torres
But then in a parallel form and in a synchronous form, it's using a machine learning model that essentially it's like the name identification model.

00:56:45 - Juan Torres
So it's the one that I was talking to you last time.

00:56:50 - Juan Torres
So let me share with you on the chat.

00:56:52 - Juan Torres
This is the library that I'm using in order to choose which model I'm going to be using for the machine learning.

00:57:01 - Juan Torres
The Machine Learning NER model, which is Name Identification Recognition Models, so I'm choosing the NCORE WebSM, which is a 15 megabytes machine learning model, and just using that additionally to the AgencTIC system, I found out that it increased the accuracy of the vendor recognition significantly.

00:57:32 - Brandon Hancock
Oh, that's awesome.

00:57:33 - Juan Torres
Yeah, so this is what I'm working on right now, and I guess, like, my question to you guys is, since this, I feel like this is going to be good in terms of increasing probability of accuracy, either in AI engineering or machine learning engineering, but now the task is to implement this AgencTIC system into the database, the PostgreSQL database.

00:58:00 - Juan Torres
The database that my client has, and so I'm thinking of how I'm going to generalize the operation of the Agentex system with the database, and maybe I'm thinking of using an MPC, NCP, in order to do so, but if you all have any other recommendations come up into suggestions.

00:58:20 - Brandon Hancock
Can you repeat the question just real fast, just to make sure I'm pulling the understanding?

00:58:27 - Juan Torres
What was that?

00:58:27 - Juan Torres
Uh, could you repeat the question?

00:58:29 - Brandon Hancock
I just want make sure I fully understand, like, what we're trying to do.

00:58:32 - Juan Torres
So, now that I have an Agentex system that it's working with a CSV file, being able to transpose, uh, vendor names, right, sooner or later, I'm going to have to use this Agentex system with its hybrid system of, of, you know, vendor identification in, uh, PostgreSQL database.

00:58:53 - Juan Torres
So, and, of, and and a, and a iterating.

00:59:00 - Juan Torres
each row and extracting that vendor name into missing values within the name column.

00:59:07 - Juan Torres
So the accessibility, I don't have an issue with that.

00:59:10 - Juan Torres
I've made access compatible issues work with me.

00:59:16 - Juan Torres
But I still have issues conceptualizing how I'm going to allow the agentic system to have access to the PostgreSQL database.

00:59:27 - Brandon Hancock
The simplest answer is, like, if this is the only tool that you're creating right now, like, I would just make it a tool call.

00:59:33 - Brandon Hancock
think doing a full-blown MCP server where you have to set up the client server, like, I think that's overkill.

00:59:39 - Brandon Hancock
So, I mean, just a straightforward tool that is, like, all the SQL commands you would want to make, such as, like, create, edit, or, you know, create, update, and row.

00:59:50 - Brandon Hancock
So, I would, that's all I would do is just make general PostgreSQL tools that can connect to your database, make the, make the operation, and commit the challenge.

01:00:00 - Brandon Hancock
That's as deep as I would go, and you could always add those tools to crew.ai, you know, there's – I have a few actual YouTube videos on creating tools for crew.ai that I think you could probably just copy and paste to just enter cursor and say, redo this, but, you know, I'm using a Postgres database.

01:00:18 - Brandon Hancock
If you're using an ORM, it makes it even easier to, you know, make those changes, to make those queries.

01:00:25 - Brandon Hancock
So, yeah, I would just stick to regular tools, that's you're trying to do, would be my advice.

01:00:31 - Al Cole
And, Ron, this is Al.

01:00:33 - Al Cole
Just a question about the life cycle of the data itself.

01:00:36 - Al Cole
Are you doing a one-time pass through those tables and then pulling out the information?

01:00:42 - Al Cole
Or do you need to worry about updates and have some kind of trigger that reprocesses that row?

01:00:50 - Juan Torres
That's a good question.

01:00:53 - Juan Torres
I believe that it's going to be more on the first option.

01:00:59 - Juan Torres
The second one can happen.

01:01:00 - Juan Torres
Happiness?

01:01:01 - Juan Torres
Well, it depends, right?

01:01:03 - Juan Torres
A whole process of iterating.

01:01:06 - Juan Torres
It's essentially, you're talking about an ETL process, right?

01:01:09 - Juan Torres
If we're talking about the second option.

01:01:10 - Al Cole
wasn't sure is the nature of change.

01:01:12 - Al Cole
So if the data gets into the tables and your app's the only one modifying it, then you have control of this.

01:01:18 - Al Cole
But if there's outside ways of modifying that same data, you need to be aware of a change so that you could maybe pull out or update the vendor information you spoke about.

01:01:28 - Juan Torres
Yeah, I don't think there's going to be outside factors changing the data.

01:01:32 - Al Cole
Okay.

01:01:33 - Juan Torres
Yeah.

01:01:33 - Brandon Hancock
Awesome question, Al, by the way.

01:01:35 - Brandon Hancock
Thinking bigger.

01:01:36 - Brandon Hancock
I love it.

01:01:38 - Brandon Hancock
But seriously, congrats also on the big project.

01:01:41 - Brandon Hancock
Once again, I'm very excited.

01:01:43 - Brandon Hancock
You know, as you get to work on it more, it would be very cool at some point maybe to do like a lesson learned or, you know, something like, hey, just did a huge client project.

01:01:51 - Brandon Hancock
Here's a few things I learned I think I'd make for a cool little post or we could do like a recorded call to share with the group.

01:01:57 - Juan Torres
I that'd be awesome.

01:01:59 - Juan Torres
Yeah, I think think the.

01:02:00 - Juan Torres
The really interesting part is that I've never thought about the process of doing a hybrid system of using LLMs and machine learning models at the same time.

01:02:10 - Juan Torres
So I think that's the thing that a lot of people will be interested about.

01:02:15 - Brandon Hancock
I think that's very – yeah, I mean, I've never done that, but it makes total sense for, I think, what you're trying to do here.

01:02:21 - Brandon Hancock
So, no, seriously, thanks, man.

01:02:23 - Brandon Hancock
You are exploring new frontiers.

01:02:25 - Brandon Hancock
Absolutely love it.

01:02:27 - Brandon Hancock
Perfect.

01:02:28 - Brandon Hancock
All right.

01:02:28 - Brandon Hancock
We're going to keep cruising.

01:02:30 - Brandon Hancock
Adam was up next.

01:02:32 - Brandon Hancock
I don't know if he's still on the call or if he hopped off.

01:02:36 - Brandon Hancock
I think he hopped off.

01:02:38 - Brandon Hancock
So next would go to Abdul.

01:02:42 - AbdulShakur Abdullah
All right.

01:02:43 - AbdulShakur Abdullah
All right.

01:02:45 - AbdulShakur Abdullah
For me, I've just – well, I didn't have as much time to actually code recently.

01:02:51 - AbdulShakur Abdullah
But I have been kind of working on building up the LinkedIn profile, sharing AI information posts.

01:03:00 - AbdulShakur Abdullah
Yeah.

01:03:00 - AbdulShakur Abdullah
And I'm trying to design a new kind of workflow system where you kind of feed an agent your brand or a link to your URL, and then it goes out to all the different agents and finds out what they think about your brand.

01:03:26 - AbdulShakur Abdullah
So kind of giving you marketing information.

01:03:31 - AbdulShakur Abdullah
I've seen a couple programs out there like that that do that, but they're all very expensive, and I was trying to make one cheaper so it would kind of use Open Router so the person would be paying for their own calls so they could kind of decide how much they wanted, if they wanted just a little call to see what people are talking about or what AI agents think about them.

01:03:56 - AbdulShakur Abdullah
Yeah, so that's kind of what I've been working on.

01:03:59 - Brandon Hancock
That's awesome, what are you uh...

01:04:00 - Brandon Hancock
So the hood, what are you thinking about using tech-wise?

01:04:03 - AbdulShakur Abdullah
What are we leaning towards?

01:04:06 - AbdulShakur Abdullah
Right now, I'm still so early in the process.

01:04:08 - AbdulShakur Abdullah
I'm just thinking kind of what would – what's my inputs and outputs?

01:04:14 - AbdulShakur Abdullah
Like, what would be the most valuable input-output?

01:04:17 - AbdulShakur Abdullah
So I'm very early in that stage.

01:04:19 - AbdulShakur Abdullah
Tech-wise, I probably would stay even closer to let me figure out what my prompts will be before I even go into tech.

01:04:31 - AbdulShakur Abdullah
But I am very open to suggestions, tech-stack.

01:04:37 - Brandon Hancock
Yeah, the second – I think the second you get a little more clarity on, like, input-outputs, would be happy to, like – here's what I think how crew AI would handle this, ADK would handle this, and LangGraph, I'd be happy to, like, walk you through, hey, here's what I think each framework would – how it could handle it, or if it should just be straight-up LLM calls.

01:04:56 - Brandon Hancock
So yeah, happy to – once you get a little bit more input-outputs, happy to – happy to.

01:05:00 - Brandon Hancock
So yeah.

01:05:00 - Brandon Hancock
To share more.

01:05:01 - AbdulShakur Abdullah
Okay.

01:05:02 - AbdulShakur Abdullah
And then, yeah, I am starting to get a little more traction on the LinkedIn profile, which is good.

01:05:12 - AbdulShakur Abdullah
That's awesome, man.

01:05:13 - AbdulShakur Abdullah
Let see if I can share my screen.

01:05:20 - AbdulShakur Abdullah
Yeah, so redid the profile, started posting more.

01:05:29 - AbdulShakur Abdullah
Heck yeah, dude.

01:05:32 - Brandon Hancock
Hey, it's consistency.

01:05:34 - Brandon Hancock
That's the key.

01:05:37 - Brandon Hancock
Real quick, something I think would be super, super helpful.

01:05:41 - Brandon Hancock
I talked about this in the accelerator program I just did, but like, if you want to explode, yeah, man, that's insane.

01:05:51 - Brandon Hancock
Yeah.

01:05:52 - Brandon Hancock
Green numbers up and to the right.

01:05:53 - Brandon Hancock
Love it.

01:05:54 - Brandon Hancock
Seriously, like, the easiest way to explode is like, build an asset, like, build a prop.

01:06:00 - Brandon Hancock
You build anything.

01:06:01 - Brandon Hancock
Like, hey, I just, you know, I'm coding 24-7.

01:06:05 - Brandon Hancock
Here are my 10 most valuable cursor rules that I use when building all Next.js projects.

01:06:12 - Brandon Hancock
DM me cursor and I will send you my rules.

01:06:16 - Brandon Hancock
Dude, that one post right there will, like, you'll get hundreds of comments because people are like, oh my god, like, I need to do this.

01:06:23 - Brandon Hancock
So, cannot recommend, like, just creating an asset.

01:06:27 - Brandon Hancock
Like, hey, here's 10 things or here's something.

01:06:30 - Brandon Hancock
DM me and I'll give it to you for free.

01:06:32 - Brandon Hancock
Because, like, people love free stuff and it just, like, creates a viral loop on LinkedIn because it sees people are commenting.

01:06:38 - Brandon Hancock
So, it pushes it to more people.

01:06:39 - Brandon Hancock
More people see it.

01:06:40 - Brandon Hancock
It gets commented more.

01:06:41 - Brandon Hancock
Because, like, you know, I did a program, Ship 30 for 30.

01:06:45 - AbdulShakur Abdullah
I don't if you guys have heard of or not.

01:06:47 - Brandon Hancock
But they're just like, hey, write for 30 days straight.

01:06:50 - Brandon Hancock
I did.

01:06:51 - Brandon Hancock
You know, it was cool to get clarity on my thoughts on things.

01:06:55 - Brandon Hancock
But, like, none of it's insanely valuable to other people because, like, people don't.

01:07:00 - Brandon Hancock
to forget to slash And You Like,

01:07:00 - Brandon Hancock
Like, people want to, you know, people want help on their problems, so if you could make something for them and give it to them for free, that's a thousand times more valuable than like, hey, I've been thinking about AI, here's what I think you should think too, like, that's, like, those types of posts just do not get the same traction as, I built something completely for free for you, it took me 10 hours to build this, and you just DM cursor and I'll give it to you for free, like, that right there, a lot of work, they have to type the word free and they get, like, you know, it just takes, so I would definitely try something like that.

01:07:33 - AbdulShakur Abdullah
Question is, what do I build?

01:07:35 - AbdulShakur Abdullah
So I did get some, lot of traction with this one, this post, where I kind of did a story and then linked and gave away the prompt, but I didn't say DM me to get the prompt, I just linked to a long article to get the prompt, so, like a video.

01:07:54 - Brandon Hancock
The trick is, you have to say, drop a comment down below with the word blank and I'll give it to you for free.

01:07:59 - Brandon Hancock
Like, that's.

01:08:00 - Brandon Hancock
That is the cheat code.

01:08:04 - AbdulShakur Abdullah
So yeah.

01:08:04 - AbdulShakur Abdullah
So I just put the prompt in.

01:08:07 - Brandon Hancock
Yeah, literally repurposing that same thing would have – you would have like 10x'd that one post just by saying drop the word blank and I'll shoot you the prompt.

01:08:17 - Brandon Hancock
That one change would have exploded it.

01:08:19 - Brandon Hancock
So if you – Homework for the Week, man, please try that and let me know how many posts you get.

01:08:24 - Brandon Hancock
Can't wait to see it.

01:08:26 - Brandon Hancock
So, all right.

01:08:27 - Brandon Hancock
Perfect.

01:08:28 - Brandon Hancock
All right.

01:08:29 - Brandon Hancock
We're going to keep on cruising.

01:08:31 - Brandon Hancock
Paul, you are up next, man.

01:08:33 - Brandon Hancock
What are we working on?

01:08:36 - Paul Miller
Hey, guys.

01:08:38 - Paul Miller
No, well, it's been – fortunately, I should start with rather than unfortunately, I've been very busy with the sales side for my base SaaS business.

01:08:50 - Paul Miller
I had worked quite a lot to load up a funnel of opportunities and I managed to close everything on the funnel.

01:08:59 - Paul Miller
That's I've never That's insane.

01:09:00 - Paul Miller
I've never had it like that before, and includes our next Australian customer, which is really good because I kind of want to expand into Australia.

01:09:11 - Paul Miller
For those who don't really understand the geographies of the populations, down here in New Zealand is quite a small country.

01:09:19 - Paul Miller
We've got just over 5 million people, but Australia is five or six times larger.

01:09:28 - Paul Miller
It's not a huge population for such a large land mass, but if you've got a business in New Zealand, you really want to be able to sell to the Australian market because it's one common market.

01:09:41 - Paul Miller
With Australia and New Zealand, people go backwards and forwards all the time, but most of the time, the head offices of trans-Tasman companies are in Australia, so getting runs on the board in Australia is fantastic.

01:09:55 - Paul Miller
But it takes me away from the thing I really enjoy doing.

01:10:00 - Paul Miller
Yeah.

01:10:00 - Paul Miller
AI stuff, but I haven't really been able to do the RAG things that much, but I was doing some work this morning with – and I kind of wanted to ask how other people are finding it with the Argentic browsers.

01:10:18 - Paul Miller
So I was using one called GenSpark, which – because I have quite a few retail sites I need to go into, and those retail sites have got all sorts of blocks and bot detectors and all sorts of stuff, and I need to pull data about what's going on with products and prices and promotions.

01:10:42 - Paul Miller
So – Why don't you spell it?

01:10:45 - Brandon Hancock
I'm trying to look it up.

01:10:46 - Paul Miller
Is it – Sorry, I'll – hold on, I'll get the website.

01:10:52 - Paul Miller
GenSparkAI.

01:10:55 - Paul Miller
I'll put it in the chat.

01:10:59 - Brandon Hancock
Okay.

01:10:59 - Brandon Hancock
Okay.

01:10:59 - Brandon Hancock
All right.

01:11:02 - Brandon Hancock
So wait, oh, sorry, I hopped away.

01:11:06 - Brandon Hancock
Oops.

01:11:08 - Brandon Hancock
Trying to share the, trying to share the link so everyone can see it.

01:11:12 - Brandon Hancock
Um, there we go.

01:11:18 - Paul Miller
So it's, yeah, there's a few different people.

01:11:23 - Paul Miller
So you can sort of do prompt-based searching and say things like, from this page, go out and, uh, create a CSV and get all of these outputs out of it.

01:11:37 - Paul Miller
Um, and you probably have to drill down into each of the, uh, each of the lists, uh, down a couple of layers, pull the data, aggregate it back, and then save locally.

01:11:47 - Paul Miller
Um, and look, there's a couple of ways, there's quite a few different products out there that does this kind of stuff.

01:11:55 - Paul Miller
Um, but, uh, uh, yeah, I'd be interested to see

01:12:00 - Paul Miller
See who – if anyone's used that or done some better things.

01:12:05 - Paul Miller
And just on the earlier conversation, I love the idea of the application you're about to do, Brandon.

01:12:12 - Paul Miller
Just as a video suggestion, I know you touched on it very lightly, just do that, do this with the whole lovable thing.

01:12:20 - Paul Miller
There's a lot of people out there that have gone down the lovable path that then want to transition from lovable to, okay, let's do it in cursor.

01:12:30 - Paul Miller
Just a video on – I think it is in the hot spot with what's out there.

01:12:37 - Paul Miller
Add it to your video list.

01:12:39 - Paul Miller
I think that would be a hit.

01:12:40 - Paul Miller
I'd certainly be up for it.

01:12:44 - Brandon Hancock
I need to – I 100% need to do that.

01:12:47 - Brandon Hancock
I was actually working literally today on the prompt to literally called Replicate Lovable.

01:12:55 - Brandon Hancock
Because, like, the thing is, it's like – like, the goal is to, like, build the app that –

01:13:00 - Brandon Hancock
Can create all apps is like, like, it's like, it's like a franchising a business, you know, it's like you want to pick up something that you can just copy and paste a thousand McDonald's.

01:13:08 - Brandon Hancock
In this case, it's like build infinite app ideas.

01:13:11 - Brandon Hancock
So yeah, the second I get this fully flushed out would 100% need to do something like that.

01:13:18 - Brandon Hancock
The kicker is, is you need a template.

01:13:21 - Brandon Hancock
Like that's the problem is like every time I've tried it without a template, without constraints, it does it differently every time.

01:13:29 - Brandon Hancock
So like you almost need to have a template of like, hey, like this is the layout for most modern applications.

01:13:36 - Brandon Hancock
Like take what you see in lovable.

01:13:38 - Brandon Hancock
That's just a quick spin up of a static page and put it into next JS land.

01:13:43 - Brandon Hancock
So that's exactly, the second I get more of this done.

01:13:46 - Brandon Hancock
Um, yeah, I can, I can work on that, but yeah, like this is what a landing page should look like after that.

01:13:52 - Brandon Hancock
Like you need to do these things.

01:13:53 - Brandon Hancock
So I'm, I'm in the middle of working on that.

01:13:55 - Brandon Hancock
Um, but yeah, I mean, I'm happy to share the, the template with, uh, with, I'm not just gonna change.

01:14:00 - Brandon Hancock
I'll it with you guys real fast.

01:14:02 - Brandon Hancock
Well, I don't know how to – I'll drop it as a file.

01:14:05 - Brandon Hancock
How about that?

01:14:06 - Brandon Hancock
I'll drop it as a file in the chat so you guys can have it.

01:14:07 - Brandon Hancock
It's a work in progress, but I'm still working on it.

01:14:11 - Brandon Hancock
But I'll drop that in chat.

01:14:12 - Brandon Hancock
Jake, if you want to go real fast, and then I think – Jake, Robert, and then I think Bastian had some cool things he wanted to share real fast on evals.

01:14:20 - Jake
Yeah, I was just going to say, the template thing is a really interesting thing.

01:14:25 - Jake
If you know of a template library, like Replit was, like, unusable code, and now I hear people are using it, and they're actually – because it does all these little tech stacks.

01:14:38 - Jake
Oh, so, like, when you want to build something, it just kind of reconfigures and then builds a tech stack around basically the most popular tech stack.

01:14:49 - Jake
But in general, people are pretty happy with it.

01:14:51 - Jake
And so, the template thing starts to make a lot of sense.

01:14:55 - Jake
So, I don't know.

01:14:57 - Jake
I keep thinking, like, you know –

01:15:00 - Jake
Um, Tailwind, right?

01:15:02 - Jake
Tailwind is all templates.

01:15:03 - Jake
And so, if you, if you have, like, a tech stack template, um, and there's a Y Combinator that's actually doing quite well, a couple of them, where it's, like, DataButton.

01:15:16 - Brandon Hancock
No, I haven't, I haven't heard of that one.

01:15:18 - Brandon Hancock
Um.

01:15:19 - Jake
It's kind of the same concept.

01:15:21 - Jake
It's, like, basically, they have a tech stack.

01:15:24 - Jake
They basically have finished projects, um, where you can change, yeah, this is it.

01:15:29 - Jake
Oh, so, if you go to templates, you can kind of see how it all works.

01:15:35 - Jake
You just basically, so these are the templates, right?

01:15:38 - Jake
So it's got Firebase, Next.js, Stripe, Python.

01:15:44 - Brandon Hancock
No, I mean, that, that makes total sense.

01:15:47 - Jake
Um.

01:15:48 - Jake
But I, I think there's something there, um, where if you can identify, like, a template library, I think there could be something really interesting, where, where you could actually make a lovable that.

01:16:00 - Jake
Actually, I mean, you're saying essentially making a replet at that point.

01:16:03 - Brandon Hancock
I mean, truthfully, like, the goal with Ship's Fast, that is, like, it, like, a template for a RAG app, a chat app, an agentic app, a Cray AI agentic app, ADK, like, that's the goal, just to make, like, a hundred templates in there, so anytime you want to spin up a project, there's just something there for you guys, so that's the, that's the long-term vision for it, so it's, but, just because, like, I think everyone's coming to the same conclusion, like, AI, once it has context on something, it's phenomenal at tweaking and adjusting, but it just needs some initial constraints of, like, okay, I see what you're trying to do here, because it doesn't need to, like, oh, you want to add chat to your AI application?

01:16:44 - Brandon Hancock
Well, how do you want to do this?

01:16:46 - Brandon Hancock
Like, you the answer is, like, it's a Vercel AI SDK, that's what we're using, we are supporting multimodal, so, like, it already has, like, like, it just needs a template, and then it can just crank out from there.

01:16:57 - Brandon Hancock
So, that's the, that's the, kind of the goal, so, yeah.

01:17:00 - Brandon Hancock
I'm happy to share, and I did just drop that lovable thing, if you want to steal that, too, to help, like, work in progress, but so far, it is kind of working.

01:17:11 - Brandon Hancock
I'll share an updated one once it's finished.

01:17:15 - Brandon Hancock
Robert, if you want to go real fast, and then, Paul, I do want to come back to your data browsing question, too.

01:17:19 - Robert
I feel like we left you hanging.

01:17:21 - Robert
Okay, super quick.

01:17:23 - Robert
The feature that Paul showed us, why was it referred to as an agentic browser?

01:17:28 - Robert
It's very similar to the AI Studio interface, so I was just curious about why that was referred to as an agentic browser.

01:17:41 - Paul Miller
It was more because you could prompt your way through the questions and interactions on the page, rather than just giving a script to say, go into that page, pull this data, do these steps.

01:18:00 - Paul Miller
to two characters.

01:18:00 - Paul Miller
Off

01:18:00 - Paul Miller
like with the with the with the code that does that kind of thing.

01:18:04 - Paul Miller
Hold on, there's a postcode being said, yeah, because there's a number of ways you can go to Chromium and generate a script, but the problem is you've got to react with what's actually on the page, and this is where there's sort of agent tech, because OpenAI have got their tool operator, but you've got to be in the pro plan to use that, so it's that kind of thing that is the one that I was looking for.

01:18:34 - Brandon Hancock
So, um, a few, a few things, Paul, so I actually tried to create a browser agent video for you guys, and I just kept hitting my head against the wall to get anything to work reliably, so I, so I just dropped, like, I watched the agent development kit team, they created a browser agent, and it works for your first three prompts, it works asterix, like not a hundred percent in the main

01:19:00 - Brandon Hancock
The main reason why is context.

01:19:01 - Brandon Hancock
So, once you take a website, what they're doing is like, cool, grab the entire content of the website, grab the first 10,000 characters, throw it over to the agent, and let the agent look through it and pick the right element.

01:19:16 - Brandon Hancock
That breaks so fast if you're working on like a big page.

01:19:20 - Brandon Hancock
What I was trying to do is make like a school management browser agent that would like read through comments and just help me answer community questions better.

01:19:27 - Brandon Hancock
But it doesn't work because it was like after the third call, it's like it blew up the context window.

01:19:33 - Brandon Hancock
So, like, that was main problem one.

01:19:37 - Brandon Hancock
So, and then a workaround is to make your own like Firebase equivalent, Firecrawl equivalent to where you like convert the raw HTML to the information the agent needs.

01:19:49 - Brandon Hancock
I got it to work a little bit, but it still wasn't good enough.

01:19:53 - Brandon Hancock
So, I was like, man, this is just becoming too complex.

01:19:56 - Brandon Hancock
Like, I understand why now there's so many like multi-million dollar startups.

01:20:00 - Brandon Hancock
I was trying to tackle this problem because I was like, oh, I'll just – give me an afternoon.

01:20:03 - Brandon Hancock
I'll recreate Firecrawl.

01:20:04 - Brandon Hancock
How hard can it be?

01:20:06 - Brandon Hancock
And I quickly – I got overconfident.

01:20:08 - Brandon Hancock
So I gave up.

01:20:10 - Brandon Hancock
So, yeah.

01:20:12 - Brandon Hancock
And just two other points really fast.

01:20:15 - Brandon Hancock
I did try browser-based and browser-less.

01:20:20 - Brandon Hancock
And, I mean, the root issue at the end of the day is still the agent that's making the call to click around.

01:20:25 - Brandon Hancock
If the website is not perfectly clear on, like, hey, this button does this, this button does this, I was just having trouble.

01:20:34 - Brandon Hancock
Like, for school, for example, like, please find the latest comment, click it, let me know what they're saying.

01:20:42 - Brandon Hancock
And, like, that's – like, I would just try and do a core loop like that.

01:20:45 - Brandon Hancock
And the second you had a comment popping up in a modal and it just became more than a static website, it just crapped the bed and I couldn't get it to work.

01:20:53 - Brandon Hancock
So, that was my quick experience with browser-based and browser-less and my own custom solution.

01:20:58 - Brandon Hancock
But if any of you guys do find any –

01:21:00 - Brandon Hancock
Any, like, agentic browser tools that are, like, competent, please let me know, because I've been looking hard for one, because that is insanely powerful when it does work.

01:21:09 - Brandon Hancock
Like an operator, you know, exactly what you're calling out.

01:21:13 - Brandon Hancock
If there's – second you see an open source tool that I can use, or paid, just let me know, because I won't use it.

01:21:18 - AbdulShakur Abdullah
Have you seen the new Perplexity Labs?

01:21:22 - AbdulShakur Abdullah
Have you tried that one?

01:21:24 - Brandon Hancock
Let me pull it up.

01:21:27 - Brandon Hancock
Perplexity Labs.

01:21:32 - Brandon Hancock
Has anyone tried it?

01:21:34 - AbdulShakur Abdullah
Has anyone tried that one?

01:21:39 - Brandon Hancock
Am I looking at the thing?

01:21:40 - AbdulShakur Abdullah
Yeah.

01:21:41 - Paul Miller
The normal Perplexity search, it's one of the options on the search.

01:21:45 - AbdulShakur Abdullah
If you have the paid version, it basically will run Perplexity like an agent, so – but you have to have the 20 bucks a month version.

01:21:59 - AbdulShakur Abdullah
Oh.

01:22:00 - AbdulShakur Abdullah
I'm on the fence about trying it, but I get it sucked in too easily.

01:22:07 - AbdulShakur Abdullah
So I was seeing if anyone else already went down that rabbit hole and could tell me if it worked.

01:22:13 - Brandon Hancock
No, I haven't got to go down that one.

01:22:17 - Brandon Hancock
But yeah, I mean, if you do try it, hey, we would love your $20 contribution for the collective of the group.

01:22:22 - AbdulShakur Abdullah
So, you know, it's for a good cause, man.

01:22:29 - Brandon Hancock
So think, Paul, I think we answered all those questions.

01:22:33 - Brandon Hancock
The one up, Bastian did just drop a cool, a second ago, a cool comment on eval.

01:22:39 - Brandon Hancock
I do think it's a really important conversation.

01:22:42 - Brandon Hancock
If you want to, Bastian, kind of recap what you were saying on those talks, and then, Andrew, hopefully, it'll add more context to what you were asking.

01:22:50 - Bastian Venegas
Okay.

01:22:50 - Bastian Venegas
There are two links in the chat, and they are both from the playlist that Brandon suggested by Langchain in

01:23:00 - Bastian Venegas
Interrupt, and one is from Andre Eng, where in the second half of the talk, he discusses, like, in a general way, how they do evals, but basically the main advice is just planning early for evals and through the different parts of the development cycle so that you have sort of an initial approach where you do the human evals, and you can also use an LLM as a judge, but after that you need to plan how you will continue to evolve that with random user data, mean, like, obviously anonymized, but you need to, like, get some insights on how the site is actually working for users.

01:23:44 - Bastian Venegas
So that leads to a lot of wasted time, and that's basically what he was suggesting.

01:23:49 - Bastian Venegas
And in the other video, it goes into more specific details because that's the topic of that talk.

01:23:57 - Bastian Venegas
And really quick, regarding the uh, browse

01:24:00 - Bastian Venegas
Sir agents, a technique that Manus AI uses for this is that they initially do a visual assessment of the website, and they overlay this CSS that basically delimits every component of the website, so every button, every form, and all of that, and that helps the agent use its internal vision to inform the next steps, and that shows So it's subtle, but if you see a video from Manus, you will see that they do this for every website.

01:24:37 - Brandon Hancock
I mean, that makes total sense, because I think, like, the raw approach, it's so confusing to the model of, like, what do I actually click?

01:24:43 - Brandon Hancock
Because when you're, like, click that, or click comment, there's 200 comments, which one do you want?

01:24:49 - Brandon Hancock
So if they were just, like, oh, there's just, the main thing is, like, let's bring the context window from this to, like, oh, there's really 10 things you should be clicking on this page, rather than a thousand lines of HTML.

01:24:58 - Brandon Hancock
So, no, that's very cool.

01:25:00 - Brandon Hancock
I'd very curious to see what their costs were for that, just because, like, you're having to use a vision model, vision model to structured output.

01:25:05 - Brandon Hancock
Like, there's a lot more to that.

01:25:06 - Brandon Hancock
So I'd be curious what their costs were for that.

01:25:09 - Brandon Hancock
That's a very cool point.

01:25:10 - Bastian Venegas
the is, it's obviously more costly, but that using the vision capabilities that basically let them, allow them to go one level deeper to the site understanding and scraping.

01:25:25 - Bastian Venegas
So it does work for them, at least.

01:25:28 - Brandon Hancock
Yeah, that's insane to know.

01:25:30 - Brandon Hancock
Yeah, that's very cool.

01:25:32 - Brandon Hancock
Okay, we'll keep on cruising.

01:25:34 - Brandon Hancock
I think Sam was up if he's still on call.

01:25:39 - Brandon Hancock
If not, yeah, if not, I think it's out.

01:25:47 - Al Cole
Okay.

01:25:48 - Brandon Hancock
How's it going?

01:25:49 - Al Cole
It's going well.

01:25:51 - Al Cole
It's going really well.

01:25:52 - Al Cole
And I want this group to know, really appreciate the exchange and collaboration here.

01:25:56 - Al Cole
I am always learning.

01:25:58 - Al Cole
It's been great.

01:25:59 - Al Cole
On my journey...

01:26:00 - Al Cole
On journey...

01:26:00 - Al Cole
I am still kind of – the way to think about my involvement so far has been kind of assessing where the tech stacks are, where the vendors are, and adopting similar tech stacks, and where there could potentially be opportunities from a business perspective.

01:26:19 - Al Cole
So it isn't, for me, pure tech at this point.

01:26:22 - Al Cole
It's also assessing kind of the industry out there.

01:26:26 - Al Cole
One thing I will say, last week I mentioned looking for tools that guide me in prompt building.

01:26:33 - Al Cole
I have a paid subscription to chat GPT, so they had a dedicated applet for prompt engineering, which turned out to be helpful.

01:26:42 - Al Cole
It essentially structures questions to guide me on how to start the prompt, and then it ends up generating useful prompts that I, in turn, took over.

01:26:54 - Al Cole
I last week I was asking about evaluations and prompt management, and I got to Langsmith, and it was

01:27:00 - Al Cole
It was really driven by all the examples I saw at the Interrupt Conference.

01:27:05 - Al Cole
So I'm wondering, and I was looking for feedback from this group, does anyone have any bad experiences adopting Langchain, LangGraph, now even LangSmith as part of your stacks as you're going after some of these use cases?

01:27:24 - Al Cole
I was really impressed by what I saw.

01:27:26 - Al Cole
I don't know if what I saw were cleaned up marketing pitches, but it felt like they were pretty real by a bunch of enterprise customers, and so that appealed to me.

01:27:37 - Al Cole
I was curious, I know we've talked about ADK out there, I know we've talked about Crew.AI out there, probably several others.

01:27:45 - Al Cole
Is there anything about Langchain that challenged people in the past?

01:27:51 - Brandon Hancock
So I'll go super fast.

01:27:53 - Brandon Hancock
So actually, my best video ever is on Langchain.

01:27:59 - Brandon Hancock
And...

01:28:00 - Brandon Hancock
Long story short, after working with every part of LangChain – so this was back in version 2, so this was almost a year ago at this point – the main things that I found valuable were the fact that you could create React agents and their rag and chunking functionality.

01:28:17 - Brandon Hancock
That was the main valuable pieces from the LangChain framework.

01:28:23 - Brandon Hancock
And outside of that, when it actually came to just using everything else inside of LangChain, I was like, I came away with the approach of like, I should just make a direct LLM call, and then go to the next statement.

01:28:35 - Brandon Hancock
And then over and over again, so I was like, a lot of this seemed to be overkill.

01:28:40 - Brandon Hancock
Fast forward, LangGraph came out, and you know, this is where you start to get to use more agents, cycles, like, they just went a lot deeper.

01:28:51 - Brandon Hancock
At first, I was like, man, this is so much work, building a graph, managing state.

01:28:58 - Brandon Hancock
Like, there was just a lot of Like, there lot work, a a graph,

01:29:00 - Brandon Hancock
Or more simple projects, and I was like, man, once again, I could just do an LLM call and a while loop if I need to do half the stuff they're doing in LandGraph, but same as you, seeing this conference, I'm like, I need to revisit it to make sure my old biases are not still valid, because what they were showing was truly amazing with how far it's come.

01:29:26 - Brandon Hancock
So I want to revisit it, but yeah, it does what it does very well, but I just have not touched on LandGraph in a minute, and I need to, so that's on me.

01:29:36 - Al Cole
What about anyone else in the group?

01:29:37 - Al Cole
Well, behalf of the team, I think I'll probably lean in here, I found a good book for the ecosystem that they have.

01:29:44 - Al Cole
So I'll share what I'm learning as I start building, and if I had any roadblocks, I know I've got ADK and other alternatives, but I'm curious to see how far I can get with the tooling based on what I saw.

01:29:57 - Al Cole
For the teams, I have also been scouting.

01:30:01 - Al Cole
So with respect to Postgres and where it is in the AI evolution, I don't know if anyone's done work with Timescale, but their PGAI extension's pretty powerful, and I sat through a webinar, they kind of walked through it.

01:30:16 - Al Cole
Effectively, what they're doing, and this is a strategy now of both EDB, which is a Postgres company, and Timescale, which is also a Postgres company, is they're trying to bring the AI to the data.

01:30:30 - Al Cole
What they're trying to do is build into the database the capabilities to, in the case of a RAG use case, to automate the hosting of the models, the actual generating of the embeddings, and allowing you to query all from within SQL and within the database proper itself.

01:30:52 - Al Cole
So I'm not sure that I love all of that, because what I do, like the ADK taught me, the ability to have

01:31:00 - Al Cole
those callbacks and to be part of those flows, which you wouldn't really be able to if you're just firing the SQL statements.

01:31:06 - Al Cole
But I did see some simplicity in, you know, the model hosting and everything else to kind of simplify the stacks that these enterprise customers might need to work with.

01:31:19 - Al Cole
And where I'm heading here, team, is I'm trying to figure out, and I think I shared this before, in terms of business models in the past that have worked well for me is being tied to partner programs.

01:31:30 - Al Cole
because you get access to customers who are already committed to the platform, and they're looking for a little ingenuity that is added to what these larger vendors are supporting.

01:31:43 - Al Cole
So that's the reason I checked out EDB, which has got more than a quarter of the committers for Postgres.

01:31:50 - Al Cole
And they've, course, got an enterprise platform.

01:31:53 - Al Cole
They're all in on AI now.

01:31:55 - Al Cole
They kind of walk through today their architecture.

01:32:00 - Al Cole
um

01:32:00 - Al Cole
It looked pretty cool, what they had.

01:32:02 - Al Cole
This is an example of some of the SQL statements, but effectively what you're looking at here is they're essentially pointing to documents in an S3, and they're able to drive the embeddings through SQL, they're able to drive the queries through SQL, and so you've kind of centralized a lot of the mechanics that we deal with, all being managed within the actual SQL database itself.

01:32:24 - Al Cole
And so my interests were, like, they did some tooling, they have the ability to reach out to Zendesk and tie it into what they're doing with the RAD use case, and, you know, they just quickly showed how they could spin up a support agent and get at all the support tickets that they had within Postgres itself.

01:32:45 - Al Cole
So I'm paying attention to this as a possible ecosystem for me to sell into in the long term, and that's why...

01:32:55 - Al Cole
I'm paying, I'm looking at these kinds of opportunities is where the bigger vendors are, if that makes sense to...

01:33:00 - Al Cole
The team.

01:33:01 - Brandon Hancock
No, totally makes sense.

01:33:02 - Brandon Hancock
So I just, I went to, going back to the technology, and I want to go to like the trusted implementer side of things.

01:33:08 - Brandon Hancock
So the main thing, my understanding going back, that slide, I think it was that the one you're about to click, the screenshot, right here?

01:33:17 - Brandon Hancock
Yeah, mm-hmm.

01:33:19 - Brandon Hancock
So in a short summary, the main, what was the main benefit of using just like their version of, you know, vectorizing?

01:33:30 - Al Cole
So the main benefit, yeah, the main benefit was, you define your table, and they have extensions which allow you to identify in the schema where your embeddings are.

01:33:41 - Al Cole
Now they did it in a very clever way.

01:33:43 - Al Cole
Their strategy is, they don't want you to actually have to touch your application code.

01:33:46 - Al Cole
So what they end up doing is, when you declare you want embeddings, they create a shadow table, and then they create a view that unifies it.

01:33:56 - Al Cole
And what that allows you to do is to really stay within SQL.

01:34:00 - Al Cole
And within the database itself, to do quite a bit of your RAG use case, and I think that's their intent.

01:34:07 - Al Cole
Their intent is to simplify your stack.

01:34:10 - Al Cole
What they're trying to do is, one, keep your model and your logic close to your data, and two, keep your stack simple, and they emphasize the fact that data governance, we can lock all this down with permission models you're already comfortable with, so we can ensure the data doesn't go anywhere, it shouldn't go, if that also makes sense.

01:34:34 - Brandon Hancock
It totally does.

01:34:36 - Brandon Hancock
So, because, like, my head right now, just when I think RAG, I'm in Postgres land, and I'm using their, you know, I'm using their tools for creating embeddings.

01:34:45 - Brandon Hancock
I was going to pull up just so people can see what it actually looks like in, like, tech lands.

01:34:52 - Brandon Hancock
Let me pull this up.

01:34:54 - Brandon Hancock
Okay, and, and a little, and a little bit.

01:34:57 - Brandon Hancock
bit.

01:34:57 - Brandon Hancock
bit.

01:34:57 - Brandon Hancock
bit.

01:34:57 - Brandon Hancock
All right, let me share.

01:34:59 - Brandon Hancock
Just because I'm just, I'm.

01:35:00 - Brandon Hancock
I'm trying to wrap my head around what they're doing because this is what typical RAG looks like, at least for document-based RAG.

01:35:11 - Brandon Hancock
There's a difference between text-based RAG to where if you have regular just SQL data or you have a regular text field with a tweet or something, that's super easy because you're not having to do the document processing.

01:35:26 - Brandon Hancock
So, you know, that is easier, but this is what actual RAG looks like, where, you know, like artifact ID, yeah, with chunking.

01:35:36 - Brandon Hancock
you have section content of the chunk, you embed it, that's where you get the, you know, the huge vector, and then any metadata that you want to link.

01:35:45 - Brandon Hancock
So this is what typical vector, like creating a vector store looks like in Postgres.

01:35:51 - Brandon Hancock
I would be curious to see what the main difference is compared to what Supabase is doing.

01:35:59 - Brandon Hancock
That would just be like my main

01:36:01 - Brandon Hancock
I'm still – I have, a question mark on that.

01:36:03 - Al Cole
Yeah, 100%.

01:36:04 - Al Cole
And I'm not sure, like I mentioned, especially with agents, I'm not sure all this makes sense to be run within a database itself because I do think there's a place for the logic.

01:36:13 - Al Cole
But part of what EDB is trying to do is they're trying to create an agent factory, right?

01:36:17 - Al Cole
They're trying to create an ecosystem where developers can come in, create add-on agents that ultimately get included in the enterprise side.

01:36:26 - Al Cole
And for me, for the team, enterprise customers have got pretty healthy budgets.

01:36:32 - Al Cole
And if you can get access to them, you can get projects that go substantially larger than you might otherwise.

01:36:39 - Al Cole
So this is just me kind of doing some research into possible business models is really what I'm looking at.

01:36:46 - Brandon Hancock
Yeah.

01:36:48 - Brandon Hancock
David, do want to double down on what you're saying on, like, A, solve race people problems?

01:36:52 - Brandon Hancock
Like, that's the best kind there's a potential client you're going to get to work with.

01:36:57 - Brandon Hancock
And I'm shooting myself in the foot for not, like, charging me.

01:37:00 - Brandon Hancock
I didn't fully understand how much they had, and how much value it could bring, I'm like, damn, I think I just sold myself 50% short, so I haven't committed to anything yet, so I gotta figure out how I can, uh-oh, I didn't fully understand, it's twice, it's twice what I originally said, but to your point, it is a rag-based project, so I just, like, the reason I'm so curious on what you're building is because, like, out of pretty much all freelance projects that have come my way, 90% have been rag-based, like, that is actually the most monetizable skill stack so far I'm seeing with AI, because it's like, there's an insane amount of knowledge, I need to take action on that knowledge with the help of AI, so just, like, if you're looking for where to get started with, like, a skill that could be, um, you could start charging for as quickly as possible, it is rag-based, so I'm always on the lookout for, like, better ways to, um, to potentially do it, but right now, Supabase is my current go-to stack.

01:37:57 - Al Cole
And I'm not suggesting a change, but what I'm trying-

01:38:00 - Al Cole
What do is just understand these big vendors have to be riding this wave.

01:38:03 - Al Cole
They've got to look for ways to add value with all these AI capabilities.

01:38:07 - Al Cole
It makes sense that the databases are now trying to bring, essentially, the AI into the actual platform, right?

01:38:16 - Al Cole
No, totally makes sense.

01:38:16 - Al Cole
But they're going to need developers.

01:38:18 - Al Cole
And developers, if you're part of their partner program, you now potentially have access to some very strongly positioned enterprises that can easily fund small consulting shops.

01:38:33 - Brandon Hancock
100%.

01:38:35 - Brandon Hancock
I absolutely love what you're saying.

01:38:38 - Brandon Hancock
The term I've heard recently, Nicholas Cole, he talked about something similar.

01:38:44 - Brandon Hancock
And it's basically like finding the faucet.

01:38:47 - Brandon Hancock
It's basically just like, where's the water coming from?

01:38:51 - Brandon Hancock
Instead of looking for little puddles all over the ground with random customers, just go find the faucet to where the water's coming from in the first place.

01:38:58 - Brandon Hancock
And that's the literally just what-

01:39:00 - Brandon Hancock
Exactly what you're saying is, I think, a more concrete version of, like, no, just the big boys, they need help.

01:39:06 - Al Cole
And every company has got a help desk.

01:39:08 - Al Cole
Every single one of them has a help desk.

01:39:10 - Al Cole
And just some of what I've heard this team talk about, you probably could get an agent in there with access to a source and kind of drive a solid chatbot based on either structured data or something you can reach externally.

01:39:25 - Al Cole
So, anyways, that's my contribution this week.

01:39:28 - Al Cole
I look forward to rolling up my sleeves and starting some coding work in the coming week and sharing more.

01:39:34 - Brandon Hancock
No, that's awesome.

01:39:35 - Brandon Hancock
And, yeah, please keep me posted on your LangGraph, LangSmith, LangFuse, all the Langs.

01:39:42 - Brandon Hancock
Keep me posted on that journey just because, like, I kind of got the LangGraph.

01:39:47 - Brandon Hancock
I was like, huh, I need to explore a little bit more.

01:39:50 - Marc Juretus
It was better.

01:39:52 - Marc Juretus
It was better.

01:39:53 - Marc Juretus
We did it for a couple of months.

01:39:55 - Marc Juretus
And it's just, you have to do so many steps to get there.

01:39:59 - Marc Juretus
Because I remember when we did

01:40:00 - Marc Juretus
The crew, I'll make it brief, the guys were like, why didn't we just learn crew in the first place?

01:40:05 - Marc Juretus
It was just funny, the chat was like five of them in a row, because you had – because we were doing the thing where you pull on a YouTube video, and then you rewrite it.

01:40:13 - Marc Juretus
That's what we did in Langchain, and it's so much easier at crew.

01:40:18 - Marc Juretus
Yeah, yeah.

01:40:19 - Brandon Hancock
So, yeah, I'm just – Al, as you go off, you know, they're making changes constantly to Langrath to improve it.

01:40:26 - Brandon Hancock
So, yeah, please, like I said, I'm very curious to hear about your journey.

01:40:30 - Brandon Hancock
So, Alex, I saw you had your hand up, and then I want to answer Mitch and Bastion.

01:40:35 - Alex
Brandon, just a quick question.

01:40:37 - Alex
If you don't mind sharing, what is the pain point of the RAG projects that you have sold?

01:40:43 - Alex
What is the pain point that you're solving with those RAG applications?

01:40:49 - Brandon Hancock
Yeah, so first one, you know, the one for the Fire Chief.

01:40:54 - Brandon Hancock
The short answer is they have to fill out documents every time they go to handle an emergency response.

01:41:00 - Brandon Hancock
What's What's

01:41:00 - Brandon Hancock
They have to do it in a particular format called SOAP, which is like, what was the situation?

01:41:05 - Brandon Hancock
What was the plan?

01:41:07 - Brandon Hancock
There's so many things I have to fill up.

01:41:09 - Brandon Hancock
So in the past, you know, they would have to like, shoot, what did I do earlier today?

01:41:13 - Brandon Hancock
Okay, so I walked in, lady unconscious, her face was like half not there or whatever, from like a stroke.

01:41:20 - Brandon Hancock
And they have to like recall everything they did.

01:41:22 - Brandon Hancock
They have to manually type it out, the vital.

01:41:24 - Brandon Hancock
They have to do so much work.

01:41:26 - Brandon Hancock
Okay.

01:41:27 - Brandon Hancock
Then after that, they're, you know, in their head, they're, what they remember is like, we showed up to the scene, we gave her an ibuprofen, we checked her vitals, here's what it was.

01:41:35 - Brandon Hancock
So like, they just have like a bullet point, like that's the memory.

01:41:38 - Brandon Hancock
Okay.

01:41:38 - Brandon Hancock
Well, part two of that is whenever they go to submit this document, they have to hit certain codes or certain things in order to like properly bill.

01:41:48 - Brandon Hancock
So long story short, what the RAG agent would do is it would take in the person's like brain dump of like what happened.

01:41:56 - Brandon Hancock
It would understand the format it was trying to do.

01:41:59 - Brandon Hancock
based on all the keywords that

01:42:00 - Brandon Hancock
They said it would make a RAG request to two different data stores.

01:42:04 - Brandon Hancock
One was to say, oh, you gave ibuprofen to a person with a stroke?

01:42:08 - Brandon Hancock
Well, looking at emergency medical procedures, it looks like – you know, I'm also butchering this – but, like, it looks like it's this dosage is probably what you gave her.

01:42:16 - Brandon Hancock
So by giving – looking at dosages and procedures, it could make their documents way more prescriptive so that the billing, like, insurance could go, oh, yeah, you gave ibuprofen, you administered this procedure.

01:42:29 - Brandon Hancock
Like, we now know why we need to cover this charge.

01:42:32 - Brandon Hancock
So it's looking at both sources.

01:42:34 - Brandon Hancock
So really just – they can now put a bullet point list in that takes 10 seconds just talking to the computer and it generates an entire report, which, you know, usually takes 30 minutes to write.

01:42:44 - Brandon Hancock
So literally two minutes instead of 30.

01:42:47 - Brandon Hancock
Second one is more just ideation.

01:42:50 - Brandon Hancock
So people just want to browse large sums of data.

01:42:54 - Brandon Hancock
Like, so imagine – it's almost like having your own internal Google at this point.

01:42:59 - Brandon Hancock
Though some people actually don't just want to get

01:43:00 - Brandon Hancock
They answer back immediately.

01:43:01 - Brandon Hancock
They're like, hey, I have a log repository from every creator I can think of.

01:43:06 - Brandon Hancock
I have 300,000 blogs.

01:43:08 - Brandon Hancock
I'm trying to now go off and put together my own small report on the best practices for, you know, starting, you know, raising a seed round for a company.

01:43:22 - Brandon Hancock
Well, what they want to do actually is not just get back the first three results.

01:43:26 - Brandon Hancock
They want to look at every blog ever that touched on that topic and almost like scroll through their own little search engine.

01:43:33 - Brandon Hancock
So, yeah, so those are the two main cases I've seen very, very recently.

01:43:37 - Brandon Hancock
So hopefully that's helpful.

01:43:40 - Brandon Hancock
So yeah, RAG for the win on both of those, VectorStores specifically.

01:43:45 - Brandon Hancock
So, okay, I think, so real fast, going back to Mitch's question, then Bastion's.

01:43:52 - Brandon Hancock
So, Mitch, for the Dan guy, he noticed that RAG apps were the main bread and butter as well.

01:43:57 - Brandon Hancock
I haven't officially got to hear him say specifically which one.

01:44:00 - Brandon Hancock
He was using and why.

01:44:01 - Brandon Hancock
Hey, good question to ask when he hops on the call.

01:44:07 - Brandon Hancock
But, I mean, it makes sense because, like, you just give people the power to do things that they normally couldn't.

01:44:11 - Brandon Hancock
It totally makes sense why it is one of the main ones, if that's true.

01:44:16 - Brandon Hancock
And then, Bastion, real fast, have you gotten to try out Convac so far?

01:44:21 - Brandon Hancock
I've been eyeing them, but I have not used them specifically because of RAG.

01:44:29 - Brandon Hancock
I did not think they fully supported it yet.

01:44:32 - Bastian Venegas
Yeah, from their docs, they do support it, but for brief context, context is a database, but it's also kind of an NPM package, and you can also self-host it.

01:44:44 - Bastian Venegas
They seem to use SQL under the hood, but if you use them, you don't need an ORM because you just write regular TypeScript, and they wrote their database thing in Rust, so it's supposed to be really...

01:45:01 - Bastian Venegas
The updates for the UI, once the database changes, it's supposed to be much more straightforward.

01:45:09 - Bastian Venegas
Actually, I don't have any personal experience with Convex, but I have been following Theo's T3 chat development, and he actually migrated to Convex everything, and they had very good results in the end, and a lot of support from the Convex team.

01:45:30 - Bastian Venegas
Like, really hands-on.

01:45:32 - Bastian Venegas
So that's why I've been meaning to try it, but not personal experience with it.

01:45:36 - Brandon Hancock
If you get to try it, specifically with the RAG functionality, I think I would 100% look at potentially switching.

01:45:43 - Brandon Hancock
It's just like, in my head, I have, like, a checklist for an AI stack.

01:45:47 - Brandon Hancock
It's like, I need to be able to do the chat functionality, and then from there, I need some way to save all my messages, and then I also, just with most modern AI applications, you probably do want to do what right.

01:46:01 - Brandon Hancock
And that's literally the main reason I have not gone down Convex yet is because I'm not only – when it comes to setting up the VectorStore, like, I understand if I automatically, like, have a text table, it might create the embedding, but the ability for me to actually, like, insert my own when I'm working with documents, I didn't know if it's capable of that, so that's literally the reason I've stayed away.

01:46:26 - Brandon Hancock
However, if it is, and you get to play with it, please let me know, because I think I would potentially make the jump, because I'm watching all of Theo's videos too, and he makes it sound like it's amazing, and it's solving all the problems for his T3 chat application, so I'm like, man, I really want to check it out, but it's just not checking all the blocks from what I'm seeing to be one universal tool.

01:46:47 - Brandon Hancock
It seems great for chat and regular databases, but the second you need more than that, I don't know if it does it.

01:46:52 - Brandon Hancock
That's why I held back.

01:46:54 - Brandon Hancock
So, yeah, let me know what you find out, because, yeah, they have very cool tools as well.

01:47:00 - Brandon Hancock
Like, they're...

01:47:00 - Brandon Hancock
Convex App Builder, AI Builder, is also really cool, so they have a lot.

01:47:07 - Brandon Hancock
Okay, perfect.

01:47:09 - Brandon Hancock
All right, so I think that was let me pull up the call order.

01:47:14 - Brandon Hancock
I think that was gone through the call order, so now we're just going to go – based on screenshots, I'm going to do this really fast.

01:47:25 - Brandon Hancock
I'm going to drop a new chat.

01:47:27 - Brandon Hancock
Let's see this.

01:47:28 - Brandon Hancock
So here's the new order, and thank you guys for being patient.

01:47:32 - Brandon Hancock
It's the good and bad part about community growing is that more people takes more time, but so many awesome conversations.

01:47:39 - Brandon Hancock
So, Alex, you're up next, man.

01:47:43 - Brandon Hancock
Alexander, sorry.

01:47:46 - Aleksandr
Hello.

01:47:48 - Aleksandr
I want to be very fast today because I just did a connection with my railway, my telegram bot, now it's working 24 hours.

01:48:00 - Aleksandr
And I think that I solved this problem because I tried different ways.

01:48:07 - Aleksandr
I tried to copy different versions from cookies.

01:48:13 - Aleksandr
And the best version was Netscape.

01:48:18 - Aleksandr
Maybe it will be useful for you.

01:48:23 - Aleksandr
Yes.

01:48:24 - Aleksandr
For Telegram, I read in GPT and in Internet, in some sites, that Netscape is the best way to copy Netscape Formate from YouTube because JSON works only in some ways, not in all ways.

01:48:50 - Aleksandr
Yes.

01:48:51 - Aleksandr
And now I just write some new function.

01:49:00 - Aleksandr
with two download YouTube videos and download YouTube audio, and now it works very good, I think.

01:49:07 - Aleksandr
It's a little progress for me.

01:49:09 - Brandon Hancock
Okay, that's awesome, man.

01:49:11 - Brandon Hancock
That's awesome.

01:49:11 - Brandon Hancock
Yeah, I know last time we got to see a demo, so that's awesome that you're still cranking out progress on it.

01:49:19 - Brandon Hancock
And did you say Netscape, like the OG internet browser?

01:49:24 - Aleksandr
In Chrome, with cookie editor, and edit this cookie.

01:49:32 - Aleksandr
I use two different options.

01:49:37 - Brandon Hancock
Okay.

01:49:38 - Brandon Hancock
Yeah, I just, I literally have not heard the word Netscape in like a very, like very long time, so that's why I was, I was just curious, you know, if that's what you're, if that's what you're using.

01:49:49 - Brandon Hancock
So, very cool.

01:49:51 - Brandon Hancock
Anything we can help with?

01:49:53 - Brandon Hancock
Want to make sure you keep cranking out the progress.

01:49:55 - Aleksandr
No, I think I want only to say that I make a little progress.

01:50:00 - Brandon Hancock
In this project.

01:50:01 - Brandon Hancock
Yeah.

01:50:02 - Brandon Hancock
That's awesome, man.

01:50:02 - Brandon Hancock
Well, hey, please keep crushing it.

01:50:05 - Brandon Hancock
And yeah, I know you're still making a ton of progress.

01:50:07 - Brandon Hancock
So next week, if you have some more cool features, we'd love to show.

01:50:10 - Aleksandr
I would love to see what you're working on.

01:50:13 - Aleksandr
Yeah.

01:50:13 - Aleksandr
Thank you.

01:50:15 - Brandon Hancock
All right.

01:50:15 - Brandon Hancock
Perfect.

01:50:16 - Brandon Hancock
Okay.

01:50:17 - Brandon Hancock
Well, keep on cruising.

01:50:19 - Brandon Hancock
AK, my man, my Florida man.

01:50:22 - Brandon Hancock
What's going on?

01:50:24 - The Dharma House
Florida for sure.

01:50:25 - The Dharma House
How's it going, guys?

01:50:27 - Brandon Hancock
Good day.

01:50:27 - The Dharma House
It's been a couple of weeks since I've been on.

01:50:31 - The Dharma House
But I've made some progress on the grant proposal MVP.

01:50:37 - The Dharma House
I was chartered to create just a POC and I'll show it to you.

01:50:45 - The Dharma House
First, I'd want to thank Bastian because I was stuck when we last talked and getting the artifact piece together and his support kind of helped me to click through.

01:50:56 - The Dharma House
And then once I pushed it to Google Cloud.

01:51:00 - The Dharma House
Use.

01:51:00 - The Dharma House
In GCS, the Artifact Service, just made things much, much, much more simple.

01:51:06 - The Dharma House
Awesome.

01:51:07 - Brandon Hancock
But yeah, I'll share a screen.

01:51:08 - The Dharma House
I'll show you what it looks like.

01:51:15 - Brandon Hancock
Yeah, always shout out to Bastian.

01:51:17 - The Dharma House
That just should be said at the beginning of every call.

01:51:21 - The Dharma House
I agree.

01:51:22 - The Dharma House
We have some Jedis on the call.

01:51:24 - The Dharma House
You guys, especially those of you who are newer, talk about your gratitude for community.

01:51:30 - The Dharma House
I think we all share that if you've been around and get help through a lot of projects.

01:51:36 - The Dharma House
Some of you talked about kind of mental development timeframes and what it's like to go through development cycles.

01:51:42 - The Dharma House
And having a group like this is, I call Brandon Sensei, because he inspired me to get started on this journey.

01:51:53 - The Dharma House
Anyway, anyway, here's just the POC.

01:51:55 - The Dharma House
A couple of questions up front as you guys take a look at it.

01:51:59 - The Dharma House
Like one, is it a...

01:52:00 - The Dharma House
Not for a POC, so I'll just kind of – and then, too, I think my question for the community is where to go with it?

01:52:08 - The Dharma House
What I'm thinking is POC, V1, and then maybe like – or V0.5, and then V1, giving these three options as to, hey, here's where we get started, here's where I think a good next milestone is, and here's kind of what I think a solid V1 looks like.

01:52:29 - The Dharma House
But as you can see, just – here's the home page.

01:52:34 - The Dharma House
It's – the home page is the local.

01:52:37 - The Dharma House
I haven't even pushed it.

01:52:39 - The Dharma House
But here's the outcome.

01:52:41 - The Dharma House
There are two different ways of proposal, to generate a proposal.

01:52:44 - The Dharma House
One's a quick proposal, and you don't have to put in a lot of information to do that.

01:52:49 - The Dharma House
I'll show you just organization info and some other things.

01:52:53 - The Dharma House
And here's the output.

01:52:54 - The Dharma House
And part of the reason I want you to see this page is because I think when we left off last time, one of the things that I was thinking about –

01:53:00 - The Dharma House
For V.5 or V.1 is what it would be to have a chat box on this page post-execution of the proposal itself to be able to maybe chat with the proposal and make some changes from here.

01:53:17 - The Dharma House
And then V.2 has – or the other part of it has this kind of full proposal builder, and I thought I'd walk you guys through it a little bit.

01:53:24 - The Dharma House
Just kind of has funder info, project details.

01:53:27 - The Dharma House
You can upload documents, which I'm not going to do to this one, and then just generate a proposal.

01:53:34 - The Dharma House
And, you know, as with all demos, there's about a 50% chance this will work and another 50% chance that we'll all experience a bug together.

01:53:43 - The Dharma House
But it takes a couple of minutes to generate that proposal nonetheless as it's working.

01:53:47 - The Dharma House
And I got a couple of agents.

01:53:49 - The Dharma House
I have an orchestrator agent.

01:53:51 - The Dharma House
So this is a small MAS.

01:53:53 - The Dharma House
There's an orchestrator agent, a research agent, a rendering agent, and I think I have one or two.

01:54:00 - The Dharma House
Two others that are – one's a parser, and the other one is a language match agent.

01:54:06 - The Dharma House
So one of the things that I think we intend to do here to make it kind of more than just spit out a document is it takes the funder info, it looks up info on the funder and even the fund itself.

01:54:20 - The Dharma House
It takes the organizational info and it marries that information so that it really aligns the language of the grant itself, the proposal to the funder's request, to what the funder's looking for, for funding.

01:54:37 - The Dharma House
So there's a box that just matches the language between those two.

01:54:43 - The Dharma House
And that's it.

01:54:44 - The Dharma House
This will generate here in a second.

01:54:47 - The Dharma House
But part of – as I get started in building solutions for other orgs, I'm like, is this enough to demonstrate as a POF, as a POC, as a proof of concept, or –

01:55:00 - The Dharma House
I should perhaps, you know, I make it a bit more spiffy and do more here on the homepage, but that's pretty much it.

01:55:09 - The Dharma House
And when that pops out, there you go.

01:55:11 - The Dharma House
There's that full proposal generated just now based on what I put in there.

01:55:17 - The Dharma House
Another question I might have for anybody that's technical is, as you guys are creating reports or documents as output, what are you using specifically around graphs and tables?

01:55:29 - The Dharma House
What's doing a great job at rendering that?

01:55:34 - The Dharma House
Yeah, and that's all I got.

01:55:37 - Brandon Hancock
So, dude, seriously, first off, awesome.

01:55:40 - Brandon Hancock
Like, just, like, just hats off, man.

01:55:42 - Brandon Hancock
This is insane.

01:55:43 - Brandon Hancock
Very cool.

01:55:44 - Brandon Hancock
You've, you know, there's nothing cooler in my mind when, like, you have an idea, and then, like, you just build the dang thing, you know?

01:55:51 - Brandon Hancock
Like, that's the coolest part about building software is, like, I want to create something to showcase to my clients what it could look like, and then you did it.

01:55:59 - Brandon Hancock
So, seriously.

01:56:00 - Brandon Hancock
seriously.

01:56:00 - Brandon Hancock
Hats off, man.

01:56:01 - Brandon Hancock
Absolutely love all the progress you've made on this.

01:56:05 - Brandon Hancock
Okay, a few things I want to cover.

01:56:09 - Brandon Hancock
Tech, output, end goal as well.

01:56:14 - Brandon Hancock
Real fast, I would like to start on the tech side or on the output side of things.

01:56:18 - Brandon Hancock
On your current – would you mind going back to the output of the proposal?

01:56:26 - Brandon Hancock
Yes.

01:56:27 - Brandon Hancock
Okay, so there is a – I need to find it for you real fast.

01:56:31 - Brandon Hancock
But there is a tool that you can use to actually make the markdown output look so clean.

01:56:39 - Brandon Hancock
Because, like, that's what you're outputting markdown.

01:56:41 - Brandon Hancock
However, you're visually just showing raw markdown.

01:56:45 - The Dharma House
Sure.

01:56:45 - Brandon Hancock
And that's not – you know, we want to actually show the real thing.

01:56:48 - Brandon Hancock
So I am going to send you a snippet of code real fast in school that you can use to repurpose repurpose it.

01:57:01 - Brandon Hancock
You can repurpose it and steal some of the libraries.

01:57:04 - Brandon Hancock
Let me find you real fast.

01:57:06 - Brandon Hancock
There you are.

01:57:07 - Brandon Hancock
I just dropped it in school, but it's some raw code.

01:57:11 - Brandon Hancock
The most important thing is you want React Markdown.

01:57:16 - Brandon Hancock
You'll see it in the code I sent you, but it'll make that table look really beautiful and not just raw markdown.

01:57:22 - Brandon Hancock
So definitely check that out.

01:57:25 - Brandon Hancock
Okay, next one, end goal.

01:57:28 - Brandon Hancock
So I know you say, trying to show this as MVP, so where are we in the cycle of, like, potentially getting paid?

01:57:37 - Brandon Hancock
What is the, yeah, just like, any context around that would be super helpful.

01:57:41 - The Dharma House
All right.

01:57:42 - The Dharma House
So I thought a lot about our last conversation, and it ate me up quite a bit.

01:57:50 - The Dharma House
I agree with, like, I want to do stuff like this in the ranges that we talked about.

01:57:56 - The Dharma House
I charged six grand to create this PLC.

01:57:59 - The Dharma House
didn't think I'm gosed It's funny,

01:58:00 - The Dharma House
For a friend, it's in-house, so, you know, I didn't kick  on it, but also, like, this is it.

01:58:09 - The Dharma House
You know, it's bare bones.

01:58:11 - The Dharma House
I haven't done anything to it, so that's why I'm like, when I present, I'll present it on Friday.

01:58:17 - The Dharma House
I want to have, you know, two other sellable options that I'm like, all right, we could go here if this is your budget, or we could go here.

01:58:25 - The Dharma House
And, you know, ultimately, we want to do the full thing, I think.

01:58:28 - The Dharma House
You know, maybe I'll build more profit.

01:58:29 - The Dharma House
I'll into that.

01:58:30 - The Dharma House
Maybe that's a dumb way of thinking about it, but, yeah, and please advise.

01:58:34 - Brandon Hancock
Okay, so, question one.

01:58:37 - Brandon Hancock
Have you tracked your time for this?

01:58:38 - Brandon Hancock
How many hours did it take?

01:58:39 - Brandon Hancock
Did you track your time by chance?

01:58:41 - The Dharma House
How many hours do I have into this?

01:58:43 - The Dharma House
I did not.

01:58:45 - The Dharma House
I'm gonna say, just based on, I'd say I put 15, 20 hours in.

01:58:52 - Brandon Hancock
I mean, that's awesome.

01:58:53 - Brandon Hancock
I mean, that's like, if it's 20 hours, that's 300 an hour, so, like, that's insane, you know?

01:58:58 - Brandon Hancock
So, like, roughly, for development work.

01:59:00 - Brandon Hancock
So, on, like, your level and, like, expertise, minimum, I would recommend charging as 100, if, you know, and, but go up from there, if you're doing a freelance project, like, if you were completely the one-man shop doing the project where you're having to do the client meetings, you're having to do all of it, you know, I would stick to 100, just because there's, that would be the base case, but 100 to 200 is, like, the sweet spot for AI development, at least what I'm seeing right now.

01:59:27 - Brandon Hancock
Okay, so, technically, like, you could easily, for what you've done so far, you could easily spend, um, 30 hours on this.

01:59:37 - The Dharma House
Yeah, I mean, I hours, like, doing a lot of other things around it, or, you know, I've been kind of working on Eleanor as well, so, I didn't include those hours, but yeah, sure, there are a lot more hours built into it, for sure.

01:59:49 - Brandon Hancock
Okay, perfect.

01:59:49 - Brandon Hancock
Yeah, but I was, I mean, you could continue to go to 40 and still make, you know, make out like a bandit on this.

01:59:55 - Brandon Hancock
So, so awesome.

01:59:57 - Brandon Hancock
So, just, just know, um, those are, those are ranges.

02:00:00 - Brandon Hancock
Okay.

02:00:00 - Brandon Hancock
Okay.

02:00:01 - Brandon Hancock
A few other things that, like, I would look at.

02:00:06 - Brandon Hancock
So just, like, from what I've seen.

02:00:09 - Brandon Hancock
So usually on the 6K projects, there is some sort of deployment included to, like, just sharing, like, you know, usual client expectations.

02:00:17 - Brandon Hancock
Usually a client would expect to be able to click around on their own on that.

02:00:23 - Brandon Hancock
So do you have it set up to where you can go to, like, deploy to Vercel and click around?

02:00:29 - Brandon Hancock
Just because if you have a demo coming up, it just hits harder.

02:00:32 - Brandon Hancock
Yeah.

02:00:32 - The Dharma House
So the only thing I would have to do, I actually, um, on this front end, I built this front end, uh, in Next.js, in Cursor, but I said, hey, and I'm building it for Vercel.

02:00:44 - The Dharma House
So I had it pretty much use Vercel SDK.

02:00:48 - The Dharma House
Also, uh, a Bastion recommendation, talk about Jedis and this group.

02:00:53 - The Dharma House
Um, and just, uh, had it build it in Cursor, but I can push this.

02:00:57 - The Dharma House
I'm, I haven't pushed it to Vercel.

02:00:59 - The Dharma House
Vercel, but because it's built Vercel.

02:01:00 - The Dharma House
On that SDK, I'm pretty sure I could do that pretty quickly.

02:01:03 - Brandon Hancock
Okay, fantastic.

02:01:04 - Brandon Hancock
Yeah, there's sometimes just some hiccups with, like, file sizes and, like, uploading documents.

02:01:09 - Brandon Hancock
So, quick question, backend.

02:01:11 - Brandon Hancock
What are we using to save stuff to?

02:01:14 - The Dharma House
What do you mean?

02:01:16 - Brandon Hancock
Like, uh...

02:01:17 - The Dharma House
It's all...

02:01:19 - The Dharma House
So I'm using Google Cloud, Firebase, and, yeah, GCS, Google Artifact Service.

02:01:30 - The Dharma House
I'm not...

02:01:31 - The Dharma House
So I don't have these actually saving in a database.

02:01:35 - The Dharma House
This isn't pushing to a database at all yet.

02:01:38 - The Dharma House
Just POC.

02:01:39 - Brandon Hancock
Okay.

02:01:40 - Brandon Hancock
So, um, it is insanely easy, like, you know, if you wanted to hop on a call this weekend, like, to put, like, let's just go, like, for what you're doing, Supabase, boom.

02:01:54 - Brandon Hancock
Like, that would handle everything that you're trying to do from saving the artifacts in your document uploader.

02:01:59 - Brandon Hancock
Like, total proposals.

02:02:00 - Brandon Hancock
Yeah.

02:02:00 - Brandon Hancock
Cool.

02:02:00 - Brandon Hancock
There's a proposal table.

02:02:01 - Brandon Hancock
Like all of that should be in a table.

02:02:05 - Brandon Hancock
And, you know, there's a lot that we could do around it.

02:02:08 - Brandon Hancock
So that's just, you know, in the 6K, like usually, like from what I have seen, there usually is a deploy component, a database component in the front end.

02:02:17 - Brandon Hancock
Like that's usually, you know, what I've seen from my clients so far, like what they are expecting around that price range.

02:02:23 - Brandon Hancock
Obviously take all what I'm saying for a grain of salt.

02:02:25 - Brandon Hancock
Like this is your project with your friends.

02:02:27 - Brandon Hancock
So like what they expect, you know, you guys might have I've said different things, but just want to like mention usually what I'm seeing.

02:02:34 - Brandon Hancock
Yeah.

02:02:35 - Brandon Hancock
And that's exactly what I was about to bash you brought up the point.

02:02:38 - Brandon Hancock
It works locally.

02:02:39 - Brandon Hancock
And then you go to deploy to Vercel and it doesn't.

02:02:42 - Brandon Hancock
I literally today had that exact problem with document uploads locally.

02:02:47 - Brandon Hancock
You, you click upload.

02:02:49 - Brandon Hancock
You're like, Oh my gosh, local.

02:02:51 - Brandon Hancock
It works fine.

02:02:52 - Brandon Hancock
You deploy it.

02:02:52 - Brandon Hancock
The customer uses it and it dies because Vercel edge functions very particular requirements.

02:02:59 - Brandon Hancock
I'm like, Oh, I,

02:03:00 - Brandon Hancock
You can max work with a five-megabyte file.

02:03:02 - Brandon Hancock
Well, now you have to start to work with, like, a client uploading service, Supabase makes that pretty easy to do.

02:03:11 - Brandon Hancock
That's why I keep recommending them over and over and over again.

02:03:13 - Brandon Hancock
So just, you know, but all of this to say, like, this is if we're trying to go further.

02:03:19 - Brandon Hancock
Like, if this is just to showcase to your friend what's possible, and he goes, thanks for exploring that idea for me, I don't care, then hey, like, there's actually no need to implement all the things we just talked about.

02:03:28 - Brandon Hancock
It's just, I don't know what your friend wants next.

02:03:31 - Brandon Hancock
Maybe you have a bit more information on that.

02:03:33 - The Dharma House
What they want is a, they have a business where they consult with non-profits right now, and they get asked to build grants based on a lot of the organizational development work that they do with non-profits.

02:03:48 - The Dharma House
But they don't want to write the grants.

02:03:50 - The Dharma House
So they do them sometimes, but they'd rather have a site.

02:03:54 - The Dharma House
They want a full-on site.

02:03:56 - The Dharma House
They send clients to and charge them to build grants.

02:03:59 - Brandon Hancock
does efforts go?

02:03:59 - Brandon Hancock
well.

02:03:59 - Brandon Hancock
Then, after try they don't And I lead

02:04:00 - Brandon Hancock
Okay.

02:04:00 - Brandon Hancock
Okay.

02:04:01 - Brandon Hancock
Yeah.

02:04:01 - Brandon Hancock
So in that case, like getting database functionality up and running to where it's a multi-tenant application is going to be pretty crucial to where you have organizations, organization have users, users have roles.

02:04:14 - Brandon Hancock
Like, you know, that's, um, you're definitely going to want to start to like, at least when you have the next conversation, just keep in mind when you're scoping things out.

02:04:22 - Brandon Hancock
These are things that are going to be a must.

02:04:24 - Brandon Hancock
So like, you're going to have an admin panel and admin panel is going to have like organizations or they're going to be able to create organizations, invite users to organizations, delete people from them, invite people to them.

02:04:35 - Brandon Hancock
Like there's, there's so many extra things the second you allow this to be multi-tenant because, you know, at the end of the day, it needs to be self-serve.

02:04:43 - Brandon Hancock
So people need to manage their own, their own, you know, environment.

02:04:47 - Brandon Hancock
Um, okay.

02:04:49 - Brandon Hancock
Um, okay.

02:04:51 - Brandon Hancock
One other thing that I think you could do is just like a quick, one other value add, and I definitely want other people to go, sorry, I know I've been on a quick rant.

02:04:58 - Brandon Hancock
Um, it would be, it's actually,

02:05:00 - Brandon Hancock
It's wild to – if you want to go back to the application where you had the grant at – yeah, perfect.

02:05:09 - Brandon Hancock
It is not crazy wild or hard to almost replicate the Canvas functionality of working with ChatGPT.

02:05:20 - Brandon Hancock
But, like, you really could, on the right-hand side, go ahead and import a chat right there and make sure – all it would have to do is structured outputs.

02:05:31 - Brandon Hancock
Stream-structured outputs, and you could pretty much recreate Canvas, where you go, like, basically the message – the output of the chat would have, like, a message and a document.

02:05:44 - Brandon Hancock
The document is obviously what you see, and the chat would be – or the message would be like, okay, great, I'm implementing the feedback you just gave.

02:05:51 - Brandon Hancock
Like, you could do that all with the AI, Vercel AI SDK, and I think that would be a huge value add for them to be like, oh, my, this is insane.

02:06:00 - Brandon Hancock
And it probably, you know, five hours of work, six hours of work, being generous, I think you could get that working pretty darn easily and really make this core loop that they're focused on doing even more impactful so they could just see the potential of what's coming next.

02:06:16 - Brandon Hancock
Because, like, right now, the question they might say is, like, couldn't I just do this in ChatGPT?

02:06:22 - Brandon Hancock
So we're going to be like, no, no, no, you could not do what I'm about to show you in ChatGPT, where we're, this is V1, it's a single LLM call to where we're updating stuff.

02:06:30 - Brandon Hancock
Future me, we're going to have agents running in the background towards making a plan, it's iterating through parts, you know, almost like a cursor-like experience, but just to give them a teaser of future functionality, I think would, like, you know, shut up and take my money.

02:06:44 - Brandon Hancock
Because that's what I think we're going for, or what we ultimately want anyway.

02:06:46 - The Dharma House
Right, right, that's what I mean in the .5 and the V1, having that vision right now, so I could either build out the demo for that or just be able to speak into it.

02:06:59 - The Dharma House
Yeah.

02:06:59 - The Dharma House
And that's what I'm looking for.

02:07:00 - The Dharma House
I appreciate that.

02:07:01 - The Dharma House
I'm open to any of the feedback before I kind of just switch gears and ask you a question about Eleanor, which I think will be relevant to some of things I've heard.

02:07:08 - The Dharma House
Guys, hop on.

02:07:10 - Brandon Hancock
Love to want to hear y'all's thoughts.

02:07:16 - Brandon Hancock
Abdul, I think you're muted.

02:07:18 - Brandon Hancock
Or, it's not good.

02:07:20 - AbdulShakur Abdullah
Can you hear me now?

02:07:21 - Brandon Hancock
Yeah, I'm perfect.

02:07:23 - AbdulShakur Abdullah
I was going to say, if I was going to add value based off of what you already did, I would try to kind of take – this, what you have, the proposal, and do a back-end, like, perplexity call to see if there's any other available grants that kind of fit in, so you could double-dip.

02:07:46 - The Dharma House
Yeah, yeah, I appreciate that.

02:07:48 - The Dharma House
I was thinking about, like, some kind of marketplace on this page, or kind of having the research bot be able to, like, say, hey, these are the grants line up, something of that nature.

02:07:58 - The Dharma House
But that's it.

02:08:00 - The Dharma House
I'm trying trying

02:08:00 - The Dharma House
You of find smart iterations without over-promising and without under-selling either.

02:08:09 - Brandon Hancock
I'm so glad you brought that up, Abdul.

02:08:11 - Brandon Hancock
One thing I usually like to do when building MVPs is almost have two versions.

02:08:17 - Brandon Hancock
It's the same application, but almost two parts.

02:08:20 - Brandon Hancock
Part one is the functional, like, hey, this is the thing I promised you.

02:08:23 - Brandon Hancock
But then part two, just because, like, it's so easy to spin up, like, mock-ups with Cursor to say, like, I'm thinking about building something.

02:08:32 - Brandon Hancock
Don't make it functional, just put dummy data.

02:08:34 - Brandon Hancock
So there's where you could almost showcase, like, the marketplace that you're talking about.

02:08:38 - Brandon Hancock
Don't build out the functionality, because he might not even like it, you know?

02:08:41 - Brandon Hancock
But, like, because you're coming to him to go, hey, you know, we're getting ready to gear it for phase two, I just want to show you what's also possible to almost, like, give you a sampler of, like, oh, I'd like where that's going, or no, mix these two ideas together, you know?

02:08:58 - Brandon Hancock
So this is where you get to kind of flex your creativity.

02:09:00 - Brandon Hancock
you, David .

02:09:00 - Brandon Hancock
As a, you know, understanding their problem and know what's possible in the world of AI, and just have Vercel or Cursor spin up fake pages for you and say, like, I was also envisioning something like this, this, and this, and this, I mean, that's a great way to almost like, let's say the next step was going to be another 12k, it's how you go from a 12k, next phase to an 18 or 20k, by just, you know, showing him what, helping him think bigger, you know, is basically what you could be doing.

02:09:27 - Brandon Hancock
All right, Bastian, the wizard, hit us, buddy.

02:09:31 - Bastian Venegas
Yeah, I was, uh, well, first of all, congratulations to AK because this looks awesome.

02:09:37 - Brandon Hancock
Yeah, it does.

02:09:37 - Bastian Venegas
My other comment regarding, like, the demo is, like, besides Markdown, I, um, when I've shown, like, agentic applications to non-tech people, um, they kind of expect some intermediate output when, um, um, when you're, like, having this, uh, big, uh, agentic system, like, go through all the steps.

02:10:00 - Bastian Venegas
They tend to appreciate if you can, like, say, step one is completed, now step two is completed, just so they know the application is not, like, hanging, because if you show this to me, I think it's great, but it can confuse people that are used to interact with AI through a chat that is, like, more like real-time.

02:10:21 - The Dharma House
Sure, sure.

02:10:22 - The Dharma House
That's great info.

02:10:23 - Bastian Venegas
Thank you.

02:10:23 - Bastian Venegas
It's definitely not a priority, though, and it can be cumbersome sometimes, but something to consider.

02:10:30 - Bastian Venegas
Sure.

02:10:31 - Brandon Hancock
Super fast, Bastian, phenomenal point.

02:10:33 - Brandon Hancock
So, right now, me looking at this, I think, under the hood, is it a sequential workflow?

02:10:39 - Brandon Hancock
Like, in ADK, did you create a sequential workflow to replicate this?

02:10:43 - Brandon Hancock
Or, under the hood, what's happening, I guess?

02:10:46 - The Dharma House
Yeah, it's some of the works happening in parallel, so it's not all happening sequentially.

02:10:53 - The Dharma House
But there's some sequential loops, some parallel loops.

02:10:56 - Brandon Hancock
So, one thing that you can do is, I'm...

02:11:00 - Brandon Hancock
A huge – let me just – could show you some code really fast so you can see what I do and steal some inspiration.

02:11:08 - Brandon Hancock
Okay, so going off of what Bastian just said, what I am a huge fan of is having jobs.

02:11:16 - Brandon Hancock
So, like, in this case, when I'm processing a RAG document, I want the user to see in real-time the status, like pending, processing, error, complete.

02:11:28 - Brandon Hancock
So, what I do is I have my background worker, which in your case would be the agent, as it is completing different parts of the process, it is updating the status.

02:11:41 - Brandon Hancock
So, in this case, I have my background job, like, going from, you know, pending, processing, like, in real-time, it's making these changes.

02:11:48 - Brandon Hancock
And then I just have my front-end polling this endpoint just over and over and over to get the latest status.

02:11:54 - Brandon Hancock
Every two seconds, it's just polling the database, you know.

02:11:59 - Brandon Hancock
So, now, in your case.

02:12:00 - Brandon Hancock
If you wanted to replicate something very similar, the way you could do that, you know, obviously it does require a database, is to your agents, you can have an after-agent callback to where all it does is it reports back, like, agent two done, agent three done.

02:12:19 - Brandon Hancock
So that way, you know, you could just have, like, hey, we know this workflow always has six steps, and in real time you could be, like, one out of six steps done, two out of six steps, three out of six steps, and you could always just have some text, like, loading, like, oh, when one step is done, we can just say, like, research done.

02:12:38 - Brandon Hancock
When two steps are done, we probably, even though it's in parallel, the user doesn't really care, they just want to see status is happening, it's like, oh, we're researching, we're planning, oh, we just wrapped up, you know, getting this tone of voice.

02:12:50 - Brandon Hancock
Generating the report, finalizing details, done, you know, so you just look at that, and the agent callback, all it would do is it would just make a...

02:13:00 - Brandon Hancock
Request to your database to say, hey, just finished this step, and it would just add, you know, it would add some additional information to let me know what just wrapped up.

02:13:10 - Brandon Hancock
So, could definitely do something like that.

02:13:13 - Brandon Hancock
So, but no, dude, we're here to keep you busy, man.

02:13:17 - Brandon Hancock
We have a thousand ideas.

02:13:20 - Brandon Hancock
Yeah, so hopefully it's helpful.

02:13:22 - The Dharma House
No, it's definitely helpful, and I certainly appreciate it.

02:13:26 - The Dharma House
Um, just, um, to flip the script a little bit on my other project that I'm not going to demo right now, is I...

02:13:35 - Brandon Hancock
Hey Kate, super fast.

02:13:36 - Brandon Hancock
Super fast.

02:13:36 - Brandon Hancock
I think Al has a really good point to, to bring up.

02:13:39 - The Dharma House
By all By all means.

02:13:41 - Brandon Hancock
You bet.

02:13:42 - Al Cole
Um, from my years of running my own consulting practice, plus when I ran it with professional services for larger startups, um, a tactic I always used and coached my team to use is when you're talking to a prospect, and my goal here in sharing this is...

02:14:00 - Al Cole
We sometimes get ourselves caught up in our value per hour, and your challenge there will always be there's somebody out on the planet who could do an hour of work for a different amount, usually cheaper.

02:14:15 - Al Cole
The better way to position yourself is on the value of the solution that you're actually delivering, and the way you get there in identifying value is essentially ask the three whys, okay?

02:14:27 - Al Cole
You ask, why anything?

02:14:30 - Al Cole
In other words, do you really need this to be solved, right?

02:14:35 - Al Cole
That's the why anything.

02:14:37 - Al Cole
Why your custom solution, right, to address their problem, and then why now?

02:14:43 - Al Cole
Why now is, well, it's nice to have, but you're not going to get an economic buyer to actually write the check because it isn't compelling yet, okay?

02:14:50 - Al Cole
If you get alignment on those three, then the last question you really ask is, if I build this view, how much revenue are you going to be able to

02:15:00 - Al Cole
...generate with this solution, or how much are you going to be able to automate and therefore save you resources?

02:15:09 - Al Cole
That helps you to get to a value statement that gets you away from the hours, because AK, what you didn't factor in in that great work you did was all the learning that you had done prior to building it.

02:15:21 - Al Cole
The hours don't match the effort there.

02:15:24 - Al Cole
So if you can get used to doing the three whys and thinking of it that way, ...and it's not hard selling.

02:15:31 - Al Cole
You're helping them to understand their own problem space and how they value it.

02:15:37 - Al Cole
And it may steer you away from things that didn't need to get built, but when you really latch on to a pain point and they can quantify it, you won't have a problem figuring out a number to present to them.

02:15:49 - Al Cole
Does that make sense?

02:15:50 - The Dharma House
Yeah, that's great advice though.

02:15:52 - Al Cole
Okay.

02:15:59 - Brandon Hancock
Yes!

02:15:59 - Brandon Hancock
here.

02:16:00 - Brandon Hancock
It's going to help us generate an additional $200,000 in revenue.

02:16:03 - Brandon Hancock
Are you a, like, oh, 10% of value, 20% of value?

02:16:08 - Brandon Hancock
Out of curiosity, in your experience, have you – once you get that top-line revenue, working back to the price?

02:16:16 - Al Cole
So if I know it's super valuable, what I might want to do is look at what's the likelihood this is going to need ongoing maintenance.

02:16:25 - Al Cole
And I might want to wrap some type of a subscription model around it, so I stay connected, I build a bit of an annuity, and continue to incrementally develop it, right?

02:16:35 - Al Cole
So is it a one-and-done, and then you're really just trying to protect your floor?

02:16:41 - Al Cole
So you don't end up undershooting where you put your value in, right?

02:16:45 - Al Cole
Because they kind of quantified it, right?

02:16:47 - Al Cole
And then you don't overshoot, because, like, if they only see it as a 5K problem you're solving, and you know it's 10K going in, you both easily then either reduce scope, or that's just not a good

02:17:00 - Al Cole
One for you to go chase, right?

02:17:01 - Al Cole
So what I will typically do is if I see there's a lot of upside and there's some strategic importance to the business, I'll try to offer some type of a subscription model where I will keep maintaining this for them as their requirements evolve because it's so valuable.

02:17:20 - The Dharma House
You set that up as managed services out?

02:17:22 - Al Cole
What's that?

02:17:23 - The Dharma House
You set that up as like a managed services package?

02:17:25 - Al Cole
Yeah, exactly.

02:17:27 - Al Cole
So what I usually do is quarterly check-ins, then we're reviewing if their initiatives have evolved at all, do they have new requirements?

02:17:37 - Al Cole
Are there new data sources I should be touching into?

02:17:39 - Al Cole
And then I'm doing some incremental work that I've already budgeted in because I have them buying into the higher tier, right?

02:17:45 - Al Cole
And I'm always managing it to the tier they bought in.

02:17:48 - Al Cole
So it's a certain number of hours, a week is the way I tend to think about it, and then I usually have quarterly check-ins.

02:17:53 - Al Cole
So what all I wanted to do for the team is just to help you understand that if you end up charging what's yourjipped in?

02:18:00 - Al Cole
By the hour, I think you'll always come up on the lower end of that, and that was me in my early days.

02:18:06 - Al Cole
When you can help them to understand and quantify the value to them, then I think you can capture more of the value you're delivering and not feel like you've got a real competitive problem when you do it.

02:18:19 - Al Cole
Does that make sense?

02:18:20 - The Dharma House
Yeah, I would do something like this in the 15 to 25 range for a solid delivered product.

02:18:28 - Al Cole
Yeah, and you want them to quantify?

02:18:32 - Al Cole
That's how they would value the pain that you're solving, right?

02:18:36 - Al Cole
Either helping them to bring in more revenue because you're helping them drive grants, or you've automated something.

02:18:43 - Al Cole
So now they've got a resource and a non-profit that they can repurpose, and that's worth something, right?

02:18:49 - The Dharma House
Yeah, because not only do they want to sell the use, they get a percentage of each of the grants.

02:18:57 - The Dharma House
So they're going to make a solid amount.

02:19:00 - The Dharma House
The money on, on this product.

02:19:01 - Al Cole
And, and, so that, that, that is a much easier way then for you to capture value when you have that.

02:19:07 - Al Cole
again, understand that this technique may steer you away from some opportunities because they don't see the value and you don't know how to get there for anything less than what you're thinking, then you save both yourselves some time, right?

02:19:21 - The Dharma House
Yeah, appreciate that.

02:19:23 - Brandon Hancock
Yeah, Alice, solid, solid advice.

02:19:27 - Brandon Hancock
Thanks, thanks for sharing.

02:19:28 - Al Cole
bet.

02:19:28 - Brandon Hancock
Um, AK, I know you were gonna, um, do one other quick question real fast.

02:19:33 - The Dharma House
Uh, happy to, happy to help.

02:19:35 - The Dharma House
Yeah, um, not really a question yet, but I'll tell you, I've heard some conversation here about Google ADK and Langchain.

02:19:43 - Brandon Hancock
Yeah.

02:19:43 - The Dharma House
If you've been around for a while, I started, I'm also working on a, uh, on an AI companion that's, uh, uh, an AI assistant.

02:19:51 - The Dharma House
Um, part of what has kind of been cool about playing in the Google work space, is that...

02:20:00 - The Dharma House
Uh,

02:20:00 - The Dharma House
I have a version – I iterate a lot.

02:20:03 - The Dharma House
kind of create a bunch of different versions of things sometimes.

02:20:05 - The Dharma House
I have a version that's kind of Google-native, so I've worked on an agent that's just – that taps into the entire Google workspace, you know, plays with all of the Google tools and also has context.

02:20:18 - The Dharma House
And I'm still kind of working on that – on the context and cash within the Google ADK system of an environment.

02:20:29 - The Dharma House
But, you know, I still like it more than LangChain.

02:20:32 - The Dharma House
I certainly certainly like it more than LangChain.

02:20:34 - The Dharma House
And it was Brandon's first LangChain video – and he talks his best, I will disagree with that – that got me going down the LangChain past last December.

02:20:45 - The Dharma House
But as I'm working in ADK ADK, I feel like maybe the best stack is LangGraph, Google-list – get Google-list.

02:21:00 - The Dharma House
ADK.

02:21:00 - The Dharma House
That's – that's – that's – I haven't, like, added a graph to it, but I think that might be the magic stack for me, so more to come on that, guys.

02:21:13 - Brandon Hancock
So, quick to piggyback off what AK just said real fast, is the main – the main reason that would force me just out of the gate to go land graph is if I was working in some sort – like, a graph, obviously, like, to where, like, there was a certain cycle of events that had to happen from left to right, and there 100% had to be an atomic action that had to be performed by code.

02:21:38 - Brandon Hancock
What I mean by that, if I have to, like, do something with my bank, if I have to do something with, like, an email, where I don't want to accidentally have an agent trigger that twice, that is the main reason I would go with land graph right now.

02:21:56 - Brandon Hancock
Yes, in ADK, you can do a loop with

02:22:00 - Brandon Hancock
You can do a loop, and you can have global state, so, you know, it might not – yeah, sorry, I'm not thinking through this as I'm saying it – you could have a conditional loop inside of ADK to where it would only call that once, but the kicker is, is, like, what is very nice about lane graph is, like, you can do agent, agent, agent, agent, get to a really nice finite state to where all you want to do is just run, like, six lines of code.

02:22:27 - Brandon Hancock
There's no reason for an agent to make – do a tool call.

02:22:30 - Brandon Hancock
Like, you sometimes just want to do straight code.

02:22:33 - Brandon Hancock
ADK does not do that through – they have flows, so, yeah, you know, that's their workaround for it.

02:22:41 - Brandon Hancock
That is the biggest downfall right now I see in ADK is the inability to do a code step.

02:22:47 - Brandon Hancock
That's the main – that's the biggest downfall I see of ADK right now.

02:22:51 - Brandon Hancock
So, hopefully, hopefully that's helpful, just how I'm seeing it right now.

02:22:56 - Brandon Hancock
So, but, hey, Al, by next week, he's going to be our

02:23:00 - Brandon Hancock
I'm LandGraph expert so he can come back and tell us.

02:23:04 - Al Cole
So that's a lot of coffee, Brandon.

02:23:06 - Brandon Hancock
Yeah, you don't need to sleep.

02:23:09 - The Dharma House
Do you think that Google manages state as well as LandGraph does?

02:23:14 - Brandon Hancock
Oh, yeah.

02:23:15 - Brandon Hancock
mean, the state management inside of ADK, beautiful, beautiful.

02:23:20 - Brandon Hancock
Like, I mean, I'll show you the background real fast.

02:23:23 - Brandon Hancock
Like, at Crew AI, like, that was one of the biggest things that, like, I wanted to make easy, was state management.

02:23:29 - Brandon Hancock
Because, like, inflows, like, I helped build all the state management.

02:23:33 - Brandon Hancock
And, like, like, it is insanely important.

02:23:36 - Brandon Hancock
So when I saw how ADK was doing it, it instantly got all the warm and fuzzies.

02:23:40 - Brandon Hancock
Because I was like, they did it right.

02:23:41 - Brandon Hancock
So, with the way they're doing it.

02:23:43 - Brandon Hancock
Because it has to, like, it has to be global.

02:23:47 - Brandon Hancock
Or else it's just not usable on bigger projects.

02:23:50 - Brandon Hancock
It's like, regular crews are left to right to where it is task one spits output to task two.

02:23:55 - Brandon Hancock
Task two goes to task three.

02:23:57 - Brandon Hancock
Which is great for, like, very straightforward.

02:24:00 - Brandon Hancock
The second you get to loops or anything else, you have to have global state.

02:24:06 - Brandon Hancock
So that's what Flows does.

02:24:07 - Brandon Hancock
Landgraf has the global state.

02:24:09 - Brandon Hancock
And ADK did a phenomenal job also having global state.

02:24:13 - Brandon Hancock
And they're doing a really good job of it.

02:24:15 - Brandon Hancock
And you can access it through the agents.

02:24:18 - Brandon Hancock
You can access it through the tools.

02:24:19 - Brandon Hancock
They did a really good job with global state that you can access through context.

02:24:24 - Brandon Hancock
Great job.

02:24:26 - Brandon Hancock
Yeah.

02:24:27 - Brandon Hancock
So, OK.

02:24:28 - Brandon Hancock
Any final questions, buddy?

02:24:30 - Brandon Hancock
want to make sure...

02:24:32 - Brandon Hancock
I think there was...

02:24:33 - Brandon Hancock
Let me go back to the chat message I just sent out to make sure.

02:24:36 - Brandon Hancock
I think...

02:24:37 - Brandon Hancock
Robert, are you up next?

02:24:38 - Brandon Hancock
think...

02:24:38 - Brandon Hancock
Right?

02:24:39 - Brandon Hancock
Let me pull up chat.

02:24:42 - Brandon Hancock
Yeah.

02:24:43 - Brandon Hancock
Yeah.

02:24:43 - Brandon Hancock
I think you're up next, right?

02:24:45 - Robert
Well...

02:24:46 - Brandon Hancock
Robert, then Neil.

02:24:48 - Robert
Yeah, cool.

02:24:49 - Robert
So, yeah.

02:24:49 - Robert
So I'm continuing along my journey towards becoming an ADK engineer.

02:24:54 - Robert
So I finally got into Cursor AI, where basically...

02:24:57 - Robert
I'm generally following Brandon's...

02:24:59 - Robert
for

02:25:00 - Robert
workflow going from requirements documents to output, so now I'm finally, like, within Cursor AI and everything.

02:25:07 - Robert
So I had a couple of questions to ask.

02:25:12 - Robert
So, Brandon, what kind of subscriptions do you have in terms of AI, terms of, like, models towards, like, Claude or is it, like, Gemini, OpenAI?

02:25:21 - Robert
So I'm just wondering what a good mix of models for subscriptions to have is.

02:25:26 - Brandon Hancock
So y'all are going to laugh.

02:25:27 - Brandon Hancock
I actually do pay the $200 for OpenAI, strictly for GPT 4.5.

02:25:36 - Brandon Hancock
I use that to write everything.

02:25:39 - Brandon Hancock
It's the best, from what I've seen, it is the best writing model.

02:25:43 - Brandon Hancock
So every time I'm making presentations, as I'm, like, writing the course right now, like, it is, by far, with its context window and its ability to, like, actually just write, like a human, it is the best one, by far, for writing.

02:26:00 - Brandon Hancock
So I use.

02:26:00 - Brandon Hancock
That one.

02:26:00 - Brandon Hancock
And then I literally have subscriptions to everything else.

02:26:03 - Brandon Hancock
The only one I don't is I don't have a subscription to Cloud Code.

02:26:07 - Brandon Hancock
So, I mean, I have Supergrok, I have Gemini.

02:26:10 - Brandon Hancock
Like, I have every single one of them, just because I use them for different things.

02:26:14 - Brandon Hancock
So, I help – I work with some, like, local businesses, and doing anything with a local business, Gemini is going to be the default AI for small to medium businesses, in my opinion.

02:26:28 - Brandon Hancock
Quickly because it can, you know, through Gemini, like, when you're over in AI Studio, it can instantly access all of their Google Drive documents.

02:26:38 - Brandon Hancock
So, it's 10 times – it's, like, with OpenAI, great.

02:26:42 - Brandon Hancock
It can do everything.

02:26:43 - Brandon Hancock
has projects.

02:26:44 - Brandon Hancock
It has all – it has everything, but you're siloed.

02:26:46 - Brandon Hancock
Yes, you can do, you know, you can search the web, but the thing that allows businesses to unlock an insane amount of value is their email, their calendar, and their Google Drive.

02:26:56 - Brandon Hancock
Because that's how a lot of small businesses run.

02:26:58 - Brandon Hancock
So, I have that subscription just –

02:27:00 - Brandon Hancock
Because I work with local businesses a lot.

02:27:02 - Brandon Hancock
Super Grok, just because I just want to see what they're doing.

02:27:05 - Brandon Hancock
Grok is like my daily model for just quick stuff.

02:27:09 - Brandon Hancock
Yeah, and then Cursor.

02:27:11 - Brandon Hancock
Those are like the main ones.

02:27:14 - Brandon Hancock
Anyone else have any big subscriptions that they're paying for?

02:27:22 - Brandon Hancock
Yeah, Bastion kind of reiterated, 4.5, you know, so much better at writing compared to any other model that I've ever seen.

02:27:33 - Brandon Hancock
I was hoping when they did 4.1, it was going to be as good as writing because it was a lot cheaper, but it's still just, it's still not.

02:27:40 - Brandon Hancock
But I think they're going to, aren't they dropping 4.5?

02:27:43 - Brandon Hancock
I can't remember.

02:27:44 - Brandon Hancock
If someone knows, would love to hear what, you know, if y'all know, because I hope they replace it with something because it's seriously, there's just nothing else like it for writing, at least.

02:27:54 - Brandon Hancock
So...

02:27:55 - Bastian Venegas
They will deprecate it, but I hope they don't.

02:27:58 - Brandon Hancock
Yeah.

02:27:59 - Brandon Hancock
I mean, it's...

02:28:00 - Brandon Hancock
So good.

02:28:00 - Brandon Hancock
Like, that's the problem.

02:28:01 - Brandon Hancock
So, you know, at writing.

02:28:05 - Brandon Hancock
But I think the average person could just get away with all the other ones.

02:28:08 - Brandon Hancock
It's just strictly because I'm trying to write courses and stuff.

02:28:10 - Brandon Hancock
And it just helps you move faster.

02:28:13 - Brandon Hancock
But anything else, Robert?

02:28:14 - Brandon Hancock
I know you were questioning it on your ADK journey.

02:28:17 - Brandon Hancock
Want to just make sure, if there's anything I can help with, happy to clear up.

02:28:21 - Robert
Yep, we're gonna have a couple more follow-up questions.

02:28:24 - Robert
basically, when developing with Cursor AI, what's that part called?

02:28:28 - Robert
that called, like, agentic development?

02:28:31 - Robert
Like, when you use Cursor AI and tools in order to help you create code in that?

02:28:37 - Brandon Hancock
I mean, I think that's the proper term, just agentic development, right?

02:28:42 - Brandon Hancock
AI-driven development, it would probably be the, like, the two words that I would use to describe it.

02:28:49 - Robert
Okay, yes, because I'm figuring out how to, like, describe the skill, like, on a resume or that type of portfolio.

02:28:55 - Robert
Okay.

02:28:55 - Robert
And last but not least is going to be about LinkedIn and building a brand.

02:29:00 - Robert
Okay.

02:29:00 - Robert
you.

02:29:00 - Robert
So what's the best way to share a link to YouTube or a link to your video on LinkedIn?

02:29:06 - Robert
The reason I'm asking is because, say, for example, back in the days of Facebook, if you had two posts, one post had a link going externally versus the other post had a link to an internal Facebook post, the internal Facebook post would perform better because you're not taking the person off the platform.

02:29:22 - Robert
So that's what I'm trying to get at here is that basically, if I, like, say, for example, create a LinkedIn post and it has, like, a link to a YouTube video, and I put it within that post, will I get penalized by the LinkedIn algorithm because I'm taking somebody off of the LinkedIn platform and giving somebody else the time spent?

02:29:39 - Brandon Hancock
Yeah, I mean, I think the short answer is, like, yes, it does.

02:29:42 - Brandon Hancock
It's not as beneficial to link outside of LinkedIn.

02:29:46 - Brandon Hancock
Like, I mean, you know, on the head, you correctly identified it.

02:29:48 - Brandon Hancock
However, if I was to link a YouTube video, the shortest way for growth or the quickest way for growth is you want to be a summarizer for a bigger brand.

02:30:00 - Brandon Hancock
For example, anytime someone posts anything, and they're like, hey, I just watched Brandon's videos, here's the five things I learned, definitely recommend copying these as well, I repost it, you know, by no means is my account huge, but I, like, when I was trying to grow a lot early, like, on X, that's all I would do is, like, a My First Million episode.

02:30:22 - Brandon Hancock
Like, anytime I learned anything from anyone, I would just almost say, like, I just watched this amazing video, five biggest takeaways, and I would tag the, you know, I would tag the person, just to say thank you.

02:30:33 - Brandon Hancock
So, like, you're doing them a service, and then they, in return, you know, are usually more than happy to share, because you just did, you know, you helped spread how awesome their stuff is, so it's, like, social proof on their end.

02:30:44 - Brandon Hancock
So, it's basically each person scratching each other's back.

02:30:47 - Brandon Hancock
So, that's, that's one way for growth.

02:30:50 - Brandon Hancock
And then, seriously, going back to earlier, what we were talking about with Abdul's LinkedIn approach, be a giver.

02:30:59 - Brandon Hancock
Like, I can, can, I I I can, express.

02:31:00 - Brandon Hancock
How much of a difference that's going to make, and by giving, I'm giving assets, so, like, cursor rules was just an example, but, like, the more you can say, I just, like, I did all of this work, and if you just comment below, keyword, I'll give it to you for free, like, that's what every person wants ever.

02:31:20 - Brandon Hancock
It's like, oh, you did all this stuff, and I can just get it for free?

02:31:22 - Brandon Hancock
Thank you.

02:31:23 - Brandon Hancock
So, you're thinking in lead magnets, and that's one way your posts are going to just get, like, tens or hundreds of thousands of impressions, so you don't have it multiple times.

02:31:34 - Robert
So, as opposed to directly putting, say, like, a link to your video in the post, I can do the giver method, where basically, I give them a link for, like, commenting or whatever.

02:31:44 - Robert
I give it to them in the back end, saying, like, okay, here's a list of all the YouTube videos associated with the posts that I've been doing.

02:31:50 - Brandon Hancock
Yeah, so, so, I would actually, I mean, I wouldn't really give links as a giveaway, like, I was saying more on, like, the, like, I just built this cool.

02:32:00 - Brandon Hancock
I just built this really cool agent development workflow, this ADK workflow, and it does A, B, and C.

02:32:08 - Brandon Hancock
Here's how it actually works under the hood.

02:32:10 - Brandon Hancock
Comment down below and I'll give you this ADK workflow completely for free.

02:32:14 - Brandon Hancock
Or like, hey, I just put together 10 templates, 5 templates to help you.

02:32:20 - Brandon Hancock
That template I just gave away on how to go from lovable to Next.js, that's a phenomenal template to give away on LinkedIn.

02:32:30 - Brandon Hancock
Because it solves a real problem.

02:32:32 - Brandon Hancock
People need it.

02:32:33 - Brandon Hancock
So like, hey, comment down below and I'll share the exact template I always put into Cursor to have it recreate my lovable projects.

02:32:39 - Brandon Hancock
Like, stuff like that towards a tangible asset, that 10Xs your post.

02:32:45 - Brandon Hancock
So if you were, like, if you were to do nothing else but just try and go on LinkedIn, that's all I would do.

02:32:50 - Brandon Hancock
Like, you know, if you were, I think you're focusing on this full time right now.

02:32:53 - Brandon Hancock
So like, I would, one a day, wake up in the morning, build an asset in the evening, share the asset on LinkedIn.

02:33:00 - Brandon Hancock
Rinse and repeat, and man, dude, you're just going to explode.

02:33:03 - Brandon Hancock
You're going to be busy responding to comments nonstop, which is a good problem to have because you're going to get to talk to a thousand really cool people, but it is the fastest way for growth.

02:33:12 - Brandon Hancock
So the second you make one, please send it to me.

02:33:15 - Brandon Hancock
I'll be happy to review and give you a few pointers of like, hey, on LinkedIn, I would tweak this or tweak that.

02:33:20 - Brandon Hancock
So just tag me on LinkedIn so I can – or just shoot me a DM on LinkedIn so I can help.

02:33:26 - Brandon Hancock
Okay, cool.

02:33:27 - Robert
Thank you much.

02:33:28 - Robert
I guess that's it for my questions for this week, and thank you much as always.

02:33:32 - Brandon Hancock
And I learned a lot from everybody this week, so thanks, everybody.

02:33:36 - Brandon Hancock
So many golden nuggets today.

02:33:38 - Brandon Hancock
Seriously, so many golden nuggets.

02:33:40 - Brandon Hancock
All right, perfect.

02:33:41 - Brandon Hancock
Neel, you're up next, man.

02:33:43 - Neel More
What's going on?

02:33:44 - Neel More
Hey, I'm doing good.

02:33:46 - Neel More
I was trying to share my screen.

02:33:48 - Neel More
Is my screen visible?

02:33:50 - Brandon Hancock
Yep.

02:33:51 - Brandon Hancock
All right.

02:33:52 - Brandon Hancock
80K.

02:33:54 - Brandon Hancock
80K run.

02:33:55 - Brandon Hancock
Yep.

02:33:55 - Neel More
Looks great.

02:33:56 - Neel More
Yeah.

02:33:56 - Neel More
Okay.

02:33:56 - Neel More
Good.

02:33:56 - Neel More
Yeah.

02:33:57 - Neel More
Just wanted to give a demo or the app.

02:34:00 - Neel More
I was creating, okay, so this is like an app for, like, you will be running your machine learning pipeline, but before that you get the data, right?

02:34:08 - Neel More
And on top of that data, I was doing the data analysis, as well as I was doing the data drift.

02:34:15 - Neel More
So now, for example, this is my user prompt, okay, and this is the data, so which is had given to check around whether to do the analysis.

02:34:25 - Neel More
And here, the coordinator comes as an agent for us, and it checks around, okay, no data drift is there, and whether there are duplicate columns, but as this is a sample data, you will see that there won't be any changes, and I'm giving the same file, and then it asks a human loop in this, whether you want to run your machine learning pipeline or not, and the reason is like to check whether the churning in this case, so let's say if I say yes, now only our agent will run the pipeline, but at the end, it will also get the predictions of it, like what was the outcome of

02:35:00 - Neel More
And I wanted to create a loop event so that if the score is less, then it will go and rerun the pipeline with some hyperparameter tuning.

02:35:08 - Neel More
So this is just a quick example I wanted to give around.

02:35:11 - Neel More
And this is where you can see your experiments in this case.

02:35:15 - Neel More
And the reason why I was making this, so you can see all this matrix, the model matrix, everything is here in this case.

02:35:23 - Neel More
And the reason why was doing this thing, because I want to create the portfolio as Robert was doing, so I'm creating my portfolio.

02:35:30 - Neel More
But I'll just stop here.

02:35:32 - Neel More
And so while doing this thing, I was learning a lot.

02:35:35 - Neel More
So I was doing the name mistakes, like the business mistake.

02:35:38 - Neel More
I was using cursor AI, the chat GPT to create everything.

02:35:42 - Neel More
But as the Gemini model also, right, it doesn't know the latest documentation.

02:35:48 - Neel More
And it was creating their own wrappers and the patterns on top of it.

02:35:52 - Neel More
And what you mentioned today, the context seven, that's the next step I was going to try.

02:35:56 - Neel More
So good you mentioned about that.

02:35:58 - Neel More
And also my basics were not.

02:36:00 - Neel More
So once I can go to ADK, and I'll start reading the documentation, I got only one question for Brandon, for you, right?

02:36:07 - Neel More
Have you used the custom agents anywhere so far?

02:36:10 - Neel More
Do you got any example?

02:36:12 - Neel More
Or even if you got a similar example where the custom agents can be applicable, that would be great to know.

02:36:19 - Brandon Hancock
So I have not used ADK custom agents yet, but just a quick recap for everybody.

02:36:26 - Brandon Hancock
Basically, what custom agents do is there's a core agent life cycle, and within a custom agent, you basically get to tap into the life cycle of an agent and, you know, do things differently.

02:36:39 - Brandon Hancock
For example, if you potentially needed to do some sort of authentication is the usual example.

02:36:45 - Brandon Hancock
There's a step in there to where you could have the agent authenticate before it proceeds with doing a certain task.

02:36:52 - Brandon Hancock
So that's the usual example you'll see for custom agents.

02:36:56 - Brandon Hancock
So, but yeah, short answer is no.

02:36:59 - Brandon Hancock
Out of curiosity,

02:37:00 - Brandon Hancock
Neha, what were you thinking of doing and maybe there's a quick workaround to where we don't have to use custom agents?

02:37:05 - Neel More
Neha, so the reason was like while I was going through the documentation, right, so I got the concept of the parallel and all the sequential and I was just wondering where is the use case of the custom agent in this case and is there really a use case where I will need to go in that line because then we have to implement or what do you say, I have to implement some APIs in that case or the functions.

02:37:29 - Neel More
Neha, I was just wondering to check with you, have you use anywhere so far in your projects or something?

02:37:35 - Brandon Hancock
Neha, so short answer is no, have not had to use custom agents.

02:37:40 - Brandon Hancock
Neha, usually it's like the order of operations, like to solve the problem, like okay, first, you know, can we just be fancy with the prompt to get it to work?

02:37:50 - Brandon Hancock
Neha, the answer is no, okay, well then the usual next step I will look at is to work with the callbacks that are provided.

02:37:58 - Brandon Hancock
Neha, of ADK.

02:38:00 - Brandon Hancock
So the agent callback, tool callback, or the model callback, 90% of the time, I can get away with like, oh, I actually, before this agent kicks off, I'll update the before agent callback, I'll trigger that, alter whatever I need to do, update state, make a change, upload information, download information, whatever I need to do, I'll do that in the before agent callback.

02:38:24 - Brandon Hancock
And that's 90% of the time, like you can get away with just doing that, I have not seen yet a need, and just for stuff I've done, I haven't had to use the custom agent callback yet, or just create a custom agent, so I haven't had to do that yet.

02:38:40 - Brandon Hancock
The other option, there was a third one, which is a loop agent, so usually between loops and, you know, sequential agents, I'm usually able to get what I need done toward the loop agent.

02:38:53 - Brandon Hancock
Just like, try to achieve this goal, go through this sequence, did you get to the goal?

02:38:58 - Brandon Hancock
No, do it again.

02:39:00 - Brandon Hancock
Pry that three times.

02:39:00 - Brandon Hancock
Like, usually, that's the typical workflows that I've had to do.

02:39:05 - Brandon Hancock
So, but, I mean, it looks like in your application, you were doing sequential workflows and everything, right?

02:39:10 - Brandon Hancock
Like, it looks like it was doing really well, right?

02:39:13 - Neel More
Yeah, yeah.

02:39:14 - Neel More
And because this chat GPT was giving me the sequential and everything, and I thought, okay, it's not the right time to go at once because I was going to do a lot of – I got a huge PRD which had created MVP, but it was creating more like an AgentOps platform.

02:39:27 - Neel More
And I thought, okay, I'll stop here and I'll just go and read the ADK functionality.

02:39:32 - Neel More
Okay.

02:39:33 - Brandon Hancock
I gotcha.

02:39:33 - Neel More
for Yeah, of course.

02:39:35 - Brandon Hancock
Of course, Neel.

02:39:35 - Brandon Hancock
Robert, I saw you had a few quick questions.

02:39:39 - Robert
Yeah.

02:39:39 - Robert
So, a similar thing that Neel ran into when I was using ChatGPT or Gemini, to go from requirements documents to, like, partitioning across to different agents.

02:39:51 - Robert
So, at first, the code was producing a class.

02:39:54 - Robert
So, as opposed to using the Agent object directly, it was creating, a wrapper class around, as Neel was mentioning.

02:39:59 - Robert
So, basically, it tells –

02:40:00 - Robert
specifically to use the agent object, and another use of thing I found was adding the actual link to the documentation inside whatever you're doing, so it has direct reference to the documentation.

02:40:13 - Brandon Hancock
Yeah.

02:40:13 - Brandon Hancock
Have you seen how to do that, Neel?

02:40:14 - Brandon Hancock
I can show real fast if you haven't had to do that before.

02:40:17 - Neel More
Yeah, I've seen how you can add the docs in the cursor.

02:40:20 - Neel More
Yeah, so I was able to check that.

02:40:22 - Neel More
Yeah, that's one thing, and then I came across Context 7 while I was going around, because I planned to create my own rag, and then suddenly I found those things.

02:40:29 - Neel More
So I was happy to find that.

02:40:31 - Brandon Hancock
Yeah, I was trying to look really fast to see if Context 7 has access to the latest ADK documents.

02:40:40 - Brandon Hancock
I guess so, I guess so, was checking.

02:40:42 - Neel More
So I guess so, it has.

02:40:45 - Brandon Hancock
I'm going check real fast, too.

02:40:47 - Brandon Hancock
I'm going to share my screen.

02:40:50 - Brandon Hancock
We'll tag team this real fast.

02:40:52 - Brandon Hancock
Use Context 7.

02:40:57 - Brandon Hancock
To the Python, the Google.

02:41:01 - Brandon Hancock
ADK, library, and – we'll see if it we'll see if it does it.

02:41:10 - Brandon Hancock
Well, I probably should have used – all right.

02:41:12 - Brandon Hancock
So, yeah, this is context 7 in action.

02:41:14 - Brandon Hancock
It's looking up the library ID.

02:41:17 - Brandon Hancock
I think it found it, maybe?

02:41:21 - Brandon Hancock
Oh, my gosh, it did.

02:41:26 - Brandon Hancock
Yeah, that's cool, guys.

02:41:28 - Brandon Hancock
It does it.

02:41:28 - Brandon Hancock
It has it.

02:41:29 - Neel More
Yeah.

02:41:30 - Neel More
Go context 7.

02:41:33 - Brandon Hancock
Yeah, this is crazy.

02:41:34 - Brandon Hancock
it literally has all of it.

02:41:35 - Brandon Hancock
So, yeah, it has everything.

02:41:37 - Brandon Hancock
So, I'm hoping this is the latest version.

02:41:39 - Brandon Hancock
I'm trying to figure out – we can actually stop it really fast.

02:41:44 - Brandon Hancock
Let's just change it to a quicker model.

02:41:48 - Brandon Hancock
What version of the Python ADK docs do you have access to in context?

02:41:57 - Brandon Hancock
I just want to make sure it's the latest one just because, like, they did cut –

02:42:00 - Brandon Hancock
That new version, yeah, it's not probably 100% because I think they're at version 1-something, but it's, you know, yeah, so they have a new minor cut, but, you know, overall, this is probably way better than, you know, the old version, which was sub 1, sub being at stable.

02:42:20 - Brandon Hancock
So, yeah, that's crazy.

02:42:22 - Brandon Hancock
Context 7, for the win.

02:42:24 - Neel More
Cool.

02:42:24 - Neel More
Thanks.

02:42:25 - Neel More
Thanks for seeing, like, this thing, how we can check the version.

02:42:27 - Brandon Hancock
Thank you, Ahmed.

02:42:27 - Brandon Hancock
Yeah, of course.

02:42:29 - Brandon Hancock
All right, guys, uh, any final, um, Bastian, you want to hop on?

02:42:33 - Brandon Hancock
I didn't know if anyone else hasn't got a hop on yet, but they would like to.

02:42:37 - Brandon Hancock
Always happy to.

02:42:37 - Bastian Venegas
would just like to, share my screen for 90 seconds for, uh, uh...

02:42:42 - Brandon Hancock
Yeah, of course, sure.

02:42:45 - Brandon Hancock
Always love to see a Bastian special.

02:42:48 - Bastian Venegas
Nah, you, you already saw this one, but...

02:42:54 - Bastian Venegas
Yeah, so, um, where is it?

02:42:58 - Bastian Venegas
Thanks, Father.

02:42:58 - Bastian Venegas
...

02:43:00 - Bastian Venegas
I want to share my desktop.

02:43:07 - Bastian Venegas
Share computer sound.

02:43:10 - Brandon Hancock
Okay.

02:43:11 - Brandon Hancock
Oh, yeah, I got to follow up with him.

02:43:12 - Brandon Hancock
By the way, I will do that right after this.

02:43:15 - Brandon Hancock
Yeah.

02:43:18 - Bastian Venegas
Well, this is just like a proof of concept of a real-time multimodal agent, because most of them go through, like, the text phase at some point, and this is just using Gemini, and leveraging its built-in Google search tool.

02:43:34 - Bastian Venegas
So, I hope you can hear this.

02:43:50 - Bastian Venegas
Yeah, yeah.

02:43:51 - Bastian Venegas
I would like to know if some of my favorite artists will be touring South America during 2025 or 2026.

02:43:57 - Bastian Venegas
years.

02:43:59 - Bastian Venegas
So, I

02:44:00 - Bastian Venegas
Yes, Dua Lipa is scheduled to bring her radical optimism tour to Latin America in late 2025, including a stop in Santiago, which is great news.

02:44:10 - Bastian Venegas
As for the weekend, there...

02:44:13 - Brandon Hancock
Thank you.

02:44:16 - Brandon Hancock
You're welcome.

02:44:17 - Brandon Hancock
Let me know if have any other questions.

02:44:19 - Brandon Hancock
Lastly, quick question.

02:44:21 - Brandon Hancock
Do you know who Brandon Hancock is?

02:44:24 - Brandon Hancock
He's an AI developer that has a YouTube channel.

02:44:28 - Brandon Hancock
Can you find his YouTube channel handle?

02:44:36 - Brandon Hancock
Yes.

02:44:37 - Brandon Hancock
Brandon Hancock has a YouTube channel dedicated to AI development.

02:44:41 - Brandon Hancock
You can find his channel under the handle at AI with Brandon.

02:44:45 - Brandon Hancock
He creates videos that teach developers how to build full-stack AI applications.

02:44:51 - Brandon Hancock
Did he publish any videos during June?

02:44:57 - Bastian Venegas
Yes.

02:44:58 - Bastian Venegas
Brandon Hancock published a video on June 11th.

02:45:00 - Bastian Venegas
...7th, 2025, titled Agent-to-Agent A-to-A Crash Course, Full Walkthrough with Real...

02:45:05 - Bastian Venegas
Yeah, so that's mostly it, just to showcase that video was recorded, like, June 12th, and Brandon had uploaded his video just the day before, so it was kind of a fun way to show it was working.

02:45:19 - Brandon Hancock
That's awesome.

02:45:20 - Brandon Hancock
And just real quick, just to give some more background, too, so just because I think it's cool for the group to know.

02:45:27 - Brandon Hancock
Sebastian and I were working on a potential client project, and basically they wanted a voice agent.

02:45:34 - Brandon Hancock
They had some certain requirements, such as they eventually went to scale to include phone numbers, and, you know, long story short, they're working to help out elderly patients that just want to have someone to chat with.

02:45:46 - Brandon Hancock
And we were going to go 80K at first, but with the requirement of having to use a phone number, Bastian found a really cool tool called LiveKit, which basically allows you to have...

02:46:00 - Brandon Hancock
Like, all the benefits of code, like, you can code the entire workflows, everything, but it also had some background support or additional functionality to include integrating phone numbers at a later point, which is awesome, because, you know, they'll just type in, call, it'll have all sort of content, like, it'll have context, it'll be able to do tool calls, just like you saw what Bastian was showing, so Bastian whipped up a cool little MVP, so got to follow up with him, because they dropped off, but yeah, Bastian was, finding the cool stuff, so.

02:46:28 - Bastian Venegas
Yeah, and the coolest thing is that I got to connect it to a phone number I purchased, just to test if it would work, and it doesn't, and the latency is pretty much the same, it's, I don't notice any difference, so that was very cool, and it's also a way to have access to AI, when you don't have any access to internet.

02:46:54 - Bastian Venegas
You could literally call this from your phone, like, a regular phone, not even a mobile phone.

02:47:00 - Bastian Venegas
So that's a cool use case.

02:47:03 - Brandon Hancock
And final question, I can't remember, so it did have interrupts or it didn't have interrupts?

02:47:07 - Bastian Venegas
I cannot remember.

02:47:08 - Bastian Venegas
It does have interrupts, yeah.

02:47:10 - Brandon Hancock
Okay, cool.

02:47:11 - Brandon Hancock
And just a quick background, interrupts are the way, like interrupt across all, like your OpenAI models, Google models, interrupt is the word and the phrase for all voice agents for it to detect the person's trying to speak over the agent and the agent needs to stop.

02:47:27 - Brandon Hancock
So that's, um, um, that's in insanely important when trying to build anything real life for voice agents is having, um, yeah, um, interrupts.

02:47:36 - Brandon Hancock
So, yeah, Bastian, once again, finding all the cool stuff.

02:47:39 - Brandon Hancock
So, okay, guys.

02:47:41 - Brandon Hancock
Well, this was seriously insane call.

02:47:43 - Brandon Hancock
Love to see all the cool things that you're, you're working on.

02:47:46 - Brandon Hancock
I'll post the recording.

02:47:47 - Brandon Hancock
usually takes like a few minutes to process, but I'll post it here a little bit later tonight, just so you guys can, um, if there was any action items or anything you want to replay, I'll post it so you guys can, can watch it.

02:47:57 - Brandon Hancock
But yeah, always love looking forward to Tuesdays to see all of you.

02:48:00 - Brandon Hancock
See.

02:48:00 - Brandon Hancock
All the cool things you're working on, and I will keep you posted on, first off, the new, speaking of interrupts, the LangChain Interrupt Conference.

02:48:09 - Brandon Hancock
I'll hopefully be working on that video tomorrow.

02:48:11 - Brandon Hancock
Outside of that, I will keep you posted when we lock down the Dan Martell live guest session, probably next Tuesday, but the one after, July 1st.

02:48:23 - Brandon Hancock
And I will also keep you guys posted as I work on the ship kit, which will include a ton of templates, courses, and everything to help you guys launch AI applications.

02:48:33 - Brandon Hancock
So I'll be doing a post on that later this week.

02:48:36 - Brandon Hancock
I want to definitely get some more feedback on, like, you know, I'm building it this way.

02:48:41 - Brandon Hancock
Just want to make sure, oh, you know, see if you guys have any suggestions or cool feedback that you would like to see implemented so it's even, you know, more valuable.

02:48:48 - Brandon Hancock
So I'll be posting some of that and hopefully even maybe some early access to some of the cool prompts and templates.

02:48:54 - Brandon Hancock
Just as a special thank you to everyone in the community.

02:48:57 - Brandon Hancock
So I will keep you posted on that front, too.

02:48:59 - Brandon Hancock
So.

02:49:00 - Brandon Hancock
Yeah, that's everything.

02:49:01 - Brandon Hancock
Yeah, I hope you guys have a great Tuesday, and see you next week, okay?

02:49:06 - Brandon Hancock
Thanks, everybody.

02:49:06 - Brandon Hancock
Bye, guys.

02:49:07 - Brandon Hancock
Have a great night.

02:49:08 - Brandon Hancock
See ya.

02:49:08 - Brandon Hancock
Bye.

