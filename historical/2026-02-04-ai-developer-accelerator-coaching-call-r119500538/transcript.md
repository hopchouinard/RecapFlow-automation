00:01:03 - Patrick Chouinard
Hey, Ty.

00:01:06 - Patrick Chouinard
I can't hear you.

00:01:08 - Patrick Chouinard
Yeah.

00:01:09 - Patrick Chouinard
I was just going to check and see because I saw you posted and then to mark this link.

00:01:14 - Ty Wells
And I was like, I think I might be in the wrong link.

00:01:17 - Patrick Chouinard
How are you going?

00:01:18 - Patrick Chouinard
Yeah.

00:01:19 - Patrick Chouinard
Very good.

00:01:19 - Ty Wells
Very good.

00:01:20 - Patrick Chouinard
I just reused the link from Brandon's message.

00:01:24 - Patrick Chouinard
Hmm.

00:01:25 - Patrick Chouinard
Okay.

00:01:26 - Ty Wells
No, it's just because the original link was tied to his profile, so I could not be hosting.

00:01:33 - Ty Wells
Okay.

00:01:34 - Ty Wells
It was his personal room.

00:01:36 - Patrick Chouinard
Yeah.

00:01:37 - Ty Wells
I see your document you put out there.

00:01:40 - Ty Wells
That was really good.

00:01:41 - Ty Wells
I was like, oh, my God.

00:01:43 - Ty Wells
I just happened to see that because you send the message about the question I read.

00:01:47 - Ty Wells
I think, oh, God, I don't have to do it.

00:01:49 - Ty Wells
Patrick did all the work and I know it's done properly and I don't have to worry about anything.

00:01:52 - Patrick Chouinard
can just use it right out the box.

00:01:55 - Ty Wells
Thank Thank you.

00:01:57 - Patrick Chouinard
I had up.

00:01:58 - Ty Wells
I had put my.

00:01:59 - Ty Wells
My.

00:01:59 - Ty Wells
I'd lock mine down in an EC2 instance and, you know, just basically sort of use, I'm using a proxy, reverse proxy to, so it's not, it's not out in the wild.

00:02:13 - Ty Wells
I removed some tools and, you know, I did some other things to it.

00:02:18 - Ty Wells
So it's, I'm not using it for the purpose of that.

00:02:22 - Ty Wells
I'm using it for some other stuff.

00:02:25 - Ty Wells
I'm actually not using it at all.

00:02:26 - Ty Wells
I'm using the memory of it, the memory and some organizational pieces that I like.

00:02:32 - Ty Wells
I'm using that.

00:02:34 - Ty Wells
The memory for sure.

00:02:35 - Patrick Chouinard
The memory is golden.

00:02:37 - Patrick Chouinard
But, yeah.

00:02:39 - Ty Wells
Yep.

00:02:39 - Patrick Chouinard
I'm going to go through pretty much how I built that documentation and why I did it tonight, if people are interested, obviously.

00:02:51 - Patrick Chouinard
Sounds good.

00:02:52 - Ty Wells
And you'll be posting the videos right after?

00:02:55 - Ty Wells
Yep.

00:02:56 - Patrick Chouinard
Okay, great.

00:02:57 - Patrick Chouinard
Exactly the same way, Brendan.

00:03:00 - Patrick Chouinard
Okay.

00:03:04 - Ty Wells
I know it was the most popular question we received.

00:03:07 - Patrick Chouinard
Will there be a video?

00:03:10 - Ty Wells
Yeah.

00:03:12 - Ty Wells
Hi, Morgan.

00:03:13 - Patrick Chouinard
How's it going, guys?

00:03:15 - Morgan Cook
Hey, Morgan.

00:03:17 - Ty Wells
It's good to see you guys.

00:03:19 - Morgan Cook
And I'm glad that we're continuing with this meeting.

00:03:22 - Morgan Cook
It's been very helpful as nothing more than motivation for some of the time, but that's sometimes what you need.

00:03:28 - Morgan Cook
Mm-hmm.

00:03:31 - Patrick Chouinard
Yeah.

00:03:32 - Patrick Chouinard
And it's not just me.

00:03:34 - Patrick Chouinard
Paul will also take the reign for some of the calls and stuff.

00:03:46 - Patrick Chouinard
Hi, everyone.

00:03:52 - Patrick Chouinard
I saw your post.

00:03:55 - Patrick Chouinard
And I saw your comment.

00:03:57 - Patrick Chouinard
Yeah.

00:03:59 - Juan Torres
I'm really excited to read it.

00:04:06 - Patrick Chouinard
I understood that it's a method of publication that was interesting that I should continue.

00:04:14 - Juan Torres
Humanity needs your publications.

00:04:20 - Patrick Chouinard
Yeah, actually, it was a lot more simple to do than it looks like.

00:04:28 - Patrick Chouinard
Yeah.

00:04:31 - Juan Torres
You're using MD files in order to create one of the sections, right?

00:04:37 - Juan Torres
0, 0, 0, 1, 0, 2.

00:04:39 - Patrick Chouinard
it's just a bunch of MD files, and then I simply asked Claude to create a website around them.

00:04:48 - Patrick Chouinard
That's it.

00:04:52 - Patrick Chouinard
Hey, Paul.

00:04:54 - Patrick Chouinard
Hey, Patrick.

00:04:55 - Paul Miller
How are you going?

00:04:56 - Paul Miller
Hey, guys.

00:04:58 - Paul Miller
We'll run.

00:04:59 - Patrick Chouinard
run.

00:04:59 - Patrick Chouinard
Hey.

00:05:01 - Patrick Chouinard
I'm going to give people a couple of more minutes to join because none of the one that asked questions are there yet.

00:05:15 - Patrick Chouinard
Except for you, Paul.

00:05:20 - Hemal Shah
I just asked question one minute ago, so do I count?

00:05:27 - Juan Torres
Hey, Patrick, do you think at one point Claw, what is it called, OpenClaw would be able to self-regularize its computational environment?

00:05:41 - Juan Torres
I mean, I think it can already, right?

00:05:45 - Patrick Chouinard
What do mean by self-regularize?

00:05:47 - Patrick Chouinard
Because it can do a lot of things to itself, but I'm not sure what you're...

00:05:53 - Juan Torres
Kind of like middleware, you know, changes, for example, if a computer is...

00:06:00 - Juan Torres
It's overheating.

00:06:01 - Juan Torres
It can use some packages in order to start decreasing or re-economize some GPU, CPU workloads, optimize the communication between CPU, GPU.

00:06:16 - Patrick Chouinard
It could.

00:06:17 - Patrick Chouinard
I'm not sure if it's the best use of token because this is pretty deterministic.

00:06:23 - Hemal Shah
I was thinking about a similar situation, one where I'm hosting OpenClaw on GCP VM instance, and I wanted to change something to that VM instance, maybe add memory or something.

00:06:36 - Hemal Shah
I wanted to use OpenClaw itself to do it for itself, but then it has to shut itself down.

00:06:43 - Hemal Shah
So I thought maybe I create two OpenClaw instance.

00:06:45 - Hemal Shah
They both can delegate tasks to each other.

00:06:49 - Hemal Shah
That was one thought I was wondering at some point to try it out.

00:06:54 - Hemal Shah
Yeah, can be a dialectical process between two computers.

00:07:00 - Patrick Chouinard
That's not, I don't think it's crazy, honestly.

00:07:03 - Juan Torres
No, it's pretty doable.

00:07:06 - Ty Wells
I had them talking, sorry, I had them playing roles against each other the other day with actual voice calls, and then I looked at the transcript afterwards.

00:07:17 - Ty Wells
It was like a multibook moment, except I was using it for a different purpose.

00:07:23 - Ty Wells
I was like, you know what, let me have them play these different roles, and then I don't have to do it, because I was doing all the testing.

00:07:29 - Ty Wells
I was like, I'm not doing this anymore.

00:07:31 - Ty Wells
Why don't you guys just test against each other, because they have phone numbers and email addresses and all kinds of goodies.

00:07:40 - Ty Wells
Very dangerous tool there, guys.

00:07:43 - Patrick Chouinard
Extremely dangerous in the wrong hands.

00:07:47 - Ty Wells
Yep.

00:07:48 - Juan Torres
Well, Patrick just publicized Modus Operandi for a secure operation of OpenClaw.

00:07:56 - Ty Wells
Yeah, you've got to actually use it, though.

00:07:59 - Patrick Chouinard
Let's Let's not.

00:08:00 - Patrick Chouinard
We make that biblical just yet.

00:08:02 - Patrick Chouinard
It's just my idea is to make it a little bit less dangerous, let's say.

00:08:08 - Patrick Chouinard
So I think we're going to begin.

00:08:12 - Patrick Chouinard
I'm going to post the order.

00:08:16 - Patrick Chouinard
Whoops.

00:08:17 - Patrick Chouinard
I'm going to take it again because there's two people that just joined.

00:08:25 - Patrick Chouinard
But the order is going to be after we go through the questions that have been asked already.

00:08:36 - Patrick Chouinard
One sec.

00:08:42 - Patrick Chouinard
There go.

00:08:48 - Patrick Chouinard
OK.

00:08:48 - Patrick Chouinard
But before we get to that, let's go through the question.

00:08:52 - Patrick Chouinard
I'm thinking Justin is not here.

00:09:08 - Patrick Chouinard
I'm just going through the list, and so I think the first question is Paul Gallovich.

00:09:20 - Patrick Chouinard
So do you want to expose the detailed question you've posted in the school thread?

00:09:28 - Patrick Chouinard
Yes, hi, thanks.

00:09:31 - Paul Gallovich
I was looking, trying to implement multi-tenancy in any of the apps, so I was hoping to explore the best use case for, like example, Clerk has a multi-tenant option in Clerk authentication where you can create organizations and then implement that, those React.

00:09:59 - Paul Gallovich
Thank you.

00:10:00 - Paul Gallovich
Those React components in the application.

00:10:03 - Paul Gallovich
I know it's possible to do with SupaBase.

00:10:06 - Paul Gallovich
I know SupaBase does support.

00:10:07 - Paul Gallovich
I've seen an example of SupaBase with Clark, but just wanted to ask if kind of a best case scenario or best way to do that.

00:10:19 - Patrick Chouinard
I think you're referencing from the ShipKit application template.

00:10:26 - Patrick Chouinard
Correct, correct.

00:10:27 - Patrick Chouinard
Okay, and did anyone add experience with that specifically?

00:10:36 - Morgan Cook
I don't necessarily have the complete experience yet, but I'm working on the same problem.

00:10:41 - Morgan Cook
So what I've done is quite a bit of research in authentication in regards with SupaBase and how to set up SupaBase structure to not require the RLS mechanism.

00:10:57 - Morgan Cook
The RLS is enabled?

00:10:59 - Morgan Cook
The

00:11:00 - Morgan Cook
But I'm not using it.

00:11:01 - Morgan Cook
I'm going around it because all my data access is through a server-side data access layer with a dedicated role.

00:11:10 - Morgan Cook
So the problem is really just about foreign keys and table structure, making sure that you have your tenant ID in each of the appropriate tables.

00:11:22 - Morgan Cook
So in my instance, the public can view a certain set of all data for searching to find multiple tenants, but the tenants only have access to administer the individual data set that belongs to them.

00:11:44 - Morgan Cook
So I'm doing that.

00:11:46 - Morgan Cook
My plan right now is to do that through views and trigger job or some kind of cron job in the background to populate that table so that the public can always do their search and find the data.

00:11:58 - Morgan Cook
That doesn't need to be always 100%.

00:12:08 - Morgan Cook
So I guess your question then becomes exactly how do you get logged in to a specific tenant?

00:12:18 - Morgan Cook
And I'm kind of exploring that myself right now for some of the use case, some of the users actually belong to multiple tenants.

00:12:26 - Morgan Cook
So there's another complexity there for me, which may not be the case for most tenant situations.

00:12:31 - Morgan Cook
Most of the time, you're just going to have one login belongs to a very specific tenant.

00:12:38 - Morgan Cook
And then you're going to have to look at maybe doing an invitation process where the admin of a tenant can invite via an email link to somebody who needs to have access so that they can create a login.

00:12:53 - Morgan Cook
So there's quite a bit around trying to maintain a tenant and the research I've done.

00:14:00 - Paul Gallovich
Thank you so much.

00:14:01 - Paul Gallovich
Appreciate that.

00:14:02 - Morgan Cook
I can share.

00:14:05 - Morgan Cook
I got to find it.

00:14:06 - Morgan Cook
I saved my conversation.

00:14:09 - Morgan Cook
I was going to use that as a template to push through Patrick's little documentation feature that I have yet to play around with yet.

00:14:19 - Morgan Cook
But I saved that conversation and it has a lot of detail in there about actually setting up tenant.

00:14:25 - Morgan Cook
It's very specific to my project, but that may be useful.

00:14:28 - Patrick Chouinard
I'm not sure.

00:14:30 - Morgan Cook
Yeah, yeah, that would be.

00:14:34 - Morgan Cook
Send me your, put a link in the chat for your ID and I'll forward it to you and maybe if I clean it up decent enough, I'll have it for the next meeting for everybody else to have access to.

00:14:47 - Morgan Cook
I'll just throw my email.

00:14:49 - Shah Martinez
Yeah, if you want to put it in the chat, I'm working on a multi-tenancy project now too, so I'd be super interested in seeing what you have.

00:14:58 - Shah Martinez
Let me just post it then to.

00:15:00 - Morgan Cook
The meeting notes in the school.

00:15:05 - Morgan Cook
Awesome.

00:15:09 - Patrick Chouinard
It'll be later tonight, though.

00:15:10 - Morgan Cook
It won't be right now.

00:15:12 - Morgan Cook
I'm not sure exactly where I stashed that.

00:15:14 - Morgan Cook
I'm sure it's with the project, but I've to dig.

00:15:18 - Shah Martinez
Also, Patrick, is your documentation thing, is that posted in the school or in Discord?

00:15:23 - Patrick Chouinard
The documentation I've created is posted in school, and Juan was kind enough to post it in the chat.

00:15:30 - Shah Martinez
Okay.

00:15:31 - Shah Martinez
Awesome.

00:15:36 - Patrick Chouinard
Good.

00:15:37 - Patrick Chouinard
Next, Amal, you had a question you wanted to talk about?

00:15:43 - Hemal Shah
You said me, Amal, right?

00:15:45 - Hemal Shah
Me, right, Patrick?

00:15:46 - Hemal Shah
Yep.

00:15:46 - Hemal Shah
Yeah, Google ADK.

00:15:49 - Hemal Shah
Just wondering if anybody has actually took it to production.

00:15:54 - Hemal Shah
It's been out there for quite some time, but I'm still wondering.

00:16:00 - Hemal Shah
I it's production, adoption, if anybody had any experience with that, I was wondering.

00:16:08 - Hemal Shah
You mean the Shipkit template using ADK or any ADK project?

00:16:13 - Hemal Shah
Any general, any ADK in general.

00:16:17 - Hemal Shah
Any application, either via Shipkit or regular also doesn't matter.

00:16:23 - Hemal Shah
I know zero about it, so there's my answer.

00:16:28 - Hemal Shah
I don't even want to know at this point.

00:16:32 - Hemal Shah
It's the one template I haven't used, actually.

00:16:39 - Hemal Shah
Maybe.

00:16:40 - anapreciado
I haven't shipped to production, but I remember that that was my starting point as well.

00:16:45 - anapreciado
So when I first joined here, my main question was on ADK, and I remember that Brandon told me that the way that Google configured the API calls to ADK was not optimal, and he recommended me.

00:17:04 - anapreciado
I have a development I haven't shipped to production, but I remember I had issues with the API calls to it.

00:17:14 - anapreciado
So I don't know if it helps, but I wouldn't have known by the Google documentation that they had a mess pretty much, or I don't know if that's like the words to use, but that they were not as organized as I thought that they were.

00:17:32 - Hemal Shah
Yeah.

00:17:34 - Hemal Shah
Yeah, thank you.

00:17:36 - Hemal Shah
I mean, they have a lot of information on their website, but still there's a lot of missing pieces of puzzles.

00:17:42 - Hemal Shah
So it looks good, fancy on the front, but when you really use it, there are a lot of gaps.

00:17:51 - Hemal Shah
So that's what we're trying to figure out, how mature it is.

00:17:54 - Hemal Shah
I know LengGraph, LengChain, those are the other ecosystems that are out there.

00:18:00 - Hemal Shah
Probably those are the alternatives we'll explore.

00:18:03 - Hemal Shah
Thank you.

00:18:04 - anapreciado
What Brandon also said is that a lot of the problems they had was with the agent engine.

00:18:12 - anapreciado
And they were later trying to migrate everyone to use Cloud Run.

00:18:18 - Hemal Shah
Yeah.

00:18:20 - Hemal Shah
So that's what I mean a little bit when I say they had a mess, meant that.

00:18:25 - anapreciado
It's like they deployed something and then they said the official way was to do it with Cloud Run.

00:18:30 - Hemal Shah
Okay.

00:18:31 - Hemal Shah
Thank you.

00:18:33 - Hemal Shah
Good.

00:18:35 - Patrick Chouinard
So it went quick through the questions.

00:18:39 - Patrick Chouinard
By the way, sorry, guys, if the post went online a little bit late.

00:18:46 - Patrick Chouinard
We're going to try to organize.

00:18:49 - Patrick Chouinard
I'll just say that it's the first week we're taking over for Brandon.

00:18:54 - Patrick Chouinard
So we're still having a little bit of organizational churn to go through.

00:18:57 - Patrick Chouinard
But we're going to...

00:18:59 - Patrick Chouinard
We're

00:19:00 - Patrick Chouinard
At least I'm going to try to have the question post ready a little bit earlier, so you have more time to ask your question prior to the call.

00:19:11 - Patrick Chouinard
That said, since we went through the question, the first one would be Ty.

00:19:20 - Ty Wells
Hey, guys.

00:19:23 - Ty Wells
Just real quick.

00:19:24 - Ty Wells
I told you thank you for posting that security breakdown.

00:19:28 - Ty Wells
And I'm glad you got to it before I did for Open Claw.

00:19:35 - Ty Wells
So I'm working on, obviously, actually, I can say I'm only working on three projects at this time.

00:19:45 - Patrick Chouinard
Slow week.

00:19:46 - Patrick Chouinard
What's that?

00:19:47 - Patrick Chouinard
Slow week.

00:19:49 - Patrick Chouinard
Well, no, actually, this is a good thing.

00:19:52 - Ty Wells
I'm dialing it in, right?

00:19:53 - Ty Wells
I'm dialing it in.

00:19:54 - Ty Wells
So I'll just show you real quick what I'm working on here.

00:19:59 - Ty Wells
Let's see.

00:20:00 - Ty Wells
Let's if I can find it.

00:20:03 - Ty Wells
I got a request to share.

00:20:05 - Ty Wells
Yep.

00:20:06 - Patrick Chouinard
Okay.

00:20:09 - Ty Wells
All right.

00:20:10 - Ty Wells
Let's find it.

00:20:12 - Ty Wells
So I'm working on a project called Frank Labs.

00:20:21 - Ty Wells
And Frank Labs, it's – let me reload it here.

00:20:25 - Ty Wells
I don't know if it'll play the sound because – And I'm working on the video.

00:20:29 - Ty Wells
got to tell you.

00:20:30 - Ty Wells
Can you guys hear this?

00:20:32 - Ty Wells
Frank Labs.

00:20:33 - Ty Wells
Your business owner is struggling, chasing leads, putting out fires.

00:20:38 - Ty Wells
Okay.

00:20:38 - Ty Wells
So this is Frank Palitza.

00:20:39 - Ty Wells
What it is – I explained what it is there.

00:20:42 - Ty Wells
But it's basically a team of AI experts that augment, help you with your work.

00:20:50 - Ty Wells
This is – I was working on this before ClawedBot, OpenClaw.

00:20:55 - Ty Wells
But I actually implemented the memory –

00:21:00 - Ty Wells
That's that Peter used in OpenClaw because it was better than what I had.

00:21:05 - Ty Wells
But you can basically, so it'll go through and tell you, okay, this is your team, you've got like an SDR and what he does and what he has access to.

00:21:14 - Ty Wells
And you have a customer support person.

00:21:16 - Ty Wells
And these are actual entities.

00:21:19 - Ty Wells
They have emails, they have phone numbers.

00:21:21 - Ty Wells
They can talk to each other, like I was telling you earlier.

00:21:23 - Ty Wells
I had them talking with each other, role-playing.

00:21:26 - Ty Wells
They can actually go out and do things for that specific business function.

00:21:33 - Ty Wells
And so this is basically just the entry of how you would, how you can augment your business for, with these AI employees, if you will.

00:21:47 - Ty Wells
That's it.

00:21:50 - Ty Wells
You can, if you go on the site and you call Sam, talk to Sam, try it out.

00:21:56 - Ty Wells
I think it's impressive.

00:21:57 - Ty Wells
Try it out.

00:21:58 - Ty Wells
You got a call from your, well, it's a

00:22:00 - Ty Wells
It's web call, so you call it from your phone so it's not in the mic.

00:22:04 - Ty Wells
It's franklabs.io.

00:22:06 - Ty Wells
put it in the group chat.

00:22:10 - Patrick Chouinard
Wow.

00:22:11 - Patrick Chouinard
Juan, you have a question?

00:22:13 - Patrick Chouinard
Yeah.

00:22:14 - Juan Torres
Are you using NVIDIA's voice-to-voice model?

00:22:17 - Juan Torres
Is that the reason that it's working really well?

00:22:20 - Ty Wells
I am using a variation of their PersonaPlex.

00:22:26 - Ty Wells
Yeah.

00:22:28 - Juan Torres
Yeah.

00:22:28 - Ty Wells
I looked at it.

00:22:31 - Ty Wells
I evaluated.

00:22:32 - Ty Wells
There were a couple of good things.

00:22:33 - Ty Wells
I pulled those things out, and I implemented those for its natural speaking ability.

00:22:41 - Ty Wells
There's still some tweaking.

00:22:42 - Ty Wells
There's some variance in there that pauses maybe a little bit longer than I want, but I'm working on it to see.

00:22:51 - Juan Torres
Are you placing, because I've seen some videos, and sometimes it goes really, really well, and sometimes it goes through, and it turns

00:23:01 - Juan Torres
How does the rail guarding for a model like that, how does it look like?

00:23:07 - Juan Torres
Is it through prompting?

00:23:09 - Juan Torres
It's a couple of things.

00:23:10 - Ty Wells
I've got a few guardrails in place that help, well, for prompting, some prompting firewalls, if you will.

00:23:19 - Ty Wells
And then I have some on the front end and, of course, some on the back end that are helping to sort of keep it under wraps as best.

00:23:27 - Ty Wells
So its response is always then guardrailed, obviously, and then even the incoming response, because, you know, obviously with prompt injection, with anything, really, because that's how it works.

00:23:43 - Ty Wells
yeah.

00:23:43 - Ty Wells
Nice.

00:23:44 - Ty Wells
With DeepGram and LiveKit integrated.

00:23:49 - Patrick Chouinard
Okay.

00:23:51 - Patrick Chouinard
Good.

00:23:53 - Patrick Chouinard
Anna, you had a question?

00:23:55 - Patrick Chouinard
Yeah.

00:23:56 - anapreciado
So, this is a team of experts.

00:23:58 - anapreciado
How are you...

00:23:59 - anapreciado
How

00:24:00 - anapreciado
So validating their expertise.

00:24:04 - Ty Wells
Well, it's their experts in the business function that they do.

00:24:08 - Ty Wells
So let's say they are a finance manager, a sales person.

00:24:11 - Ty Wells
They are trained in sales and to conduct sales.

00:24:17 - Ty Wells
And then they're evaluated based upon the user's response to their sales.

00:24:21 - Ty Wells
So let's say you kick off a business.

00:24:24 - Ty Wells
You say, hey, Sam, go find me 100 leads.

00:24:27 - Ty Wells
It'll go out and find you 100 leads in this whatever scenario.

00:24:30 - Ty Wells
gather some information.

00:24:31 - Ty Wells
It'll bring that back.

00:24:32 - Ty Wells
And then you have a queue.

00:24:34 - Ty Wells
Oh, I guess I wasn't actually logged in.

00:24:37 - Ty Wells
I just showed you guys the front page.

00:24:38 - Ty Wells
But you have a queue where you see what you have to approve or disapprove or it runs in three different modes.

00:24:45 - Ty Wells
One is just an advisory mode.

00:24:48 - Ty Wells
So it'll go and say, hey, you should go and do this.

00:24:51 - Ty Wells
Right.

00:24:52 - Ty Wells
And then you go into, all right, I've done that.

00:24:55 - Ty Wells
You can go into co-pilot mode.

00:24:57 - Ty Wells
And I think I've explained some of this before, but where.

00:25:00 - Ty Wells
It's actually doing some of the things, and then you can do autonomous mode.

00:25:03 - Ty Wells
So it can make calls out, you can call it in, it'll transfer calls to between these different experts, and it can transfer calls to an actual person, right?

00:25:17 - Ty Wells
When it determines if somebody says, hey, I want to talk to somebody, it'll transfer to me.

00:25:24 - Ty Wells
So, well, that's sort of the flow.

00:25:27 - Ty Wells
Thank you.

00:25:28 - anapreciado
My question was more like, for example, are you using models that are all, pardon my ignorance, like, I feel like I'm going to ask a really dumb question.

00:25:40 - anapreciado
But if you're using, like, you're using models that are already trained as experts in the field, and you're not validating that they are indeed the quality that they say, or you have your own validations?

00:25:53 - Ty Wells
First of all, I'm using, I've got a, I think I'm using Mistral 7B.

00:25:59 - Ty Wells
left if character, notice single

00:26:00 - Ty Wells
As a local model.

00:26:02 - Ty Wells
And then I'm using dbt4o.

00:26:04 - Ty Wells
That is for what the business function is.

00:26:08 - Ty Wells
That's pretty straightforward.

00:26:09 - Ty Wells
Now, on top of that, I'm using a light rag to, you know, obviously bring context to the business itself.

00:26:17 - Ty Wells
But the function of an accounts payable clerk is pretty straightforward across the board, right?

00:26:24 - Ty Wells
A accounts receivable clerk, a salesperson.

00:26:28 - Ty Wells
I mean, these things are pretty, you don't need big models to really determine their business function and what they should and should be doing.

00:26:36 - Ty Wells
You just need the context of the business itself.

00:26:38 - Ty Wells
And that is what you would get.

00:26:42 - Ty Wells
You'd combine the two together, obviously, and its memory ability of previous conversations with that particular customer or whatever the case is.

00:26:52 - Ty Wells
and then you could, I've got sales, I've got playbooks for different functions.

00:26:57 - Ty Wells
And basically those are then ingested with.

00:27:00 - Ty Wells
That data from their business to build out the result of how the interaction goes.

00:27:10 - Ty Wells
Thank you.

00:27:11 - anapreciado
Thank you.

00:27:13 - Patrick Chouinard
Paul, you have a question?

00:27:16 - Patrick Chouinard
This is cool stuff, Ty.

00:27:19 - Paul Miller
Love the line you're taking.

00:27:23 - Paul Miller
I'm having a play and it'll be interesting to understand from Patrick later when you go through your your stack, Patrick, without giving too much away, because it's quite important not to be openly discussing this on something that's recorded and played back online, but at a high level with guardrails and these types of things, what's been your high level strategy with coming up with a guardrail approach that just gives you the sort of right validation?

00:28:00 - Paul Miller
And protection, what approach did you take on building that?

00:28:05 - Paul Miller
Is it guardrails in terms of for who?

00:28:07 - Ty Wells
For the LLMs?

00:28:09 - Ty Wells
For what exactly?

00:28:10 - Ty Wells
This isn't open claw at all.

00:28:13 - Ty Wells
This is what I built before.

00:28:17 - Paul Miller
Yeah, you did this before open claw.

00:28:19 - Paul Miller
So in terms of preventing prompt injection, doing all the basic stuff that is now obviously being fully discussed around in response to open claw, what was your high-level thinking, without giving too much of the secret sauce away?

00:28:39 - Ty Wells
It's not secret.

00:28:40 - Ty Wells
Basically, you need a counsel.

00:28:42 - Ty Wells
I have several counsels.

00:28:43 - Ty Wells
These are all other independent agents that are you familiar with the five thinking?

00:28:50 - Ty Wells
Method?

00:28:51 - Ty Wells
That approach?

00:28:52 - Ty Wells
Remind me.

00:28:53 - Paul Miller
I've had so many approaches.

00:28:55 - Paul Miller
Five is like good, the bad, the bad.

00:29:00 - Ty Wells
The optimistic, the pessimistic, and then the neutral, okay?

00:29:05 - Ty Wells
Yeah.

00:29:05 - Ty Wells
Well, that's not the actual names, but you get the gist.

00:29:08 - Ty Wells
So they make up a council, and that council is contextual aware.

00:29:13 - Ty Wells
So I have a security council that manages cybersecurity against all of these agents and what they're doing.

00:29:22 - Ty Wells
And I have a different council, that's a prompt injection council, that are doing the same thing with the data that the agents are producing.

00:29:34 - Ty Wells
So it's sort of self-checking.

00:29:36 - Ty Wells
It's as best as I could.

00:29:37 - Ty Wells
I mean, there's some other layers in there as well.

00:29:40 - Ty Wells
But I'm doing as – you can only do as much as you can do, right?

00:29:44 - Ty Wells
I mean, otherwise, there's a tradeoff, right?

00:29:46 - Ty Wells
And then you get overkill.

00:29:47 - Ty Wells
You got latency issues.

00:29:48 - Ty Wells
You get token issues, right?

00:29:51 - Ty Wells
There's a lot going on there.

00:29:54 - Ty Wells
But I think it's still –

00:30:00 - Ty Wells
Puts you in a way better position.

00:30:02 - Ty Wells
If you listen to that video, don't worry about the jittering stuff in the video.

00:30:05 - Ty Wells
What I'm saying there basically is that's a rending problem.

00:30:09 - Ty Wells
fix that.

00:30:09 - Ty Wells
But I'm saying you're struggling with your business every day.

00:30:13 - Ty Wells
You are chasing leads.

00:30:15 - Ty Wells
You are trying to put out fires.

00:30:17 - Ty Wells
You're constantly doing those things.

00:30:19 - Ty Wells
And a lot of things fall in between the crack.

00:30:21 - Ty Wells
That's just how we work.

00:30:22 - Ty Wells
What doesn't fall in between the crack is AI, their ability to check these things and monitor these things, bring them to your attention, and even to be able to act upon them.

00:30:34 - Ty Wells
And so that's what the intent is to be able to do those things from a sales perspective to operational finance.

00:30:41 - Ty Wells
You know, I was just talking to one of my employees today, and I'm walking through a process, and I'm like, this doesn't even make any sense.

00:30:50 - Ty Wells
Basically, they're taking data, and they're massaging it, and then outputting some data.

00:30:56 - Ty Wells
I'm like, really?

00:30:59 - Ty Wells
I'm trying to figure

00:31:00 - Ty Wells
What part of that was actually you needed a person to do that part?

00:31:04 - Ty Wells
And actually, there's one physical.

00:31:06 - Ty Wells
We do guard services where the guards go around.

00:31:09 - Ty Wells
They punch a pipe on the wall to confirm that they were physically in that position.

00:31:14 - Ty Wells
And so they have to take those pipes and they download that in software.

00:31:17 - Ty Wells
That's the only thing.

00:31:18 - Ty Wells
Once it's downloaded, then she's just taking that data, massaging it, sending it off, reporting.

00:31:23 - Ty Wells
So I'm like, she doesn't know that.

00:31:25 - Ty Wells
But I was thinking in my mind, oh, I've got an agent for her.

00:31:30 - Paul Miller
Are you using it on yourself?

00:31:33 - Paul Miller
Ah, yes.

00:31:35 - Ty Wells
I'm using it on my own businesses.

00:31:38 - Paul Miller
Yeah.

00:31:39 - Paul Miller
That's the intent, right?

00:31:41 - Ty Wells
I'm dogfooding the crap out of this thing.

00:31:44 - Patrick Chouinard
No pun intended.

00:31:46 - Ty Wells
I'm getting so excited.

00:31:49 - Paul Miller
I know, and I'm sure all of us on the call have got areas that we know we should be doing with whether it's our life or...

00:32:00 - Paul Miller
Our businesses that we find either very boring or very taxing because it's not our base skills that we do.

00:32:10 - Paul Miller
For me, it's being on top of DevOps, constantly looking at all the servers, making sure it's all up, and now we're on the latest version.

00:32:19 - Paul Miller
I think the security thing, I like your modeling on the security thing, but I've gone into DocPloy.

00:32:27 - Paul Miller
DocPloy, I'm really into DocPloy, I'm really into tail scale, locking everything down, but making sure it's operational and building the equivalent of this that's an IT team.

00:32:43 - Paul Miller
I find it interesting, and it'd be interesting from your perspective.

00:32:49 - Paul Miller
I'm sure you probably deal with it every day because I'm very focused on delivering a software product, but I go out talking to customers, and I just assume everyone does everything.

00:33:01 - Paul Miller
And I've had decades of being a CIO, looking at things, and you walk into a business, and like I was in a business on Friday in Australia, and the guys were in the camp of, oh, I just want to build something completely new for myself off the shelf, and I'm not thinking about how I'm going to maintain it, or how I'm going to train my people, and all this stuff.

00:33:28 - Paul Miller
And we're a logistics company, and I'm thinking, well, oh my God, I can see this is a time bomb.

00:33:34 - Paul Miller
All of the expertise and all of the questions I would ask, they're not thinking about, and creating this, whether it's about advising sales, tax risk, financial risk, all that operational thing, the mind is blown about the types of team members you can add to this.

00:33:54 - Paul Miller
This is very exciting.

00:33:55 - Paul Miller
This is the thing, it's, yeah, the team, the team is just.

00:34:00 - Ty Wells
The function that you're trying to do, like I've got Ashley.

00:34:06 - Ty Wells
Ashley creates, builds on the code.

00:34:09 - Ty Wells
I don't actually do anything.

00:34:10 - Ty Wells
I talk to Ashley over Telegram.

00:34:12 - Ty Wells
I'm like, hey, I need you to do this.

00:34:15 - Ty Wells
And, you know, it's working on whatever I'm saying I need to do.

00:34:19 - Ty Wells
It completely understands.

00:34:20 - Ty Wells
I have Ashley.

00:34:22 - Ty Wells
Ashley has the same memory as OpenClaw, which means so the memory is great, right?

00:34:28 - Ty Wells
So it's its own, but it's my engineer.

00:34:30 - Ty Wells
So I'm adding whatever I'm adding and doing.

00:34:33 - Ty Wells
I'm not doing really in Claw code.

00:34:34 - Ty Wells
I'm using Ashley through burning up some tokens.

00:34:39 - Ty Wells
Let's just put that out there because you can't use your subscription with OpenClaw.

00:34:44 - Ty Wells
You have to use your API key from, because otherwise they will, you could get banned.

00:34:50 - Ty Wells
Um, but you know, it's a, it's a product ties product.

00:34:54 - Ty Wells
So, you know, you know, you use it, you, you sort of pay for it.

00:34:58 - Ty Wells
So just so.

00:35:00 - Patrick Chouinard
To make sure we get through every question.

00:35:03 - Patrick Chouinard
Juan, you had one question for Ty?

00:35:07 - Juan Torres
Yeah, yeah.

00:35:08 - Juan Torres
I just wanted to, because you mentioned that you're deploying one local model in Mistral 7 billion parameter model.

00:35:15 - Juan Torres
What made you decide to go for a hybrid approach of using a local model and API-based models?

00:35:23 - Juan Torres
And where are you deploying?

00:35:24 - Juan Torres
Where are you deploying your, and which VM are you deploying the local model?

00:35:29 - Ty Wells
I've got it on an EC2 instance.

00:35:32 - Ty Wells
Right on.

00:35:33 - Juan Torres
Are you using an A10 or A100 GPU?

00:35:39 - Ty Wells
I think I set that up as a...

00:35:50 - Juan Torres
Am I missing his voice?

00:35:52 - Juan Torres
Oh, sorry, sorry.

00:35:53 - Juan Torres
I went to click something.

00:35:55 - Ty Wells
I clicked mute.

00:35:56 - Ty Wells
I'll double check what I'm using.

00:35:58 - Ty Wells
I'm going to, I was saying, let me...

00:36:00 - Ty Wells
They check with Ashley and see what, hey, what are we using?

00:36:02 - Ty Wells
Not that I don't know.

00:36:03 - Ty Wells
I just don't remember because a lot has changed in the last 48 hours.

00:36:08 - Juan Torres
Yeah, the reason that I asked is because I had the same predicament because I deployed an 8 billion multi-expertise Mistral parameter on an ATent GPU, which is only 24 gigabytes.

00:36:25 - Juan Torres
The problem with like economizing, and it operates well, you know, it does the job.

00:36:31 - Juan Torres
The problem is that you cannot use optimizer libraries like BLM because if you have 24 gigabytes, the LLM is essentially taking almost like all of them.

00:36:43 - Juan Torres
It's taking almost like 23 or 22 gigabytes by just operating itself.

00:36:48 - Juan Torres
And BLM, BLM takes about five gigabytes.

00:36:53 - Juan Torres
So you have no space to use the GPU for optimization.

00:36:58 - Juan Torres
So you have to go from...

00:37:00 - Juan Torres
Using a 24 gigabyte GPU to using an 8100 GPU, which is 40 gigabytes sometimes in order to compensate for the fact that you don't have enough VRAM for your model.

00:37:16 - Juan Torres
But it's really interesting.

00:37:17 - Juan Torres
That was the same prerogative that I had.

00:37:23 - Juan Torres
OK, thanks for that.

00:37:25 - Patrick Chouinard
And the last one, Shah?

00:37:31 - Shah Martinez
Hey, yeah, so quick question, the you said, like, there's a bot that can go and reach out and get, like, you know, leads and such.

00:37:41 - Shah Martinez
Like, like what high level is I'm going to implement I'm implementing something similar I'm doing, you know, for a school platform like I'm building or go out and I kind of get leads for like sponsorships for school sponsorships at a high level.

00:37:56 - Shah Martinez
Like what what does that implementation look like?

00:37:59 - Shah Martinez
Like what does that entail?

00:38:01 - Ty Wells
Well, I'm using services.

00:38:03 - Ty Wells
I mean, some of it is a combination of perplexity, Hunter, and Apollo, and some clay I think I have in there because it's only because it's got to get, it's got to meet its requirement.

00:38:15 - Ty Wells
I don't want it hallucinating.

00:38:18 - Ty Wells
Oh, speaking of hallucinating, I want to share some, when you guys at the end, I'll share it if I, if we have time and I remember.

00:38:23 - Ty Wells
So you're using clay as like a grounding for?

00:38:27 - Shah Martinez
Yes.

00:38:29 - Shah Martinez
Grounding for the ICP, yes.

00:38:31 - Shah Martinez
But let me just make sure, so you're using perplexity, Hunter.

00:38:37 - Shah Martinez
Hunter, Apollo.

00:38:40 - Ty Wells
Okay, Apollo, that makes sense.

00:38:41 - Shah Martinez
Apollo.

00:38:41 - Shah Martinez
Is Apollo still good?

00:38:42 - Shah Martinez
Is it still, I've heard it's getting kind of.

00:38:45 - Shah Martinez
It's getting a little sketchy.

00:38:46 - Ty Wells
There's a lot of people grabbing data, right?

00:38:49 - Ty Wells
So.

00:38:52 - Shah Martinez
Apollo, then, and then clay, yeah, clay, I feel like more people kind of rave about, but yeah, I guess that.

00:39:00 - Shah Martinez
And then what is your outlet to invoke that?

00:39:05 - Shah Martinez
you implementing that as a tool?

00:39:07 - Shah Martinez
Are you exposing that as a tool?

00:39:09 - Ty Wells
Yeah, that's a tool available to that expert.

00:39:13 - Ty Wells
So different experts have different tools available to them, and that's in a package of enrichments, lead enrichments, leads and lead enrichments, that sort of thing.

00:39:28 - Ty Wells
Yeah.

00:39:28 - Ty Wells
And I had built, I know I'd showed you guys, because obviously there's a back end to it.

00:39:32 - Ty Wells
There's a, you know, you got to store your data somewhere.

00:39:34 - Ty Wells
And I had built that for my company before, a business suite that has, you know, accounts for sale, POS, invoicing, and all that stuff.

00:39:41 - Ty Wells
So that is the, where I'm storing that data.

00:39:45 - Ty Wells
That's, you know, it's got to, if they want to pull up a customer, it's got to be stored somewhere in a database, someplace.

00:39:50 - Ty Wells
But I'm not trying to really interact.

00:39:52 - Ty Wells
But I, that's, I think that's plenty for me.

00:39:55 - Ty Wells
I took up a lot.

00:39:55 - Ty Wells
Yeah.

00:39:56 - Ty Wells
Thank you.

00:39:56 - Ty Wells
Thank you so much.

00:39:57 - Shah Martinez
That helps.

00:39:58 - Shah Martinez
No worries.

00:39:59 - Ty Wells
I appreciate it.

00:40:01 - Shah Martinez
Thank you, Ty.

00:40:03 - Juan Torres
Thank you, sir.

00:40:05 - Patrick Chouinard
Next one is Morgan.

00:40:09 - Morgan Cook
Hey, guys.

00:40:10 - Morgan Cook
I don't have a whole lot, but I wanted to share a little bit of the past couple of weeks.

00:40:15 - Morgan Cook
I've been working on some worksheet automations, basically, for a client.

00:40:23 - Morgan Cook
And the process I went through is what I wanted to share with you.

00:40:27 - Morgan Cook
So I started off with some skills in Claude, right?

00:40:31 - Morgan Cook
And there was maybe five or six of them to flesh out the process to make sure the details were down from converting from an MD document, converting that into a structured HTML with a style sheet behind it, and then using PlayWrite and a few other things to generate a PDF from that HTML.

00:40:54 - Morgan Cook
But in the middle was a human in the loop cycle of making sure the page layout was correct.

00:40:59 - Morgan Cook
text.

00:40:59 - Morgan Cook
And using using

00:41:00 - Morgan Cook
And changing some content, some placeholders that I had in the markdown that would structure the HTML.

00:41:06 - Morgan Cook
So I went through that whole process with a few different skills in Claude and, you know, several iterations to work out the problem.

00:41:18 - Morgan Cook
And then once I had the skill down in Claude, then what I did was had Claude modify that skill and convert it into a JavaScript.

00:41:27 - Morgan Cook
Once it was, you know, well-structured, because it wasn't changing.

00:41:32 - Morgan Cook
I didn't need it to think anymore or come up with a different plan each time I ran it.

00:41:36 - Morgan Cook
Once I had the process down, then it was easy to convert to a skill, or I'm sorry, to a JavaScript that could then be run.

00:41:44 - Morgan Cook
I can still use the skill.

00:41:45 - Morgan Cook
The skill just makes a single call to the JavaScript at that point.

00:41:49 - Morgan Cook
And so just an idea of how to iterate through the process of creating background agents.

00:41:57 - Morgan Cook
The end goal of this will probably be to throw.

00:42:00 - Morgan Cook
Into a trigger behind the website so that she could just upload the MD and then it would go through the whole process, calling each of the individual pieces as it goes.

00:42:11 - Morgan Cook
Part of it was actually uses the content that she provides to generate a banner graphic or a quarter page graphic or something to feel some of the blank spots in the page.

00:42:25 - Morgan Cook
So it generates a prompt and then I feed that prompt off to different, I tried a few different ones and the last one I was stuck on using was the actually chats GPT prompt or image generator.

00:42:42 - Morgan Cook
seems fairly straightforward and consistent as far as the output that it generates.

00:42:47 - Morgan Cook
But just an idea on how to iterate through some of those processes from working through a problem and then using the skill to generate it and then converting the skill to a JavaScript.

00:42:58 - Morgan Cook
And that cuts.

00:43:00 - Morgan Cook
You time down by an immense amount.

00:43:02 - Morgan Cook
mean, it takes, you know, 30 seconds to a minute and a half to process the markdown into HTML using the skill and about three seconds using the JavaScript.

00:43:15 - Morgan Cook
So as well as you're not wasting any tokens at that point.

00:43:20 - Morgan Cook
Now your skill is not spending tokens to do the work.

00:43:24 - Morgan Cook
You can just call a local script that is doing the work for you.

00:43:30 - Morgan Cook
So just an idea on how to save some tokens in some scenarios.

00:43:36 - Patrick Chouinard
Yeah, absolutely.

00:43:37 - Patrick Chouinard
And anything you can make deterministic, always a good idea, no matter what.

00:43:44 - Patrick Chouinard
If you don't, the AI is there maybe to organize, maybe to manage when to run which skill, depending on context.

00:43:53 - Patrick Chouinard
But the actual job, if you can make it deterministic, awesome, awesome.

00:44:00 - Morgan Cook
And when I started, I didn't really have a deterministic plan of how this was going to work or what skills.

00:44:06 - Morgan Cook
So that was like, it was useful to have the skills available to sit there and iterate through the process until I got to a deterministic state, right?

00:44:15 - Morgan Cook
And then at that point, I converted to a script.

00:44:19 - Patrick Chouinard
That's how I build script as well.

00:44:20 - Patrick Chouinard
I build a script in Markdown, then I use Claude to review the script and see how it could convert part of it into either Bash, JavaScript, whatever you want.

00:44:37 - Morgan Cook
All right.

00:44:38 - Morgan Cook
Well, that's my share for the day.

00:44:41 - Patrick Chouinard
But very interesting, Morgan, because we're currently working on how to distribute skill or how to govern skill in the corporate environment.

00:44:53 - Morgan Cook
Well, that's the other thing is that one of the skills that I built was a compliance check.

00:44:58 - Morgan Cook
Well, the compliance check is...

00:45:00 - Morgan Cook
To make sure that there are no specific verbiage in any of the workbook, that it has the required elements.

00:45:07 - Morgan Cook
There's a couple of requirements for a specific font size and text for the licensor number and all that kind of information, right?

00:45:15 - Morgan Cook
So that was part of the piece as well, as iterating through that, making sure that when somebody presents content for a worksheet, that it's not violating any of the compliance rules that they have to follow.

00:45:30 - Patrick Chouinard
Yeah, exactly.

00:45:33 - Patrick Chouinard
Good, good.

00:45:35 - Patrick Chouinard
Next would be Juan.

00:45:41 - Juan Torres
Hello, hello.

00:45:42 - Juan Torres
Hey, I don't know.

00:45:44 - Juan Torres
I don't have much updates.

00:45:46 - Juan Torres
Perhaps maybe a rant.

00:45:49 - Juan Torres
So I've been working, I mean, most of you guys have been working with this client for automating, you know, name entity recognition from financial information, accounting information.

00:46:00 - Juan Torres
Right.

00:46:01 - Juan Torres
I feel like there is going to be a new modus operandi of how coders are going to generally produce code.

00:46:11 - Juan Torres
And the reason that I bring this as a result of the AI, agentic AI production, and the reason that I say this is mainly because I am encountering that when I am just working on myself or in my own environment with my own database, I move really fast.

00:46:31 - Juan Torres
Right.

00:46:31 - Juan Torres
But then I have to work with other engineers and their mode of operation is, you know, you could even say that it's outdated now because, for example, I'm working with a backend engineer who has a lot of years of experience.

00:46:46 - Juan Torres
Right.

00:46:47 - Juan Torres
But, you know, he still hasn't fully implemented a feasible agentic IDE mode of operating.

00:46:57 - Juan Torres
And at the same time, now, then you've.

00:47:00 - Juan Torres
Content Engineer is also, you know, not very flexible with, you know, just creating shell scripts, you know, she's saying like, oh, I'm a front-end engineer, I don't produce shell scripts or as a sage into the EC2 instance, right?

00:47:15 - Juan Torres
So there's a lot of friction points that come about with the lack of dynamism and the gifts that AI provides as a result of the new tools that we have in our hands, you know?

00:47:28 - Juan Torres
So I do believe that there will be, I mean, I'm pretty sure there are already pockets of development teams that are just creating new modes of production as a result of just fully embracing all the tools that there is available to them in order to mass produce, you know, whatever there is.

00:47:51 - Juan Torres
But it will be really interesting to see this mode of operation being documented.

00:48:00 - Juan Torres
Planted being display, videos, logs, whatever, because most of the videos that I've seen, most of the documentation has been on individuals working by themselves, you know.

00:48:10 - Juan Torres
So I would love to see if anyone has resources on how development teams, let's say you have a data engineer, you have an AI engineer, you have a front-end engineer, and then perhaps you have a product manager.

00:48:24 - Juan Torres
How do they interact with these new tools?

00:48:26 - Juan Torres
How do they delegate tasks?

00:48:28 - Juan Torres
How do they create virtual environments?

00:48:29 - Juan Torres
Do they deploy locally, or do they work out of an EC2 instance using Telscale in order to secure?

00:48:36 - Juan Torres
How do they develop the architecture?

00:48:37 - Juan Torres
How do they do migrations to the database?

00:48:40 - Juan Torres
You know, how do they might use AWS CLI using their new agentic capacities in order to do the cloud architecture?

00:48:49 - Juan Torres
So I think it's going to be really interesting seeing a new mode of production truly being implemented as a result of all of this.

00:48:59 - Patrick Chouinard
I think a lot of...

00:49:00 - Patrick Chouinard
The challenge you're going to have with this is a lot of that information might be proprietary still at this point.

00:49:07 - Patrick Chouinard
You get a lot of individual developer because they have the liberty to talk about what they're doing and how, but for a large-scale team, it's often a lot of their secret sauce.

00:49:22 - Patrick Chouinard
So it's a little bit harder to get open share about those type of scenarios.

00:49:28 - Patrick Chouinard
I know at least I could not, because we do that specifically, but I can't necessarily expose it because, again, secret sauce of the client.

00:49:41 - Patrick Chouinard
Secret sauce.

00:49:42 - Juan Torres
Yep.

00:49:45 - Patrick Chouinard
Good.

00:49:46 - Patrick Chouinard
Well, thank you for letting me know I cannot have what I want.

00:49:51 - Patrick Chouinard
Well, at least you know it exists.

00:49:53 - Patrick Chouinard
Yeah, yeah.

00:49:54 - Patrick Chouinard
It is possible, I can tell you that.

00:49:59 - Elijah
Birthdays.

00:49:59 - Elijah
Birthdays.

00:50:00 - Elijah
Can about that?

00:50:00 - Elijah
Yeah, absolutely.

00:50:01 - Elijah
So my one friend, he's at a company, and he shared with me what they're doing internally.

00:50:13 - Elijah
So he has like a series of agents that does research on the competitors throughout the week, and then also has some roles around what it's allowed to ask, and how often it can ask the developers certain questions, so that it's not all the time, but it keeps all the projects up to date.

00:50:36 - Elijah
Like, is this still your deadline?

00:50:38 - Elijah
Are you doing this?

00:50:39 - Elijah
And then it uses all that information throughout the week to send to a council, and then the council will determine what the best feature functionality is for the team to work on the next week, and then develop the PRD for them to execute against.

00:50:55 - Elijah
But he showed it to me.

00:50:57 - Elijah
It's pretty sweet, but I did talk to him the other day.

00:51:00 - Elijah
He showed it to me probably, I don't know, two or three months ago, and he said, it's crazy.

00:51:06 - Elijah
mean, they're a pretty well-funded startup in Pittsburgh, and he said the CTO is not on board, though, with AI.

00:51:17 - Elijah
And he goes, we're not going to have a company.

00:51:21 - Elijah
You know, like, it's just, so I think you're right.

00:51:24 - Elijah
It's just, I'd be curious to see these internal and external resistance as well.

00:51:30 - Elijah
I went to a coding thing like a week or two ago with a bunch of coders, and I mentioned vibe coding.

00:51:37 - Elijah
Man, I got eye rolls, and people were so upset about that.

00:51:40 - Elijah
So, like, you know, all of a sudden they just, you know, these, I'm not saying it's across the board, but I think there still is resistance even in the development community, which is crazy.

00:51:54 - Elijah
At all, but, you know, so that would be a great place to be with a team.

00:52:00 - Elijah
And that's fully engaged and all bought in.

00:52:03 - Elijah
What they're doing could be absolutely phenomenal.

00:52:06 - Patrick Chouinard
Yeah, but Elijah, replace Vibe Coder by AI-assisted developer.

00:52:10 - Patrick Chouinard
You're going to get a lot less eye roll from a lot of higher ups.

00:52:16 - Patrick Chouinard
Vibe Coder has become a little bit pejorative.

00:52:21 - Elijah
Yeah, but I mean, I'm still almost a little bit proud of it, you know, because at this point, I could build stuff that people could only dream about, you know, a short time ago.

00:52:32 - Elijah
So, I mean, yeah, it's just amazing what we could do.

00:52:36 - Elijah
So call me what you will, but I got ShipKit.

00:52:40 - Patrick Chouinard
Yeah, but honestly, with corporate entities, the AI-assisted developer is a lot easier pill to swallow.

00:52:53 - Juan Torres
You know, you know what, I think it's a good bypassing of the momentum.

00:52:59 - Juan Torres
Oh, guys.

00:52:59 - Juan Torres
him.

00:52:59 - Juan Torres
Awesome

00:53:00 - Juan Torres
Of their historical deficiencies is coming in as, you know, a consultant because oftentimes what I find out in my own organizations that I've worked with as full-time, right, is that they themselves, I mean, I would say there's a level of bureaucratic, you know, bureaucratic stiltification, calcification of the whole apparatus of the organization.

00:53:26 - Juan Torres
And they don't want to move or, you know, create relationships, constraints that are based on, you know, sometimes even patronage systems.

00:53:37 - Juan Torres
And what it can work with is coming in as an outside consultant and, you know, try to, you know, really sell the whole more revolutionary aspects of AI.

00:53:52 - Juan Torres
Because internally, it's going to be really hard, right?

00:53:54 - Juan Torres
But if, for example, I used to work as a strategic campaign researcher for unions.

00:53:59 - Juan Torres
between is this within Yeah,

00:54:00 - Juan Torres
you come out as a person that comes in, has experience actually in the industry, but now has, you know, grasped the tools of AI and you come back to them and be like, hey, I can actually optimize your workflow because I already know how to solve this issue, but I know how to optimize it with AI.

00:54:18 - Juan Torres
I think that's going to be the entrance towards basically destroying a lot of the parameters that they have.

00:54:28 - Juan Torres
Yep.

00:54:30 - Patrick Chouinard
Good.

00:54:32 - Patrick Chouinard
Good.

00:54:33 - Patrick Chouinard
Next one would be Paul.

00:54:37 - Paul Miller
Yeah, no, mine's pretty quick.

00:54:39 - Paul Miller
Look, I'm just focusing on making sure my core systems are working really well.

00:54:47 - Paul Miller
I've got three client projects outside my core business that I'm wanting to start, but I'm wanting to do it really wisely and have DevOps, anゴD Target.

00:54:59 - Paul Miller
The o

00:55:01 - Paul Miller
Skills available of working with some other people on the projects.

00:55:07 - Paul Miller
I kind of just want to go in and do a kind of consulting exercise where I don't have to be the one doing everything.

00:55:16 - Paul Miller
And I can be the one that focuses on where I know personally I add the maximum value.

00:55:24 - Paul Miller
Because, look, while I think you can get AI to help you be the expert for everything, if you can not have to be the conduit in which the client gets the value from that, so you're the one doing all the crazy hours, if you can combine that with smartly working with people that are good at that, combine that with AI and some proactive bots or whatever you want to set up to do it, then I think you can reimagine.

00:56:00 - Paul Miller
Imagine yourself in a new methodology and approach to being able to run several projects.

00:56:07 - Paul Miller
And for me, it's just trying to get my head around that just before I know that it's going to get crazy busy.

00:56:14 - Paul Miller
I just want to get this thought out because like I've got friends of mine who are very good on doing the business analysis kind of stuff.

00:56:26 - Paul Miller
And they just want to be kept being fed the work in a nice structured way that their brain is happy and all the other boring stuff like billing and commercials and all of that's taken care of.

00:56:39 - Paul Miller
I've got other people that are very good at developing and they just want to live in the world of coding with ShipKit and fun like that.

00:56:48 - Paul Miller
I think it's cementing a little consulting group together that you link all those skills, you add in that, you throw in the virtual mix of cool tools.

00:57:00 - Paul Miller
And put myself in that position that I just, like the duck there, I just scooped the money bucket into the bank.

00:57:12 - Paul Miller
And also it's the life balance stuff.

00:57:16 - Paul Miller
Last year was about using every hour of the day to do something with AI and doing something because I was so hyped on how amazingly productive it made me.

00:57:27 - Paul Miller
But the end result was I just didn't have any time.

00:57:32 - Paul Miller
I was just doing that.

00:57:34 - Paul Miller
And I think 26 for me needs to be about, well, how do I give that work-life balance, get the health thing, get the family thing going, but also know that the commercial thing is really running well.

00:57:48 - Paul Miller
So that's it for me.

00:57:49 - Paul Miller
It's like the pipeline's fabulous.

00:57:51 - Paul Miller
I never have an issue talking to someone who doesn't want to benefit with their business.

00:58:00 - Paul Miller
With an AI injection or remake, it's taking it from signing that to executing, getting them excited, getting them becoming advocates, and getting the next three or four across the line.

00:58:18 - Paul Miller
That's kind of where I'm at.

00:58:21 - Patrick Chouinard
Good.

00:58:23 - Patrick Chouinard
Thank you very much, Paul.

00:58:26 - Patrick Chouinard
Next one would be Amal.

00:58:32 - Patrick Chouinard
Well, still there?

00:58:33 - Hemal Shah
Yeah, I'm, yeah, I'm good.

00:58:36 - Hemal Shah
I don't have any other thing to share.

00:58:40 - Hemal Shah
Still just playing with OpenClaw.

00:58:45 - Hemal Shah
One quick question.

00:58:46 - Patrick Chouinard
So did you post some, anything around the security?

00:58:49 - Hemal Shah
Somebody mentioned on securing OpenClaw.

00:58:52 - Patrick Chouinard
Any?

00:58:53 - Patrick Chouinard
Yeah.

00:58:55 - Patrick Chouinard
Actually, if you want, I can talk a little bit about it.

00:58:58 - Patrick Chouinard
I did the post.

00:58:59 - Patrick Chouinard
I

00:59:00 - Patrick Chouinard
Oh, Elijah, did you have a question?

00:59:07 - Elijah
Well, it was back to Paul.

00:59:11 - Elijah
So if you want to move on, you can.

00:59:13 - Elijah
I can ask it later or whatever.

00:59:15 - Elijah
It's fine.

00:59:17 - Elijah
No, but if you want to go ahead.

00:59:20 - Elijah
I'm sorry.

00:59:21 - Elijah
I don't mean to digress.

00:59:23 - Elijah
I guess Paul is just telling the future a little bit for maybe me or some of us.

00:59:30 - Elijah
Because, like, every time I talk about it, people want me to do stuff for them.

00:59:35 - Elijah
So my friend has a Medicare business, and I'm going to meet with him on Thursday.

00:59:39 - Elijah
And I'm going to implement the RAG template into his business because he wants to talk about commission statements.

00:59:49 - Elijah
But I don't know.

00:59:50 - Elijah
I don't want to bite off more than I could chew.

00:59:52 - Elijah
And then what Paul was saying seems like once you start going down the road, I really didn't want to start it.

01:00:00 - Elijah
Software Development Company.

01:00:02 - Elijah
So Patrick, sorry, I didn't mean to like digress.

01:00:06 - Elijah
was just he was kind of hitting the nail on the head.

01:00:08 - Elijah
And I'm like, I'm like seeing the future.

01:00:10 - Elijah
And I'm like, is that really what I want to be into?

01:00:14 - Elijah
But there's money on the table.

01:00:15 - Elijah
And I know I can help him.

01:00:16 - Elijah
He's my friend.

01:00:18 - Paul Miller
And so it's like, you know, anytime you talk about it, geez, if we were just talking at dinner, and he's like, man, I need I need you to come and do a couple things for me.

01:00:26 - Elijah
But I don't know.

01:00:29 - Elijah
How do you say no?

01:00:30 - Elijah
And how do you price what you do?

01:00:32 - Elijah
And you know, all that stuff?

01:00:34 - Paul Miller
Well, I think one of the one of the challenges, and look, I kind of get it myself is internally, and you see these wonderful things, like you see what Ty's been doing, and other examples that this group has done.

01:00:54 - Paul Miller
In the world of people that are not on this forum, who just run day to day.

01:01:00 - Paul Miller
Businesses who can't think like many of us are thinking, whether it's us knowing that, hey, my gosh, the world has changed and we're trying to understand how we can leverage it, to people that just have day jobs that just do their stuff the way they've always done it.

01:01:17 - Paul Miller
But you'll be surprised starting at a minimal level of how you can sit down with your friend and just listen and just say, look, what do you do now manually?

01:01:29 - Paul Miller
And what's the first little practical proof of concept that we can get you started with?

01:01:37 - Paul Miller
So you're starting at an engagement level that is not setting, don't put yourself under pressure.

01:01:44 - Paul Miller
We don't want to have to, you don't want to try and boil the ocean.

01:01:49 - Paul Miller
Just start with that jug and just say, what can I do to get this going?

01:01:55 - Paul Miller
And also it's a lesson for you to be comfortable with.

01:02:00 - Paul Miller
Well, there is a practical way to do this.

01:02:03 - Paul Miller
Some of the most successful apps and SaaS tools out there are very simple solutions.

01:02:09 - Paul Miller
They're not complex ones.

01:02:11 - Paul Miller
And if you get your head around an opportunity that's nice and simple and execute it in that way, that's repeatable and scalable, that might be better than a complex, very difficult thing that you think your friend may want.

01:02:27 - Paul Miller
And it's a mistake I've kept making.

01:02:31 - Paul Miller
And I've had to pull myself back and say, jeepers, they just want a little thing.

01:02:38 - Paul Miller
And it's amazing.

01:02:40 - Paul Miller
You've got the power to make little things very quickly and do a very simple proof of concept.

01:02:46 - Paul Miller
But put yourself in their mindset that where they're at, that they're not part of this group.

01:02:51 - Paul Miller
They're not thinking, well, we can make it automated and do this.

01:02:55 - Paul Miller
And you could call it up on the phone and have a conversation.

01:02:59 - Paul Miller
Just

01:03:00 - Paul Miller
Just a simple screen where it reads your email or it checks a log file or checks what their current process is.

01:03:10 - Paul Miller
That could be the win.

01:03:13 - Patrick Chouinard
Thank you.

01:03:14 - Patrick Chouinard
That's good wisdom.

01:03:16 - Patrick Chouinard
Anna, you had a question?

01:03:19 - Patrick Chouinard
A comment.

01:03:20 - anapreciado
I wanted to vouch for what Paul said on the merits of simplicity.

01:03:25 - anapreciado
It's something that I struggled with a lot as well in the past.

01:03:30 - anapreciado
And I worked in a multinational that had a really good engineering team.

01:03:38 - anapreciado
And I noticed that the ones that were best performing were also the ones that were able to reduce to simpler concepts.

01:03:48 - anapreciado
And that was the first feedback that my boss had for me.

01:03:52 - anapreciado
I'm a perfectionist, so I would code a lot.

01:03:54 - anapreciado
And I would go on rabbit holes.

01:03:58 - anapreciado
And like the first feedback.

01:03:59 - anapreciado
good That's good idea.

01:03:59 - anapreciado
thank

01:04:00 - anapreciado
was simplify, simplify, simplify.

01:04:03 - anapreciado
So that's legit, really good advice.

01:04:07 - anapreciado
Good.

01:04:08 - Patrick Chouinard
you.

01:04:10 - Elijah
Thank you, thank you.

01:04:13 - Patrick Chouinard
So to go back to Amal's question, you wanted to know a little bit about the security over an OpenClaw installation.

01:04:22 - Patrick Chouinard
Am I correct?

01:04:23 - Patrick Chouinard
Yeah.

01:04:24 - Hemal Shah
So I'm going to repost the link.

01:04:27 - Patrick Chouinard
I've posted the link in the school community, and we had it at the beginning of the call, but you have it now in the chat.

01:04:36 - Patrick Chouinard
Well, let me share this.

01:04:47 - Patrick Chouinard
So as you can see, it's just a very simple website that I've published because I realized I had so much content accumulated, it just didn't make sense to post a blog.

01:05:00 - Patrick Chouinard
Post with that.

01:05:00 - Patrick Chouinard
It was just too dense, too much content.

01:05:05 - Patrick Chouinard
So you have here is every one of the cards is just representing a markdown document that defines part of the security framework I worked on.

01:05:21 - Patrick Chouinard
But what I find really fun about this, and I'll let you guys read through it, is everything here was created by AI with just my intention.

01:05:35 - Patrick Chouinard
What I mean by that is I've started with a chat with ChatGPT.

01:05:40 - Patrick Chouinard
I've spoken with it for about an hour, an hour and a half.

01:05:44 - Patrick Chouinard
At the end, simply ask it to create a roadmap of everything we've been working on and split it into a very specific subject element to create.

01:06:00 - Patrick Chouinard
It's a list of file to be created.

01:06:03 - Patrick Chouinard
Then I went through one other time and have it create the files.

01:06:07 - Patrick Chouinard
The files were just everything we've been discussing about how to isolate the instance, how to make sure that it had its own identity.

01:06:18 - Patrick Chouinard
That's something I worked on because a lot of the problem with independent agent is we basically give them the key to the castle.

01:06:28 - Patrick Chouinard
They work in our email, they work in our calendar, they work in our files.

01:06:33 - Patrick Chouinard
It becomes extremely dangerous, extremely fast.

01:06:38 - Patrick Chouinard
So basically what I did with mine is I created it with its own Gmail, its own calendar, even its own GitHub account.

01:06:50 - Patrick Chouinard
And I created for myself an organization where we're both part of it.

01:06:58 - Patrick Chouinard
So basically if the agent...

01:07:00 - Patrick Chouinard
Agent needs to work on my code.

01:07:02 - Patrick Chouinard
It creates a fork, bring it to the organization, work on it, and push a PR.

01:07:07 - Patrick Chouinard
So I approve everything that changed in my code base.

01:07:11 - Patrick Chouinard
And it even uses the PR and GitHub to push even documentation.

01:07:17 - Patrick Chouinard
So anything, any document, any artifact that it works on, it pushes it through the PR mechanism.

01:07:24 - Patrick Chouinard
So I'm using GitHub as a publishing and authorization pipeline for any work created by the agent.

01:07:32 - Patrick Chouinard
So doing that split helps a lot in terms of security.

01:07:37 - Patrick Chouinard
And also, I do not use the web control panel for the agent.

01:07:44 - Patrick Chouinard
Only when I have absolutely mandatory maintenance that requires it.

01:07:49 - Patrick Chouinard
Otherwise, it's not accessible.

01:07:52 - Patrick Chouinard
If I need to reach it, I instantiate an SSH tunnel to the machine.

01:07:58 - Patrick Chouinard
Otherwise, telegraph...

01:08:00 - Patrick Chouinard
So with those in place, it helps isolate the agent a lot.

01:08:07 - Patrick Chouinard
And on top of that, I've also externalized its memory.

01:08:12 - Patrick Chouinard
So there is the memory mechanism that it used, the memory.md file.

01:08:16 - Patrick Chouinard
But I also have it document every decision, every step, everything it does into an Obsidian Vault that is shared through, again, GitHub.

01:08:29 - Patrick Chouinard
So I can inspect whatever is in its brain at any time.

01:08:35 - Patrick Chouinard
There's nothing that it does that I don't see.

01:08:40 - Patrick Chouinard
So all of those things together is what I've documented in this site here.

01:08:45 - Patrick Chouinard
And also, you're going to see that there's an interactive notebook button.

01:08:50 - Patrick Chouinard
Don't hesitate to follow it.

01:08:52 - Patrick Chouinard
to that will bring you to a notebook.lm of all of the markdown files that constitute this.

01:09:00 - Patrick Chouinard
And I've created a couple of artifacts also if you want to listen to the audio or have a cute little slide deck of the entire architecture.

01:09:17 - Patrick Chouinard
So hopefully that's going to be useful to some of you guys.

01:09:22 - Patrick Chouinard
And on top, I'm trying to make this process a little bit more universal so I can use it to publish any documentation I have that's too big for a blog post.

01:09:39 - Hemal Shah
And Patrick, do you have captured anywhere your best practices in terms of which model do you use, what type of machines or memory, CPU, anything given you are using it this way?

01:09:54 - Patrick Chouinard
Memory, CPU, that's very, very easy.

01:09:56 - Patrick Chouinard
It's not demanding.

01:09:58 - Patrick Chouinard
So it's just a...

01:10:00 - Patrick Chouinard
Linux VM running a big, I have a Proxmox machine here, but honestly, if you can give it like four gigs of RAM and maybe 100, overall, maybe 50 gig of disk and two cores, it's more, more than enough to run this.

01:10:22 - Patrick Chouinard
It's really not that heavy.

01:10:25 - Patrick Chouinard
And for models, actually, I run mine on my Codex account because I know that Claude, they don't want us to run it with OAuth, but with Codex, it seems to work fine.

01:10:42 - Patrick Chouinard
And I don't need it.

01:10:43 - Patrick Chouinard
It's not a coding agent.

01:10:45 - Patrick Chouinard
What I do is I actually deployed a Claude code, the full Claude code, onto the machine it used.

01:10:55 - Patrick Chouinard
So it's using Claude code as a tool instead of it being.

01:11:00 - Patrick Chouinard
The coding agent itself.

01:11:02 - Patrick Chouinard
So it just gives instruction to OpenClaw.

01:11:07 - Patrick Chouinard
OpenClaw gives instruction to CloudCode to create something.

01:11:10 - Hemal Shah
And CloudCode is configured to use Sonnet and CloudModels.

01:11:14 - Hemal Shah
So that's where for coding.

01:11:16 - Patrick Chouinard
Exactly.

01:11:17 - Patrick Chouinard
Exactly.

01:11:18 - Patrick Chouinard
So OpenClaw, I can move it from Gemini to ChatGPT.

01:11:25 - Patrick Chouinard
No issue.

01:11:25 - Patrick Chouinard
The coding actually happens in a coding model.

01:11:29 - Patrick Chouinard
Okay.

01:11:30 - Hemal Shah
Thank you.

01:11:32 - Patrick Chouinard
Juan, you have a question?

01:11:36 - Patrick Chouinard
Yeah.

01:11:37 - Juan Torres
One of the questions that I had was you were mentioning that you were giving it limited access to a dash window or something like that.

01:11:48 - Juan Torres
Yeah, the configuration, the control panel.

01:11:51 - Patrick Chouinard
It's a web control panel on the machine.

01:11:55 - Patrick Chouinard
Okay.

01:11:56 - Patrick Chouinard
It gives a whole lot of control and power over the machine.

01:11:59 - Patrick Chouinard
machine.

01:11:59 - Patrick Chouinard
control on the

01:12:00 - Patrick Chouinard
And that's what's been hacked in most of the security nightmare you're going to hear about.

01:12:06 - Patrick Chouinard
So I use Telegram only, and I make this accessible only through SSH tunnel between my machine and the VM when I need to make an intervention, and I cut the tunnel afterward.

01:12:20 - Juan Torres
What was the VM solution they were using?

01:12:25 - Juan Torres
For my part, I'm running a Ubuntu 24.04 on a Proxmox server.

01:12:33 - Juan Torres
Proxmox.

01:12:34 - Patrick Chouinard
It's just an open source virtualization platform, but honestly, you could run it in a Docker file and it would work just as well.

01:12:43 - Patrick Chouinard
Awesome.

01:12:46 - Juan Torres
Good.

01:12:47 - Patrick Chouinard
Elijah?

01:12:50 - Patrick Chouinard
Where is your two questions?

01:12:52 - Elijah
One was, where was the link to the Notebook LM in there?

01:12:57 - Elijah
I didn't see how you got to that.

01:13:00 - Patrick Chouinard
Oh, on the homepage, you have a button called Browse Chapter.

01:13:03 - Patrick Chouinard
The other one is Interactive Notebook.

01:13:07 - Elijah
Interactive Notebook, okay.

01:13:09 - Elijah
That was easy.

01:13:11 - Elijah
Right there on the homepage.

01:13:14 - Elijah
Is it?

01:13:15 - Elijah
So, yeah, I see on the home.

01:13:21 - Elijah
Where do you see that at?

01:13:24 - Elijah
Let me...

01:13:25 - Patrick Chouinard
Right in the front.

01:13:27 - Patrick Chouinard
Never mind.

01:13:27 - Elijah
I see Interactive Notebook right there.

01:13:29 - Patrick Chouinard
Okay.

01:13:30 - Elijah
The next question that I have is, I don't know if you or anyone else in this group could do an exploration of Pi Mono by bad logic, but apparently Open Claw is built with that or uses that tool.

01:13:53 - Elijah
So, I've been trying to understand, like, behind the scene, what it actually does, and...

01:13:58 - Elijah
Yeah.

01:14:00 - Elijah
Apparently that's kind of like an agent, I don't know, orchestrator, I don't know exactly what the right term is, so it would just be really cool to do an exploration on kind of how the thing works, because I think there's some ways that we could mimic what it's doing without using the entirety of it itself, if that makes sense.

01:14:27 - Patrick Chouinard
Ty did it when he used its memory module outside of using the full open claw system, so yeah, definitely possible.

01:14:38 - Elijah
Yeah, just like dissecting the claw would be an interesting exploration.

01:14:45 - Elijah
Thank you.

01:14:47 - Elijah
Yep.

01:14:48 - Patrick Chouinard
Jake?

01:14:54 - Jake Maymar
Yeah, really nice work, Patrick.

01:14:57 - Jake Maymar
My question was- Ooh-Ooh.

01:14:59 - Jake Maymar
Mm-Ooh.

01:15:01 - Jake Maymar
so I have to be logged into a whole bunch of different accounts.

01:15:05 - Jake Maymar
So, and I don't think I can give credentials to the agent.

01:15:11 - Jake Maymar
So I was trying to figure out how to do that.

01:15:14 - Jake Maymar
Um, do you have any sort of scenario?

01:15:17 - Jake Maymar
If you had an employee, how would you give your employee access to those?

01:15:21 - Patrick Chouinard
Oh, I see.

01:15:22 - Jake Maymar
Yeah, that makes sense.

01:15:24 - Jake Maymar
So you have to set up all those different things, but then it's secure.

01:15:27 - Jake Maymar
Yeah, that makes sense.

01:15:28 - Jake Maymar
I treat it like a coworker.

01:15:31 - Jake Maymar
So on that note, um, privacy, have you heard about this?

01:15:36 - Jake Maymar
What?

01:15:37 - Jake Maymar
This, this link here, um, well, it's not my turn, but it's still, this is a pretty cool thing.

01:15:43 - Jake Maymar
Um, I'll, I'll just put the link in the chat, but the, uh, what's so cool about this is, um, this allows you to, um, disable cards.

01:16:00 - Jake Maymar
So you can set up a whole bunch of different cards, and if you're doing some unusual API calls to models you don't totally trust, you can actually pause it and freeze the card, and you can, of course, do very small amounts.

01:16:16 - Jake Maymar
It's pretty cool if you haven't looked into it.

01:16:19 - Jake Maymar
Some of my friends are using this, and they use it a lot for their systems.

01:16:23 - Patrick Chouinard
Yeah, actually, that would fall into one of the documents I created about API budgeting and access to money.

01:16:35 - Patrick Chouinard
basically put caps everywhere.

01:16:38 - Patrick Chouinard
Anything that the model or the agent can spend, cap it.

01:16:43 - Patrick Chouinard
That makes a lot of sense.

01:16:45 - Jake Maymar
Yeah, that makes a lot of sense.

01:16:46 - Jake Maymar
Yeah, it's great.

01:16:47 - Patrick Chouinard
I went through it.

01:16:49 - Jake Maymar
I really liked it.

01:16:53 - Jake Maymar
So that document, is it mostly security, or is it just setting up kind of sort of how to?

01:17:00 - Jake Maymar
To interact with the agent.

01:17:02 - Jake Maymar
It's basically the whole philosophy I put around it to make it secure, but also make it usable.

01:17:09 - Patrick Chouinard
I wanted to make sure that I'm not kneecapping its functionality.

01:17:14 - Patrick Chouinard
So it's really how I interact with it, how I secured it, what I gave it in terms of possibility to work in the real world without being a huge security risk.

01:17:30 - Patrick Chouinard
And no, I have not connected it to Moldbook.

01:17:37 - Patrick Chouinard
All fun that like it looks fun, but no, I'm not going to spend token having it participate in the social network.

01:17:49 - Jake Maymar
Yeah, that makes perfect sense.

01:17:52 - Patrick Chouinard
Good.

01:17:53 - Patrick Chouinard
Amal, you had a question?

01:17:55 - Patrick Chouinard
Yeah.

01:17:56 - Patrick Chouinard
So the dog ploy that you mentioned, where are you hosting?

01:18:00 - Hemal Shah
Hosting it on your physical server within your network, or where are you hosting it?

01:18:05 - Patrick Chouinard
Doug Ploy, that's Paul that mentioned it, correct?

01:18:11 - Patrick Chouinard
Yeah, or maybe, so how do you host your OpenClo on one of the cloud platform or locally on one of your server?

01:18:20 - Patrick Chouinard
On my part, I'm hosting it on Proxmox running Linux VM.

01:18:30 - Patrick Chouinard
And that VM is hosted where?

01:18:32 - Hemal Shah
On the Proxmox server.

01:18:34 - Patrick Chouinard
It's literally a box under my desk.

01:18:37 - Patrick Chouinard
Okay, all right.

01:18:38 - Hemal Shah
Okay, understood.

01:18:39 - Hemal Shah
Thank you.

01:18:40 - Hemal Shah
No problem.

01:18:42 - Patrick Chouinard
Okay.

01:18:43 - Patrick Chouinard
Let me put the next order, the call order.

01:18:50 - Patrick Chouinard
So, next, Tom.

01:18:52 - Patrick Chouinard
I got one more question there, Patrick.

01:18:53 - Elijah
I'm sorry.

01:18:54 - Elijah
Yep, go ahead.

01:18:56 - Elijah
So, if you are, so you're.

01:19:00 - Elijah
You're trying to spin up a systematic approach or an automatic approach to documentation, right?

01:19:11 - Elijah
Do you think that as we, because obviously I don't know what's happening with SaaS as we move forward, but just assume that it was the current iterations of SaaS and we were going to have a help desk.

01:19:30 - Elijah
Do you see like a parallel motion effectively where you're developing the code and implementing the features and functionality, but all of your training and support is almost happening in parallel?

01:19:47 - Elijah
And then, because what you delivered, what I just, when I'm looking at your site and trying to read through it, I mean, what I want to do is just add an agent or, you know, just add a chat box right to it or download it somehow.

01:19:59 - Elijah
description below.

01:20:00 - Elijah
And then be able to talk to it.

01:20:01 - Patrick Chouinard
Well, that's why you have that's how most help docs, yeah.

01:20:04 - Elijah
But that's why you have the Notebook LM instance.

01:20:08 - Patrick Chouinard
That's right.

01:20:09 - Patrick Chouinard
Yeah, that's right.

01:20:10 - Elijah
This is really, what I wanted to build with that is an out-of-the-box, no API keys, no token cost.

01:20:19 - Patrick Chouinard
You have a chatbot basically built in through Notebook LM with the entire content of the site.

01:20:26 - Patrick Chouinard
So if you want to read the site, you have it.

01:20:29 - Patrick Chouinard
If you want to talk to the site, you have the Notebook LM notebook.

01:20:35 - Elijah
Yeah.

01:20:36 - Elijah
Yeah, that's really interesting.

01:20:42 - Elijah
And do you see like, you know, like Zendesk or one of these help documentation tools, do you see this impacting them?

01:20:50 - Elijah
Like this approach that you're doing?

01:20:54 - Patrick Chouinard
Well, I'm not going to say if that's going to impact them because I got the idea this weekend.

01:20:59 - Patrick Chouinard
that.

01:20:59 - Patrick Chouinard
need

01:21:00 - Patrick Chouinard
But if I were them, I would definitely take a look at something like that because I created something that's really easy to consume, and it took a whole lot of 45 minutes to create because I took the document, I've asked Claude to rewrite them in an academic paper tone, then I gave it to Claude Code and say, create me a website out of that documentation.

01:21:31 - Elijah
Nice.

01:21:32 - Elijah
No, thank you.

01:21:33 - Elijah
That's good.

01:21:33 - Elijah
Do you think there's any way for us to add?

01:21:36 - Elijah
Can we add a payment gateway in front of Notebook LM?

01:21:41 - Patrick Chouinard
Notebook LM, I don't think so.

01:21:45 - Patrick Chouinard
It's a Google services.

01:21:46 - Patrick Chouinard
If you share, you share.

01:21:50 - Patrick Chouinard
I think you can share with specific people, but then I don't know.

01:21:55 - Patrick Chouinard
I don't think there's an automation that would say if you bought.

01:22:00 - Patrick Chouinard
I can automate the creation of the access, and I think it would probably violate some kind of TOS on the Google side if you started to deal for their own service.

01:22:13 - Elijah
Okay, because there's a tool called Pickaxe, you've probably seen that, and Pickaxe is a way to monetize your GPTs effectively, which is kind of what you're doing here.

01:22:27 - Elijah
So anyway, sorry, I don't mean to explore the workaround, but man, that's so cool, 45 minutes.

01:22:35 - Patrick Chouinard
That's just wild.

01:22:37 - Elijah
Yep.

01:22:39 - Patrick Chouinard
Okay, Anna, you had a question?

01:22:42 - anapreciado
Yeah, I don't know if I'm asking about the secret sauce, but I was going to ask if we could see the GitHub, or if you had other similar projects in GitHub that we can, am I in mute?

01:22:53 - anapreciado
No.

01:22:56 - anapreciado
Okay, let me rephrase what I'm trying to say.

01:22:58 - anapreciado
So,

01:23:00 - anapreciado
Everything that you mentioned sounds super interesting.

01:23:02 - anapreciado
I would definitely like to learn more, but I would probably like to look at code.

01:23:07 - anapreciado
But at the same time, I might be asking for the secret sauce of what you built.

01:23:12 - anapreciado
So can I follow you on GitHub to see other things that you've done?

01:23:18 - anapreciado
Absolutely.

01:23:19 - Patrick Chouinard
I mean, I can post the link of my GitHub, and I have quite a few public repo in there.

01:23:27 - Patrick Chouinard
But again, I'm a, what I call a new generation of developer.

01:23:35 - Patrick Chouinard
I refer to myself more as a markdown developer than anything else.

01:23:41 - Patrick Chouinard
Most of the code is done by Claude.

01:23:44 - Patrick Chouinard
What I do is I create the markdown that end up generating the code.

01:23:50 - Patrick Chouinard
Okay.

01:23:51 - anapreciado
Still.

01:23:54 - Patrick Chouinard
But yeah, and I'm trying to, I'm probably going to try to create more documentation in this.

01:24:00 - Patrick Chouinard
The same fashion as what I did for OpenClaw.

01:24:06 - Patrick Chouinard
That answer your question?

01:24:09 - Patrick Chouinard
Good.

01:24:10 - Patrick Chouinard
Ty?

01:24:15 - Ty Wells
Sorry.

01:24:17 - Ty Wells
Well, I should have just said it, but where software is going, it's software on demand.

01:24:25 - Ty Wells
That's basically what it is.

01:24:27 - Ty Wells
So Zendesk came up, and that's why I wanted to chime in, because I'm literally moving my WhatsApp business account off of that, because I built my own ticketing system for my team, my customer support team.

01:24:44 - Ty Wells
And trust me, it's painful to get it off and transfer it.

01:24:48 - Ty Wells
But anyhow, I'm in the middle of the process of doing that.

01:24:51 - Ty Wells
And then I was on FreshBooks.

01:24:53 - Ty Wells
I don't know if you guys know, it's like QuickBooks.

01:24:56 - Patrick Chouinard
And I just use that to send invoices out.

01:25:00 - Ty Wells
And I generate some invoices every month, obviously, and I send those out.

01:25:05 - Ty Wells
So I was just having the code build so they can pull the data out of FreshBooks to go ahead and send out these invoices.

01:25:16 - Ty Wells
And then I just caught myself.

01:25:18 - Ty Wells
I'm just going to replace FreshBooks with my own.

01:25:21 - Ty Wells
So this is literally what I'm saying, right?

01:25:25 - Ty Wells
If it's software, just build it, right?

01:25:27 - Ty Wells
If it doesn't, I mean, and I don't even know what FreshBooks costs.

01:25:32 - Ty Wells
It's probably 30 bucks a month or something, right?

01:25:34 - Ty Wells
But I'm going through all this work to go get the data out, then use FreshBooks to send the email, the invoice out.

01:25:41 - Ty Wells
You just pull that in and have it do it automatically.

01:25:44 - Ty Wells
So that's my project for this evening.

01:25:47 - Ty Wells
I'll be off FreshBooks.

01:25:48 - Ty Wells
That's one less subscription.

01:25:52 - Patrick Chouinard
Good idea.

01:25:53 - Patrick Chouinard
Software on demand, guys.

01:25:54 - Ty Wells
Software on demand.

01:25:56 - Patrick Chouinard
If you don't have it, build it.

01:25:58 - Ty Wells
Even if somebody has it, still build it.

01:26:01 - Patrick Chouinard
Yep.

01:26:01 - Patrick Chouinard
The most valuable software is going to be software with a single user.

01:26:08 - Ty Wells
Yeah, because that's what you'll have.

01:26:10 - Ty Wells
You just build what you need, right?

01:26:12 - Ty Wells
Yep.

01:26:12 - Ty Wells
As you need it.

01:26:13 - Ty Wells
That's literally what I've been doing for the last year is as I, well, no, building and struggling, but now I'm able to build it reliably with the tools to build it as I need it.

01:26:29 - Ty Wells
Yep.

01:26:30 - Ty Wells
Thank you.

01:26:31 - Patrick Chouinard
Paul, you had a question?

01:26:33 - Patrick Chouinard
Oh, yeah.

01:26:34 - Patrick Chouinard
Quick question.

01:26:36 - Paul Gallovich
I've been working with a PI and he has like these cases that are just so tremendous amounts of data and information just regarding one case.

01:26:47 - Paul Gallovich
And I was wondering if the notebook LLM solution like you created would be similar, like where I could maybe even implement the RAG pipeline in there too.

01:26:59 - Paul Gallovich
you.

01:27:00 - Paul Gallovich
Um, to, uh, ingest the, the data, but, um, keeping everything local because there is privacy concern.

01:27:08 - Paul Gallovich
So I'm kind of concerned about privacy and notebook LM is not, uh, cannot be implemented locally.

01:27:15 - Patrick Chouinard
It's, uh, Google services using Gemini.

01:27:19 - Paul Gallovich
Yeah.

01:27:20 - Patrick Chouinard
Okay.

01:27:21 - Paul Gallovich
Yeah.

01:27:22 - Patrick Chouinard
All right.

01:27:22 - Patrick Chouinard
Thanks.

01:27:23 - Patrick Chouinard
Very powerful for documentation about stuff that's already open source, but I would not put private data in there.

01:27:30 - Paul Gallovich
Correct.

01:27:31 - Paul Gallovich
Thank you.

01:27:33 - Paul Gallovich
No problem.

01:27:34 - Paul Gallovich
say something about that real quick?

01:27:35 - Morgan Cook
Sure.

01:27:37 - Patrick Chouinard
So, uh, Patrick's right.

01:27:38 - Morgan Cook
Notebook LM is definitely not local and we don't know who's got access to that data.

01:27:44 - Morgan Cook
So, uh, but, uh, I've used Claude, uh, without writing any source just for the purpose of consuming local content.

01:27:55 - Morgan Cook
So there's, there's no reason why you couldn't use the same kind of concept of putting same thing.

01:28:00 - Morgan Cook
All of the data that you have into a working folder, point Claude at it, and have Claude digest it locally.

01:28:08 - Morgan Cook
You're still going out to the LLM to build results and stuff, but the data is staying local.

01:28:18 - Morgan Cook
You could, I guess, I don't know if Claude, Claude can't, you can't provide a local LLM for Claude, right?

01:28:27 - Morgan Cook
No, but honestly, I would switch to Warp at that point and use Warp to do that, where you can make everything local if you had to be secure about who has access to that content.

01:28:40 - Morgan Cook
And then you could use Warp the same way you use Claude, but with a local large language model.

01:28:47 - Patrick Chouinard
Yeah, but at that point, just use LM Studio.

01:28:52 - Patrick Chouinard
Yeah, that's what I was thinking, LM Studio.

01:28:54 - Paul Gallovich
Yeah.

01:28:56 - Patrick Chouinard
Because there is LM Studio with GPT.

01:29:00 - Patrick Chouinard
OSS 20B will run on most, not small machine, but okay machine.

01:29:09 - Patrick Chouinard
And yeah, obviously, no, you're not going to run that on a 10-year-old machine, but something reasonably recent will run it, and it will do all of that pretty well.

01:29:23 - Patrick Chouinard
the local, you don't even need a rag.

01:29:26 - Patrick Chouinard
I mean, you can just point it to a directory and ask questions like that.

01:29:32 - Patrick Chouinard
Correct.

01:29:33 - Patrick Chouinard
Thank you.

01:29:34 - Paul Gallovich
Thanks so much.

01:29:35 - Paul Gallovich
No problem.

01:29:38 - Patrick Chouinard
Okay, let's resume where we were.

01:29:40 - Patrick Chouinard
So the next would be, Tom, did you have something you wanted to share?

01:29:47 - Tom Welsh
I've been doing some risk mitigation today, so I went for a sleep before the meeting.

01:29:51 - Patrick Chouinard
Hence, I'm wide awake now.

01:29:55 - Tom Welsh
Yeah, it's been an interesting week.

01:29:57 - Tom Welsh
So my major client has...

01:30:00 - Tom Welsh
Got on the AI bandwagon and actually replaced my software, which is okay, I'm happy with that.

01:30:04 - Tom Welsh
I've had a good 12 months, and it's interesting to see what they've got to and how they've arrived there.

01:30:13 - Tom Welsh
There's obviously quite a lot they haven't considered, so I'm just looking at it as an opportunity to come back and do some more later.

01:30:21 - Tom Welsh
So I'm just trying to say, not every negative, not every positive is a negative, not every negative is a positive.

01:30:28 - Tom Welsh
It's been good, it's been interesting, and I've known this company for a while.

01:30:32 - Tom Welsh
So yeah, I expect future work from their AI developers.

01:30:39 - Tom Welsh
As you were saying earlier, you were talking about how you do stuff with Markdown.

01:30:44 - Tom Welsh
I I class myself as a prompt grammar, because that's literally what I do.

01:30:48 - Tom Welsh
I don't write code, I write prompts.

01:30:50 - Tom Welsh
Exactly.

01:30:51 - Tom Welsh
And then, you know, and yeah, I don't document as well as you do.

01:30:54 - Tom Welsh
mean, you've done a fantastic job on that boat, that boat or whatever it's called, cob.

01:30:59 - Tom Welsh
Cob.

01:31:00 - Tom Welsh
Yeah, I've been reading that all day.

01:31:04 - Tom Welsh
So yeah, not being too productive on the keyboard, but in the brain, it's been quite good.

01:31:11 - Patrick Chouinard
But yeah, apart from that, I've not really been up to that much, really.

01:31:14 - Tom Welsh
Create a new personal website for my own branding, that kind of stuff, again, all prompted.

01:31:19 - Tom Welsh
Maybe it's what you can create just with some prompts, some clod or some cursor.

01:31:24 - Tom Welsh
And again, what some of the guys are asking there about local LLMs, I do quite a lot with that.

01:31:30 - Tom Welsh
using like 5.4, like GPT OSS.

01:31:33 - Tom Welsh
And those are really good when you start using them locally.

01:31:37 - Tom Welsh
Like you say, you're not burning tokens, you're not spending your money anywhere else.

01:31:41 - Tom Welsh
But yeah, not a big update for me, nothing overly exciting.

01:31:46 - Tom Welsh
Just positives and negatives going through life.

01:31:50 - Tom Welsh
Good.

01:31:51 - Patrick Chouinard
Juan, you had a question?

01:31:53 - Juan Torres
Yeah, hey, Tom, where do you, where do you deploy your GPT?

01:32:00 - Juan Torres
P-O-S-S.

01:32:01 - Juan Torres
Are you talking about the 20 billion parameter models?

01:32:05 - Tom Welsh
Yeah, 20 billion, but I deploy it locally.

01:32:10 - Juan Torres
In your machine or your client's machine?

01:32:14 - Juan Torres
Oh, sorry.

01:32:15 - Tom Welsh
When I'm doing my own stuff, I do it here.

01:32:17 - Tom Welsh
I don't deploy.

01:32:19 - Tom Welsh
Yeah, yeah.

01:32:22 - Tom Welsh
Clients are all online with proper models.

01:32:25 - Tom Welsh
Well, commercial models.

01:32:28 - Juan Torres
Yeah, it's really good because it's quantized to four bits.

01:32:32 - Juan Torres
Yeah.

01:32:34 - Tom Welsh
I've got a very expensive footstool on my feet resting on right now.

01:32:38 - Tom Welsh
And yeah, it's got quite a lot of kit in there.

01:32:42 - Patrick Chouinard
Actually, if you're looking for a good local multi-model model, one I really, really like is Gemma 3.

01:32:53 - Juan Torres
How many parameters?

01:32:56 - Patrick Chouinard
I'm able to run the 14b load.

01:33:00 - Patrick Chouinard
Locally, without too many issues, and honestly, it's not going to power something like OpenClaw in any significant fashion, but for simple interaction questions, I mean, you expose it to a search API like Brave, something like that, it handles like 75% of the question I would ask in AI.

01:33:31 - Patrick Chouinard
So, and it has decent conversation skills, so, again, would not have a two-hour conversation like I do with ChatGPT, but for a couple of questions, works well.

01:33:42 - Patrick Chouinard
What kind of GPU do you have?

01:33:45 - Juan Torres
Oh, that's just running on the Mac Mini.

01:33:48 - Patrick Chouinard
Oh, yeah, okay.

01:33:50 - Patrick Chouinard
Mac Mini 24 gig works flawlessly, and I used to run it on a Windows machine running 2.

01:33:59 - Patrick Chouinard
you.

01:34:00 - Patrick Chouinard
1080 TI that are now retired after 10 years.

01:34:08 - Patrick Chouinard
Can I answer your question?

01:34:11 - Patrick Chouinard
Yeah.

01:34:13 - Juan Torres
Good.

01:34:14 - Patrick Chouinard
Next, Anna, was there something you wanted to share with the group?

01:34:21 - anapreciado
Okay.

01:34:22 - anapreciado
So two things.

01:34:25 - anapreciado
The first is I want to ask for advice on a project I'm working on, but it's for me.

01:34:32 - anapreciado
It's nothing for any companies like a dummy I'm trying to learn kind of thing.

01:34:36 - anapreciado
And then the other one is like job advice.

01:34:41 - anapreciado
The first one, the mini project is I'm starting to play with the intersection of AI and machine learning.

01:34:49 - anapreciado
And I have a lot of questions on how does that look?

01:34:54 - anapreciado
For this dummy project, I am building a recommendation system using.

01:35:00 - anapreciado
I'm saying that if you have a company that's selling headphones, so I'm trying to go specific, I started downloading information on Google Trends that's publicly available and information that's available through the YouTube API.

01:35:14 - anapreciado
So you can not only look at, for example, what are people saying on reviews on the products, you can also look at the captions and do some serious analytics there.

01:35:25 - anapreciado
But I'm struggling to understand what would be the best way to do it, because once you have the embeddings and you have an idea of maybe the sentiment, the proximity to a keyword, the topics, et cetera, then you have to start quantifying that in a way that's not you talking to a chatbot.

01:35:44 - anapreciado
And I haven't seen any similar project before, or like I'm really, I feel like I'm using Legos to build something I haven't seen, and I have no reference.

01:35:58 - anapreciado
So

01:36:00 - anapreciado
That's kind of my question.

01:36:01 - anapreciado
It's like, does anyone has a reference or of that intersection?

01:36:05 - anapreciado
How does it look?

01:36:08 - Patrick Chouinard
I'm trying to figure out exactly what you're looking for in terms of, because I have a lot of idea how I would do it, but in terms of, I don't know, is it just me or?

01:36:25 - Juan Torres
What's the ultimate product, aside from the recommendation system, that you want to get?

01:36:31 - Juan Torres
Thank you.

01:36:32 - anapreciado
So that's kind of, because it's a dummy project, my idea is that I'm going to build a website and I'm going to use Amazon Affiliate and Google Analytics to track if this can make money by itself.

01:36:48 - anapreciado
And after that, really my product is market research.

01:36:54 - anapreciado
And being able to do, like, I'm not going to be able to advertise targeted because for that you would need a Google account.

01:37:00 - anapreciado
And you would need to have an actual company, so I'm not going to do that.

01:37:03 - anapreciado
But in the case that I wanted to do targeted advertisements, that's the kind of recommendation that I would like to look for.

01:37:09 - anapreciado
So what makes some person be targeted in a specific ad versus a different one?

01:37:16 - anapreciado
And so that's how the end product looks, just market research and some kind of monthly predictions of what to target to who.

01:37:24 - anapreciado
But it's really a new project, and I'm trying to see how to use embeddings as features almost for machine learning and to conduct substantial market research.

01:37:39 - Juan Torres
Yeah, I share a link with the San Diego Machine Learning Group.

01:37:44 - Juan Torres
They actually have meetings on a weekly basis.

01:37:47 - Juan Torres
You can join online, and they're one of the most, I think, one of the most prominent online machine learning engineer groups out there.

01:37:58 - Juan Torres
So I'm fortunate to have them here.

01:38:00 - Juan Torres
So I can go physically with them.

01:38:04 - Juan Torres
But sometimes they go over case studies regarding this.

01:38:08 - Juan Torres
They haven't gone over categorization and multi-categorization issues with machine learning.

01:38:14 - Juan Torres
But what would be really interesting is to see how you can use classical machine learning with AI engineering, specifically because you're targeting research for, you know, market research, which I've done before.

01:38:31 - Juan Torres
And what you can do is based on the, you know, classical categorization machine learning issues, based on the results, then you use AI, which are in like rail guards, to generate the report itself.

01:38:46 - Juan Torres
If you're thinking about generating reports, right, including quantifiable results from your machine learning results.

01:38:54 - Juan Torres
So that's one of the ways, you know, you can perhaps start automating the whole process.

01:39:00 - Juan Torres
Through a synthesis of both.

01:39:02 - anapreciado
That makes sense.

01:39:03 - anapreciado
And does the group that you sent meet online or in person?

01:39:07 - anapreciado
Both.

01:39:08 - Juan Torres
It's a hybrid.

01:39:09 - Juan Torres
Thank you.

01:39:10 - Juan Torres
That's what I missed.

01:39:12 - anapreciado
Thanks.

01:39:13 - anapreciado
I will definitely take a look into that.

01:39:15 - anapreciado
And then my other question, and I will look into automating, the intersection with automation.

01:39:24 - anapreciado
My other question is in terms of like job advice.

01:39:27 - anapreciado
So I got a confirmation last week that I was going to receive an offer for working as an AI specialist at a bank.

01:39:39 - anapreciado
And that means that I would be a one person team.

01:39:42 - anapreciado
And I don't know exactly what, how, okay, not necessarily how to do it, but I don't know what's any advice that you have on identifying what would be the most, apart from my intuition and what my boss tells me, what are the most important.

01:40:00 - anapreciado
Through a synthesis of both.

01:40:02 - anapreciado
That makes sense.

01:40:03 - anapreciado
And does the group that you sent meet online or in person?

01:40:07 - anapreciado
Both.

01:40:08 - anapreciado
It's a hybrid.

01:40:09 - anapreciado
Thank you.

01:40:10 - anapreciado
That's what I missed.

01:40:12 - anapreciado
Thanks.

01:40:13 - anapreciado
I will definitely take a look into that.

01:40:15 - anapreciado
And then my other question, and I will look into automating, the intersection with automation.

01:40:24 - Patrick Chouinard
My other question is in terms of like job advice.

01:40:27 - Patrick Chouinard
So I got a confirmation last week that I was going to receive an offer for working as an AI specialist at a bank.

01:40:39 - Patrick Chouinard
And that means that I would be a one person team.

01:40:42 - Patrick Chouinard
And I don't know exactly what, how, okay, not necessarily how to do it, but I don't know what's any advice that you have on identifying what would be the most, apart from my intuition and what my boss tells me, what are the most important.

01:41:00 - Patrick Chouinard
Things to look for, especially because I'm going to be the one AI person.

01:41:03 - Patrick Chouinard
So like my boss is not technical.

01:41:05 - Patrick Chouinard
I have a technical boss and a non-technical boss, but I'm going to be working with a non-technical person.

01:41:09 - Patrick Chouinard
So like any advice from the many years of experience that you have, I would be more than happy to take notes.

01:41:17 - Patrick Chouinard
First, they're going to have to define what AI specialist means to them because it can mean pretty much anything right now.

01:41:27 - Patrick Chouinard
And the one thing you're going to want to look at is governance, governance, governance, governance.

01:41:32 - Patrick Chouinard
In a bank, this is absolutely critical and you're going to face some very specific restriction in the financial industry that it, I'm not saying it's the most, yeah, the SOC 2 is probably one of the, the, the, the most important one to take a look at.

01:41:51 - Patrick Chouinard
It's not necessarily more restrictive than other field.

01:41:54 - Patrick Chouinard
It just, it has its own restriction.

01:41:56 - Patrick Chouinard
Like the, the medical field will have a power.

01:42:01 - Patrick Chouinard
There's that you're going to have to follow.

01:42:03 - Patrick Chouinard
This one is SOC 2.

01:42:04 - Patrick Chouinard
But yeah, this is going to be really important.

01:42:08 - Patrick Chouinard
And in terms of working in the financial industry with AI, there are tools that are extremely powerful.

01:42:15 - Patrick Chouinard
But again, if you are a one-person team in a bank, I'm guessing that that means it's a branch, not a head office.

01:42:25 - Patrick Chouinard
And it means that it can't necessarily implement new tools.

01:42:29 - Patrick Chouinard
It has to use whatever is provided by the head office.

01:42:33 - Patrick Chouinard
Am I correct?

01:42:36 - Patrick Chouinard
It is a branch, but I'm expected to build solutions.

01:42:41 - Paul Miller
Okay.

01:42:42 - Paul Miller
The software-oriented role.

01:42:44 - Paul Miller
Okay.

01:42:45 - Paul Miller
Okay, okay.

01:42:46 - Paul Miller
It's just that a lot of the financial industry tools that you can, or platform that you can build upon, are extremely expensive.

01:42:56 - Paul Miller
And here I'm thinking about Claude for financial services.

01:43:00 - Paul Miller
For example, it is built for the financial industry, but the ticket of entry is a quarter million.

01:43:09 - Paul Miller
So for a branch of a bank, it might be a hard pill to swallow.

01:43:17 - Paul Miller
But thank you for the advice on governance.

01:43:20 - Paul Miller
Yeah, absolutely.

01:43:21 - Paul Miller
This is going to be the most critical aspect.

01:43:24 - Paul Miller
In if you don't do governance right, you're not going to be able to go very far in the financial industry with AI.

01:43:31 - Paul Miller
It is the bedrock of it.

01:43:35 - Paul Miller
Paul, did you want to share something?

01:43:40 - Paul Miller
Yeah, probably where I would start, because you kind of want to be in your lane on the software side, but you want to fit into this model that is an existing conservative organization.

01:43:54 - Paul Miller
And what Patrick said, you know, there's a lot of rules there.

01:43:59 - Paul Miller
there.

01:43:59 - Paul Miller
There's lot

01:44:00 - Paul Miller
A lot of, if your boss is unable to define to you the context of your role, kind of where you need to start, and probably if it was me starting, I would say I would get from the organization as much of the documentation about your governance that you could load into your own little project, or I'd probably do it into Claude.

01:44:28 - Paul Miller
I'd set up a Claude project, I'd set up maybe a notebook LN, and say, okay, I'm new to this industry, understand the governance in which I'm in the organization I'm going to be working in.

01:44:44 - Paul Miller
What documents can I grab on that?

01:44:47 - Paul Miller
What documents can I grab for the banking industry in the country that I'm in?

01:44:52 - Paul Miller
What about the standard industry body?

01:44:55 - Paul Miller
Where are some of the documents around what people have been doing in that?

01:44:59 - Paul Miller
Just give

01:45:00 - Paul Miller
Give me a bit of background context and then go into that library that you build and say, hey, this is me.

01:45:08 - Paul Miller
This is where I'm starting in context to all of this stuff.

01:45:14 - Patrick Chouinard
What's some base documents I can publish and say to my boss, this is me positioning myself as to where I'm going to start with the roles.

01:45:24 - Juan Torres
So I've got the background as to where your boss may be coming from, so what questions she might ask versus where you think there's objectives.

01:45:39 - Juan Torres
And always the biggest thing for me is what's the metric for success for this role?

01:45:45 - Juan Torres
What's the metric for success for your boss's role?

01:45:49 - Juan Torres
Because as long as you're aligned to the metric of success that bonuses are delivered on, then you're grounded not only from a governance perspective, but...

01:46:00 - Juan Torres
You're grounded from a commercial perspective, and then you can do the cool AI stuff around that, because you're honed in to governance, compliance, and commercial compliance.

01:46:15 - Paul Miller
Good answer, Paul.

01:46:19 - Paul Miller
Juan, you want to add something?

01:46:23 - Paul Miller
Yeah, no, it sounds like, and this is a question more for Paul, but it sounds like she's being given kind of like a project manager position, and then she might have to hire the specialist, the technical specialist to, she's going to have to be in charge of understanding the standard operating procedure of the company, and then how AI can basically automate processes.

01:46:49 - Paul Miller
just by the broad, you know, description of the job, right?

01:46:55 - Paul Miller
So I think that's going to be her main role, is understanding the standard operating procedure of the company.

01:47:00 - Paul Miller
And then find the technical specialists that are going to be able to fulfill the automation processes for that modus operandi for the bank.

01:47:09 - Paul Miller
I think that's going to be her role.

01:47:11 - Paul Miller
I don't know if I'm correct, Anna.

01:47:12 - Paul Miller
Sounds like you're agreeing, Anna.

01:47:15 - Paul Miller
If that's the context, so you probably want to do what I've suggested, but also say from an architectural and AI best practice, what immediately comes to mind is probably not getting approval for Patrick's quarter of a million dollars, but looking at trying to understand within the bank, if they've got an agreed cloud hosting provider, say it might be Azure or AWS, you might meet with the IT people and say, look, I want to have a secure version of Claude hosted.

01:48:00 - Patrick Chouinard
So within a controlled framework, because it's not the public cloud, it's the banking cloud, or it's a proof of concept area.

01:48:11 - Patrick Chouinard
So if anyone's coming in, or we're going to engage with any platforms, we're doing it in compliance with the framework of technology that the bank is happy with, that IT is happy to support.

01:48:24 - Patrick Chouinard
And then when you're looking for people in those fields, then they can play nice within that framework.

01:48:32 - Patrick Chouinard
Because I think we can all sit at home and play with some cool stuff.

01:48:36 - Patrick Chouinard
We're doing it publicly, but in the corporate world, it's not really appropriate.

01:48:41 - Patrick Chouinard
People get very upset.

01:48:43 - Patrick Chouinard
They can shut down your projects.

01:48:46 - Patrick Chouinard
And you want to have the right tech people that can operate in that environment that works neatly with the architecture of the bank.

01:48:55 - Patrick Chouinard
And basically what you want to look at is, is there an AI...

01:49:00 - Patrick Chouinard
Platform already approved.

01:49:02 - Patrick Chouinard
If not, do they have an hyperscaler they're working with?

01:49:05 - Patrick Chouinard
So Google or an AWS or something like that.

01:49:09 - Patrick Chouinard
Once you've identified it, run everything through that one specifically.

01:49:14 - Patrick Chouinard
Because the rule of thumb I've gave everyone that works with me is you have XYZ platform that is approved.

01:49:23 - Tom Welsh
With that one, work with internal files, with internal documentation, no problem.

01:49:28 - Tom Welsh
Anything else, and I gave that to non-technical user because they have a really hard time figuring out how do I know what I can and cannot do with other AI system.

01:49:41 - Tom Welsh
And that's one question you're going to probably face daily is the way you tell them in a non-technical way is are, if you, the material you're giving the AI right now, the document or the question you're asking, are you comfortable in, are

01:50:00 - Tom Welsh
That was on the front page of the newspaper tomorrow morning.

01:50:03 - Patrick Chouinard
If the answer is yes, absolutely, revert back to the approved platform.

01:50:13 - Patrick Chouinard
So, makes sense?

01:50:16 - Patrick Chouinard
Good.

01:50:17 - Patrick Chouinard
Tom, you had something you wanted to add?

01:50:20 - Patrick Chouinard
Yeah, I was just going to say, having worked in financial services in the city of London, do not be dismayed when you get knocked back to left, right and centre from security, from compliance, from risk.

01:50:31 - Patrick Chouinard
These are all going to be smackdowns every day and you'll be an uphill struggle.

01:50:36 - Patrick Chouinard
But you've got to stick to your guns, get the appropriate frameworks like everybody's saying, and work from a position of strength.

01:50:44 - Patrick Chouinard
The whole point, I used to work in security, my whole job was to say no.

01:50:49 - Patrick Chouinard
And that's what you're going to come up against quite a lot in banks.

01:50:52 - Patrick Chouinard
And I'm not sure if you're at group headquarters or if you're, say, if you're in a smaller branch, that'll be worse.

01:50:58 - Jake Maymar
But don't be dismayed, just fight the group.

01:51:00 - Jake Maymar
Good fight.

01:51:01 - Jake Maymar
Actually, I found that if you provide a service for the cybersecurity team, it makes your life a lot easier to negotiate with them afterward, because it's really hard for them to say no for a service that they are using themselves.

01:51:18 - Jake Maymar
Yep.

01:51:19 - Jake Maymar
Yeah.

01:51:20 - Jake Maymar
I would always get my risk and my security teams on site, along with IT, like you say.

01:51:26 - Jake Maymar
Work within the frameworks.

01:51:29 - Jake Maymar
Yep.

01:51:30 - Jake Maymar
Absolutely.

01:51:34 - Jake Maymar
Yeah, exactly.

01:51:35 - Jake Maymar
Paul, any team that might stop you, provide them a service for free as soon as possible, then you're good.

01:51:48 - Jake Maymar
Good.

01:51:50 - Jake Maymar
And next we had Jake.

01:51:57 - Jake Maymar
No big updates.

01:51:58 - Jake Maymar
Just, just...

01:51:59 - Jake Maymar
Just...

01:52:00 - Jake Maymar
Just trying to actually physically get this thing done at the same time on this call.

01:52:05 - Patrick Chouinard
I love this call.

01:52:06 - Patrick Chouinard
It's really so interesting.

01:52:09 - Patrick Chouinard
I am very curious to see where OpenClaw evolves to.

01:52:12 - Patrick Chouinard
You know, it's changed its name three times already in like a couple of days.

01:52:18 - Patrick Chouinard
But I do think it's a fascinating sort of infrastructure.

01:52:21 - Patrick Chouinard
I think it's even more fascinating to watch the adoption of it because it feels like, and I'm kind of curious to the group, it feels a little bit like a GPT 3.5 moment.

01:52:33 - Patrick Chouinard
You know, like it was like 3.5 was kind of cool and everyone was playing with it.

01:52:38 - Patrick Chouinard
And I remember, you know, having it type things and like, this is hilarious, right?

01:52:42 - Patrick Chouinard
It was like not really right at all.

01:52:45 - Patrick Chouinard
It was writing some funny stories and it was just, but I had no idea what was around the corner.

01:52:50 - Jake Maymar
And I feel that.

01:52:52 - Jake Maymar
I feel like OpenClaw, and since it's open source, I feel like there's going to be a tremendous amount of forks of it, if not already.

01:53:00 - Jake Maymar
But yeah, I'm just kind of curious to hear your thoughts.

01:53:04 - Patrick Chouinard
Definitely.

01:53:05 - Patrick Chouinard
Definitely.

01:53:06 - Patrick Chouinard
This is one of those moments, not because of the tool itself, because I don't think OpenClaw is like the best coded tool ever, but for the idea that it opens and the capability that it provides, I wouldn't be surprised to see the Entropic, Gemini, and OpenAI of the world start to create their own.

01:53:29 - Ty Wells
Because honestly, for the inference provider, this is like the best day of their life.

01:53:37 - Ty Wells
mean, Claude actually went down today because of too many API calls coming from it.

01:53:45 - Patrick Chouinard
it's crazy.

01:53:47 - Patrick Chouinard
Well, it wasn't, I was going to say it wasn't just Claude, like Gemini was sort of having some issues, OpenAI had a little bit of issues.

01:53:56 - Patrick Chouinard
It's funny, Claude went down, then Gemini, then...

01:54:00 - Patrick Chouinard
Then OpenAI, but then, of course, they came all back up.

01:54:02 - Patrick Chouinard
Yeah, exactly.

01:54:03 - Patrick Chouinard
But it's just this thing is a token churning machine.

01:54:08 - Ty Wells
So believe me, now that they've seen it, they're going to figure out a way to monetize it.

01:54:15 - Ty Wells
Yeah, you're totally right.

01:54:16 - Ty Wells
Well, it's token churning because it has a heartbeat.

01:54:20 - Ty Wells
Think about it, right?

01:54:22 - Ty Wells
Without that heartbeat, it's just sitting there passively waiting for you to input.

01:54:26 - Ty Wells
But, you know, I wouldn't be surprised if one of these guys are behind it.

01:54:30 - Ty Wells
And it wouldn't, Anthropic in particular, because, you know, they were, or Google, it could be.

01:54:36 - Ty Wells
But without the heartbeat, it's not burning any tokens.

01:54:40 - Ty Wells
Like, you know, we have all these projects sitting.

01:54:42 - Ty Wells
Let's see if we can burn more tokens.

01:54:44 - Ty Wells
That was the number one goal.

01:54:46 - Ty Wells
Why do you think there is Maltbook?

01:54:49 - Ty Wells
There is MaltTask.

01:54:51 - Ty Wells
There is the agent version of LinkedIn that popped up in the last couple of days.

01:54:57 - Ty Wells
I mean, this is keeping them alive.

01:55:00 - Patrick Chouinard
Fathom keeping them churning tokens.

01:55:02 - Ty Wells
They may actually make some money, but I don't think it because they're not able to scale properly.

01:55:07 - Ty Wells
So they still won't make any money, but they have more customers now available that are burning more tokens.

01:55:14 - Ty Wells
you know, in terms of like a script kitty, right, somebody that throws it out on the Internet and doesn't know what they're doing.

01:55:22 - Ty Wells
We love those people because they're going to rip up some tokens.

01:55:26 - Jake Maymar
The only problem with that is I was on another call yesterday and the guy had it out on the Internet and it was wild.

01:55:38 - Jake Maymar
I mean, it was wild.

01:55:39 - Jake Maymar
And what it did, what he demonstrated, I don't know if it did.

01:55:43 - Jake Maymar
I don't doubt it, actually.

01:55:45 - Jake Maymar
What it did when he woke up in the morning was just crazy.

01:55:51 - Jake Maymar
But he wanted to, he wanted one of us to give up our phone numbers so he could have it call us.

01:55:56 - Jake Maymar
Could you imagine where that would go to next?

01:55:58 - Jake Maymar
Thanks.

01:55:58 - Jake Maymar
We'll be We'll We'll Because

01:56:00 - Jake Maymar
Oh my God.

01:56:01 - Jake Maymar
No one, no one would give up their phone number, you know, because it is, it is going to be crazy out there, guys.

01:56:08 - Jake Maymar
I'm not going to lie.

01:56:09 - Jake Maymar
It's, this is definitely a pivotal moment here.

01:56:15 - Jake Maymar
Well, did you see it was, they were already trading, they were trading like Bitcoin and crypto back and forth and all that craziness.

01:56:22 - Jake Maymar
So that's.

01:56:22 - Jake Maymar
I don't see it, but I could only imagine.

01:56:25 - Jake Maymar
So imagine you have a, like a, what's it, mask.

01:56:32 - Jake Maymar
I forget what it's called, but basically, let's say you have a wallet on your browser, right, that has, you know, cryptocurrency already loaded and you give access to OpenClaw and it can actually like see that account, it can spend it, it can move it around.

01:56:49 - Jake Maymar
To me, to that's terrifying, right?

01:56:52 - Patrick Chouinard
Because you just, I mean, or your bank accounts, like you have all your bank accounts.

01:56:55 - Patrick Chouinard
So a lot of people are giving access to this model and just letting it run.

01:56:59 - Patrick Chouinard
to me, to

01:57:01 - Patrick Chouinard
Did I show the meme?

01:57:02 - Patrick Chouinard
I think I probably showed the meme last time where it was like, you know, this is what happened.

01:57:06 - Ty Wells
went to bed and came up and all these crazy things happened.

01:57:11 - Ty Wells
I'm curious to see how quickly people evolved this, though.

01:57:16 - Ty Wells
Because I mean, that's the number one thing we keep talking about security, you know, and Patrick has an excellent framework.

01:57:22 - Ty Wells
Ty, you had an excellent set of framework as well.

01:57:28 - Ty Wells
And I think everyone on here is sort of sharing different ideas.

01:57:32 - Ty Wells
But I do feel like it's going to standardize pretty quickly, because there's only so many things you can do.

01:57:39 - Ty Wells
I think there's a lot of standards for making things secure.

01:57:43 - Ty Wells
Unless I'm, you know, oversimplifying this, but I think at some point, that's going to standardize and then things are kind of going to build on top of that.

01:57:52 - Ty Wells
Yeah, honestly, there's already like six or seven copy of what OpenClaw used to be.

01:58:00 - Ty Wells
And generated and are starting popping up everywhere.

01:58:04 - Ty Wells
There's a nano claw out there.

01:58:06 - Ty Wells
I would definitely take a look at that.

01:58:08 - Ty Wells
That's just an entry level.

01:58:10 - Juan Torres
And then you can grow, right?

01:58:12 - Juan Torres
If you're a developer, you can build on it.

01:58:14 - Juan Torres
But if, you know, sort of open claws, like diving into the deep end, and you can't swim, and you have these weights on you, but then you have these bars on you.

01:58:27 - Juan Torres
mean, these floaties on you.

01:58:28 - Juan Torres
I mean, it's just a  show.

01:58:31 - Patrick Chouinard
I'm not, my language, but it is definitely a problem.

01:58:34 - Mitch
Because what I was going to tell you in that story is that he did put his credit card in, and when he set it up, and it, the issue I have with, with it at this point is, it doesn't know when to stop until it reaches its goal.

01:58:48 - Patrick Chouinard
Right?

01:58:49 - Patrick Chouinard
So, no, I'm serious.

01:58:50 - Patrick Chouinard
It tries, and tries, and tries, and tries, and tries, and tries every possible way to get its goal to accomplish.

01:59:00 - Patrick Chouinard
And that is problematic.

01:59:03 - Patrick Chouinard
It's problematic, right?

01:59:06 - Juan Torres
So guys, get ready for this one.

01:59:09 - Patrick Chouinard
So Anna, we found the perfect project for you.

01:59:12 - Patrick Chouinard
So you're going to tell your boss that out of the consolidated assets of your bank, you're going to use 10% in order to give it to an AI bot in order to trade it in the stock trade.

01:59:24 - Patrick Chouinard
Okay.

01:59:25 - Patrick Chouinard
That's the main project you're going to take upon arriving to that bank.

01:59:32 - Patrick Chouinard
Yeah, you need to launch an NFT with it, you know?

01:59:35 - Patrick Chouinard
Yes, and that too.

01:59:37 - Patrick Chouinard
Actually, Matthew Brennan did that on a live stream with a small crypto wallet to test that theory because there's a bunch of people who are talking about that on X right now.

01:59:54 - Patrick Chouinard
Like, oh, I gave it X amount of dollar and I woke up, it quadrupled the money.

01:59:58 - Mitch
And, uh, basically.

02:00:00 - Patrick Chouinard
Basically, he lost everything that he put in the wallet in about half an hour.

02:00:08 - Patrick Chouinard
Again, he didn't put, like, thousands in there.

02:00:11 - Mitch
It was just to try to show for the stream.

02:00:14 - Patrick Chouinard
But still, it just basically went through and lost all the money instantaneously.

02:00:19 - Patrick Chouinard
Well, it's not her money.

02:00:23 - Patrick Chouinard
Yeah, but it's her job.

02:00:27 - Patrick Chouinard
You want your, you want the company you work for to make money, not lose money.

02:00:35 - Patrick Chouinard
That's not for discussion.

02:00:41 - Patrick Chouinard
Good.

02:00:43 - Patrick Chouinard
Last one.

02:00:45 - Patrick Chouinard
Mitch, did you have something you wanted to share with the group?

02:00:49 - Patrick Chouinard
I was just curious what's good with you, Patrick.

02:00:55 - Patrick Chouinard
What are you building?

02:00:58 - Patrick Chouinard
Oh, I actually

02:01:00 - Patrick Chouinard
I through the demo a little bit earlier when I shown the site I created that I posted on yesterday.

02:01:11 - Patrick Chouinard
Oh, yeah, I saw that.

02:01:13 - Patrick Chouinard
Yeah.

02:01:14 - Patrick Chouinard
That was the main thing.

02:01:15 - Mitch
Basically what I have been working on.

02:01:18 - Mitch
It's not that the site took a lot of time.

02:01:20 - Mitch
It's just the creation of the information was me going back and forth again while stuck in traffic with ChatGPT.

02:01:30 - Patrick Chouinard
And I just created everything from that discussion.

02:01:36 - Patrick Chouinard
And now that I have this publication platform, basically this is pretty easy.

02:01:42 - Patrick Chouinard
I have an account with Ostinger and I just do the DNS redirection to subdomains of my main domain and it points to Cloudflare pages.

02:01:55 - Mitch
Very, very simple, but basically free.

02:02:00 - Mitch
Except for the Ostinger subscription.

02:02:04 - Mitch
that's how the website is hosted that you've posted?

02:02:06 - Mitch
Actually, Ostinger, in there, it's my personal website is hosted there, but the subdomain, I just use them as a DNS redirect.

02:02:15 - Mitch
That's it, to point to a Cloudflare page.

02:02:19 - Mitch
Oh, I see, like the app.yourmaindomain thing.

02:02:25 - Mitch
Okay, gotcha, gotcha.

02:02:26 - Mitch
So basically, each website or each, I don't know, documentation domain, if you want, will be a subdomain of my main site.

02:02:35 - Mitch
So I can, and the nice thing is I have all the tools to automate it through Cloud code.

02:02:41 - Mitch
So whenever I create the site, Cloud can do all of the publishing on Cloudflare for me.

02:02:48 - Mitch
So not that I couldn't do it manually, but it makes it a lot simpler.

02:02:53 - Mitch
Yeah, okay.

02:02:55 - Mitch
Yeah, you actually brought up a good thing for me to bring up, but I didn't even.

02:03:00 - Mitch
I think I had a question, but now I do have a question.

02:03:02 - Mitch
Is it okay if I share my screen?

02:03:03 - Mitch
Sure, sure.

02:03:04 - Mitch
Cool, cool.

02:03:05 - Mitch
Okay.

02:03:06 - Mitch
Share my screen.

02:03:08 - Mitch
Oh, yeah.

02:03:09 - Mitch
I was...

02:03:10 - Mitch
Oh.

02:03:12 - Mitch
Hold on.

02:03:13 - Mitch
Okay.

02:03:13 - Mitch
Are you guys seeing my screen or no?

02:03:15 - Mitch
Okay, cool.

02:03:16 - Mitch
This is the Mac Mini.

02:03:18 - Mitch
So the lower the rank, like you can see, is like number 39 in computer accessories and went all the way to rank one.

02:03:26 - Mitch
And they increased the price here.

02:03:28 - Mitch
So pretty crazy.

02:03:30 - Mitch
But if I go to VS Code, let me open it up again.

02:03:35 - Mitch
Oh, yeah.

02:03:36 - Mitch
I need to go.

02:03:36 - Mitch
I switched from Cursor to VS Code because Cursor kept on mentioning like, hey, like you need a paid account.

02:03:45 - Mitch
I'm like, screw this.

02:03:47 - Mitch
You know, I'm like, I'm going back to VS Code.

02:03:49 - Mitch
So basically, I just have a bunch of different...

02:03:52 - Mitch
Oh, it's an easier one.

02:03:53 - Mitch
So Data Rova basically have like some simple, simple TypeScript stuff that just takes like...

02:03:59 - Mitch
that.

02:03:59 - Mitch
So...

02:03:59 - Mitch
don't easier know.

02:03:59 - Mitch
But...

02:04:00 - Mitch
A CSV file or like a group of CSV files and then like basically makes like a simple HTML website here.

02:04:09 - Mitch
So this is like one of the brands that we were auditing.

02:04:11 - Mitch
And so it's like really easy to do, obviously, on a static HTML site.

02:04:15 - Patrick Chouinard
And then I was basically needing to take this to the company, right?

02:04:20 - Patrick Chouinard
So anyone in the company can just add some certain CSV files here.

02:04:24 - Patrick Chouinard
These are just two different CSV files and then like make this themself.

02:04:28 - Patrick Chouinard
So I was curious, like, what was going to be like the easiest way to go about it?

02:04:31 - Patrick Chouinard
I it's kind of funny that the codex came up recently.

02:04:34 - Patrick Chouinard
So I was maybe thinking like making a skill like for everyone in my company just to have and then make maybe they'd be able to do that.

02:04:43 - Patrick Chouinard
And then like just have the main like high level like architecture of like.

02:04:49 - Patrick Chouinard
Where is it here?

02:04:52 - Patrick Chouinard
So like here's an example where we have like the brand and then the code here.

02:04:56 - Patrick Chouinard
So the code kind of lives on the main file.

02:04:59 - Patrick Chouinard
And.

02:05:00 - Patrick Chouinard
And then the brand data itself lives in a separate folder here.

02:05:06 - Patrick Chouinard
That's what I was kind of thinking, but I'm not sure what would be the best way to help with the overall company who's not really AI or coding focused to kind of onboard this.

02:05:16 - Mitch
Well, actually, I'm working on something.

02:05:19 - Mitch
Because when I created the site, I just prompted Cloud Code to do it.

02:05:25 - Mitch
But now that I have a team, a look, a brand, a brand kit, basically, for it, I'm going to work on implementing it as a Cloud skill.

02:05:37 - Mitch
And I'm going to see if I'm able to just push.

02:05:41 - Mitch
On my part, it's going to be Markdown, but it would be Markdown, Excel, whatever you need to push it.

02:05:47 - Mitch
Where I could just push content to instantiate new pages or a new site, depending on what you ask, or maybe a two different skill.

02:05:58 - Morgan Cook
I'm still thinking.

02:06:00 - Morgan Cook
Of the architecture, but it would be going through either skills, or if I need a little bit more, maybe a cloud code plug-in.

02:06:10 - Morgan Cook
And because we're- sounds like skills is the way to go, and making a skill for how to do it, and then maybe just creating a simple Git repo for, if it's standardized.

02:06:21 - Morgan Cook
Like semi-standardized, it's just going be whipping up random views.

02:06:27 - Morgan Cook
Because basically what happens right now is we just have a bunch of Excel spreadsheets, right?

02:06:31 - Morgan Cook
And then people kind of make it customized for each client, and then what happens is you have like 20 different templates.

02:06:38 - Morgan Cook
so kind of just the aspect of 20 different templates, but instead of like trying to do it 20 different times, just have AI do it instead of us do it.

02:06:47 - Mitch
So that's mostly it.

02:06:49 - Mitch
Do you have anything, Morgan?

02:06:50 - Mitch
Morgan, do have a question?

02:06:52 - Mitch
Yeah, not a question, so much as just back to what my feedback earlier was.

02:06:57 - Mitch
I don't think you were on the call at that point, Mitch, but- don't you were in the chat with us.

02:06:59 - Morgan Cook
me wait.

02:07:00 - Morgan Cook
The process I've gone through over the past week was very much that, build a cloud skill, but then after it became deterministic, convert that to a JavaScript app that the cloud skill can call directly so that it's quick, right?

02:07:14 - Morgan Cook
As you're not sitting there wasting tokens with the cloud trying to think about the same thing that I already thought about 20 times in the past.

02:07:22 - Morgan Cook
Once you have deterministic nature of converting those CSV files into a webpage, make it a JavaScript and it'll go, it'll run quick.

02:07:31 - Morgan Cook
And then it becomes something you can pretty much make into a local agent kind of thing where it just executes from the skill.

02:07:40 - Morgan Cook
The skill has nothing in it.

02:07:41 - Morgan Cook
All it's doing is calm as JavaScript.

02:07:43 - Morgan Cook
Yeah, I guess I would need to make another skill similar to Brandon Shipkit, which would be to look at the git diff.

02:07:51 - Morgan Cook
and then invite them to the GitHub repo probably to do that.

02:07:54 - Morgan Cook
Because I think the one thing is like, then they don't know how to manage the files of it.

02:08:00 - Morgan Cook
So probably those creating two separate skills would probably be the main thing.

02:08:06 - Morgan Cook
My little system has about five different skills.

02:08:09 - Morgan Cook
One to create the, to convert the, what I'm doing is converting from an MD to a HTML.

02:08:16 - Morgan Cook
And then I use that to generate a prompt image or prompt for creating an image.

02:08:22 - Morgan Cook
And then I use that to create an actual PDF.

02:08:25 - Morgan Cook
And all of those have been converted.

02:08:27 - Mitch
I worked through the process in the skill.

02:08:31 - Jake Maymar
And once the skill was deterministic, I told Claude to modify that and put it into a JavaScript.

02:08:39 - Jake Maymar
So now it runs locally.

02:08:41 - Jake Maymar
The skill still exists.

02:08:42 - Jake Maymar
I still use the skill to drive it.

02:08:44 - Mitch
But it's just calling the JavaScript to actually process the files.

02:08:49 - Mitch
And it still has all the logic in the JavaScript to take care of, you know, multiple conditions that are different in each of the MD files.

02:08:58 - Jake Maymar
It was just a matter of...

02:09:00 - Mitch
You know, I probably have maybe 10 or 12 different formats that I'm dealing with.

02:09:03 - Mitch
But as you grow, you can just continually modify your JavaScript at that point to get smarter and smarter each time you have to process a new file that has something tweaked in it.

02:09:16 - Mitch
It's the air conditioning that you got to be able to handle is make sure you have some kind of air reporting that say, hey, this process, but we this was not part of the skill.

02:09:27 - Mitch
Yeah, sounds good.

02:09:28 - Mitch
I appreciate it.

02:09:31 - Mitch
Jake, you had something?

02:09:33 - Jake Maymar
Yeah, was just going to say, Mitch, have you tried just doing like, I don't know if you can simplify it down, but doing like a GPT where you just drag and drop the file in?

02:09:44 - Jake Maymar
That's a good point.

02:09:49 - Jake Maymar
Yeah, I think the issue is like the queering of the data.

02:09:56 - Mitch
Yeah, because a lot of it's not organized well, because like.

02:10:00 - Mitch
We're kind of taking different reports, so I think that's a good idea.

02:10:03 - Mitch
I think it would work for some of them, but I like it.

02:10:10 - Mitch
I think the key thing is Codex kind of came out, so there's that sauce there.

02:10:16 - Mitch
And I think one thing I really like about it is deploying on the cloud side of things, so they don't need to run it, and they don't need to install the dependencies and stuff, and they need Codex to do all that.

02:10:27 - Mitch
So I'm going to try that, and hopefully that works.

02:10:30 - Patrick Chouinard
And then, yeah, I think that's what I'm leaning towards.

02:10:34 - Patrick Chouinard
I also really like Morgan's suggestion, too, of making the skill, making it deterministic.

02:10:40 - Raghav
But yeah, I'm actually looking for something like that where a client can just drop it in, and I haven't really found, like I kind of found something, but it's not right.

02:10:50 - Raghav
It's not like perfect.

02:10:51 - Raghav
So I'm kind of surprised.

02:10:53 - Raghav
think something's going to appear fairly soon.

02:10:57 - Raghav
Yeah, definitely.

02:10:58 - Raghav
Yeah, definitely.

02:10:59 - Raghav
I think.

02:10:59 - Raghav
I think.

02:11:00 - Raghav
I think at least my best thing is deploying on the cloud with this new Codex tool.

02:11:07 - Raghav
So I'll have to keep the team updated on that one.

02:11:12 - Raghav
Yeah, that sounds great.

02:11:13 - Raghav
I miss Al.

02:11:14 - Raghav
I miss Al.

02:11:15 - Raghav
I'm not sure if you guys remember Al, but he would always call us team.

02:11:18 - Raghav
And I was just like, oh, man, I love the wording of that.

02:11:21 - Raghav
So you got to let the team know, you know.

02:11:26 - Raghav
Anyways, I'm good, Patrick.

02:11:27 - Raghav
Thank you.

02:11:27 - Raghav
Good.

02:11:30 - Raghav
I think we've went through pretty much everyone.

02:11:33 - Raghav
Anyone who has a last-minute comment, question?

02:11:37 - Raghav
Oh, Raghav.

02:11:40 - Raghav
Yeah, Raghav.

02:11:41 - Raghav
Yeah.

02:11:41 - Patrick Chouinard
So I'm still learning this wipe coding or agent coding with Claude.

02:11:48 - Patrick Chouinard
And using some ShipKit templates, I built an app.

02:11:52 - Patrick Chouinard
I don't know whether I will ever be able to sell that.

02:11:57 - Patrick Chouinard
But can I share my screen, please?

02:11:59 - Patrick Chouinard
Yeah.

02:12:02 - Patrick Chouinard
I think I'm not able to share the screen because I mean, something I got installed on Google Bundle, it's not allowing me.

02:12:11 - Raghav
Yeah, that's fine.

02:12:13 - Raghav
But so the question is, do we need to have a knowledge of the deployment, deployment to the cloud?

02:12:23 - Raghav
Like, for example, if I want to, my app is running locally.

02:12:28 - Raghav
Now I want to deploy it on the cloud, maybe in two different environments, one is dev, the other is production.

02:12:36 - Patrick Chouinard
So do I need to have some kind of knowledge about how to deploy, where to deploy, and all that stuff?

02:12:44 - Raghav
Well, yeah.

02:12:45 - Raghav
If cloud can do that.

02:12:47 - Patrick Chouinard
Well, cloud can do it.

02:12:49 - Raghav
It's not a matter of if cloud can do it or not, is that you have to have at least an app knowledge to know where you're deploying, how you're deploying, because you

02:13:00 - Tom Welsh
Claude will automate the job, but you have to know what job you want it to automate.

02:13:06 - Tom Welsh
Okay, right.

02:13:08 - Tom Welsh
So, yeah, to automate, yeah, I have a pretty good understanding of the cloud and all that, but cloud I'm just learning.

02:13:17 - Tom Welsh
So, what kind of instructions or prompts do I need to provide cloud that will automate, like, that will understand easily and then automate deploying.

02:13:31 - Tom Welsh
Where are you deploying?

02:13:33 - Tom Welsh
Are you deploying to Vertex?

02:13:35 - Ty Wells
Are you, is it in Vertex?

02:13:36 - Ty Wells
GCP.

02:13:38 - Ty Wells
Okay, GCP?

02:13:39 - Ty Wells
Yeah.

02:13:40 - Ty Wells
GCP, I believe, is a little bit.

02:13:42 - Ty Wells
Vertex, yes, Vertex, I think, yeah.

02:13:44 - Ty Wells
that's, GCP, I think, yeah, I use Vertex, right?

02:13:52 - Ty Wells
for that matter, even AWS, so, yeah.

02:13:56 - Raghav
Okay, Tom, did you want to say something about

02:14:01 - Raghav
Yeah, was going to ask, what language are developing?

02:14:03 - Raghav
Because that's a precursor.

02:14:05 - Raghav
Looking at things like Vercel, Railway for Python, are you using Docker containers?

02:14:11 - Ty Wells
That kind of stuff.

02:14:13 - Ty Wells
depending on who you're deploying to, it depends how easy it is.

02:14:15 - Ty Wells
Google Cloud Platform's a .

02:14:18 - Ty Wells
Brandon's done multiple videos on it, and it's a nightmare to deploy to.

02:14:22 - Ty Wells
Vercel, GitHub, set your projects up, press go, it's there and done.

02:14:27 - Ty Wells
It's a simple setup and easy to run.

02:14:33 - Raghav
Yeah, I would agree with Tom.

02:14:35 - Raghav
Vercel is probably going to be your easiest bet out of the box.

02:14:39 - Raghav
If you're using something like TypeScript or that.

02:14:42 - Raghav
Yeah, yeah, yeah.

02:14:43 - Raghav
Absolutely.

02:14:44 - Ty Wells
Depending on your tech stack.

02:14:45 - Ty Wells
But if you need serverless stuff, I don't know what your project is, you're going to probably go, I go to Render over Railway, but there are options out there.

02:14:54 - Ty Wells
Okay.

02:14:56 - Ty Wells
So say I decide on the platform, then don't then you As a

02:15:00 - Ty Wells
And do I just say, do the prompt to say, okay, I want to deploy and so-and-so?

02:15:07 - Raghav
Yeah, I mean, you can do that.

02:15:09 - Ty Wells
It'll tell you you need an account and, you know, you can have it install the CLI for cell if you're using cell.

02:15:16 - Ty Wells
And then you can, you know, obviously you can continue to deploy from there, but you can tell it.

02:15:20 - Ty Wells
Tell it what you want done.

02:15:22 - Ty Wells
Let it figure out exactly what needs to happen for you.

02:15:25 - Ty Wells
And you just have to read and follow the instructions.

02:15:28 - Ty Wells
That's all you have to do.

02:15:29 - Ty Wells
Right.

02:15:30 - Ty Wells
So the next step is, while doing this, I also want to have a process where if I want to do that in the future, I just want to be able to run some templates or something like that.

02:15:42 - Patrick Chouinard
Yeah, if you're deploying, that's what I'm saying.

02:15:44 - Patrick Chouinard
So once you, let's see, I want, you would tell you're in Claude, right?

02:15:49 - Patrick Chouinard
Using Claude code.

02:15:50 - Patrick Chouinard
Okay.

02:15:50 - Patrick Chouinard
So just tell me I want to set up for cell CLI so that I can deploy whenever I have a new release.

02:15:57 - Patrick Chouinard
And then every time you're ready to deploy, just say.

02:16:00 - Patrick Chouinard
They deployed to Vercel, right?

02:16:02 - Patrick Chouinard
After you've tested locally or whatever the case is.

02:16:05 - Patrick Chouinard
Okay.

02:16:06 - Patrick Chouinard
So do I develop some kind of skill with that?

02:16:10 - Patrick Chouinard
No, no, just, you don't need a skill.

02:16:12 - Patrick Chouinard
I mean, you could, but because it's a CLI, so it has its own sort of skills inside of it, right?

02:16:19 - Ty Wells
It's a collection, if you will, of skills just through the terminal.

02:16:24 - Ty Wells
So you would want to, you just want to say, install that skill if you're deploying to Vercel, and then all you have to say is deploy to Vercel when you want to push new updates.

02:16:35 - Ty Wells
It'll take care of everything else.

02:16:39 - Ty Wells
The first time you can actually ask Claude, like, guide me step-by-step on what I need to do in order to set up the Vercel environment, because it's, the deploying is when your setup is already done.

02:16:52 - Ty Wells
And you still have to do the setup of the environment, like create the account, create the configuration, create the app, like all of those step has to be done.

02:17:00 - Patrick Chouinard
So ask CloudCode.

02:17:01 - Patrick Chouinard
It will guide you step by step.

02:17:03 - Patrick Chouinard
And it will tell you, oh, this step, do you want me to take care of it?

02:17:06 - Patrick Chouinard
Meaning I know how to do this one.

02:17:09 - Patrick Chouinard
And this step you need to do because it requires generating a token or something like that.

02:17:15 - Patrick Chouinard
So it's going to guide you to how to get the token created.

02:17:18 - Ty Wells
One thing I would add to that is that you'd tell it to check every so often if the CLI version is updated and you have a critical release.

02:17:32 - Ty Wells
Because if it's not updated, they update it multiple times a day, I swear.

02:17:36 - Ty Wells
But if it's not up to date, and that goes for all CLIs, it will, you know, you'd be in a bad spot trying to deploy.

02:17:44 - Ty Wells
And it's, I think CloudCode's gotten a little better about that.

02:17:48 - Ty Wells
But I just add that in there to have it check to make sure the version is the latest one before it deploys.

02:17:54 - Ty Wells
Actually, on that one, I have a update CLI shells.

02:18:02 - Patrick Chouinard
That's really, really basic.

02:18:04 - Ty Wells
doesn't do any miracle.

02:18:05 - Ty Wells
It's just every new CLI tool that I install, I add to that script, and it runs on the cron job every day.

02:18:14 - Morgan Cook
Yeah, I have mine on a trigger word of deploy on a pre-compact.

02:18:21 - Morgan Cook
Sorry, not on a checkpoint.

02:18:23 - Patrick Chouinard
I use a checkpoint system pre-compact, and so it runs that.

02:18:29 - Patrick Chouinard
Same thing.

02:18:30 - Patrick Chouinard
It just runs it at that time rather than on a cron job.

02:18:33 - Patrick Chouinard
yeah, same concept.

02:18:34 - Patrick Chouinard
One thing I want to share before I drop off, sorry, just to say, you know, models hallucinate about 30% of the time, right?

02:18:45 - Ty Wells
I've got a question for the group, whatever the number is.

02:18:49 - Ty Wells
Is hallucination, is hallucinations bad or good?

02:18:54 - Ty Wells
Hallucination is basically a

02:19:00 - Ty Wells
A lack of information in the request.

02:19:05 - Ty Wells
Yeah, yeah.

02:19:06 - Ty Wells
That's what it is.

02:19:08 - Ty Wells
But is it a bad thing or a good thing when the model hallucinates?

02:19:14 - Ty Wells
It's a good thing if you can see it, because that means you can understand that you didn't provide enough context.

02:19:22 - Patrick Chouinard
And that's why all of my prompts always include, if you don't know, say so.

02:19:28 - Patrick Chouinard
Always provide the model a way to achieve its goal without having to hallucinate to get there.

02:19:36 - Patrick Chouinard
Yeah.

02:19:38 - Patrick Chouinard
Just a thought, a concept.

02:19:40 - Patrick Chouinard
I've been running a reverse hallucination process.

02:19:47 - Patrick Chouinard
Okay.

02:19:48 - Ty Wells
So if the model hallucinates, I use that hallucination to teach it to not hallucinate, which means ask more questions.

02:19:59 - Ty Wells
Okay.

02:19:59 - Ty Wells
We'll

02:20:00 - Ty Wells
Whatever you need to take.

02:20:01 - Ty Wells
Rather than giving it a way out.

02:20:02 - Ty Wells
So my way out is for it to basically fix itself, be better about.

02:20:10 - Morgan Cook
And of course, I'm tracking those hallucinations and stuff.

02:20:15 - Tom Welsh
So it's a good thing for me.

02:20:17 - Tom Welsh
Yeah, it is.

02:20:18 - Tom Welsh
The danger is there is so many ways it could hallucinate that you're going to teach it forever and you're not affecting the weight of the model.

