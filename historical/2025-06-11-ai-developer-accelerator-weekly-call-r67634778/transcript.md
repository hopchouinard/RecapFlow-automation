00:01:03 - Mitch
Thank you.

00:01:50 - Mitch
How's it going, Paul?

00:01:55 - Paul Miller
Good, Mitch.

00:01:56 - Paul Miller
How are you?

00:01:57 - Mitch
Good.

00:01:58 - Mitch
know, you started your day as...

00:02:01 - Mitch
It's close to the end of mine, right?

00:02:03 - Paul Miller
Oh, yeah.

00:02:05 - Mitch
Getting some good work done, managing clients, and trying to keep this project moving forward.

00:02:12 - Mitch
Kind of thrifted it out, and now it's time to actually build a realistic software stack.

00:02:18 - Paul Miller
Yeah, yeah, yeah.

00:02:20 - Paul Miller
Comes the time, we've got to get it right.

00:02:24 - Mitch
Yeah, Airtable can only do so much, and I'm like, yeah.

00:02:28 - Mitch
Yeah, it's unfortunate, because you're, like, tech debt, but also at the same time, it's, like, exciting.

00:02:34 - Mitch
It's, like, now actually have it be, like, what you want it to be.

00:02:38 - Paul Miller
Yeah, yeah, yeah.

00:02:39 - Paul Miller
Well, I've enjoyed working with the fast API stuff.

00:02:43 - Paul Miller
It's been good.

00:02:45 - Paul Miller
Having a nice separate segregated back-end part that I can control, and without having to take on the complexity of dealing with JavaScript-based or TypeScript.

00:03:00 - Paul Miller
Script-based backend stuff, which I just couldn't do.

00:03:03 - Paul Miller
It's good for the frontend and maybe get lovable to generate the code or cursor, but I really want to control the backend because if you don't have that right, then you're kind of stuffed.

00:03:16 - Mitch
I see.

00:03:17 - Mitch
So basically you're backend pure Python based and you use Fathom, you got to manage that.

00:03:23 - Paul Miller
Yeah.

00:03:23 - Paul Miller
Yeah.

00:03:24 - Mitch
Yeah.

00:03:25 - Mitch
I haven't watched Brandon's course.

00:03:27 - Mitch
I've been going through it.

00:03:31 - Mitch
And yeah, it's kind of like the thing that scares me is the typescript end of it all.

00:03:35 - Mitch
And I'm just like, yeah, it's like a little, but like with how lovable and super-based like connect together, I'd say it's pretty good for someone who like semi-knows stuff.

00:03:48 - Paul Miller
Yeah.

00:03:56 - Paul Miller
I'm on board now.

00:04:00 - Brandon Hancock
I'm on board now.

00:04:00 - Brandon Hancock
Thank you.

00:04:00 - Brandon Hancock
What's up, gang?

00:04:02 - Paul Miller
Hey, Brayman.

00:04:04 - Brandon Hancock
Hello, hello.

00:04:05 - Brandon Hancock
Hope everyone's having an awesome week so far.

00:04:09 - Brandon Hancock
Let me get everything ready, and we'll start the fun.

00:04:15 - Brandon Hancock
All right, cool.

00:04:16 - Ty Wells
I take it you're going to tell us about the world sphere, the AI engineering, because you're wearing the t-shirt.

00:04:21 - Ty Wells
You're promoting it.

00:04:23 - Brandon Hancock
I know, I know.

00:04:24 - Brandon Hancock
I only have so, so much AI swag, so I have to represent on my calls, make it look like I know what I'm doing, you know?

00:04:34 - Brandon Hancock
If you have enough AI words on your shirt, they assume you know what you're doing, you know?

00:04:40 - Brandon Hancock
But, yeah, hope everyone's having an awesome week.

00:04:43 - Brandon Hancock
Just taking a screenshot so I can share the call order for today.

00:04:47 - Brandon Hancock
But, also, welcome if it's your first time to the call.

00:04:51 - Brandon Hancock
Love to have new developers and everyone else hopping on.

00:04:56 - Brandon Hancock
Quick lay of the land.

00:04:58 - Brandon Hancock
Usually, the way we go about these calls is we go...

00:05:00 - Brandon Hancock
So I just dropped a screenshot, but that's the order we'll go for calls, so kind of first come first serve, and basically when we're going around the room, usually keep it to around like six to eight minutes, so that way everyone has a chance to go, and usually just talk about like problem that you're having, happy to help as a team, or any cool AI news or anything that you think the group would find interesting.

00:05:20 - Brandon Hancock
So that's the lay of the land, and I just dropped the order in the chat.

00:05:25 - Brandon Hancock
So that's the call order for today.

00:05:28 - Brandon Hancock
Quick updates for you guys before we kick things off.

00:05:33 - Brandon Hancock
Just wrapped up an A-to-A tutorial for you guys, so agent-to-agent tutorial, just describing exactly how the protocol works, some simple examples, and then pretty excited because the last example in the video, I haven't seen anything else like it on YouTube, but it's basically you have an A-to-A agent that's using the A-to-A protocol to talk to a CRI agent, a land graph agent, and another ADK agent, so it's like the full shebang.

00:06:00 - Brandon Hancock
It's taken way too long to make and record, so I apologize for the delay.

00:06:04 - Brandon Hancock
A2A kicked my butt, but I finally figured out how to do it and make it simple for you guys.

00:06:08 - Brandon Hancock
So that'll be in the video, hopefully actually coming out tomorrow.

00:06:12 - Brandon Hancock
So I told my editor to be on the lookout for it.

00:06:15 - Brandon Hancock
So that'll be fun.

00:06:16 - Brandon Hancock
So yeah, that's everything on my end.

00:06:18 - Brandon Hancock
And we'll see.

00:06:21 - Brandon Hancock
No, I mean, I had so much fun with ADK.

00:06:24 - Brandon Hancock
ADK, still absolutely loving it.

00:06:28 - Brandon Hancock
But yeah, literally zero negative things at this point to say about ADK.

00:06:34 - Brandon Hancock
I will, a quick update for future videos.

00:06:37 - Brandon Hancock
They released, as we saw on last week's chat, basically the like fast API for it.

00:06:43 - Brandon Hancock
So it's basically ADK, how do you just quickly expose it to where that it's a website that you can almost like chat with or an API endpoint that you can chat with.

00:06:50 - Brandon Hancock
I will be doing a video on that late next week.

00:06:54 - Brandon Hancock
So, so a lot of people had questions on deploying ADK agents and that will be, that's on the roadmap.

00:06:59 - Brandon Hancock
So yeah.

00:07:00 - Brandon Hancock
So that'll be fun.

00:07:02 - Brandon Hancock
So I know I'm pumped.

00:07:03 - Brandon Hancock
I'm pumped.

00:07:04 - Brandon Hancock
All right.

00:07:04 - Brandon Hancock
We'll start going around.

00:07:05 - Brandon Hancock
Robin, Mitch, you are up first, man.

00:07:08 - Brandon Hancock
What awesome stuff have we been working on?

00:07:11 - Mitch
Oh, it's been good.

00:07:13 - Mitch
I haven't hopped on one of these calls in a while.

00:07:16 - Mitch
But yeah, for everyone's info, working on this tool where I basically input a series of prompts that have like a seed idea and then like a kind of clone ideas from Do you want show the screenshot or the main page?

00:07:33 - Brandon Hancock
think it's pretty cool looking.

00:07:35 - Brandon Hancock
Let me click the button for you.

00:07:36 - Mitch
Oh, okay.

00:07:37 - Mitch
appreciate it.

00:07:38 - Brandon Hancock
All yours, man.

00:07:46 - Mitch
So yeah, we have like an Airtable where we have just different like series of stories and then those stories would have kind of sub columns or data points underneath it.

00:07:56 - Mitch
Then when we press this button, it will then create a rescape.

00:08:00 - Mitch
And of that idea to then create a series of shots, those shots are just like a long list of describing what each scene is.

00:08:11 - Mitch
So then when we do the request to the Google Image Gen API, then we can generate the large list of shots they load.

00:08:23 - Mitch
Oh, there we go.

00:08:25 - Mitch
And yeah, basically from here, then we generate the videos.

00:08:31 - Mitch
But basically this takes the bulk of the work.

00:08:34 - Mitch
It's really creating the shots is key.

00:08:38 - Mitch
And if you're curious why we have to generate four, it's because sometimes Image Gen messes up.

00:08:44 - Mitch
But yeah, and so basically Airtable has been great, but it also has like its limitations as far as like shot selection and stuff like that.

00:08:52 - Mitch
So basically starting to like map out like, hey, what do I want each page to look like?

00:08:57 - Mitch
What do I want to do?

00:08:58 - Mitch
Where are my questions?

00:09:00 - Mitch
can ask thing You will

00:09:00 - Mitch
And, like, how is it going to be organized and stuff?

00:09:03 - Brandon Hancock
That's looking clean, man.

00:09:05 - Brandon Hancock
Yeah, real quick.

00:09:06 - Mitch
Yeah, your course is helpful.

00:09:09 - Brandon Hancock
Thanks, man.

00:09:09 - Brandon Hancock
The thing I was going to say is I got to talk to Mitch earlier and just going through how, like, he has a very cool process that he did in Airtable.

00:09:19 - Brandon Hancock
And it's like, how do you actually turn this into an application that you can use, like, you know, in a more scalable format than Airtable?

00:09:27 - Brandon Hancock
So it's cool to see that it's, you're like, dude, you're doing the work, man.

00:09:31 - Brandon Hancock
And it's actually, like, it's really coming together.

00:09:33 - Brandon Hancock
So this is absolutely loving it.

00:09:35 - Brandon Hancock
Have we got to code yet, or are still in wireframe?

00:09:38 - Mitch
Yeah, honestly, the coding part has been a little bit scary just because of all the TypeScript and stuff.

00:09:45 - Mitch
Like, I haven't been on that train yet.

00:09:47 - Mitch
So excited for it, but also really, like, postponing it a little bit.

00:09:53 - Brandon Hancock
I got you.

00:09:53 - Brandon Hancock
Yeah, the unknown, man.

00:09:54 - Brandon Hancock
That's the worst part is.

00:09:56 - Brandon Hancock
But, hey, I mean, it's not going to blow up.

00:09:58 - Mitch
So, you know, what's the worst that can happen?

00:10:00 - Mitch
No, 100%.

00:10:00 - Mitch
Hopefully I'm not sharing too much, but this section right here has been, like, the most helpful as far as just, like, what do I need to think about before I even, like, hop into the code of things.

00:10:13 - Mitch
And so, yeah, I really liked it.

00:10:14 - Mitch
I think the one thing I would like in the future is, like, a checklist.

00:10:19 - Mitch
So, like, when we go into, like, this section, it's, like, a to-do list of, like, okay, if you have a project, here's, like, an example task, and then here's, like, your task, and, you know, please fill this in and do, like, that checklist.

00:10:31 - Mitch
That'd be, like, really cool, because that's what I had to do, kind of, after these videos.

00:10:35 - Mitch
Because the other ones I noticed were, like, really good at it, but the higher level ones, it's always a little bit more complicated to, like, here's this key thing, but yeah.

00:10:45 - Brandon Hancock
Awesome feedback.

00:10:45 - Brandon Hancock
No, I appreciate that.

00:10:46 - Brandon Hancock
That's the goal for ShipKit.

00:10:49 - Brandon Hancock
That's the goal, is to actually make everything just, like, simpletized GPTs to help you with everything, kind of, like, with the AI Authority Accelerator.

00:10:57 - Brandon Hancock
So, like, that's the goal.

00:10:59 - Brandon Hancock
But I love that you like them all.

00:11:00 - Brandon Hancock
Pauline Vue Park, because like, seriously, like most developers are just like, oh, I need to code.

00:11:03 - Brandon Hancock
And it's like, no, no, no.

00:11:04 - Brandon Hancock
Before you even code, you need to figure out what the heck you're trying to build.

00:11:07 - Brandon Hancock
So, um, just to make sure you're starting off with the right foundation.

00:11:10 - Brandon Hancock
So, uh, but yeah, I totally understand where you're coming from.

00:11:14 - Brandon Hancock
Definitely should have added something like that.

00:11:16 - Mitch
But yeah, it's been great.

00:11:17 - Mitch
I'm excited to hop into the code of things.

00:11:19 - Mitch
Just wanted to update everyone here and, you know, dude, absolutely love it.

00:11:24 - Brandon Hancock
Hey, well, seriously, um, next steps, just like, just so everyone else can, you know, get some feedback too.

00:11:30 - Brandon Hancock
Uh, if I was in Mitch's shoes, what I would do next is as soon as he gets done wireframing it, I'd hop over to lovable and just have lovable mock up the entire application.

00:11:40 - Brandon Hancock
You're going to pay 20 bucks probably to like, have it do the work for you, but you're going to have a full blown MVP that you can go like, hmm, does this workflow even work for what I'm trying to do from a UI perspective?

00:11:53 - Brandon Hancock
And then once you're done with that, cool.

00:11:55 - Brandon Hancock
You now have a get repository that you can just like pull down to your.

00:12:01 - Brandon Hancock
And then you can always like, hey, start building that page from the lovable app, but yeah, so that's next steps, so I'm very pumped to see where you go in there.

00:12:11 - Mitch
My that one is, so how far do you kind of document the database and like the valid values within the database?

00:12:18 - Mitch
Because like on the course that you were talking about, forgot what you call them, but basically you had different databases before we even hopped into the wireframe part, or maybe I might be mistaken.

00:12:29 - Brandon Hancock
Yeah, just data models, yeah, I mean, I just keep data models as the core information that's necessary.

00:12:36 - Brandon Hancock
So like if it's a person, name, phone number, email, like whatever the core information is, just high level, what value and a quick description.

00:12:45 - Brandon Hancock
And that's usually enough, especially when you hop over to lovable, for it to understand what the key data types are.

00:12:51 - Brandon Hancock
And it's just going to make dummy data anyway, so it's not like we're making like, there is no database in lovable.

00:12:56 - Brandon Hancock
It's all just fake dummy data, so you don't have to get.

00:13:00 - Brandon Hancock
Okay.

00:13:00 - Brandon Hancock
Okay.

00:13:00 - Brandon Hancock
Okay.

00:13:00 - Brandon Hancock
It's insanely technical with like data model ID, it's a UUID, like you don't have to do any of that, you're just like, there's a person, he has an ID.

00:13:07 - Mitch
Oh, yeah.

00:13:08 - Brandon Hancock
Because all we're trying to do is just say, do I like this workflow in Lovable?

00:13:12 - Brandon Hancock
That's all we're trying to do.

00:13:14 - Mitch
Yeah, I got mixed up because there's someone else who does Lovable and they connect with the Superbase.

00:13:19 - Mitch
And I'll have to chat with you guys to see what's the pros and cons of that versus the other, but yeah.

00:13:25 - Brandon Hancock
Yeah, happy to answer any questions.

00:13:29 - Brandon Hancock
High level, real fast though, I'm not the biggest fan of keeping the project in Lovable.

00:13:34 - Brandon Hancock
I want Lovable to go from zero to one, and then I want to be in Cursor as quickly as I can.

00:13:39 - Brandon Hancock
And I specifically want to be doing a Next.js application.

00:13:43 - Brandon Hancock
So if you look, what they actually create, it's a Vite project, and it's not the same.

00:13:54 - Brandon Hancock
Let me show you real fast.

00:13:56 - Brandon Hancock
Let me pull this screen up over here.

00:13:59 - Brandon Hancock
Yeah, so.

00:14:00 - Brandon Hancock
So, share, share, basically, like, when they're building out applications, I don't think it's a full-blown Next.js application, it's a lot more just, I think, what they're doing is a much more simple, lightweight framework that is just really good at quickly cranking out, you know, static pages in, like, very shallow, dynamic pages, so, yeah, you end up hitting a wall, at least, I feel like, when I'm using Byte, I hit a wall, when I'm like, no, I actually want to fetch the data here as a server action, and then I want to pass it down to my client component, like, there's a lot of walls that you're going to hit with Byte, so, as quickly as I can, I get out of there and go to Next.js, once I'm happy with the layout, so, yeah, that's, yeah, happy to talk more, so we can keep you cruising, absolutely love building out collapse, man, so, keep up the good work, Mitch, pumped, so.

00:14:55 - Mitch
Thank you.

00:14:56 - Brandon Hancock
Perfect, all right, Juan, you're up next, man.

00:15:03 - Juan Torres
Are you going to me?

00:15:04 - Brandon Hancock
Yep, sounds great.

00:15:05 - Juan Torres
Awesome.

00:15:06 - Juan Torres
Hey, yeah, just, what did I do?

00:15:11 - Brandon Hancock
I had a presentation.

00:15:13 - Juan Torres
What was that?

00:15:15 - Brandon Hancock
The good news on the project?

00:15:17 - Juan Torres
Oh, yeah, yeah.

00:15:18 - Juan Torres
So I'm working with a client and deploying AI infrastructure, deploying the LLMs, and then the RAC system in order to manage And get tabular data to read that information.

00:15:34 - Juan Torres
So hopefully they're going to give us the keys to the data center pretty soon.

00:15:38 - Juan Torres
But essentially what I'm working with is a data center that has eight 100 NVIDIA graphic cards.

00:15:47 - Juan Torres
So they can handle pretty big models.

00:15:51 - Juan Torres
So I've got to figure out which open-sourced RAC system, vector, database, models I'm going to...

00:16:00 - Juan Torres
I use for that, I'm thinking of Lama Index in order to create the infrastructure in order to unify everything, but I'm open to suggestions in that sense.

00:16:15 - Brandon Hancock
So real quick, what functionality led you to picking Lama Index?

00:16:21 - Brandon Hancock
Like, is there certain things that you're like, oh, I'm mostly doing RAG requests?

00:16:25 - Brandon Hancock
Is that what you're mostly doing?

00:16:26 - Juan Torres
Yes, and it seems to be, has other infrastructure that is well, you know, what is it called?

00:16:38 - Juan Torres
Well modulated to handle tabular structure data.

00:16:42 - Juan Torres
Yeah.

00:16:43 - Juan Torres
So I'm not going to be fitting it PDF.

00:16:46 - Juan Torres
And it just seemed that Lama Index was had a comprehensive like integration of a lot of, you know, a lot of sets.

00:16:56 - Juan Torres
So that's, that's the reason why.

00:16:59 - Brandon Hancock
Okay, I got you.

00:16:59 - Brandon Hancock
No, totally makes sense.

00:17:00 - Brandon Hancock
Yeah, because it's mostly CSVs is everything you're working with, right?

00:17:04 - Brandon Hancock
For what you're doing?

00:17:05 - Juan Torres
they, yeah, they do have a PostgreSQL database.

00:17:10 - Juan Torres
So we're going to use the CSV files in order to test the RAC, you know, system, but at one point, I think we also want to transpose the PostgreSQL database into a backer database if necessary, right?

00:17:29 - Juan Torres
In order for that data to be, uh, funneled directly through, um, to the LLM.

00:17:35 - Juan Torres
Um, so that's, that's what I'm thinking.

00:17:38 - Brandon Hancock
Yeah, no, I mean, Lama Index is awesome.

00:17:42 - Brandon Hancock
Like, I mean, they've been around for a minute.

00:17:43 - Brandon Hancock
They, they definitely are more on the, like, data side of, like, of agents.

00:17:47 - Brandon Hancock
So I like that, like, just shallow, like, rule of thumb, definitely check out, absolutely understand where you're, where you're coming from.

00:17:55 - Brandon Hancock
real quick, only thing I would mention for instantly going from PostgreSQL to...

00:18:00 - Brandon Hancock
Ragland, I really think with just creating custom queries for data, like for each table, like you could probably get away with using just like custom SQL queries, like you don't always have to go to rag unless you're just doing like, the whole point of rag is like similarity searches for like, does this data similar to this data?

00:18:19 - Brandon Hancock
Like, you know, you could actually probably get away with just like creating three to five tools that are like, that do some sort of regular SQL command.

00:18:29 - Brandon Hancock
Uh, or more advanced SQL commands and just joins, you know?

00:18:33 - Brandon Hancock
So that's another approach.

00:18:35 - Brandon Hancock
heck, you can even have it kind of like a SQL tool that's just a read tool and all it can do is read and just give it unfettered access to all the tables and just say, hey, create your, create your queries in this read tool.

00:18:50 - Brandon Hancock
Um, so you can definitely get away with that too.

00:18:53 - Juan Torres
Yeah.

00:18:54 - Juan Torres
And I was thinking that it, perhaps the most dynamical way to deliver insights.

00:18:59 - Juan Torres
Yeah.

00:19:00 - Juan Torres
Yeah.

00:19:00 - Juan Torres
Yeah.

00:19:00 - Juan Torres
Yeah

00:19:00 - Juan Torres
Is if I were developed a SQL system that doesn't even need to use a backtraced database and can just use the tools for SQL query in order to do that.

00:19:10 - Juan Torres
I was actually thinking that too.

00:19:12 - Brandon Hancock
I think the second it starts making queries based on like, huh, what is the best month we had at our business?

00:19:20 - Brandon Hancock
And they just like, oh, I understand the table, the schemas.

00:19:22 - Brandon Hancock
Cool.

00:19:23 - Brandon Hancock
I'll just make the SQL query for you and instantly give you the data and potentially show it in a graph of some sort, because it can do that too.

00:19:28 - Brandon Hancock
Like you would have a second graph, um, uh, agent.

00:19:32 - Brandon Hancock
I mean, my God, like, like this is insane.

00:19:35 - Brandon Hancock
You know, it's like having a data scientist inside and all I have to do is ask you that question and boom.

00:19:39 - Brandon Hancock
So absolutely love, I, I'm, I cannot wait.

00:19:42 - Brandon Hancock
Hopefully you can showcase some of the things you build or maybe just like screenshots at a high level, but I think this is going to be a really awesome tool as you, uh, as you go for it.

00:19:50 - Juan Torres
Um, go ahead.

00:19:53 - Juan Torres
No, no, I just, uh, just wanted to ask one last question.

00:19:57 - Juan Torres
Uh, before that, before they give us access to the data center, um.

00:20:00 - Juan Torres
And,

00:20:00 - Juan Torres
Working in transforming a column that has descriptions.

00:20:05 - Juan Torres
It's just like language, normal language, right?

00:20:08 - Juan Torres
And so I'm trying to explore how I can extract the name of the vendor from that description into the vendor column that may have no entity, may have no characters inside.

00:20:25 - Juan Torres
And we might also have to extract the other information.

00:20:29 - Juan Torres
So I was just wondering if people had the knowledge on using Agentex systems to do that, or do you guys recommend me to use machine learning models like name entity recognition in order to extract that information from each one of the columns?

00:20:48 - Brandon Hancock
If anyone has any suggestions, I'd love to go at the end.

00:20:55 - Sam
Can you repeat the question, sorry?

00:20:57 - Sam
I thought I'd go ahead and catch all of it.

00:21:00 - Juan Torres
Yeah, it's essentially the extraction of vendor names from a column that is just text on the description of each row.

00:21:12 - Juan Torres
So imagine you have like each row having a one-point column that has the title description and just it has text, a lot of text in it.

00:21:21 - Juan Torres
And from that, what we want to do is identify the vendor name within that text, extract that character, and then transpose it into the column name vendor.

00:21:33 - Juan Torres
Because some of the times the vendor name is empty, so we just want to transpose that information.

00:21:40 - Juan Torres
And so right now I am thinking of two possibilities.

00:21:44 - Juan Torres
One is use just an agentic system that breaks down the task of finding that vendor name and other characteristics within that text.

00:21:54 - Juan Torres
Or use, you know, a machine learning model that's called name entity.

00:22:00 - Juan Torres
what doing with that.

00:22:00 - Juan Torres
Thank

00:22:00 - Juan Torres
The recognition that is specialized for this kind of stuff, uh, in order to carry out this, that task.

00:22:06 - Juan Torres
And so I'm just wondering if people had had the experience of having to use, um, you know, AI in order to extract information from, uh, a description column name entity recognition is one, by the way, I'm Al, everybody.

00:22:20 - Al Cole
I'll introduce myself further in a couple of minutes.

00:22:22 - Al Cole
Um, but that is what I've seen used.

00:22:26 - Al Cole
Um, and I come from the search space and, um, Um, that is a, uh, and even ones that don't have strong models, you can just have simple rules for them.

00:22:36 - Al Cole
can be pretty lightweight.

00:22:37 - Al Cole
Um, but if you've got a known list of entities that can feed it, otherwise you can pick from a collection of, um, captured entities, um, in a database that you could reference.

00:22:50 - Al Cole
So, um, I'll look up on the side, some I've been part of in the past to see if that might help jumpstart you.

00:22:57 - Brandon Hancock
Um, that's awesome advice.

00:23:00 - Sam
I think there's some good advice in the chat about, yeah, with a named entity recognition, if it's reasonably formulaic or determinative in the context, you probably want to, you could go with a machine learning, but I've had a lot of success with sort of turning an AI or just an LLM call into a named entity recognition through prompting, and it's, if the format is variable or it's not, you know, there's, there's maybe a little reasoning step, potentially you infer, inferring what the company name is, then I would go that approach using an AI to do it.

00:23:38 - Sam
And it doesn't have to be a strong one, like, I did a lot of my stuff back in the day on, like, some of the early big LLM models, you know, the early Mr.

00:23:47 - Sam
ones, and they, they handled it reasonably well if your prompt was there, so you don't have to go for the, the  beasts out there, it can be a small AI model to do it.

00:23:58 - Brandon Hancock
Absolutely love all the advice.

00:24:00 - Brandon Hancock
The, basically kind of going off of what was just discussed, like, if I was like in Python, Jupyter Notebook open in front of me, I mean, what I would do first is just like, like, um, I would probably go more of the AI route, just like GPT-41-nano, being so deep at this point, and what I would do is like, first, I'd go through the table, extract all existing business names, and then, um, and, um, so there, and I'd come up with a unique set, like, hey, here's exact examples of real-life businesses in there.

00:24:31 - Brandon Hancock
I'd also maybe pull out 10 examples of, like, here's a description, here's the company name, just to give the prompt some more instructions, and then finally, what I would do, um, I would, as I'm setting up the LLM call for row, I'd set up, you want to make sure you use, like, structured outputs of, like, hey, you are here to return a name, like, nothing else, no commentary, the raw name, or NA, or no, you know, something that's a keyword, um, then, um, so once I have that like,

00:25:00 - Brandon Hancock
Single call set up, so it's an LLM structured call, single shot, what I would do is per row, I would call that, but I would just save it to like an SCV at first, like the ID of the row, the company name, just so you can analyze it before you just accidentally go right to your database, 10,000 names when you're like, oh shoot, 20% of them were wrong, well now how do I roll it back, like, you know, so I would just save it to somewhere external first, then so you can validate it with your own eye, and then just do like a batch, you know, SQL, SQL write statement, but yeah, that's how I would tackle it, but seriously, everyone, love all the, love all the ideas.

00:25:37 - Brandon Hancock
So, dude, you're getting to work on the fun problems, man.

00:25:40 - Juan Torres
Yeah.

00:25:41 - Brandon Hancock
And if you do go down the GPT-4-1-nano, I'd love if you could let me know how much it costs.

00:25:46 - Brandon Hancock
My, I don't know how much data you're working with it, but like, I'm guessing like, 20 cent, and you could write, like, insane amount of data, like an insane amount, so I think you'll be, I think you'll be good, unless you're working with like terabytes, then yeah.

00:26:00 - Brandon Hancock
But probably megabytes are fine.

00:26:03 - Brandon Hancock
So, okay.

00:26:04 - Brandon Hancock
Perfect.

00:26:05 - Brandon Hancock
All right.

00:26:07 - Brandon Hancock
Next up, Alex, what's going on, man?

00:26:13 - alexrojas
Hey, guys.

00:26:14 - alexrojas
Good, good.

00:26:15 - Brandon Hancock
Hello, hello.

00:26:16 - alexrojas
Just getting some videos done.

00:26:19 - alexrojas
Also, I did a couple of videos, just the editing part.

00:26:23 - alexrojas
You know, Brandon, takes a long time.

00:26:28 - alexrojas
So, that's coming up.

00:26:30 - alexrojas
And I also, I just, also, I wanted to make a comment regarding Juan.

00:26:35 - alexrojas
I don't know if you have seen this video.

00:26:36 - alexrojas
I posted it now.

00:26:38 - alexrojas
It talks exactly about the data analyst, what Brandon was talking about.

00:26:43 - alexrojas
Like in that, I think that is one of the examples of Google ADK, that they have a data scientist that actually they do a sub-agent that makes those queries.

00:26:55 - alexrojas
And I think it's very close to what Brandon was saying.

00:26:59 - alexrojas
And you could...

00:26:59 - alexrojas
Okay.

00:27:00 - alexrojas
So some ideas from that analyst, it's pretty cool, very well explained as well.

00:27:07 - alexrojas
Great find, man.

00:27:08 - alexrojas
Yeah, yeah.

00:27:09 - Brandon Hancock
Great find.

00:27:10 - alexrojas
I think someone shared some video related last time and I just went through many of those.

00:27:19 - alexrojas
Also, I want, you know, I got addicted to uploading everything in railway.

00:27:25 - alexrojas
So I did the one on the voice agent and I set it up in railway.

00:27:34 - alexrojas
I just ran into one problem that everything works perfectly, but the date does not get updated unless I redeploy.

00:27:45 - Brandon Hancock
The date?

00:27:47 - alexrojas
Yeah, like the current time.

00:27:49 - alexrojas
So let's say next day I go and I say like, hey, everything works perfectly, but I just tell him like, hey, what day is today?

00:27:55 - alexrojas
And it's the day that I deployed my agent.

00:27:59 - Brandon Hancock
did not take per party.

00:28:00 - Brandon Hancock
With I if you did you

00:28:00 - Brandon Hancock
Would you mind sharing code, just like real fast, like your screen, and maybe I could point at it?

00:28:04 - alexrojas
Yeah, for sure.

00:28:05 - alexrojas
That's what I wanted to ask.

00:28:07 - alexrojas
So this is the one I share.

00:28:13 - alexrojas
Okay, so that's the agent.

00:28:14 - alexrojas
I just redeployed it.

00:28:15 - alexrojas
That's why it's right.

00:28:18 - alexrojas
Yeah.

00:28:19 - alexrojas
And I think I updated it here in Calendar Utils.

00:28:23 - alexrojas
According to me, that's where I made that every time the chat opens, it kind of calls to this last GetCurrentDateTime.

00:28:35 - alexrojas
But I redeployed it and it's just not happening.

00:28:39 - alexrojas
You know, I tried a couple of days and I do need to go to redeploying Railway.

00:28:44 - alexrojas
So I don't know if I need to do something in Railway or can I just do it here in the code.

00:28:51 - Brandon Hancock
And real quick, can we look back at who's calling GetCurrentTime?

00:28:54 - Brandon Hancock
I just want to make sure, like if you just right click on GetCurrentTime.

00:28:57 - Brandon Hancock
GetCurrentTime.com you find references.

00:29:00 - alexrojas
GetCurrentTime

00:29:00 - Brandon Hancock
Yeah, find all references, it's like down four, that'll work too.

00:29:05 - Brandon Hancock
And then if you go to agent.py on the right, or sorry, all the way right.

00:29:13 - alexrojas
Care?

00:29:15 - Brandon Hancock
Yeah, that works too.

00:29:17 - Brandon Hancock
And git current time, could I see where we're calling it in this file?

00:29:23 - alexrojas
Okay, I could.

00:29:31 - Brandon Hancock
Okay, today's date is, if we can click down, um, down one, yeah, right there.

00:29:37 - Brandon Hancock
Yes.

00:29:39 - Brandon Hancock
Okay, yeah, so what I would do differently is, I think what's happening is your agent, so here's what's, I mean, I'll stay with you, your agent started running, and it's a long running agent.

00:29:51 - Brandon Hancock
So what's happening is the second this agent was deployed, like, that's it, like, today's date is, and that's a hard-coded string.

00:29:58 - Brandon Hancock
Right?

00:29:59 - Brandon Hancock
So that string is not.

00:30:00 - Brandon Hancock
Like, the second the agent's deployed, the session's running, and it's not every night, like, oh, I need to redeploy.

00:30:05 - Brandon Hancock
It has no idea.

00:30:07 - Brandon Hancock
So, what you could do, just a quick workaround, is to actually put get current time in the tool call down below.

00:30:15 - alexrojas
Yeah.

00:30:16 - alexrojas
Okay.

00:30:17 - Brandon Hancock
Exactly.

00:30:18 - alexrojas
So it works, isn't it?

00:30:20 - Brandon Hancock
Exactly.

00:30:23 - Brandon Hancock
And then...

00:30:25 - Brandon Hancock
Yeah.

00:30:28 - Brandon Hancock
Perfect.

00:30:29 - Brandon Hancock
Yeah.

00:30:29 - Brandon Hancock
So you would just put that down there.

00:30:31 - Brandon Hancock
And then you would delete line 65.

00:30:36 - alexrojas
Sped boy.

00:30:37 - Brandon Hancock
Goes out.

00:30:38 - Brandon Hancock
Yep.

00:30:39 - Brandon Hancock
Yep.

00:30:39 - Brandon Hancock
And then just say, always, like in the important section, I would say, always call, get current time, before making a request, so that you understand what's going on.

00:30:51 - Brandon Hancock
Now, so that's the, like, high-level one.

00:30:53 - Brandon Hancock
The other option that you could do is, what seems like you wrote a function, huh?

00:30:59 - Brandon Hancock
we're And then we're

00:31:00 - Brandon Hancock
Yeah.

00:31:00 - Brandon Hancock
The other option that you could do is use callbacks.

00:31:04 - Brandon Hancock
So every time before you make an LLM request, you could always just say today's current, like, you could update that master prompt and just at the end of it, just say today's current date is this, but you'd have to do callbacks for that one.

00:31:16 - Brandon Hancock
So you can either say, do the tool call every time, or you could just update the tool calls and use callbacks.

00:31:25 - Brandon Hancock
So those are two approaches.

00:31:26 - alexrojas
In every tool, I just get the time and then, like, operate your tool.

00:31:35 - Brandon Hancock
So actually, sorry, no, because if you look at the way, if you look at create event, so you can see it has a start time and end time.

00:31:46 - Brandon Hancock
So the LLM is passing that information in.

00:31:49 - Brandon Hancock
What I was saying is, you could update the before LLM callback.

00:31:55 - Brandon Hancock
Like, that's a callback that you have access to.

00:31:57 - Brandon Hancock
So before that gets called in, you would just dynamic.

00:32:00 - Brandon Hancock
callback.

00:32:00 - Brandon Hancock
that's callback.

00:32:00 - Brandon Hancock
that's

00:32:00 - Brandon Hancock
We pass in the today's date into the, into the message history.

00:32:04 - Brandon Hancock
That way it goes, oh, today is, you know, June 10th.

00:32:07 - Brandon Hancock
So yeah, before, before, sorry, before model callback is what you'd want to do.

00:32:12 - alexrojas
Okay.

00:32:13 - alexrojas
And that, that is exactly in, in the agent?

00:32:17 - Brandon Hancock
Yep.

00:32:18 - Brandon Hancock
In the, uh, in the root agent, you would just set up before model callback right at the end.

00:32:25 - alexrojas
Oh, okay.

00:32:26 - Brandon Hancock
And the end, the one with later?

00:32:28 - Brandon Hancock
No, no, no.

00:32:29 - Brandon Hancock
Just, um, on line 73, where the comma's at, the end bracket, comma, go down just a little bit more.

00:32:36 - Brandon Hancock
Yeah, hit enter, and just type in before, and it should fill.

00:32:41 - Brandon Hancock
Yeah, see, before model callback, you could actually just create a function.

00:32:46 - Brandon Hancock
And I would definitely go check out the ADK Masterclass, but you'll see an example of exactly how you can update the prompt and just dynamically put in the time.

00:32:56 - Brandon Hancock
So that's the kicker.

00:32:58 - alexrojas
yeah.

00:32:59 - alexrojas
Okay.

00:32:59 - alexrojas
Perfect.

00:33:00 - Brandon Hancock
Perfect.

00:33:00 - alexrojas
So I can take a look then at the at the masterclass.

00:33:05 - Brandon Hancock
Robert, love to hear your ideas, buddy.

00:33:08 - Robert
Well, the question I have to ask is I noticed that you built a lot of your own tools.

00:33:14 - Robert
So would MCP have been an alternate way of interacting with the Google Calendar service?

00:33:20 - Robert
I'm not saying this is the wrong or right way, but I was just curious about that.

00:33:23 - Brandon Hancock
No, awesome question.

00:33:24 - Brandon Hancock
So actually, what I would have done instead now is I would have used Google Calendar does have an MCP tool.

00:33:34 - alexrojas
Actually, that was my second question.

00:33:36 - alexrojas
Because I'm doing an API call, it could have been better just to use MCP, right?

00:33:43 - Brandon Hancock
So that's the kicker.

00:33:45 - Brandon Hancock
I know there are MCP servers, I just don't see one from Google.

00:33:49 - Brandon Hancock
Like, there's a random guy, NS.

00:33:51 - alexrojas
Oh, yeah.

00:33:52 - Brandon Hancock
NS Paddy.

00:33:53 - Brandon Hancock
If you trust him to make sure he doesn't do anything with your keys, then yeah.

00:33:58 - Brandon Hancock
You know, but so it really...

00:34:00 - Brandon Hancock
So it comes down to like, I prefer only to use MTP servers that come from GitHub or Google.

00:34:04 - Brandon Hancock
So if you see one from Google, I would use it.

00:34:08 - Brandon Hancock
I'm just a little hesitant of, uh, I'm a little hesitant of using random people's MTP servers because they literally have access to your tokens.

00:34:14 - Brandon Hancock
Like it gets passed in and then, I mean, you can look at their code, but it's up to you then to like, are they doing anything shady?

00:34:20 - Brandon Hancock
I don't know.

00:34:21 - Brandon Hancock
So, um, Yeah, I haven't seen any official one from, from Google, just two guys that like provide everything.

00:34:28 - alexrojas
That's why I was also wondering the same thing.

00:34:31 - alexrojas
You just answered my question.

00:34:33 - Brandon Hancock
Yeah.

00:34:34 - Brandon Hancock
So Brandon, could you grab the, the fast MTP, the MTP, um, folder and could you develop your own, um, uh, Yes, yes, you could really, I mean, you could, but for what you were doing, like at the end of the day, you're calling five different tools, create event, list event, delete event, edit event.

00:34:56 - Brandon Hancock
At the end of the day, you're, even if you're doing fast MTP, you're still going.

00:35:00 - Brandon Hancock
It'll still be 20% more code, even if you're doing it that way, and especially if you're not planning on sharing with anybody, just a straight-up tool call is the easiest one, is what I would do.

00:35:09 - alexrojas
My end call is to connect the workspace of Google into my agent.

00:35:17 - Brandon Hancock
if that's the case, then yeah, you could probably create a Google MCP server that has 20 different tools, everything from calendar to docs to, like, you and...

00:35:27 - Brandon Hancock
If you're going down that approach, yeah, I would 100% create a fast MCP server that takes an environment variable, which is probably going to be your credentials, or it'll be a file path to your credentials, and that's what I would do.

00:35:42 - alexrojas
And should I look into the Google documentation, or should I base my own server from the ones that these guys have created?

00:35:52 - alexrojas
Should I steal some ideas, or should I...?

00:35:56 - Brandon Hancock
Dude, mean, hey, I would, I mean, they probably did it right.

00:36:00 - Brandon Hancock
So I...

00:36:00 - Brandon Hancock
I would definitely look at just seeing what they did and implementing it on your own, just to see at first, you know?

00:36:05 - Brandon Hancock
And then if it doesn't work, then go troubleshoot.

00:36:07 - Brandon Hancock
So yeah, I see no problem with that.

00:36:09 - Brandon Hancock
And it's expedited learning, so hey.

00:36:12 - alexrojas
Superb.

00:36:12 - alexrojas
Yep.

00:36:13 - Brandon Hancock
All right, perfect.

00:36:14 - alexrojas
Thank you very Thank much.

00:36:16 - Brandon Hancock
Keep me posted, and good luck cranking out the rest of the videos, man.

00:36:20 - Brandon Hancock
And yeah, ping me if, I mean, the date stuff should work.

00:36:23 - Brandon Hancock
So yeah, after you do the before model callback, let me know.

00:36:26 - Brandon Hancock
But that should keep you cruising.

00:36:28 - Brandon Hancock
Yeah.

00:36:29 - Brandon Hancock
Okay.

00:36:29 - alexrojas
very much.

00:36:30 - alexrojas
Yep.

00:36:31 - Brandon Hancock
Perfect.

00:36:31 - Brandon Hancock
Perfect.

00:36:32 - Brandon Hancock
All right.

00:36:32 - Brandon Hancock
Al, you're up next, man.

00:36:34 - Brandon Hancock
Nice to meet you.

00:36:35 - Al Cole
How you doing?

00:36:35 - Al Cole
Nice to meet you as well.

00:36:37 - Al Cole
And thank you for all the contributions you've been making out there.

00:36:40 - Al Cole
You've got some great videos.

00:36:42 - Al Cole
I've been learning a lot.

00:36:43 - Al Cole
I appreciate it.

00:36:44 - Al Cole
So just to introduce myself to the team here, I literally have wrapped up 10 years of running professional service organizations for Silicon Valley companies.

00:36:56 - Al Cole
And prior to that, I ran my own consulting practice for 18 years.

00:37:00 - Al Cole
So I'd like.

00:37:00 - Al Cole
I'd to open up to the team that while I'm catching up on the technical side again, used to be highly technical, I really understand the business of running consulting, so if any of you ever have questions about scenarios or how to partner with companies or things like that, I'm happy to at least help you in that capacity as I'm ramping on the technical side.

00:37:22 - Al Cole
So, in terms of what I'm focusing on right now, one, just to the team, I was at Google, and I'm up here in New England, so I went to Boston to catch a Google event.

00:37:34 - Al Cole
They had a half day there to go over the ADK.

00:37:38 - Al Cole
Just props to you, Brandon, your video was way better than the presentation of the ADK there.

00:37:44 - Al Cole
You did a much better job explaining their tech.

00:37:47 - Brandon Hancock
I'll take it.

00:37:48 - Al Cole
I'll take it.

00:37:49 - Al Cole
Thank you.

00:37:50 - Al Cole
But I did accumulate some artifacts, which I'm sure are freely available for all the people the way they are.

00:37:56 - Al Cole
So, if the team's interested, I've got the general presentation.

00:38:00 - Al Cole
That kind of gives you an overview of their tech, and then also they had some pretty in-depth labs that if anyone wanted to understand how they walked us through a bunch of different scenarios with agents, obviously running it on Google Cloud, but it was pretty good.

00:38:17 - Al Cole
We did not get agent-to-agent communication, but we did do a bunch with their tools, and we also leveraged Spanner.

00:38:24 - Al Cole
So they wanted to do like a social platform kind of scenario, so they exported data, threw it up in Spanner as a graph, and you were leveraging the social graph to figure out how to put together an event planner.

00:38:38 - Al Cole
It was actually kind of a clever little lab, all agent-driven.

00:38:41 - Al Cole
So I think we all gather in the AI developer accelerators, so I'll put those artifacts there as a follow-on to this email, and then I hope to contribute.

00:38:54 - Al Cole
Technically, with the team here in the coming weeks, right now, I'm just getting my Python legs under me, long-time job.

00:39:00 - Al Cole
I'm developer, so it's just a language transition, I'm getting there, I love Python, much, much easier.

00:39:05 - Al Cole
So I've got a ChatGPT type thing going with Streamlit, which has been fined.

00:39:10 - Al Cole
I guess a question for the team, as I start thinking about a services focus, from a prompt management perspective, has anyone thought that it was worth the time to put together a kind of a prompt application that gathers prompts, maybe tags them for different LLMs that we know they're good for, maybe different roles that you might want to apply them to, and almost kind of validate rank and then maybe reapply them if you get a new model to see how well they do with the new model.

00:39:49 - Al Cole
So my question is, is it worth building a simple app to kind of manage prompts and then maybe leverage them from an embedded perspective in the agents that we build, simply because we know, we've validated...

00:40:00 - Al Cole
with this, like, test harness.

00:40:01 - Al Cole
Does that make any sense?

00:40:03 - Brandon Hancock
No, I totally understand where you're coming from.

00:40:06 - Brandon Hancock
Andrew, I saw you dropped a comment.

00:40:08 - Brandon Hancock
If you wanna...

00:40:09 - Brandon Hancock
I think you had some ideas.

00:40:11 - Andrew Nanton
Yeah, I mean, I've been playing with a couple of different things that do something similar.

00:40:16 - Andrew Nanton
And, I mean, you could certainly build your own if you don't like how they're doing it.

00:40:20 - Andrew Nanton
But some of the ones that I was pretty impressed with were LaneFuse has a completely open-source implementation that you can deploy locally if you wanna just check it out and see.

00:40:31 - Andrew Nanton
But it will let you version and edit prompts and run evals against those prompts, you know, so you can see, like, what you think of that.

00:40:40 - Andrew Nanton
BrainTrust is...

00:40:41 - Andrew Nanton
I think their UI is more slick, but, you know, it's not...

00:40:47 - Andrew Nanton
You can't just get a free version of it.

00:40:50 - Andrew Nanton
And then prompt layer also looked kind of neat.

00:40:53 - Andrew Nanton
But, yeah, I mean, you could just sort of poke around and see.

00:40:57 - Andrew Nanton
But there's some cool stuff out there.

00:41:00 - Al Cole
Yeah, if it's pre-built, I don't need to build it.

00:41:02 - Al Cole
I just thought that prompt management would be key, especially with the agents, and especially with models that are evolving, just some way to sanity check and just qualifying them before you throw that new model in that we might be working with.

00:41:20 - Andrew Nanton
Yeah, I mean, so this is what came to mind when Juan was talking about extracting the names of companies out of that description, is, you know, let's say you did a few of those, you could put the description in, and then the result that you want is the company name, and, you you put together 15 or 20 of those, and then as you tweak your prompt in something like Langfuse, you can run it, like you were saying, like a test suite, and say, oh, well, this got 18 out of 20, or this got, you know, 80 out of 200 of the names right, let's tweak this prompt a little bit, okay, well, I got, you know, 95 that time, so that's better, and, you it gives you a much more empirical way to continue to refine.

00:42:01 - Al Cole
And one of the other reasons I like this type of solution is when you're working with a client and you're able to educate them about the prompts that are being utilized and their effectiveness is also, I think, some value in that education so they understand the probabilistic nature of what you're doing as well because you can get varied responses just by pointing to a different model, right?

00:42:24 - Brandon Hancock
Yeah.

00:42:24 - Brandon Hancock
Yeah.

00:42:25 - Brandon Hancock
100%.

00:42:25 - Brandon Hancock
So, Al, quick question back to you.

00:42:29 - Brandon Hancock
on business experience, I know said, sharpen it up, the tech skills.

00:42:33 - Brandon Hancock
So, what's a long-term plan, man?

00:42:35 - Al Cole
I want to run the consulting practice again.

00:42:38 - Al Cole
Absolutely.

00:42:39 - Al Cole
That was a passion I had for a number of years.

00:42:42 - Al Cole
So, spinning it up again.

00:42:45 - Al Cole
Where I had success was being solution-oriented.

00:42:48 - Al Cole
And one of the novel ways that I built a sustaining annuity with my business was I looked to, I would join through-

00:43:00 - Al Cole
Partnerships with technology companies, would find niche ways to bring, in the case, for me, it used to be search before search was really broadly adopted, right?

00:43:10 - Al Cole
And helping, let's say, a relational database and an application built on it, discover information in just unique ways.

00:43:17 - Al Cole
I had a whole subscription business going with that for years, because that was a nice value add, and I could sell into that ecosystem.

00:43:25 - Al Cole
So I got known as an expert there.

00:43:27 - Al Cole
So as you're thinking about your agents, you may have opportunities partnering with companies that can't innovate this quickly and being able to help them with some capabilities and essentially get tied in to that ecosystem and that base.

00:43:42 - Al Cole
So just sharing things that I learned over the years where you can simplify that customer acquisition process just by getting aligned with vendors that you think you could have complementary solutions to.

00:43:57 - Brandon Hancock
No, that's awesome.

00:43:58 - Brandon Hancock
No, it totally makes sense.

00:43:59 - Brandon Hancock
You're meeting the business where they are.

00:44:00 - Brandon Hancock
I mean, yeah, everything you're saying totally makes sense.

00:44:03 - Brandon Hancock
If there's anything we can help with, please always DM away.

00:44:07 - Brandon Hancock
And when it comes to either tech side of things or AI, a lot of smart guys on the call.

00:44:12 - Brandon Hancock
So happy to help however we can, man.

00:44:15 - Al Cole
Thank you.

00:44:15 - Al Cole
Appreciate it.

00:44:16 - Al Cole
Great to be here.

00:44:16 - Al Cole
Looking forward to continuing your contribution.

00:44:19 - Brandon Hancock
Awesome.

00:44:20 - Brandon Hancock
Awesome.

00:44:21 - Brandon Hancock
All right.

00:44:21 - Brandon Hancock
Next up, Ty, how's it going, man?

00:44:25 - Ty Wells
Hey, good.

00:44:26 - Ty Wells
How are you doing?

00:44:27 - Brandon Hancock
Hey, great Tuesday so far.

00:44:29 - Brandon Hancock
Tuesdays are call days.

00:44:30 - Brandon Hancock
I wake up and I code for like two hours or record, and then I'm on calls.

00:44:35 - Brandon Hancock
So that is, I've been doing that since like 10.

00:44:39 - Brandon Hancock
So it's a busy day.

00:44:40 - Ty Wells
There you go.

00:44:42 - Ty Wells
Yeah.

00:44:42 - Ty Wells
Thanks for everything.

00:44:44 - Ty Wells
You put some great videos.

00:44:46 - Ty Wells
I can't wait to see this ADK 2A video.

00:44:50 - Ty Wells
That should be sweet.

00:44:51 - Brandon Hancock
I will say it is deep.

00:44:53 - Brandon Hancock
It is deep.

00:44:54 - Brandon Hancock
It's not my fault.

00:44:55 - Brandon Hancock
They made it deep.

00:44:56 - Brandon Hancock
So I wish it was a little bit simpler to implement, but...

00:44:59 - Brandon Hancock
Yeah.

00:45:00 - Brandon Hancock
And just a heads up, like, A2A, the version, is that, like, version 0.2?

00:45:06 - Brandon Hancock
The second they hit version 1.0, I will do, like, a full-blown masterclass, because, like, it is going to be, like, I think one of the ways actual, like, everyone's like, oh, I want to have 1,000 agents that work together.

00:45:18 - Brandon Hancock
This is how it's going to happen.

00:45:20 - Brandon Hancock
But they're just making it easier every month, like the Google team is.

00:45:23 - Brandon Hancock
They're making it easier and easier.

00:45:25 - Ty Wells
So the second it comes out, I'll have another one for you guys that's even better.

00:45:28 - Ty Wells
Sounds good.

00:45:29 - Ty Wells
Yeah, I'm going to wait for probably close to 1.0, but yeah, I'll take a look at the video.

00:45:37 - Ty Wells
What am I working on this?

00:45:39 - Ty Wells
What am I working on?

00:45:40 - Ty Wells
I've got four different projects going right now.

00:45:46 - Ty Wells
I've got a couple of businesses, and we're in the life safety business, security business, and we use some software that just clunky, you know, they don't make customizations, it's a German

00:46:00 - Ty Wells
And it's really heavy for sort of managing assets in a life safety fire alarm system type scenario.

00:46:08 - Ty Wells
So I met with my business partner and like the operations manager and went over the software, I have access to it.

00:46:18 - Ty Wells
And so I went ahead and reverse engineer it and rewrote it and hopefully they're in production next week.

00:46:25 - Ty Wells
So we'll be saving, we'll be saving 10 grand a year on, on fees or something they're probably using 60% of.

00:46:34 - Ty Wells
So.

00:46:35 - Brandon Hancock
You get a cut?

00:46:37 - Ty Wells
Well, since I'm half owner, I'm going to charge them the one time fee, one license fee.

00:46:43 - Ty Wells
Yeah, so.

00:46:44 - Brandon Hancock
All right, that makes sense.

00:46:45 - Brandon Hancock
I'll say, as you're doing all these innovative projects, you got to make sure you get a...

00:46:49 - Ty Wells
Oh yeah, no, no.

00:46:50 - Ty Wells
Well, we needed this.

00:46:51 - Ty Wells
I win both ways.

00:46:52 - Ty Wells
This is a win-win situation.

00:46:53 - Ty Wells
But I, you know, it's, it's a, it was very complicated software.

00:46:58 - Ty Wells
Just getting the data out of it was crazy.

00:47:00 - Ty Wells
I got you.

00:47:01 - Ty Wells
Sort of midstream here, but what I will, what can I show you?

00:47:05 - Ty Wells
Oh, so we have another piece of software, same company, we do for accounting, and then we have a POS for the store, and servicing in the back end, you know, access control, CCTV, that type of stuff.

00:47:21 - Ty Wells
So that's like, I looked at that, that's like 30 grand, so I'm in the process of, you know, creating a software just, a SaaS solution just for what they need, so, because they don't use a lot of pieces in the other software as well, but that was more of an 80-20, in terms of, there are other pieces they want that we can't get customized, so, gonna build all that, hopefully I'll have that done in a couple of weeks.

00:47:51 - Brandon Hancock
You're a software machine, man, I love it.

00:47:53 - Ty Wells
I know, I mean, just, the ability to just produce at record pace is just crazy, you know, I, I like

00:48:00 - Ty Wells
I build all that UI in Lovable, and then I switch to Cursor, and off I go, that's it, so.

00:48:07 - Brandon Hancock
Yeah, it is, I think there's, I don't know how long the, like, arbitrage window exists, where, like, meaning, like, anybody can make a Lovable app, and then they're like, cool, this is awesome, but then actually getting it functional, because, like, right now, Cursor's doing so much for us, I don't know how many years, maybe months, until, like, AI can do all of it, I do get worried about that, when it's like, yeah, AI just does the entire thing, that worries me, but for, for right now, oh my gosh, golden era of helping other people, like, bridge the gap and build functionality for them.

00:48:41 - Ty Wells
Yeah, I'm hoping it stays around for a while, for my own sake.

00:48:45 - Ty Wells
I know, well, I think Lovable's getting there, they're really pushing hard, they are, I love their security feature, because I'm a, I'm a security professional, and so, I, I run their, their security review, and it's actually pretty good.

00:49:00 - Ty Wells
And then I run the app against my tools and, you know, it missed a lot of stuff, but, you know, lower item stuff.

00:49:08 - Ty Wells
No, it doesn't miss any of the high critical stuff, but it's a good starting point.

00:49:14 - Brandon Hancock
Quick question for you.

00:49:15 - Brandon Hancock
Are you actually connecting to Supabase through Lovable?

00:49:19 - Brandon Hancock
Like, are you directly allowing Lovable to connect to Supabase in your own projects?

00:49:23 - Ty Wells
Yeah, I always start my project, and then I connect it to Lovable, and Lovable will create all the tables and so forth.

00:49:30 - Ty Wells
Yeah.

00:49:31 - Brandon Hancock
I got you.

00:49:32 - Brandon Hancock
Any issues with that ever?

00:49:34 - Ty Wells
Just out of curiosity?

00:49:36 - Ty Wells
No, actually, there were some issues, but that was really in Lovable 1.0.

00:49:41 - Ty Wells
They fixed those.

00:49:41 - Ty Wells
It doesn't happen as often.

00:49:43 - Ty Wells
The infinite recursion that it causes, it basically has a trigger on top of a function and on top of a new insert.

00:49:50 - Ty Wells
Yeah.

00:49:51 - Ty Wells
So they fixed that.

00:49:54 - Ty Wells
I haven't run across, usually it takes a max of three tries for it to

00:50:00 - Ty Wells
Fick something.

00:50:00 - Ty Wells
Now, if it goes beyond that, then I will, I go into chat mode and actually walking through, it'll find the answer.

00:50:07 - Ty Wells
And I'll see you to better understand what it was trying to do and what it did and so forth.

00:50:12 - Ty Wells
So, but no, Superbase running in lovable is great.

00:50:15 - Ty Wells
And then into cursor with the MCP tool.

00:50:17 - Ty Wells
The only thing is the MCP tool is not very stable.

00:50:21 - Ty Wells
I keep getting disconnected.

00:50:23 - Ty Wells
I mean, well, probably because I've got multiple instances of cursor running.

00:50:27 - Ty Wells
And I know that's causing, it's, it's switching back and forth.

00:50:31 - Ty Wells
It's, you know, keeps turning it off, but I just turn it on when I need it, but...

00:50:36 - Brandon Hancock
I gotcha.

00:50:37 - Brandon Hancock
There's also a concept in, in Superbase for setting up your database of like, is it, like, is it persistent on, because like, correct me if I'm wrong, but one thing that I think Superbase does is like a, if no one's accessing the database, it almost does like a cold, like off, but like a cold boot.

00:50:59 - Brandon Hancock
So then when you try and symptoms...

00:51:00 - Brandon Hancock
It has, like, a spin-up, so I'm curious, maybe that could be causing some issues.

00:51:03 - Ty Wells
You know, that's a good point, but I'm not sure if it's that.

00:51:07 - Ty Wells
I think it's my multiple instances, because they, I turn it on, I run a few, it uses it, and then I go over to the other app, check something, come right back, it's off.

00:51:16 - Ty Wells
So it's not like it's a timeout type thing.

00:51:19 - Ty Wells
I think it's just the multiple instances, if I use it from one, it disables the other way.

00:51:24 - Ty Wells
So I may have to run Cursor in a container or something to, so I can run multiple copies of it.

00:51:32 - Brandon Hancock
Okay, no, awesome.

00:51:33 - Brandon Hancock
Yeah, like I said, very cool that you're using Supabase directly with Lovable.

00:51:37 - Brandon Hancock
I've been, I've been holding on to my developer roots and like, no, I'm gonna do that.

00:51:44 - Brandon Hancock
So very cool that you're having a good experience with that.

00:51:47 - Ty Wells
Let me show you guys this real quick.

00:51:50 - Ty Wells
I just came across this little thing on, I can't remember.

00:51:52 - Ty Wells
Right.

00:51:53 - Ty Wells
This is the POS thing that I'm, I'm building out this for my company, but

00:52:00 - Ty Wells
Do you see the style in this?

00:52:01 - Ty Wells
This isn't lovable.

00:52:02 - Ty Wells
Do you notice anything different about what you've seen in a lot of lovable sites?

00:52:08 - Ty Wells
This is a new, what's it called?

00:52:13 - Ty Wells
Apple, ILS.

00:52:15 - Ty Wells
This is supposedly their new glass view look.

00:52:17 - Brandon Hancock
Oh, the liquid glass?

00:52:18 - Ty Wells
The liquid glass look that I threw out here, and it actually looks pretty good.

00:52:24 - Ty Wells
Well, this one I'm tweaking a little bit, but it looks pretty good.

00:52:27 - Ty Wells
So I think I'm switching all a bunch of apps to it.

00:52:29 - Ty Wells
It's an easy prompt to get it to switch over.

00:52:33 - Ty Wells
And then I figure it because some of these colors are too dark, but yeah.

00:52:37 - Brandon Hancock
Alex, I saw you had your hand up, buddy.

00:52:41 - alexrojas
Yeah, I ran into this Google product.

00:52:45 - alexrojas
It's called AppSheet.

00:52:46 - alexrojas
I don't know if you guys have heard of it.

00:52:49 - alexrojas
It's the lovable version, but of Google.

00:52:52 - alexrojas
And I think if you're integrated in Google Workspace, you can really take it like...

00:53:00 - alexrojas
Fath, like, into production, really, like, I was just playing around with it, and it's pretty cool.

00:53:07 - alexrojas
It's even included if you have a Google Workspace, and yeah, like, I tried a couple, it's the same, you you could do your, through Gemini, start the app, or just grab a template, or even you could even start your app if you have a database.

00:53:24 - alexrojas
Fath, just upload it, and then, like, it's more, it's less beautiful, because yeah, what Ty is showing, it's a, quite nice looking, this is more, like, internal, and very, process-efficient.

00:53:36 - alexrojas
Fath, yeah, just wanted to drop that in.

00:53:42 - Brandon Hancock
Fath, that's very cool.

00:53:43 - Brandon Hancock
Yeah, I, so I'm guessing it's, was it mostly to connect to your internal Google tools, I'm guessing, and then just build apps around what you already have in Google?

00:53:54 - alexrojas
Fath, Exactly.

00:53:56 - alexrojas
Fath, that's awesome.

00:53:57 - alexrojas
the best case.

00:53:58 - alexrojas
Yeah, if you're, if you're, like, integrated into a...

00:54:00 - alexrojas
So of Google, these can like, that 60%, it takes you like 90 or, you know, maybe two.

00:54:08 - Brandon Hancock
That's awesome.

00:54:09 - alexrojas
Yeah.

00:54:09 - Brandon Hancock
Very, very cool.

00:54:10 - Brandon Hancock
Yeah.

00:54:12 - Brandon Hancock
Because I saw in the Google I.O.

00:54:14 - Brandon Hancock
thing, they mentioned AppSheet.

00:54:15 - Brandon Hancock
I was like, wait, they have Firebase Studio.

00:54:17 - Brandon Hancock
I didn't understand why, but oh, it's because internal, external.

00:54:22 - Brandon Hancock
I see.

00:54:22 - Brandon Hancock
Totally makes sense.

00:54:23 - Brandon Hancock
Totally makes sense.

00:54:24 - alexrojas
It's quite entertaining.

00:54:25 - alexrojas
So just for you guys to, if have some free time.

00:54:29 - Brandon Hancock
Yeah.

00:54:30 - alexrojas
thanks.

00:54:31 - Brandon Hancock
Ty, anything else we can help with?

00:54:37 - Brandon Hancock
Good job.

00:54:41 - Brandon Hancock
I think you had to go.

00:54:42 - Brandon Hancock
Okay.

00:54:43 - Brandon Hancock
All right.

00:54:44 - Brandon Hancock
We'll keep on cruising.

00:54:46 - Brandon Hancock
Paul, you're up next, man.

00:54:49 - Paul Miller
Hey guys.

00:54:51 - Paul Miller
Yep.

00:54:52 - Paul Miller
Latest on my side, I wasn't able to come on the call last week.

00:54:58 - Paul Miller
Um, I've got a, uh, for those people.

00:55:00 - Paul Miller
For people that don't know my background, I have a sort of a day job that's a SaaS business that I started up about 10 years ago, and suddenly I'm getting this wave of new customers signing up, because one of our biggest competitors seems to have imploded, and it's always good when sales sort of drop out of the sky, rather than having to get out there and get people on board.

00:55:28 - Brandon Hancock
That's awesome.

00:55:31 - Paul Miller
So that's been really great.

00:55:33 - Paul Miller
And then, sorry, let me get rid of that.

00:55:37 - Brandon Hancock
There's more sales.

00:55:38 - Brandon Hancock
They're just coming in.

00:55:38 - Paul Miller
They're just boom, boom, boom.

00:55:40 - Paul Miller
I wish.

00:55:42 - Paul Miller
And then the other cool thing was, I've been dealing with a US company that was wanting to acquire us, and then they got acquired.

00:55:55 - Paul Miller
And now the company that's acquired them has contacted me and said, look.

00:56:00 - Paul Miller
We want to start conversations with that, so look, I'd love to get an exit, thank you, I'd love to get an exit, of course, the multiplier that I want and my other shareholders want, so I've been a bit distracted with that, and if you've got kind of upward sales trajectory, you're profitable, that's everything an investor wants, so I'm quite excited, but I kind of get more kicks, while money is nice and be great not to have a mortgage, um, I want to just play more with AI, so.

00:56:37 - Paul Miller
Well, St.

00:56:38 - Brandon Hancock
Paul, you just, you get all the money, and then boom, you just play around with AI like me all day, man.

00:56:42 - Brandon Hancock
Well, that's the plan, that's the plan.

00:56:47 - Brandon Hancock
I love it, I love it.

00:56:49 - Brandon Hancock
So, what's next steps, you think, go through, or what's going on?

00:56:53 - Paul Miller
Well, I've got another call with them tomorrow, and, um, I've kind of got a, uh, I've got a, sell house.

00:57:00 - Paul Miller
How we can complement what they do with their existing investments, they're certainly not short of money, and in New Zealand, we don't have many big VC funds looking for businesses, niche businesses that operate in the B2B space, so when they come out of the US, they're a lot better geared for this kind of thing, because it's a much more evolved market market for this type of thing, and the multipliers are much better than what we see in Australia and New Zealand, so I'm pretty excited about that, but I have, I have got a practical question on one of the projects that I'm doing now, and I'm really keen to get some feedback, let me just share my little Excalibur background, so can you see my, my picture here?

00:57:59 - Brandon Hancock
Jared Ranere, Pxum Ranere, Pxum

00:58:00 - Paul Miller
Okay, so if you, just from a user perspective, so my users want to be able to extract information from a council, our city council in Auckland, they produce minutes of every meeting, it all goes into a PDF for every meeting, there's hundreds hundreds and hundreds of these PDFs, and I'm trying to look over the last three years, that's the sort of term of local government, and put it into a system that I can have a kind of a hybrid rag search, I can extract document sort of NER stuff out of those documents, and I'm thinking that sort of dockling is the problem, it sounds like based on all the calls that we've had, it's the the way to go.

00:59:00 - Paul Miller
The question I had for everyone is, is there some coding project with a RAG project that I could get started with, with Python to just grab it, or should I just hack something together?

00:59:17 - Paul Miller
And I was thinking too, if the objective is to understand what people are talking about, or what certain people talked about in certain meetings, maybe a graph-based RAG might be the better way to go, but any thoughts?

00:59:39 - Paul Miller
So we're talking about four or five hundred documents, averaging about a quarter of a meg per document, but we'd stick it through Dockling to extract good stuff out of it.

00:59:51 - Paul Miller
But what are people thinking in terms of architecture?

00:59:56 - Paul Miller
Is there a code set that I could jump into?

01:00:00 - Paul Miller
What, what would, what would people suggest?

01:00:03 - Brandon Hancock
So, so real fact, I definitely would love all the ideas on this one, but I just want to make sure I understand.

01:00:08 - Brandon Hancock
So I understand chatting with the documents totally makes sense.

01:00:12 - Brandon Hancock
What was the, the second part about the summary?

01:00:14 - Brandon Hancock
What was the, what was the goal?

01:00:16 - Brandon Hancock
Um, uh, in the second part?

01:00:19 - Paul Miller
So the kind of, the goal is to, um, so I'm supporting one of the political parties, um, and I do a lot of stuff with, with working with certain political parties and, and they need to be able to dig up for certain candidates.

01:00:35 - Paul Miller
They went out and said three years ago, they're going to do this.

01:00:38 - Paul Miller
They're going to do that.

01:00:39 - Paul Miller
I wanted to compare what they promised with what they did.

01:00:43 - Paul Miller
So, so getting the insights of, well, they said they were going to do this to improving the bus routes or the trains or whatever.

01:00:51 - Paul Miller
This is what actually extracting all of those reference, uh, well, all of the information information and what they did,

01:01:00 - Paul Miller
Um, along with the references back to the document, uh, the documents where the source of that information was if they wanted to find out further.

01:01:09 - Brandon Hancock
Okay, I gotcha.

01:01:10 - Brandon Hancock
So, I can go from the chat side first, and then, um, summary second.

01:01:16 - Brandon Hancock
So, um, chat, everything you have set up, absolutely love it.

01:01:21 - Brandon Hancock
PDFs, makes sense.

01:01:23 - Brandon Hancock
Dockling to, uh, do the extraction, totally makes sense.

01:01:27 - Brandon Hancock
The thing that I think you'd be, um, to get better performance when it comes to chunking, I would be very curious what the transcript style is like.

01:01:37 - Brandon Hancock
So, for example, there is, uh, let me look, I can't remember why I did it on a project I'm working on right now, but, like, there's multiple different types of chunkers, and you want to make sure the chunker you're using actually ties to the data you're using.

01:01:50 - Brandon Hancock
Because, like, you could just default, like, oh yeah, throw 500 tokens in, and it is what it is.

01:01:56 - Brandon Hancock
But, like, you're not going to get as good of results as you would expect.

01:02:00 - Brandon Hancock
expect.

01:02:01 - Brandon Hancock
So usually, let me pull this up really fast.

01:02:08 - Brandon Hancock
Here, I'll share this really quickly.

01:02:13 - Brandon Hancock
I'll actually scream real fast, if that's okay with you, Paul.

01:02:20 - Brandon Hancock
Okay, cool.

01:02:21 - Brandon Hancock
So this is a project working on for a client.

01:02:27 - Brandon Hancock
Where is it at?

01:02:31 - Brandon Hancock
Yeah, so the document DocLink converter.

01:02:35 - Brandon Hancock
So this is what you're going to use to process your documents.

01:02:40 - Brandon Hancock
Basic tokenizer, what are you going to use?

01:02:43 - Brandon Hancock
DocLink does all the useful under the hood stuff for you.

01:02:50 - Brandon Hancock
So for example, if, you know, every, for example, let's say you were trying to work on a chunk, and that chunk was over your max token and embeddings, it will split it up to where.

01:03:00 - Brandon Hancock
where it handles all of it for you, so you still get the best results, then the Hybrid Chunker is one that I've had the best luck for, at least when it comes to working with documents.

01:03:13 - Brandon Hancock
So, would definitely look at using this one.

01:03:17 - Brandon Hancock
There was something else that I did.

01:03:19 - Brandon Hancock
Sorry, I just want to make sure I'm not leaving anything out that you would care about.

01:03:26 - Brandon Hancock
Not at the top of my head.

01:03:30 - Brandon Hancock
But yeah, just know there's a few different types of chunkers, and I would look to make sure the information you're passing in aligned with what that chunker is expecting.

01:03:40 - Brandon Hancock
Because that document chunker is expecting headings, subheadings, and stuff you would see in a normal document.

01:03:46 - Brandon Hancock
So that's why I picked that one.

01:03:47 - Brandon Hancock
In your case, it might be more transcript, or it's like, speaker, content, timestamp, speaker, like, I'm not sure.

01:03:53 - Brandon Hancock
So I would just keep that in mind, and you might have to create a quick custom chunker, but just know...

01:04:00 - Brandon Hancock
Just go to a point, you know, cursor to an existing one, hey, do this for this type of document, and you probably get some really good results.

01:04:07 - Brandon Hancock
Anyone else have any suggestions or anything for what Paul's working on?

01:04:18 - Andrew Nanton
Is it specifically transcripts, Paul?

01:04:22 - Paul Miller
It's meeting minutes, so it's not transcript format.

01:04:27 - Paul Miller
Let me show you an example of one of the documents, hold on, I'll call it up.

01:04:38 - Paul Miller
So it's quite structured, so it's already coming very structured to start with.

01:04:49 - Paul Miller
Rather than transcripts, they kind of, they throw it together in quite a usable format.

01:04:57 - Paul Miller
Why they can't then use that themselves.

01:05:00 - Paul Miller
For the public to access it is another matter, but that's government for you, but it's got some quite logical groupings of data.

01:05:10 - Andrew Nanton
And it's only PDF, or do they offer any other format?

01:05:15 - Paul Miller
I'm just looking at, while they do have other document format types, so say if someone comes to the council and they do a presentation, like a PowerPoint presentation, they'll share those documents, but I decided that I'll take the path of looking at the meeting minutes that they generate automatically and just focus on that, because that's going to be the most of what I'm looking for to start with.

01:05:44 - Andrew Nanton
Thanks.

01:05:45 - Andrew Nanton
Yeah, okay, so if the meeting minutes are all in PDF, then, yeah, I was playing with, I put a link in the chat, Chonky AI, and the...

01:06:02 - Andrew Nanton
You can grab the whole chunking library off of GitHub, and I was playing with it a while ago, and then it disappeared for a bit, and I don't know what happened to it, but it's back now, and it seems really good, and they have a nice, if you click through to some of the demos, they have like a chunking visualizer that somebody made that you can sort of visualize how it's chunking stuff up, and that's really nice, because you can, you know, see, for real how it looks.

01:06:32 - Paul Miller
Oh, cool.

01:06:33 - Paul Miller
So that might save a bit of time, then, if it's an existing environment that kind of really doesn't.

01:06:40 - Andrew Nanton
because, I mean, these, like, the most basic naive chunking where it's just a number of tokens is almost never, almost never produces good results, and so some of these other ones, if you, if you get more structure out of something like with dockling, if you end up with a more structured document, then .

01:07:00 - Andrew Nanton
You can do a whole lot better than that.

01:07:06 - Brandon Hancock
I love, this is exactly what Andrew's talking about, and same thing, it's just like, honestly, picking the chunker is one of the most important parts, because like, you just want to make sure the data you're capturing goes in the right thing, and it looks like they have some really clear, like, different types of chunkers, depending on what you need.

01:07:25 - Brandon Hancock
It's like, you want to do it by sentences, you want to do it by, like, yeah, like this one, for example, the recursive chunker, like, really good for a book or research paper, probably would be very applicable to you.

01:07:38 - Brandon Hancock
And then, and then, potentially the semantic chunker, both of those look pretty, both of those look pretty relevant based on what you're trying to do.

01:07:51 - Andrew Nanton
Also, I the name chunking.

01:07:52 - Andrew Nanton
I don't if you, yeah, late chunking is really cool, because what that does is embed the whole thing.

01:08:00 - Andrew Nanton
name chunking.

01:08:00 - Andrew Nanton
I I

01:08:00 - Andrew Nanton
So embed first, then chunk, yeah, there's some really, really interesting choices.

01:08:06 - Andrew Nanton
So you just play with them and see what works.

01:08:09 - Paul Miller
Brilliant, very cool.

01:08:12 - Brandon Hancock
Real quick, something to mention, Paul, so this is just like something to keep in mind, whatever model you pretty much do the embedding with, remember, like, obviously, when you're doing the rag request, you need to keep it the same.

01:08:24 - Brandon Hancock
So, like, at this point, like, if you're going to go with the open source model, just remember, like, you then, whenever for your deployed web application, you need to have the same deployed model accessible.

01:08:37 - Brandon Hancock
So, like, I mean, it's like, yes, it is awesome to go with, like, GTE 3, small, but then you have to, like, because it's open source, it's free, when you're running on your local computer, you're like, man, this is amazing.

01:08:47 - Brandon Hancock
But then the second you go to a deployed application, you're like, oh, shoot, now I now need to have my model deployed on the server.

01:08:55 - Brandon Hancock
So, personally, just, like, if you're just going to go for a max efficiency, just open AI.

01:09:00 - Brandon Hancock
Their embedding is just all around the easiest that I've always had luck with.

01:09:05 - Brandon Hancock
So just remember, when embedding, have it there, and then when you're doing your query embedding, it's the same one.

01:09:11 - Brandon Hancock
So just universal, and it's very affordable.

01:09:14 - Brandon Hancock
It's gotten insanely cheap.

01:09:18 - Brandon Hancock
Yeah, it's gotten very cheap.

01:09:20 - Brandon Hancock
So we definitely recommend checking that out.

01:09:23 - Paul Miller
Brilliant.

01:09:24 - Paul Miller
Thank you.

01:09:24 - alexrojas
Well, I just have a question.

01:09:26 - alexrojas
When you talk about hybrid, where do you draw the line between the RAG part and the simple search, or the SQL search?

01:09:37 - Paul Miller
Well, I always liked with the hybrid, being able to sort of do like a parallel search and then get the LLM to look at, well, that's kind of what you're matching.

01:09:50 - Paul Miller
This is, if you do that direct query, what makes more sense in the context of the original question, just for improving accuracy?

01:09:59 - Paul Miller
Um, that...

01:10:00 - Paul Miller
That...

01:10:00 - Paul Miller
That was kind of the logic I was coming from with the with the hybrid thing.

01:10:05 - Paul Miller
I tend to use Mongo.

01:10:08 - Paul Miller
I kind of like Mongo from the document database side of things with the with the structures and doing searches on but I was humming and harrying whether I should stick it into a graph database because of the logic of connecting with all of the different people talking about different topics.

01:10:27 - Paul Miller
But yeah, who knows?

01:10:31 - alexrojas
Cool.

01:10:33 - Brandon Hancock
Oh, yeah.

01:10:35 - alexrojas
So you run both and you kind of compare them or like make them which one has a better outcome?

01:10:44 - Paul Miller
Yeah, a vector match and then do a do a match based on the the Mongo search logic with getting the AI to call Mongo based on on what it understands the questions of the question.

01:11:00 - Paul Miller
Yeah.

01:11:00 - Paul Miller
And how that maps against the document database that Mongo is based on.

01:11:06 - alexrojas
Cool.

01:11:07 - Brandon Hancock
And real quick, Alex, just to, like, give a little more context to what Paul's talking about.

01:11:13 - Brandon Hancock
So, like, inside of your Next.js applications, a lot of people use the AI SDK to handle just, like, super easy interfacing with AI inside your Next.js applications.

01:11:26 - Brandon Hancock
So, just to give you a quick example, like, I'm working with, like, a fire chief to help them when it comes to, like, doing SOAP operations and answer medical questions.

01:11:36 - Brandon Hancock
So, like, all I'm doing is I'm making a two-RAG request, kind of like what Paul was talking about, just two separate requests, and then you feed them into your prompt.

01:11:45 - Brandon Hancock
So, for example, one goes off and looks up billing, so it searches through all the billing documents.

01:11:51 - Brandon Hancock
Then the other one is, like, oh, medical-wise, I need to go through all these medical documents.

01:11:57 - Brandon Hancock
It's all in the same VectorStore, but you can do some, like, unique.

01:12:00 - Brandon Hancock
You can tricks with metadata tags, so you can be like, I only want to look at all embeddings that have this meta ID, so it's a really cool way to like use one vector store, but use it for multiple purposes, and you can then, what's nice is like, cool, I have billing information, and I have medical information, now what I'm going to do in my prompt is say, hey, your job is to answer this question, but for context, here's all the data I grabbed on billing, also here's all the data I grabbed around medical protocols, do your best to answer the question.

01:12:31 - Brandon Hancock
What's cool though, like, you can also chain, so that's parallel calls, you can also chain different calls together, so for example, you could first just get all the embeddings, the embeddings will tell you which meeting notes they came from, so like, April 15th, there's stuff, and then you can have a second LLM call that actually reads that whole document, so like you could chain stuff together, so don't think it just has to be a RAG request.

01:12:58 - Brandon Hancock
You can get parallel sequential.

01:13:00 - Brandon Hancock
You can get as fancy as you want with a lot of these workflows.

01:13:02 - Brandon Hancock
And Paul's, he's getting fancy, he's doing the cool stuff.

01:13:08 - Brandon Hancock
So yeah, love the document, Paul.

01:13:11 - Brandon Hancock
Yeah, let me know if you have any questions on this.

01:13:12 - Brandon Hancock
I mean, I'm actively working on a project like this.

01:13:15 - Brandon Hancock
know Andrew has a ton of experience too, so happy to help however we can, Paul.

01:13:18 - Paul Miller
Thanks, Brandon.

01:13:19 - Brandon Hancock
We just got to get you this exit so we can play around all day, Paul.

01:13:22 - Brandon Hancock
I mean, come on, man.

01:13:23 - Brandon Hancock
You gotta, let's go and sell the thing so we can hang out.

01:13:26 - Paul Miller
Well, the good thing is I'll probably have to come up to the U.S.

01:13:31 - Paul Miller
all going well.

01:13:32 - Paul Miller
So I gotta go and do the, do the visit.

01:13:35 - Paul Miller
And, well, it sounds like, based on what Maxim says, I've got to go to Mexico as well and maybe pop down to Chile and see Bastien.

01:13:46 - Brandon Hancock
Yeah, I mean, hey, I mean, I still can't get over the call where Andrew and Maxim both popped on the same camera.

01:13:52 - Brandon Hancock
It's never been a two-player camera.

01:13:54 - Brandon Hancock
It is always one camera, one person, drinking their Coronas, having a good time.

01:13:58 - Brandon Hancock
So jealous.

01:14:00 - Brandon Hancock
I absolutely love it.

01:14:03 - Brandon Hancock
All right, we'll keep on cruising, guys.

01:14:06 - Brandon Hancock
Next up, oh, Andrew, you were up, buddy.

01:14:09 - Andrew Nanton
Great.

01:14:10 - Andrew Nanton
Yeah, not a ton of updates.

01:14:12 - Andrew Nanton
I'll just mention a few things I've been playing with in case they are useful to anyone else.

01:14:17 - Andrew Nanton
So Langfuse, which I already mentioned, for the prompt management and evals, that's pretty cool.

01:14:26 - Andrew Nanton
And with a .edu address, they gave me a free year of the cloud hosted version that's HIPAA compliant.

01:14:34 - Andrew Nanton
So that was really, yeah, yeah.

01:14:37 - Andrew Nanton
Like no questions asked, like a single line email, because they said, I mean, they said on their website, like, oh, if you have a .edu address, we'll give you a year.

01:14:45 - Andrew Nanton
I was like, hey, can I get that HIPAA compliant one?

01:14:48 - Andrew Nanton
And yeah, okay, sure.

01:14:51 - Andrew Nanton
The, so the other thing, HIPAA wise, that I was dealing with is using LLM guard, LLM.

01:15:00 - Andrew Nanton
Alright.

01:15:00 - Andrew Nanton
I don't know if you all have heard of this, but so it does use named entity recognition, you can, it'll do, by default, it does regex, but it will do NER via spaCy, and it has a, the sort of built-in model, or the model it tries to default to is one that is pretty specific to anonymizing health data, and LLM guard, yeah, yeah, that's it, and it's all open source, you can, you grab it for nothing, it has a great integration with light LLM as well, where, you you can, you can stick those two together pretty easily, and then Langfuse works well with this combo also.

01:15:46 - Andrew Nanton
Langfuse has some cool tracing stuff with, with using this Observe decorator that you stick on stuff, and it tracks things pretty well, so that was a cool combo, to work with.

01:16:00 - Andrew Nanton
I haven't really gotten anything to a point that I would want to show it off, but it's, anyway, those are cool technologies that I've been playing with, and the last thing that I've mentioned is I was trying to use FastHTML, the website is FastHT.ML for prototyping UIs, and it's nice because there is no front-end or back-end, it's all just one thing.

01:16:32 - Andrew Nanton
And so, you know, ostensibly, it's pretty simple, and it has an LLNs text file that you can point Cursor or Windsurf or whatever to, and that's pretty slick.

01:16:44 - Andrew Nanton
So, but there's just, it doesn't seem like there's enough documentation about it, or, you enough information that it, that I can just vibe code my way out of my horrible knowledge of I know, don't know.

01:17:00 - Andrew Nanton
Making UIs and web technologies, but it's out there.

01:17:05 - Andrew Nanton
You know, if people are using something like Streamlit, it's a viable alternative.

01:17:09 - Andrew Nanton
There's a thing called Monster UI that basically lets you use all of the Tailwind stuff in FastHTML very, very easily.

01:17:21 - Andrew Nanton
I'll drop some links in the chat, but that's the stuff I've been playing with.

01:17:25 - Andrew Nanton
And working my way around a Claude code and Jules and trying some of these CLI-based tools because I've been such a cursor guy.

01:17:34 - Andrew Nanton
So, yeah, that's the rundown for this week.

01:17:39 - Brandon Hancock
Real quick, because I know Juan has his hand up.

01:17:42 - Brandon Hancock
For LLM, I was looking at it.

01:17:44 - Brandon Hancock
So does it do banning, like, I was trying to look at the quick code.

01:17:49 - Brandon Hancock
So, like, banning talking about people, meaning, like, hey, no patient data.

01:17:54 - Brandon Hancock
Because I know that's probably something up here.

01:17:56 - Brandon Hancock
Like, hey, you can never say the patient's name.

01:17:59 - Brandon Hancock
Or do you know if it doesn't?

01:18:00 - Brandon Hancock
Anything like that, or is it more...?

01:18:01 - Andrew Nanton
I know it has some guardrail stuff.

01:18:03 - Andrew Nanton
It's a pretty big library, but what I was using it for is anonymize this content.

01:18:09 - Andrew Nanton
know, like, I turn documents into Markdown, and then it will go through and do named entity recognition and be fairly smart about things like, you know, if someone's named Bill, and it has Bill and William, and it's, you know, Bill Jones, and it says Mr.

01:18:28 - Andrew Nanton
Jones, it'll replace all of those with Person 1.

01:18:32 - Brandon Hancock
Oh, that's so nice.

01:18:33 - Andrew Nanton
So there's some continuity through the document, and it will let you sort of seed that as well, you know, give aliases and nicknames and that kind of stuff.

01:18:42 - Andrew Nanton
And so, yeah, it's cool on that front.

01:18:45 - Andrew Nanton
That's what I was using it for.

01:18:48 - Brandon Hancock
That's cool.

01:18:48 - Andrew Nanton
But that is like 5% of what it does.

01:18:52 - Andrew Nanton
There's a bunch of stuff in there, and I can't speak to the rest of it.

01:18:55 - Brandon Hancock
Great find.

01:18:57 - Brandon Hancock
Always finding the cool stuff, man.

01:18:58 - Brandon Hancock
That's awesome, Andrew.

01:18:59 - Juan Torres
Hold on, I'm sorry, Andrew.

01:19:01 - Juan Torres
Yeah, no, this is pretty cool.

01:19:03 - Juan Torres
So this is the thing that you're saying that makes you HIPAA compliant, Andrew?

01:19:07 - Andrew Nanton
No, I mean, so, Langfuse, that's, I was saying, they have a, which is prompt management and emails, they have a HIPAA compliant version that they were quite generous with giving me access to.

01:19:25 - Andrew Nanton
As a separate thing, this is a, this is a tool that will anonymize data or, you know, it'll anonymize and then de-anonymize.

01:19:36 - Andrew Nanton
And so, you know, I, I, as far as I understand that, that does not make something HIPAA compliant.

01:19:41 - Andrew Nanton
I mean, you could, but you can sort of round trip it to say, you know, replace all of these instances with sort of a, a person one, and then ship it out to an LLM.

01:19:52 - Andrew Nanton
And then when it comes back, replace all of that information.

01:19:57 - Andrew Nanton
You know, HIPAA is a large income.

01:20:00 - Andrew Nanton
EAST.

01:20:01 - Andrew Nanton
And as I understand it, just doing that isn't really enough.

01:20:04 - Andrew Nanton
Like, just anonymizing it, especially with sort of an automated tool, probably isn't enough to say that you're HIPAA compliant.

01:20:12 - Andrew Nanton
But it doesn't hurt.

01:20:14 - Andrew Nanton
So, I mean, if you're looking to anonymize things and at least reduce the footprint of spreading around personal health information or personally identifiable information, it's a good tool to have in your pocket.

01:20:27 - Andrew Nanton
Because the other thing that I'm thinking about is, going back to the evals, is I have this HIPAA compliant access on length use, but I don't necessarily want to put real documents on there.

01:20:40 - Andrew Nanton
And so for my evals, I can squirt out a bunch of anonymized actual documents, but they're anonymized.

01:20:46 - Andrew Nanton
And it's a HIPAA compliant service, but I don't want things just resting on there that have a bunch of people's information on them.

01:20:52 - Andrew Nanton
And for evals, I don't need that level of detail.

01:20:55 - Andrew Nanton
And so I can anonymize those and then, you know, work with those in a way that...

01:21:02 - Juan Torres
So are they HIPAA compliant because they're hosting their models in their secure servers?

01:21:08 - Andrew Nanton
Is that a reason?

01:21:09 - Andrew Nanton
One kind of like bridge shift?

01:21:12 - Andrew Nanton
So Langfuse does not do models as far as I know.

01:21:17 - Andrew Nanton
It's just this tool for sort of storing prompts and storing evals that you will test your prompts against.

01:21:26 - Andrew Nanton
So it still has to leave to go to an LLM.

01:21:30 - Andrew Nanton
And I have a HIPAA compliant Claude or Anthropic API account.

01:21:36 - Andrew Nanton
And on Azure, I have a HIPAA compliant GPT 4.1 deployment.

01:21:45 - Andrew Nanton
And so those are the ones that I use.

01:21:47 - Andrew Nanton
And as far as I understand, if you set up an Azure account, you have a BAA with them.

01:21:55 - Andrew Nanton
And so you can deploy your own and, you know, do it that way.

01:21:59 - Andrew Nanton
And Amazon has something.

01:22:00 - Andrew Nanton
things similar if you want to deploy the anthropic models.

01:22:03 - Andrew Nanton
but, uh, yeah, I mean, I, I think if you put those two things together, you're, you're looking pretty good.

01:22:12 - Brandon Hancock
How did you, real fast, Andrew, how'd you find the, the, uh, LLM guard tool?

01:22:17 - Andrew Nanton
Oh, so, yeah, well, I was looking at, um, I was using light LLM along with length use because I wanted to do some evals and compare the results of different models.

01:22:32 - Andrew Nanton
and, uh, and, but then as I was looking, I was like, well, maybe I want to anonymize this.

01:22:36 - Andrew Nanton
And so I did just a quick search and, um, in the length use documentation, or excuse me, in the light LLM documentation, it's like, oh, did you know, light LLM has this, you know, anonymization and de-anonymization feature integrated because of light LLM, or excuse me, because of LLM guard.

01:22:57 - Andrew Nanton
Gosh, all these names sound so similar.

01:22:59 - Andrew Nanton
All the same, yeah.

01:23:00 - Andrew Nanton
Um,

01:23:00 - Andrew Nanton
LANG and LLM, but yeah, so I found it in the, in the light LLM documentation and I thought, oh, well, great.

01:23:08 - Andrew Nanton
Let me use the most closely integrated stuff I can to make it simple.

01:23:12 - Brandon Hancock
No, totally makes sense.

01:23:13 - Brandon Hancock
And just to answer some questions that everyone is having some, so LANGFUSE is the vulnerability tool, which, so all it's doing is just like taking in like, hey, what did your agent do?

01:23:24 - Brandon Hancock
I'm going to store everything about that so you can look at it at a later date.

01:23:28 - Brandon Hancock
And what they're saying is, hey, LANGFUSE itself, the way it stores information, it is HIPAA compliant.

01:23:34 - Brandon Hancock
So, like, yes, it actually will have the patient's name.

01:23:37 - Brandon Hancock
It, like, we're not using LANGGARD, like, quickly pull out the person's name, like, does not, like, not, like, that has nothing to do with HIPAA compliant.

01:23:46 - Brandon Hancock
It's just more just like, hey, what, how do you want your LLM to behave?

01:23:49 - Brandon Hancock
So I just wanted to, like, clear that up.

01:23:51 - Brandon Hancock
It's not like LANGFUSE goes, no name, then, yeah.

01:23:55 - Brandon Hancock
So I just wanted to, like, clear that up.

01:23:57 - Brandon Hancock
Yeah, and really quick, someone here was asking about

01:24:00 - Andrew Nanton
the anonymization processing, doesn't that leak the names?

01:24:04 - Andrew Nanton
So that happens locally.

01:24:06 - Andrew Nanton
That's before any data leaves your system.

01:24:09 - Andrew Nanton
That anonymization step and using spaCy for the named entity recognition is running locally.

01:24:15 - Andrew Nanton
And so, I mean, it is faster if you, know, have something that accelerates PyTorch.

01:24:20 - Andrew Nanton
But, yeah, anyway.

01:24:23 - Brandon Hancock
Awesome.

01:24:24 - Brandon Hancock
Very cool.

01:24:25 - Brandon Hancock
Very, very cool tools.

01:24:26 - Brandon Hancock
I had no idea that that existed, but now they see it on, like, that makes so much sense.

01:24:31 - Brandon Hancock
Absolutely love it.

01:24:33 - Brandon Hancock
All right.

01:24:33 - Brandon Hancock
We will keep on cruising.

01:24:35 - Brandon Hancock
I think next up it is Robert and then Mark right after that.

01:24:43 - Robert
Good afternoon, everybody.

01:24:44 - Robert
How things going?

01:24:45 - Robert
Just for reintroduction, I'm Robert.

01:24:48 - Robert
Basically, I'm a beginner ADK developer.

01:24:51 - Robert
So, basically, I'm starting my journey into AI directly with ADK.

01:24:56 - Robert
So, I totally skipped, like, LangChain, LandGraph.

01:24:58 - Robert
I'm a crew AI.

01:25:00 - Robert
I'm

01:25:00 - Robert
So, with that being said, this is also one of the obstacles I've had to become is just letting go of my old mindset of the way I used to deal with, like, developing various things and that, and be more trusting of the AI, meaning that AI can help me do a lot of things that I used to do and free up time for, like, more valuable tasks and that, so that has been part of my journey as well.

01:25:24 - Robert
So, as a follow-up question from last week, Brandon, your video about your AI workflow, when you created your master plan, your document, and then you went to your tasks, when you created your tasks, do you specifically request for your tasks to be, like, independent of each other?

01:25:40 - Robert
Because there was that great point where you're basically able to, like, feed three tasks to Chris at the same time to, like, parallelize your workflow.

01:25:51 - Brandon Hancock
Yeah, so, let me just give you an example from what I did.

01:25:54 - Brandon Hancock
This week for A to A.

01:25:56 - Brandon Hancock
So, because I did literally the exact same workflow I was recommending, copied it.

01:26:00 - Brandon Hancock
So basically, in the A2A workflow, at the end, in phase three, we have multiple server agents.

01:26:08 - Brandon Hancock
One's LandGraph, one's Cray-AI, one's ADK.

01:26:11 - Brandon Hancock
So when I was going through and creating task, as I was creating task documents, like, like they were basically encapsulated work.

01:26:20 - Brandon Hancock
So as I was creating the ADK agent, I was outlining the task.

01:26:25 - Brandon Hancock
So I was like, hey, your job is to create the ADK task, it needs to be a follow A2A protocol, so there's gonna be an agent executor, you need to have a server, you need to spin up a server, here's some examples code that you should look at for reference, and here's the purpose that I'm trying to accomplish.

01:26:44 - Brandon Hancock
And that's, and then I just rinse and repeat one for ADK, did another one for Cray-AI, and another one for LandGraph.

01:26:52 - Brandon Hancock
So that is the exact workflow.

01:26:54 - Brandon Hancock
I tried to keep everything isolated for tasks.

01:26:57 - Brandon Hancock
However, when I was creating task two, took, like,

01:27:00 - Brandon Hancock
Let's say I did ADK and I was going to Cray.ai.

01:27:02 - Brandon Hancock
I was totally fine to point back to the first one to say like, hey, this task just finished up.

01:27:07 - Brandon Hancock
I really like the style and approach it finished.

01:27:09 - Brandon Hancock
Now we're just going to do it again for the next technology.

01:27:12 - Brandon Hancock
So you could also use previous tasks to help you create future tasks.

01:27:17 - Brandon Hancock
So that's literally exactly what I did this week.

01:27:20 - Brandon Hancock
So, practice and what I preach, man.

01:27:24 - Robert
Yeah, totally get that because I was also working on a non-technical related project using AI Studio.

01:27:31 - Robert
So basically, I had to finish an online certification that was working on.

01:27:34 - Robert
So, there was nothing against using AI.

01:27:36 - Robert
It was like open book, basically.

01:27:38 - Robert
So basically, I used an AI Studio to help me like, for example, our context and everything where I was able to upload like this manual and this manual, the digital version, of course, into AI Studio, into like the context window, as well as like a written journal that I've had of like various ideas I had.

01:27:58 - Robert
I was able to take my ideas I had to use this style.

01:28:00 - Robert
realistically to create the answers that I had to sound like more like me and everything.

01:28:03 - Robert
So that was like another evolution in my process of using like AI to push what I perceive to be its boundaries within the context of my personal life and that.

01:28:16 - Robert
my next step definitely is to build that agent that I've been talking about for the past couple of weeks and have like maybe a brief demo like next week of a high-level agent just to get the feedback and commentary from individuals.

01:28:30 - Robert
Because now that I've gone through your video about the workflow and everything, I'm finally able to put everything step-by-step-by-step.

01:28:37 - Robert
Because if I tried to create that agent about three weeks ago before I created your content, it would have been a very long, painful, like, process.

01:28:47 - Brandon Hancock
So what is the goal of the agent you're looking to build?

01:28:50 - Robert
So basically it's a virtual customer service agent that helps like individuals with customer service.

01:28:56 - Robert
So whether or not it's already been built or not, that's fine.

01:28:59 - Robert
So the end goal is like the end

01:29:00 - Robert
learning process of, like, building agents and everything.

01:29:04 - Brandon Hancock
Yeah.

01:29:04 - Brandon Hancock
So, um, yeah, so it, so a few things I definitely recommend checking out.

01:29:10 - Brandon Hancock
I think it was towards the end of the crash course.

01:29:14 - Brandon Hancock
I think there was something around just, like, hey, if you, I was pretending, like, you bought the course that you can access thing, I would, I would look at that one for, for inspiration.

01:29:25 - Brandon Hancock
I think that would be a really good, like, reference one.

01:29:29 - Robert
Yep.

01:29:29 - Robert
That was, like, the, um, permanent state, um, agent where you, like, showed us how to use, like, permanent state and store it into, like, the database and retrieve it.

01:29:37 - Robert
Yes, I really remember.

01:29:38 - Robert
So, yeah, so as Al was saying, like, um, I also stand by what Al said about how, um, your videos are amazing and even better than, um, the Google's, like, tutorials themselves.

01:29:47 - Robert
So, I also test what Al had said.

01:29:50 - Brandon Hancock
I'm waiting for them to pay me.

01:29:51 - Brandon Hancock
No checks have come in the mail.

01:29:53 - Brandon Hancock
So, um, but as soon as it does, I'll let you guys know.

01:29:56 - Brandon Hancock
But, uh, yeah.

01:29:57 - Brandon Hancock
But seriously, thank you guys.

01:29:58 - Brandon Hancock
I appreciate, appreciate that.

01:30:01 - Robert
So that's it for me for now.

01:30:03 - Robert
So thank you very much, Brandon, and everybody else.

01:30:05 - Brandon Hancock
Thank you for listening.

01:30:07 - Brandon Hancock
Perfect.

01:30:07 - Brandon Hancock
All right.

01:30:07 - Brandon Hancock
Well, hey, I'm pumped to see your ADK agent in action next week, man.

01:30:12 - Robert
Would love to see it.

01:30:14 - Brandon Hancock
And yeah, like I next week, if you have any questions about building it, like, hey, can you look at this for me?

01:30:20 - Brandon Hancock
Happy to look at it on the call.

01:30:22 - Brandon Hancock
I'm pumped to see it.

01:30:23 - Robert
Yeah, because essentially you've already given me the blueprint beyond, like, building the bot itself, but the fast API to give it voice.

01:30:33 - Robert
And that's in one of your videos already.

01:30:35 - Robert
And then my last one is deploying it to, I can't remember if it's agent, agent or agent space, but that's another part.

01:30:41 - Robert
So I already have a roadmap review on where to go from when I actually create the MVP on how to actually deploy it into my personal Google Cloud account.

01:30:50 - Brandon Hancock
No, I'm so excited for you.

01:30:52 - Brandon Hancock
And I will say, though, real fast, I am going to be doing a second video on deployment now that they've released the new way.

01:31:00 - Brandon Hancock
to deploy, because everything in the past was, yeah, you deploy a root agent, like in that first video I did on ADK, and you know, it just works, like it was magic, but if you want a little bit more control with what's happening, you might want to, the new approach I'm going to show, you're going to see how it exposes an API endpoint, we can maybe massage some data along the way, so you're going to have a little bit more control in the new version that I'll showcase here late next week.

01:31:28 - Robert
Will it also include Cloud Run?

01:31:31 - Brandon Hancock
Yes, yeah, I was going do Cloud Run.

01:31:33 - Robert
Okay, that's good, yep, and I guess the last thing I just want to close off is that this journey towards being an ADK developer has really required like an identity shift on my part, meaning that letting go of all the old practices that made me successful previously in my tech career, and embracing like a whole new mindset, similar to what Jyota said, you need to unlearn what you've learned.

01:31:58 - Brandon Hancock
No, yeah, no.

01:32:00 - Brandon Hancock
Yeah, totally, totally makes sense.

01:32:02 - Brandon Hancock
It's funny, and like seriously, 100% agree with you, like a lot of developers just refuse to use, they're like, I'll never let AI write code for me.

01:32:09 - Brandon Hancock
It's like, okay, cool, you just used, you just like, it took you one afternoon to make one file.

01:32:16 - Brandon Hancock
Cool.

01:32:16 - Brandon Hancock
I've literally built the entire project.

01:32:19 - Brandon Hancock
You know, like it is, it's wild.

01:32:21 - Robert
So I totally understand where you're coming from.

01:32:24 - Brandon Hancock
Yeah, exact same.

01:32:25 - Juan Torres
Juana, your hands up, buddy.

01:32:27 - Juan Torres
Yeah, just a question, Brandon.

01:32:30 - Juan Torres
Um, do you know if ADK has a similar, uh, crew AI enterprise structure that allows you to interact and then build the agent deck system automatically, or it still doesn't?

01:32:44 - Brandon Hancock
At this point, no, it does not have, uh, they have a thing called agent garden, which is like, you can find, but like, the agent workflow UI builder that you're, I think, referring to an enterprise to a basically, like, it almost feels like N8N to where it's like, okay.

01:33:00 - Brandon Hancock
cool, I'm going to have a research agent, I'm have a writer agent, and you're just plopping it in and giving them tasks, no, they don't have that set up yet.

01:33:09 - Brandon Hancock
So that's like the one, it's like the work, it's like the ADK is both, it can be a workflow agent or just a straight up chat rag agent, whereas like crew AI at this point is like almost pure workflow, so like it makes so much sense for crew AI to always be like workflow, A, B, C, D, always left to right, but with ADK, there's, there's more steps to it, because it's like, oh you have a workflow, well like, is the root agent the entry to the workflow, does the root agent call the workflow, like there's, there's a little bit more complexity to it.

01:33:40 - Brandon Hancock
So you get all the, you get all the niceties of land graph and crew AI, and a nice chat functionality, but yeah, they're still I think cranking out a lot of those like more UI features, because they just released agent engine UI, like two weeks ago, so they're cranking out code, but yeah, the second they make that, that though, oh my.

01:34:00 - Brandon Hancock
Oh gosh, I will be, I can't tell you how excited I will be.

01:34:03 - Brandon Hancock
It's gonna, it's gonna be amazing.

01:34:05 - Brandon Hancock
Um, okay, uh, perfect.

01:34:09 - Brandon Hancock
Um, let's see, wanna go back to, uh, Paul List.

01:34:13 - Marc Juretus
Uh, I think, Marc, you're up next, right?

01:34:15 - Marc Juretus
Marc yeah.

01:34:16 - Marc Juretus
Can you guys hear me?

01:34:17 - Marc Juretus
Marc Staying out of trouble?

01:34:18 - Marc Juretus
You know me!

01:34:19 - Marc Juretus
I stay out of trouble, right?

01:34:21 - Brandon Hancock
Marc Juretus Don't get caught.

01:34:23 - Marc Juretus
just usually, I usually just get on to see what everybody's up to, but, um, I can get kind of going on.

01:34:28 - Marc Juretus
One thing I'll say, Robert, and I saw, Marc start now, as Brandon knows, I've learned Landgraf, and then I've learned Crew very well, and then, of course, he came out and started with ADK videos, so now I'm in that, so this dude, man, is just killing me here.

01:34:40 - Marc Juretus
It's like walking by Foot Locker store and seeing New Jordans, but what I, what I will say, though, out of the three frameworks, like, ADK is the most fun, the easiest to use, the intertwined, uh, Landgrafs could be a pain, but Crew AI is, kick butt, too, but I really like ADK.

01:34:57 - Marc Juretus
So, um, what I'm working on right now 2.

01:34:59 - Marc Juretus
1.

01:35:00 - Marc Juretus
2.

01:35:00 - Marc Juretus
3.

01:35:00 - Marc Juretus
4.

01:35:00 - Marc Juretus
Thank

01:35:00 - Marc Juretus
Of course, work is starting to get that AI thing, so we developed a job at Spring Boot, so there's a Spring AI that's out there, so we kind of did just a demo where I had like an employee where you had the first name, the last name, the skill set needed for the job, and then the last piece was it went out with the AI, pulled in a journey to learn and get them ready to go for the last property in the field for the database.

01:35:25 - Marc Juretus
So I just kind of showed them how I would connect and stuff, just to show the infancy of like, you know, you might have a data set of three or four things, but you might go get a couple other items to insert into the table that are AI-driven.

01:35:36 - Marc Juretus
But what I'm working on right now is in ADK, I'm trying to have some fun now and stop trying to learn new stuff.

01:35:43 - Marc Juretus
So you know I'm gonna do the Fantasy Football app coming up July, but unfortunately right now, August 1st is when that kind of kicks in, so what I'm doing is, I'm a big video game, I'm probably the oldest on the call here, but I'm a big arcade game fanatic, I had Donkey Kong and Punch Out My Basement, so I created a company called

01:36:00 - Marc Juretus
Rallo port is my little game, right?

01:36:02 - Marc Juretus
So I have an inventory where you can go on with ADK with the customer service agent.

01:36:07 - Marc Juretus
I have a Docker Postgres database where you query it and it'll tell you the number in stock, what they have, what's the price.

01:36:14 - Marc Juretus
I can actually show it real quick.

01:36:15 - Brandon Hancock
I'll just show a couple of queries.

01:36:16 - Brandon Hancock
Yeah, that'd be awesome.

01:36:17 - Marc Juretus
What I got.

01:36:19 - Marc Juretus
But I did have one question for you, though, as I'm rambling on, as I always do.

01:36:25 - Marc Juretus
So I apologize, guys.

01:36:29 - Marc Juretus
Can you see my screen?

01:36:31 - Brandon Hancock
It'll be popping up.

01:36:32 - Brandon Hancock
Nope, perfect.

01:36:33 - Brandon Hancock
I can see the manager agent.

01:36:34 - Marc Juretus
Yeah, so I mean, there's not too much to it right now, but it's actually functioning pretty well.

01:36:38 - Marc Juretus
So basically, it's called Rallo Port.

01:36:41 - Marc Juretus
Long story short, biggest video game arcade around here was called Space Port.

01:36:44 - Brandon Hancock
My name on the internet was like Rallo, like whatever you call your handle.

01:36:49 - Marc Juretus
So I call it Rallo Port.

01:36:50 - Marc Juretus
So anyways, I have, obviously I have the sub-agents with the customer service agent.

01:36:54 - Marc Juretus
Not a customer service agent is basically using a tool with that, but I'll talk to you about that.

01:37:00 - Marc Juretus
That's where I have a question.

01:37:01 - Marc Juretus
They'll answer the questions like, hey, my joystick stuff or I won't power on.

01:37:05 - Marc Juretus
And then I have the sales agent, which goes in.

01:37:08 - Marc Juretus
Now this goes back against this Postgres database here.

01:37:13 - Marc Juretus
And it'll come in and it'll basically pull in, like, here's the inventory in here.

01:37:17 - Marc Juretus
I have Pac-Man, Defender, Donkey Kong, Dragon Slayer, Galaxian if anybody wants the game and stuff.

01:37:23 - Marc Juretus
But anyways, let me go back to the code here.

01:37:27 - Marc Juretus
But anyways, and then I'll have a, I also have another agent for customer service that I'll put in there.

01:37:33 - Marc Juretus
But I have the technical agent here that answers questions.

01:37:36 - Marc Juretus
So I think I have it in the browser here.

01:37:38 - Marc Juretus
So right now this is what it does.

01:37:40 - Marc Juretus
So right now I can say, do you have Donkey Kong?

01:37:50 - Marc Juretus
And then it'll come back.

01:37:54 - Marc Juretus
Doing the agent, getting inventory.

01:37:56 - Marc Juretus
That's going against Docker.

01:37:57 - Marc Juretus
It's pulling in from the database.

01:37:59 - Marc Juretus
And then it'll come back.

01:38:00 - Marc Juretus
And come back.

01:38:00 - Marc Juretus
that we have in stock, please list all video games in stock, this does, that's the one thing, I know you were talking earlier about the database, but the one thing you can't beat is with, when it goes back in and pulls in a data set, it can massage the data, think, a lot, and then a bunch of queries that, you always have some query and it doesn't work, so now it lists all the games, and then the other one is, like, my machine won't turn on, and now, before saying that, could you go to events, the last one, I'm just curious which agent, so, uh, fives, um, yeah, okay, I would just, I was curious, I saw there was an agent delegation earlier, I was curious if it went back to root agent, or if it stayed at the current agent, so I was just, I was just curious, what happened, okay, all right, oh, but anyways, I mean, I'm rambling, but anyways, it didn't, my

01:39:00 - Marc Juretus
My machine won't turn on, which is obviously going to call the trouble agent, you know?

01:39:06 - Marc Juretus
So I need to go with that.

01:39:07 - Marc Juretus
And, like, right now, I'll have that.

01:39:09 - Marc Juretus
That's going to be pulling from...

01:39:11 - Marc Juretus
So there's my question.

01:39:13 - Marc Juretus
So right now, I went into Claude and I said, hey, my company's name is RolloPort.

01:39:18 - Marc Juretus
Here's our warranty information.

01:39:21 - Marc Juretus
And here I want...

01:39:22 - Marc Juretus
I just said, give me, like, a bunch of troubleshooting stuff for Arcade Games.

01:39:25 - Marc Juretus
So I had to do all that.

01:39:27 - Marc Juretus
Now, what I did was...

01:39:29 - Marc Juretus
And I wanted to ask you this in industry, is this how it's used, where...

01:39:33 - Marc Juretus
Would somebody take, like, say you had 10 or 15 PDFs?

01:39:37 - Marc Juretus
Like, I basically have a conversion to Chrome DB.

01:39:41 - Marc Juretus
I have it in RAG, using OpenAI embeddings.

01:39:43 - Marc Juretus
And I'm able to query that.

01:39:46 - Marc Juretus
But against...

01:39:47 - Marc Juretus
Like, I did a PDF and I did a text document.

01:39:50 - Marc Juretus
Well, my one problem that I had was, that the first question was, I saved this as a PDF using, like, QPDF or something.

01:39:57 - Marc Juretus
Any other PDF, that I read in for RAG?

01:40:00 - Marc Juretus
was fine, ran it in, I could ask whatever question I want, I got a data set, but this one here, when I would pull it in, I would have a bunch of backslash N's or A's that were empty.

01:40:12 - Marc Juretus
And I was like, I was trying to wonder, like, was there a specific format of PDF you had to save it as?

01:40:17 - Marc Juretus
That's where I was, like, really kind of confused.

01:40:19 - Marc Juretus
Does that make any sense to you?

01:40:20 - Brandon Hancock
Have you seen that before?

01:40:22 - Brandon Hancock
No, I'm just, what tool did you use to generate the PDF?

01:40:26 - Brandon Hancock
What happened?

01:40:26 - Marc Juretus
Um, I did ChromaDB and I did, uh, language, uh, link chain, uh, embeddings here.

01:40:31 - Marc Juretus
I'll pull up the code that I have for the actual creation of it.

01:40:34 - Marc Juretus
Um, sorry, it should be right here.

01:40:37 - Marc Juretus
Uh, it's, yeah, PhilDB3.

01:40:40 - Marc Juretus
So basically I'm doing, uh, well, I still use link chain and crew AI.

01:40:44 - Marc Juretus
I still use for some stuff that, obviously, you know, you can embed it as a tool, but anyways, for this embedding, I did link chain embeddings.

01:40:52 - Marc Juretus
Um, and then I've, you know, brought in this text embedding small.

01:40:55 - Marc Juretus
Now it works fine.

01:40:56 - Marc Juretus
Like I just basically copied that as text, Brandon and read it in.

01:41:00 - Marc Juretus
and it ragged fine, without issue, but when I tried to use a PDF, I was like, all right, you know, I started using PDFs where I want to, like, make my whole documentation for, like, the customer service agent.

01:41:12 - Marc Juretus
I want to make sure it's able to read it in.

01:41:14 - Marc Juretus
So my question was, did you ever see that where you tried to read it in and there were a bunch of blank lines from something you got from Claude?

01:41:21 - Brandon Hancock
No, I mean, I'm curious if just the link chain document processor is what was causing that issue.

01:41:27 - Brandon Hancock
I'd be, if, if you did that exact same process with docling, I would be curious if it just does a better job processing PDFs.

01:41:34 - Brandon Hancock
And I would assume yes, um, batching brought up a good point.

01:41:39 - Brandon Hancock
If you're going to be generating stuff, probably just going directly to markdown would probably be the easiest.

01:41:44 - Brandon Hancock
Like, if you're going to be doing the data generation.

01:41:47 - Marc Juretus
Just have it as an end file as opposed to PDF.

01:41:50 - Brandon Hancock
Yeah.

01:41:50 - Brandon Hancock
Oh, it's so clean.

01:41:51 - Brandon Hancock
And it's like, easy headings, easy subheadings.

01:41:54 - Brandon Hancock
Yeah.

01:41:55 - Marc Juretus
I was like thinking like, say somebody came to me, like, I see like a code of you guys have that had a bunch

01:42:00 - Marc Juretus
PDFs, or say I had Word documents or whatever, and I was like, all right, let me just convert them all to PDFs, but you're probably saying, like, I just want to make sure I don't have a stupid issue with stuff that I save, like, was there some specific tool to save it as?

01:42:14 - Marc Juretus
Like, I use QPDF.

01:42:16 - Brandon Hancock
I know there's a ton of PDF creators out there.

01:42:19 - Brandon Hancock
Yeah, I mean, I haven't really used QPDF, so my guess is what happened during the, because I knew you said, wait, was the blank?

01:42:30 - Brandon Hancock
Where was the blank spaces or blank returns getting added?

01:42:33 - Marc Juretus
So, basically, when I ran this and I did a loop of, like, the data that the output here, like, it's, you know, the things and stuff, it was writing, like, the text file was fine, but the PDF, it just, like, I was kind of, like, the output as it was doing, you know, the read.

01:42:48 - Marc Juretus
It was, like, the backslash, backslash, send, zero, zero, zero.

01:42:51 - Marc Juretus
And I'm like, what's odd in that clogged document that I saved as a PDF that's causing that, which was, like, strange.

01:42:58 - Marc Juretus
So.

01:42:58 - Brandon Hancock
Yeah.

01:42:59 - Brandon Hancock
Seriously, I think.

01:43:00 - Brandon Hancock
Yeah.

01:43:00 - Brandon Hancock
I mean, Dockling, because you would do the exact same thing with Dockling, like, that is going to get copied 99% the exact same, you're gonna have a, you're gonna have pretty much the hybrid splitter, you're gonna have the embedding model, it's 99% the exact same, or, what was Chunky, what was the new tool we learned today?

01:43:17 - Brandon Hancock
I would try either one of those, and I, like, they are dedicated tools to extracting out of documents like that, so I'm 99% sure that Chroma from documents, I don't think, I think Chroma, I'd also be curious what version of Chroma you're using, too, because I think that could be another one.

01:43:39 - Marc Juretus
Really?

01:43:41 - Brandon Hancock
Yeah, potentially, because, yeah, yeah, yeah, I would, I would look to see which version you're using.

01:43:49 - Marc Juretus
Okay, so, yeah.

01:43:51 - Marc Juretus
So, of the questions I had was, so, anyways, the thing is with this is, like, obviously football starts in, like, a month or two, and, like I said earlier, I'm gonna try to build an app.

01:44:00 - Marc Juretus
that runs a fantasy team on its own for an entire season to see how it does.

01:44:05 - Marc Juretus
That's just my thing, but the thing is how I learned is like, all right, let me make a project that's fun, and I want to have FastAPI, I'll have Next.js consuming it, so I'll have everything down pack, I'll probably have a Next.js, a FastAPI container running on Docker, and then, all right, I know how to do all this stuff, now let's just apply it to the project that I'm working for next.

01:44:27 - Brandon Hancock
That's how I do it.

01:44:28 - Marc Juretus
But I want to do stuff like, okay, when you search Pac-Man, it goes out with Dali, or whatever you guys would say would be the best image generator, show me a picture of the front of the game and the side art.

01:44:38 - Marc Juretus
You know, I'll have to do like all that stuff, that's kind of fun to me.

01:44:42 - Marc Juretus
Instead of you putting out more videos and I got to learn something new every week.

01:44:47 - Brandon Hancock
Keeping you busy, man.

01:44:48 - Brandon Hancock
Yeah, that's what I'm here for.

01:44:50 - Marc Juretus
But the question I had was, if somebody had like, say, I did say the customer service agent there, would somebody do that where they had, say, 20 PDFs on the company?

01:45:00 - Marc Juretus
Listen,

01:45:00 - Marc Juretus
that were, like, technical documents.

01:45:02 - Marc Juretus
Would they, is that how they would structure their agent that, hey, we need to build something that somebody wants to ask a question about.

01:45:08 - Marc Juretus
Any of the items that we own, that would not be in any way database-driven.

01:45:12 - Marc Juretus
that be, would that be something that, in the industry, that they would pull in 10, 20 PDFs, rag it up, not make it searchable?

01:45:19 - Brandon Hancock
Yeah, it's, yeah, there's just a direct knowledge base is what, what they would do.

01:45:24 - Brandon Hancock
There's a, oh my gosh, I worked for the company that was, or, we almost, yeah.

01:45:30 - Brandon Hancock
There's a company that does this really well.

01:45:32 - Brandon Hancock
I have to go find them.

01:45:33 - Brandon Hancock
yeah, they basically, you just throw in PDFs, we make an open-ended chat bot that your users can talk to.

01:45:38 - Brandon Hancock
So yeah, if there's just 20 PDFs that are all made to help handle external requests, yeah.

01:45:43 - Brandon Hancock
That's, that's literally exactly what you would do.

01:45:45 - Marc Juretus
So, I was going to say, like, Brandon knows I took that course with the gentleman in India from January for that and stuff, but we would jump on calls at WebEx, so if anybody ever wants to jump on and, like, share what they're doing, I always find, they're

01:46:00 - Marc Juretus
It's fun to see what you're up to.

01:46:01 - Marc Juretus
I'll gladly join and jump on the Webex at any time.

01:46:04 - Marc Juretus
So I always find these interesting, all you guys are doing.

01:46:06 - Marc Juretus
That's why I'm on every week, man.

01:46:08 - Marc Juretus
Now, the Brandon's going, I'm going to not have a girlfriend ever.

01:46:12 - Marc Juretus
This is, with this stuff, man, you keep putting videos out, man.

01:46:16 - Brandon Hancock
She's like, babe, babe, what are you doing?

01:46:18 - Brandon Hancock
Brandon just made a new video.

01:46:20 - Brandon Hancock
Leave me alone.

01:46:22 - Marc Juretus
I think the best story, though, one time, because I listen to fantasy football in the car, and they're going over wide receiver rankings for the week, and the girls in the front seat, like, can we listen to some music, please?

01:46:31 - Marc Juretus
like, hey, there's a game on Sunday.

01:46:33 - Marc Juretus
Let's keep our priorities ready.

01:46:37 - Brandon Hancock
I love it.

01:46:38 - Marc Juretus
I love it.

01:46:39 - Marc Juretus
Oh, that's funny.

01:46:40 - Marc Juretus
guys.

01:46:40 - Marc Juretus
appreciate it.

01:46:41 - Brandon Hancock
Of course.

01:46:43 - Brandon Hancock
Any?

01:46:43 - Brandon Hancock
I know we have a few other guys on the call without a camera on.

01:46:47 - Brandon Hancock
If anyone has any questions, hey, we'd love to, if you want to pop on, ask some questions.

01:46:52 - Brandon Hancock
I'd love to hear what you guys are working on.

01:46:56 - Brandon Hancock
And then we'll take We'll it from there.

01:47:00 - Brandon Hancock
There, um, if not, I can potentially share some updates if no one has questions, um, so yeah, all right, so cool, I'll ask questions to you guys, we'll flip the script.

01:47:15 - Brandon Hancock
So, uh, put, oh wait, all Robert, up to you, then I'll, I'll take it back.

01:47:20 - Robert
Just one super quick question, um, are you still going to have the, um, cursor AI video?

01:47:26 - Brandon Hancock
I know that you've been working very hard on the A to A video.

01:47:30 - Brandon Hancock
Yes, so, hundred percent, the goal is, the next video is to be the cursor one, like that is the, like, A to A cursor, then, uh, um, ADK deployed, like that is the, the list, um, ADK, ADKs kicked my butt so hard, like, I cannot, like, I had to talk to the Google guys, I just didn't understand how it worked, I was like, what's happening, so it is taking triple the amount of time I expected it to, so just know there's a lot of blood, sweat, and tears in this video.

01:47:58 - Robert
Yep, I totally understand.

01:47:59 - Robert
Yeah, I totally understand.

01:48:00 - Brandon Hancock
A hundred percent, and the video definitely has expanded the Cursor one, so it'll probably be like a, cover the new update for Cursor, and then the back half will just be like tips, tricks, and everything, and I know that I said this was gonna be like the first community video, so I'll definitely add some, all the tips and tricks you guys shared, I'll do that at the end of it, so very excited and still pumped for all the cool tips and tricks you guys added.

01:48:26 - Robert
Cool thing.

01:48:27 - Brandon Hancock
Of course.

01:48:30 - Brandon Hancock
Uh, quick, uh, back to you, Paul, um, no, um, not at all, so you could actually deploy, that's the cool thing that you're gonna see in the new video, is ADK is going to have, uh, they basically have like two, two ADK, two fast API, to where it's like basically just boom, you know, have a, an endpoint that you can shoot requests to, so like, at that point, throw in a Docker container, throw it anywhere, you know, so you don't have to go vertex AI.

01:48:56 - Brandon Hancock
So all right, did make up that to make them a deep brush.

01:49:00 - Brandon Hancock
Thank

01:49:00 - Brandon Hancock
is their agent engine to where all you have to do is just like, hey, I have been playing with APK web and my app works perfect.

01:49:09 - Brandon Hancock
My agents are working.

01:49:10 - Brandon Hancock
They're delegating.

01:49:11 - Brandon Hancock
It's doing perfect responses.

01:49:13 - Brandon Hancock
Now, all I want to do is just deploy that work, the agent, and then have my front end application start making requests to that deployed, to the deployed agents.

01:49:24 - Brandon Hancock
So yeah, definitely.

01:49:25 - Brandon Hancock
But there's a lot more going on.

01:49:28 - Brandon Hancock
Yeah.

01:49:29 - Brandon Hancock
So I'll, I'll, talk more about that in the video coming up.

01:49:32 - Brandon Hancock
Okay.

01:49:32 - Brandon Hancock
Uh, a few questions for you guys.

01:49:34 - Brandon Hancock
So, um, uh, well, uh, for crew AI, they have been cranking out a bunch of updates, potentially doing a video with him on Friday.

01:49:43 - Brandon Hancock
I was curious if you guys had any questions for him, um, on anything crew AI.

01:49:50 - Brandon Hancock
So he's, I think mostly going to talk about new features that they've been building.

01:49:53 - Brandon Hancock
And yeah, I was just curious if you guys had any, had any questions.

01:49:57 - Brandon Hancock
Um, so far, was mostly just going to ask about like, Hey, any new use.

01:50:00 - Brandon Hancock
cases, any better, yeah, any new use cases, any ways that like, I think most of us are pretty entrepreneurial driven, any, you know, new ways you think developers can get involved, make money.

01:50:12 - Brandon Hancock
So those are like, I was going to go down more of the entrepreneur developer angle, but I was curious if y had any.

01:50:18 - Brandon Hancock
So, are they releasing any new tools coming out soon?

01:50:23 - Brandon Hancock
Okay.

01:50:25 - Brandon Hancock
Great question.

01:50:26 - Brandon Hancock
The short answer, I think, is yes.

01:50:29 - Brandon Hancock
I think they are integrating with a partner.

01:50:31 - Brandon Hancock
It's going to give them access to an insane amount of tools, I think, but I will ask.

01:50:37 - Brandon Hancock
Um, that is a phenomenal question.

01:50:39 - Brandon Hancock
Um, um, uh, Juan.

01:50:43 - Juan Torres
Yeah, what is the, what is the highest market demand for people you see in Korea right now in the market?

01:50:51 - Juan Torres
Like, what is it that they're building a genetic system for news analysis, for spreadsheet analysis, for PBA of analysis?

01:51:00 - Juan Torres
this.

01:51:00 - Juan Torres
I just want to know what's the highest demand out there, specifically for the finance sector, I would say.

01:51:07 - Brandon Hancock
Okay, so we'll break it down by sector.

01:51:10 - Brandon Hancock
Okay.

01:51:11 - Brandon Hancock
Um, no, it totally makes sense.

01:51:14 - Brandon Hancock
Um, okay.

01:51:16 - Brandon Hancock
Um, yeah, basically use cases.

01:51:19 - Brandon Hancock
Um, so do you want me to answer that question?

01:51:23 - Brandon Hancock
Or are you saying like what you want, uh, to answer?

01:51:27 - Brandon Hancock
Or both, I guess?

01:51:30 - Brandon Hancock
Uh, Paul.

01:51:34 - Paul Miller
Uh, no, I think it would be good for you to ask him, um, in terms of that, with ADK, ADK out, where does crew AI sit?

01:51:45 - Brandon Hancock
Um, okay.

01:51:49 - Brandon Hancock
Okay.

01:51:50 - Brandon Hancock
I'm honestly scared to ask that question, but I will ask it.

01:51:53 - Paul Miller
Just say, just say, it's not coming from you.

01:51:55 - Brandon Hancock
It's, uh...

01:51:56 - Brandon Hancock
Probably not Brandon.

01:51:58 - Paul Miller
From Paul.

01:51:59 - Paul Miller
That's I mean.

01:52:00 - Brandon Hancock
Good, Brad.

01:52:00 - Paul Miller
I mean, I'll be, I'll be, please release that at Webex if you do ask that question.

01:52:05 - Brandon Hancock
I want to see his face.

01:52:06 - Brandon Hancock
No, I mean, I think it's, mean, it really is a great question.

01:52:09 - Brandon Hancock
I'll tell you my answer too, by the way, because like what, what, like there are certain things that Crue AI does insanely well.

01:52:17 - Brandon Hancock
Um, so like it for standardized workflows, there's not a better, like, I think it is the most straightforward tool to allow you to automate processes with AI.

01:52:27 - Brandon Hancock
Cause like, especially the, uh, the multi-agent, multi-agent aspect.

01:52:32 - Brandon Hancock
In ADK, you can't do that.

01:52:35 - Brandon Hancock
Like right now in ADK, if you want one agent, if you have one task and you want multiple agents to work on that task, you, you have to, you have to basically like do loops and like pass in active agents.

01:52:49 - Brandon Hancock
Like it is a ton.

01:52:50 - Brandon Hancock
So like a Cray, I still has that, like no one, no one's even come close right now on true multi-agent to where they're all working on the same task, collaborating, working together.

01:53:00 - Brandon Hancock
because right now, even in ADK, it's just straight up tool calls.

01:53:04 - Brandon Hancock
It's like, okay, agent, what do you think?

01:53:06 - Brandon Hancock
Okay, other agent, what do you think?

01:53:08 - Brandon Hancock
And then it takes action.

01:53:09 - Brandon Hancock
It's never really true multi-agent.

01:53:12 - Brandon Hancock
But yeah, that's my fixing.

01:53:14 - Brandon Hancock
Straight up workflows, Kurei dominates.

01:53:20 - Brandon Hancock
So if I had to just like automate something end to end, I mean, Kurei is probably where I go.

01:53:25 - Brandon Hancock
But the second I have to do chat with it, yeah, I mean, that's when I would probably like, oof, now you're making me forced.

01:53:33 - Brandon Hancock
I have to make a harder decision to figure out how important chat is versus AI automations.

01:53:39 - Brandon Hancock
There's obviously flows, but that's still not as easy as just straight up chatting.

01:53:44 - Brandon Hancock
But no, all right, Paul, I'm throwing you under the bus, buddy.

01:53:48 - Brandon Hancock
Your picture will pop up on screen.

01:53:50 - Brandon Hancock
This guy is trying to make you mad.

01:53:54 - Brandon Hancock
But no, yeah, I think it'll be a great conversation.

01:53:56 - Brandon Hancock
I'm sure he'll have a great answer.

01:53:59 - Brandon Hancock
So, I don't know.

01:54:02 - Brandon Hancock
Daxian, did you want me to ask about MCP?

01:54:05 - Brandon Hancock
Oh, it's just a comment.

01:54:07 - Bastian Venegas
I guess they are using it as a way to add tools to their agents for now, not like resources and prompts.

01:54:16 - Brandon Hancock
Okay, I got you.

01:54:18 - Brandon Hancock
I want to ask about MCP.

01:54:20 - Brandon Hancock
I think it's another quick question.

01:54:24 - Brandon Hancock
Makes sense.

01:54:26 - Brandon Hancock
I don't Thank you.

01:54:29 - Brandon Hancock
Fair in contrast.

01:54:30 - Brandon Hancock
Andrew, I like your more diplomatic approach.

01:54:33 - Andrew Nanton
We'll see how spicy I feel on the day, you know?

01:54:37 - Andrew Nanton
Yeah.

01:54:37 - Brandon Hancock
Brandon, can I ask a quick follow-up there?

01:54:40 - Andrew Nanton
Yeah.

01:54:40 - Andrew Nanton
Because you mentioned that you were doing this A2A stuff, and I guess while we're discussing Crew AI and MCP, I'd be curious his thoughts on A2A and is there a role in Crew AI for that?

01:54:54 - Andrew Nanton
And I'm also curious what you think.

01:54:56 - Andrew Nanton
You know, do you think A2A is going somewhere or do you think it's a...

01:55:01 - Brandon Hancock
Yeah, so, on the A to A front, so, so, if you just, like, if we just start abstracting up from the bottom, okay, so, right now, age, so, sorry, I had a thought and then it left me, but, basically, at the end of the day, like, an LLM to a tool call, it's kind of abstracted, meaning the agent does, doesn't know what's happening in the tool call, all it knows is the parameters it's gonna send in, and then it knows what the tool is gonna send back.

01:55:36 - Brandon Hancock
It also has, like, a high-level description of when to call the tool.

01:55:39 - Brandon Hancock
So, what A to A is doing is basically just abstracting upstream.

01:55:44 - Brandon Hancock
So, instead of, like, hey, I don't need to know exactly the code that's happening inside of this tool call, well, they're just going upstream and saying, hey, I actually don't need to know the inner workings of this other agent, I just need to know what inputs I can give it, what I can expect to get back, and when I should call it.

01:56:00 - Brandon Hancock
All they're doing is is

01:56:00 - Brandon Hancock
just going up the abstraction chain, and it logically makes sense, or there could be a need for it.

01:56:08 - Brandon Hancock
It kind of feels like Web3 right now, like, oh, I understand that, like, it is cool if there's these digital wallets and, like, we could do it to hold currencies, we could do it to, like, do all these fancy stuff, so I see the need for it in, like, a world where, like, Andrew's agent, Andrew's, you know, public-facing agent is trying to talk to Paul, agent, and they're gonna go hash stuff out, figure a plan, see when they can meet, schedule a trip, like, that makes sense.

01:56:34 - Brandon Hancock
Or if I'm trying to have my agent talk to a Google agent to, like, send us some calendar events, it makes sense.

01:56:41 - Brandon Hancock
The second they finish, they get authentication working.

01:56:45 - Brandon Hancock
That's when it makes sense.

01:56:48 - Brandon Hancock
Like, when they can properly do handshakes, because, oh my gosh, it's gonna be so easy to say, like, all right, I would like to go send an email, check a calendar, and almost not have to do MCP.

01:56:59 - Brandon Hancock
And that's the problem of...

01:57:00 - Brandon Hancock
GCP is like, I have to pass in environment variables and I'm instantly limited to the 10 tools that I have access to.

01:57:07 - Brandon Hancock
Whereas if you do A to A, well, like, hey, I can actually just go search all the agents that, you know, potentially in a repository and go from there.

01:57:15 - Brandon Hancock
So I do think, like, 100% honest answer, I think it's early.

01:57:20 - Brandon Hancock
I do think it's early, but it's like one of those things of like, I think it's a very important technology that will gain traction as more companies make external facing agents.

01:57:29 - Al Cole
Is, like, my, like, short answer.

01:57:31 - Al Cole
And just 30 seconds.

01:57:33 - Al Cole
This is Al again, Brandon.

01:57:35 - Al Cole
I wanted to highlight from the slides I'll share with the team, but they covered A to A very, very lightly, but they did give us this diagram and I remember back you mentioning the same thing about crew AI and its ability to have kind of competing agents and then you kind of evaluate.

01:57:53 - Al Cole
They're claiming in their slides here that the A to A is how you would get there.

01:57:59 - Al Cole
So that kind of an architecture.

01:58:03 - Brandon Hancock
No, it totally makes sense.

01:58:05 - Al Cole
That's, I think, how they think they're going to get to that answer of having competing agents and then synthesizing.

01:58:15 - Brandon Hancock
No, yeah, totally makes sense.

01:58:18 - Brandon Hancock
Yeah, definitely early.

01:58:19 - Brandon Hancock
I think the second 1.0 comes out probably in a few months, I think A, it'll be simpler.

01:58:25 - Brandon Hancock
I think it's going to have better authentication and then I think you're going to see an insane rise in people building front-end, especially front-end and internal agents.

01:58:37 - Brandon Hancock
Because everyone's always like, oh, I want to have an army of agents.

01:58:39 - Brandon Hancock
Well, right now you can't.

01:58:40 - Brandon Hancock
Like, the truthful answer is you can't.

01:58:42 - Brandon Hancock
Because I have an ADK agent, it has a fixed number of sub-agents, and that's all that little cluster of agents can do.

01:58:50 - Brandon Hancock
It can make some tool calls, but there's no actually, like, talking to the next cluster of agents, if that makes sense.

01:58:58 - Brandon Hancock
That doesn't exist right now.

01:58:59 - Brandon Hancock
what's.

01:58:59 - Brandon Hancock
But

01:59:00 - Brandon Hancock
that's what they're solving.

01:59:01 - Brandon Hancock
So it gets, it gets me hyped that it's like happening, but, um, but it is early.

01:59:06 - Brandon Hancock
So, yeah.

01:59:08 - Brandon Hancock
And, um, yeah, Al, seriously, I would love to see those samples and any other stuff that they talked about, just because I think it's, I think it's super cool what they're, what they're talking about and doing.

01:59:18 - Brandon Hancock
Um, it's cool that got the inside scoop.

01:59:22 - Brandon Hancock
Um, okay, uh, any other quick question, Nate, if you want to, what's up, buddy?

01:59:36 - Brandon Hancock
It's fighting you.

01:59:40 - Brandon Hancock
I think it's still muted.

01:59:41 - Nate Ginn
Oh, there.

01:59:42 - Nate Ginn
Can you hear me now?

01:59:43 - Brandon Hancock
Yeah, there we go.

01:59:45 - Brandon Hancock
Hello, hello.

01:59:45 - Nate Ginn
Okay, there we go.

01:59:47 - Nate Ginn
Okay, so I'm gonna dummy down this conversation like I usually do.

01:59:52 - Nate Ginn
Is, is, there's a lot of, I'm looking for a CRM program.

01:59:58 - Nate Ginn
Yeah.

01:59:59 - Nate Ginn
And I know there's a lot

02:00:00 - Nate Ginn
There's lot of them out there that you can choose from.

02:00:01 - Nate Ginn
Some of them are even pretty probably free and stuff like that.

02:00:05 - Nate Ginn
But with all the stuff that you're working on, it seems like this would be like the simplest thing to create with all of this.

02:00:13 - Nate Ginn
But, you know, where it might have like not only the database of your contacts, but also like a chat component that you could ask questions like, you know, when was the last time we had a conversation with this to get our contact?

02:00:29 - Nate Ginn
Things like that.

02:00:30 - Nate Ginn
Anyway, I just was trying to get suggestions if anybody had like a recommendation for a simple, it just needs to be a super simple CRM.

02:00:38 - Nate Ginn
Look at Paul's already going as usual.

02:00:41 - Nate Ginn
Thanks, Paul.

02:00:42 - Brandon Hancock
So my, uh, so I'm gonna show my example or my, my suggestion.

02:00:48 - Brandon Hancock
I'd seriously love for everyone to stop on.

02:00:50 - Brandon Hancock
Um, go high level, a hundred bucks a month.

02:00:53 - Brandon Hancock
You get a CRM.

02:00:54 - Brandon Hancock
You get the ability to send emails, text messages, phone calls.

02:00:57 - Brandon Hancock
You can set up like pipelines, automation.

02:01:00 - Brandon Hancock
you can set up.

02:01:01 - Brandon Hancock
Now they have the ability to do, like, AI employees.

02:01:04 - Brandon Hancock
I haven't seen this in action yet, but I think they are, like, on the cusp of something where, like, I think eventually all small to medium-sized businesses, it makes sense to just use GoHighLevel for everything.

02:01:20 - Brandon Hancock
Like, they're, they're, like, crushing it.

02:01:23 - Brandon Hancock
Because, like, chatbots, cool.

02:01:25 - Brandon Hancock
GoHighLevel, put a chatbot on your website.

02:01:27 - Brandon Hancock
They already allow you to do that.

02:01:29 - Brandon Hancock
I am now curious if they're going to allow you to automate outreach using these AI employees.

02:01:34 - Brandon Hancock
So that would be the next thing.

02:01:35 - Brandon Hancock
And then asking internal questions.

02:01:39 - Brandon Hancock
I don't know if they have that yet, but they are continually shipping out AI.

02:01:43 - Brandon Hancock
So I don't know why they wouldn't add that sooner or later.

02:01:45 - Brandon Hancock
So, yeah, that is my pitch.

02:01:48 - Brandon Hancock
But if other people have other suggestions, you know, we'd love to hear it as well.

02:01:57 - Brandon Hancock
For the price point, I think it's, it's pretty good in what they are.

02:02:00 - Ty Wells
They had a massive amount of features on there.

02:02:03 - Ty Wells
I built my own just because it was more AI-related.

02:02:08 - Ty Wells
Chatbot's already built into it and prompt library and all kinds of stuff.

02:02:12 - Ty Wells
But it was that and ATIO I looked at as well, ATTIO.

02:02:20 - Ty Wells
But yeah, go high level.

02:02:22 - Ty Wells
Can't beat the price for what you get.

02:02:25 - Paul Miller
Yeah, just from my perspective, we just moved my SaaS business back to Pipedrive.

02:02:34 - Paul Miller
used to use Pipedrive.

02:02:36 - Paul Miller
It's just really easy to use and it's simple and it's got a good UI UX.

02:02:44 - Paul Miller
It depends on how many users and what features you're using and what you're trying to do.

02:02:49 - Paul Miller
There's some devils in the detail.

02:02:51 - Paul Miller
But it's got a really good API that comes with it.

02:02:57 - Paul Miller
So if you're wanting to do like really weird queries,

02:03:00 - Paul Miller
or update records in a unique way.

02:03:03 - Paul Miller
It's really easy just to go into Claude and make an interface that communicates with the API.

02:03:13 - Paul Miller
So you might say, oh, I want to create tickets against customers in this way or these types of records from this other database.

02:03:24 - Paul Miller
And it's so easy to do because Pipedrive's been out there for quite some time.

02:03:30 - Paul Miller
And you can do that with the base license because I see with HighLevel, to get the API access, you've got to go to the $300 a user one, but the HighLevel's got a lot more features included in the price.

02:03:45 - Paul Miller
Pipedrive's one of those models that you keep stacking on top, and it ends up getting quite expensive.

02:03:51 - Paul Miller
But it's so simple to use.

02:03:55 - Nate Ginn
Thanks, Paul.

02:03:59 - Brandon Hancock
All right.

02:03:59 - Brandon Hancock
All right.

02:04:00 - Brandon Hancock
Any final questions?

02:04:00 - Brandon Hancock
Questions, guys?

02:04:00 - Brandon Hancock
I gotta hop off to get ready for another call in just a few, but any final things I can help with?

02:04:06 - Brandon Hancock
I love all the...

02:04:08 - Brandon Hancock
I've learned so much.

02:04:09 - Brandon Hancock
I think I learned, like, I love these calls because I learned so many new things, and I love getting hyped up to see all the cool projects you guys are working on, too.

02:04:15 - Brandon Hancock
So, I always love the Tuesday calls, but just want to check, any final things?

02:04:21 - Brandon Hancock
If not, just want to apologize, Brandon, I confused the time period.

02:04:26 - Brandon Hancock
I'm pretty LA-centric.

02:04:29 - Brandon Hancock
Dude, no worry.

02:04:30 - Brandon Hancock
I'm Eastern-centric, so I'm like, oh, 5.30, it's 5.30, dude.

02:04:32 - Brandon Hancock
I literally was on the call, and I was like, he wanted to do this.

02:04:36 - Brandon Hancock
Where is he?

02:04:37 - Brandon Hancock
And I was like, he's always on time to everything.

02:04:40 - Brandon Hancock
So, hey, we can just do something later in the week, just if you want to shoot over another, I'll send you my calendar, Lee.

02:04:48 - Brandon Hancock
We'll take it from there.

02:04:50 - Brandon Hancock
All right, perfect.

02:04:51 - Brandon Hancock
But yeah, I'll post this recording, guys.

02:04:52 - Brandon Hancock
I'll keep y'all posted, and A2A coming out to the crew AI interview, hopefully on Friday.

02:04:58 - Brandon Hancock
And I'll keep you guys in the loop.

02:05:00 - Brandon Hancock
Bye.

02:05:00 - Brandon Hancock
Yeah, hope you guys have a great rest of your week, and talk to you soon, okay?

02:05:03 - Brandon Hancock
All right, thanks.

02:05:04 - Brandon Hancock
All right, see you guys, bye.

