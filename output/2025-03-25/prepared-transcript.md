=== SESSION ===
date: Not explicitly stated (references to "last Thursday" and upcoming events suggest mid-week session, circa March/April 2025)
duration_estimate: ~82 minutes
main_themes: Member project updates, Gemini 2.5 Pro release, graph databases and RAG, AI tooling for content/legal/audio workflows, AWS Bedrock Flows, NVIDIA Digits supercomputer, job search progress

---

<!--SEGMENT
topic: Session Open and Member Introductions
speakers: Tom Welsh, Paul Miller, Brandon Hancock, Mitch, Andrew Nanton
keywords: community call, Alex Hormozi, content creation, AWS Bedrock, GCP Gemini, N8N, agentic applications, developer tools, full-stack, tutorials
summary: The session opens with casual check-ins and Brandon Hancock announces his transition from full-time employment to full-time content creation starting the following week. He outlines plans to produce tutorials on real-world AI agentic applications using AWS Bedrock and GCP Gemini, noting that N8N is popular for personal automation but full developer tools are needed for building apps for others.
-->

00:00:00 - Tom Welsh
Going?

00:00:01 - Tom Welsh
I think I turned up last Thursday. I'd been a bit under the weather having been in London for the evening. I think I turned on, signed in, and promptly fell asleep.

00:00:10 - Paul Miller
Yeah. I feel good at night your time. My brain just doesn't work for this kind of stuff at that time of night. So I'm lucky.

00:00:18 - Tom Welsh
It's 11 o'clock in the morning my time, so perfect. Well, it's 10 a.m. now, which is great.

00:00:27 - Brandon Hancock
Hey, Brandon. Hello, everybody.

00:00:35 - Mitch
Hello.

00:00:35 - Brandon Hancock
I love that you wore the acquisition hat. Mine's somewhere upstairs. I have to go find it at some point.

00:00:43 - Mitch
Got to be a marketing shill, you know?

00:00:45 - Brandon Hancock
Got to say you're part of the cult. For those who don't know, whenever Alex Hormozi [tool:Alex Hormozi book launch] did his huge book launch, if you bought three books, you got a hat. So he got me. I wanted a hat so bad.

00:01:01 - Paul Miller
I bought the books.

00:01:07 - Brandon Hancock
Yeah, no crazy updates on my side, guys. Basically, I think everyone here knows — last week at full-time job, and then starting next week, all in on content creation. I have so many things I cannot wait to cover. I want to do so many real-world AI agentic applications for you guys, starting with AWS on their Bedrock [tool:AWS Bedrock], GCP [tool:Google Cloud Platform] when it comes to all their Gemini [tool:Gemini] stuff. There's just so many things that I don't think are getting talked about in the developer community or getting enough attention as they deserve. Because obviously everyone's doing N8N [tool:N8N] automations right now, which is awesome for automating your own stuff. But the second you want to build an app for other people as well, you kind of need to start to lean back on full developer tools. So yeah, very excited to start diving in and cranking out a bunch of tutorials for you guys.

---

<!--SEGMENT
topic: Andrew and Maxim Mexico Meetup; Car Dealership AI App
speakers: Andrew Nanton, Brandon Hancock
keywords: expert witness AI, Cloudflare Workers, WhatsApp, authentication, voice agents, LATAM dealerships, scaling, 30k users, Mexico, in-person meetup
summary: Andrew Nanton joins from Mexico where he has met up in person with community member Maxim and his colleague Emilio. Andrew reports that the expert witness AI application has been deployed securely. Maxim's team shares that their car dealership AI app for salespeople is scaling to 3,500 users and will expand to all LATAM dealerships in April, targeting 30,000 users, with voice agents for customer support as the next development phase.
-->

00:02:27 - Andrew Nanton
Great. Well, so I went for a little change of scenery here.

00:02:38 - Brandon Hancock
Where are we at? Was that Maxim?

00:02:39 - Tom Welsh
It was Maxim.

00:02:55 - Brandon Hancock
I love that you guys are hanging out in real life. That is so cool.

00:03:01 - Andrew Nanton
Yeah. So we were taking a trip to Mexico, me and the family. And as Maxim was here, he graciously agreed to come down from Mexico City and say hello. He says we're not allowed to leave until someone's pregnant or in jail.

00:04:52 - Andrew Nanton
So, Maxim got the code pushed for the first version of the expert witness AI [tool:Expert Witness AI] stuff. So I'm taking a look at that. Hopefully some updates on that soon.

00:05:12 - Andrew Nanton
Finally the version is deployed. So the expert witness is deployed. It's all secure. I'm pretty confident in this. And I'm amazed at how much time it took me to do it. But it's finally done.

00:05:39 - Andrew Nanton
So basically what we are doing is right now we are scaling. We are deploying this app for the dealerships for the salespeople, and we are reaching to 3,500 people, and in April, we are going to be launching it to all LATAM dealerships. So we are going to go to more users. It's going to arrive, I believe, until 30k users, something like this.

00:06:23 - Andrew Nanton
We also have been working on authentication for this app that was made with Cloudflare Workers [tool:Cloudflare Workers]. We were using that over WhatsApp [tool:WhatsApp], and we rolled our own auth for the users, for the salespeople, and we also have been working on that. That's already rolled out.

00:06:42 - Andrew Nanton
And we are also going to be working on some voice agents for customer support. So that's the next step we are also going to be working on. So yeah, that's a quick recap.

00:07:00 - Brandon Hancock
▶ Please keep me posted. Yeah, I would love as y'all dive into more scaling stuff, if there's anything I can help with — same with the voice stuff. If there's anything I can help with, please let me know.

---

<!--SEGMENT
topic: Gemini 2.5 Pro Release and Google AI Strategy
speakers: Paul Miller, Brandon Hancock
keywords: Gemini 2.5 Pro, Google, NotebookLM, graph database, knowledge graph, RAG, API access, one million context window, deep research, Google search, LLM, AI investment
summary: Paul Miller highlights the overnight release of Gemini 2.5 Pro, noting its one-million-token context window, API access, and strong document analysis capabilities as a significant upgrade over NotebookLM. Brandon and Paul discuss why Google's underlying knowledge graph gives its search-augmented LLM a structural advantage, and both express long-term confidence in Google's AI position relative to Microsoft and OpenAI.
-->

00:11:51 - Paul Miller
One of the things — and I'm sure you guys have probably seen it — Google released the Gemini 2.5 Pro [tool:Gemini 2.5 Pro] model, which is really, really good. It's good for development. It's got the one million context initially, and it's going to go to two million soon. And it's got API access, which unlike — so they've got their deep research [tool:Google Deep Research], which is quite good. But given it's API accessible, we've been doing some great things overnight where just in the Google chat mode, you can upload multiple large documents or code libraries with high context. And it can do analysis on that.

00:12:51 - Paul Miller
And it can do that thing where, with NotebookLM [tool:NotebookLM], you can get it to create an audio description about what it sees. It can do that as well from the chat mode. You don't even have to do it from NotebookLM. So that's amazing.

00:13:12 - Paul Miller
So for the use case that I've got with looking at politics, I can upload a whole lot of political documents, and we've done that overnight. And it's analyzed that and it's put it in a format that summarizes it really well. So it's a really, really good model.

00:13:32 - Brandon Hancock
<Q>What are they currently pricing it at?</Q>

00:13:35 - Paul Miller
<A>They haven't announced any pricing on it. So it's really just come out. So in an experimental version, it is restricted in terms of API access. But it's really good. If you want to try — I'd suggest people copy and paste it into what you've been doing previously.</A>

00:14:18 - Paul Miller
▶ If you go gemini.google.com [link:gemini.google.com], it comes up. You have to sign up to it, but it's free. And then you can just go from there. But select the Gemini Advanced in the corner.

00:14:34 - Brandon Hancock
Yeah, I haven't — I generally think in the AI race, I think Google long term is actually who I'm betting on. If I had to put a guess out there, strictly just because Google is where work gets done, in my opinion, with Google Sheets, Google Docs. I think Google is just going to dominate long term, especially because with access to the internet. Microsoft is more local on people's computers, whereas Google's more internet-based. So I'm scooping up Google stock.

00:15:10 - Paul Miller
Well, I think you're right on the Google search. One of the YouTube videos I watched in the last week talked about why is Google good at Google search? And why is that search better than other people's search added to LLM? The basics of Google search is that it's based on an advanced graph database that links all of the intuition of the knowledge entities of the internet. And if you combine that graph and the understanding of research, and then you tie that into the LLM, the outcome is pretty amazing.

00:16:00 - Paul Miller
Their issue is — NotebookLM is kind of okay, but maybe if you use the Gemini model but tie it into some other way of doing RAG [tool:RAG], but tie it into Gemini, that might be a better way to go in terms of building better knowledge apps.

00:16:21 - Paul Miller
But I'm stepping away from the code side for a little time and jumping into N8N so I can sort of step back and say, well, here's what I'm trying to do at a high level. I'll go back into coding it once I can do faster proof of concepts because everyone seems to be doing N8N, as you were saying before.

---

<!--SEGMENT
topic: Graph Databases and Neo4j Learning
speakers: Paul Miller, Brandon Hancock
keywords: Neo4j, graph database, relational database, document database, graph RAG, knowledge graph, proof of concept, N8N, Aaron
summary: Paul Miller discusses his progress learning graph databases, specifically Neo4j, noting that while he understands relational and document databases well, graph databases require a different mental model he is still developing. Brandon encourages Paul to connect with community member Aaron, who is actively building with graph RAG, once Paul has mapped out his approach.
-->

00:16:41 - Brandon Hancock
<Q>Any updates on the graph RAG side of things out of curiosity, Paul?</Q>

00:16:45 - Paul Miller
<A>No, no. I built a little proof of concept. I'm doing a course on, just to get myself familiar with Neo4j [tool:Neo4j]. I'm a relational database guy. I've gone document databases, and I kind of get that completely. But graph databases, while I get what they do, I don't understand how they do it, and I need to get my head around that whole thing. So I'm trying to educate myself before getting into building.</A>

00:17:28 - Brandon Hancock
▶ Yeah, please keep me posted, especially if you start to map some stuff out — would love for you and Aaron to have a follow-up call at some point, because I know he's actively diving into it. And on last week's call, he was like half brain dead from not sleeping for like 24 hours. So when he's 100%, I'd love for you two to connect up together.

00:17:54 - Paul Miller
Yeah, no, we've talked about it, and I think he's the man in terms of understanding where he's at. That'd be really great to work with him on that.

---

<!--SEGMENT
topic: GitHub Pages, Developer Tooling, and Learning Path
speakers: Mitch, Brandon Hancock, Tom Welsh
keywords: GitHub Pages, static site, HTML, CSS, JavaScript, Vercel, Next.js, Python, Docker, Linux, Git, deployment, Jest, Cursor, functional tests
summary: Mitch asks about GitHub-hosted URLs he has seen on repositories, which Brandon and Tom clarify is GitHub Pages — a feature allowing static HTML/CSS/JavaScript sites to be published directly from a repo at a username.github.io URL. The conversation broadens to Mitch's learning path through Linux commands, Git, and Python, with Brandon offering to help map a focused roadmap toward a specific app goal.
-->

00:08:18 - Brandon Hancock
Mitch, you are up first, man. So what's been going on? Cool projects?

00:08:23 - Mitch
I know I've given you homework for other stuff. Yeah, I'm doing that currently. And then I spent some time just learning all the Linux commands. So that was fun. Now it's just to learn Git. I obviously know how to use some of the basics, but just really want to make sure I dive in and learn all the different toolings.

00:08:47 - Mitch
One of the things I was just like, really, I didn't know you could do this — like, run, like, post the code, right? And then you can have like a Git run the kind of code somewhat locally. You can run it through like a URL. I was just a little confused with that. Like, when someone posts like the product or like the SaaS, and then there's some like URL, like sub URL that they link and they like host it through GitHub.

00:09:19 - Brandon Hancock
Yeah, send me a screenshot. I'd be happy to clear that up. But I'm curious if they're deploying it like through Vercel [tool:Vercel]. Like, is this a Next.js [tool:Next.js] application?

00:09:06 - Mitch
GitHub Pages?

00:09:08 - Tom Welsh
Yeah.

00:09:19 - Brandon Hancock
<A>Yeah, basically, in GitHub, you can actually turn your code into a website. Like, you can actually publish a website through GitHub. Yeah, basically, what you can do is you can deploy a repo, and then you can basically say "publish as website." And that's literally what they're doing. It ends up using your name. ▶ If you're making a support page or a very quick overview — very simple static HTML, CSS, JavaScript — you can actually do it through GitHub Pages [tool:GitHub Pages], which is wild that they let you do that. Your username is where you can deploy the website to. So like Mitch.github.io is where you deploy your site.</A>

00:19:50 - Mitch
Yeah, same. I got a lot of stuff. So I was just like, well, I need to actually learn how to deploy this because I don't really want to just say, hey, run this Python. And it's like, OK, well, first, you need to download Python. And then I'm just like, OK, let me just give it in a way like everyone really likes Google Sheets in the Amazon space. So it might have to be a bit more of the Apps Script [tool:Google Apps Script] side of things, but I kind of don't want to do that at the same time.

00:21:00 - Brandon Hancock
Yeah, Mitch. I know last time you said you were diving in deeper into more Python-style stuff to just dive deeper into development and everything. So seriously, if there's certain — if you want to point me to, hey, here's the app I'm trying to build, I'd be happy to show — actually cut out all this. You need to learn this thing in Docker [tool:Docker]. You need to learn these few things in Python and would be happy to cut the journey shorter for you. So yeah, just if there's any app in particular you're looking at, let me know. ▶ I'd be happy to paint your roadmap.

---

<!--SEGMENT
topic: Tom Welsh Client Work, Jest Testing, and Upcoming Presentations
speakers: Tom Welsh, Brandon Hancock
keywords: Jest, Cursor, functional tests, Next.js, CVE, GitHub, AI in construction, M&A presentation, IT asset management, context window, prompting
summary: Tom Welsh describes frustrations with a disorganized IT client and shares that he spent eight hours learning Jest to write functional tests for a CVE-related video, ultimately using Cursor to generate the tests. He notes that Cursor's context window held up through four-plus hours of continuous prompting without degradation. Tom also mentions an upcoming M&A presentation and a college invitation to speak on AI in construction.
-->

00:21:39 - Brandon Hancock
All right. We are going to hop over to Tom next. What's going on in your world, Tom?

00:21:52 - Tom Welsh
Nothing overly exciting. I mean, at this client site, just doing — I work with an IT team that's — we'll have a bunch of Muppets, and their answer to everything is, that's not my problem, that's somebody else's. I've got a project manager that can't manage projects. I went to a site today to do some stuff, and I walked in and go, like, where is everything? There wasn't a single thing on site. Two hours to get there.

00:22:23 - Tom Welsh
So I'm trying to speak with IT directors to try and get the information database that we've got pulled into a RAG or some description, because they've got a whole bunch of asset tags. They have no idea where they are. Like, it'd be great — the guy who's written his own asset management database instead of buying one. This is the IT director. He spent two years of his life writing an asset management database. He's like, what, 100 grand a year, and you can buy, like, HP off the shelf for 50K. Just stupid stuff like that I'm dealing with.

00:23:03 - Tom Welsh
But apart from that, yeah. I've got one contract. I've got four or five clients and the big client. So yeah, I've got my six things going on. And then I did my little video at the weekend about that CVE just to get stuff going. So I taught myself Jest [tool:Jest].

00:23:22 - Tom Welsh
I wrote up in Bastian's post about how you should go through doing an upgrade — make sure you've got backup your code in GitHub, run your functional tests, blah, blah, blah. Well, I never had any functional tests. So I thought, well, I better go get some functional tests just so I'm doing it right. So I spent eight hours learning Jest, which was quite entertaining for a seven-minute video in the end.

00:23:48 - Tom Welsh
I mean, yeah, the tests showed up for about a minute. But yeah, apart from that, that's nothing exciting happening. I'm just mopping along.

00:24:00 - Brandon Hancock
And real quick, just for those who haven't got to use — Jest is basically just to help write tests for more of like your websites, like Next.js websites. So it's a very helpful tool. But yeah, did you get Cursor [tool:Cursor] to write all the tests for you once you figured out the basics?

00:24:14 - Tom Welsh
Yeah. Yeah. I like going to test this, test that. I fired up and it comes up with an output at the end, which is where your coverage is. So my coverage was very, very red. So I spent like eight hours basically going through it, making it all work. And then I learned a lot about Cursor. I was going round and round in circles. So I improved my prompting and all that kind of stuff.

00:24:35 - Tom Welsh
But what I found quite interesting was I didn't change my stream for a good four or five hours. I was prompting constantly for about four hours.

00:24:46 - Brandon Hancock
▶ It never ran out of context. Seriously. I mean, it's getting so much better. It's like, as long as you can sit down, stay focused, it is no longer the limit. It's back to us — putting ideas and working fast. This is the new limit.

00:25:01 - Brandon Hancock
One other thing I did want to ask — I know a while ago we talked about you doing a big presentation. Is that still in the cards?

00:25:11 - Tom Welsh
Yes, that's the M&A thing that's coming up in about a week and a half. But I've had a touch from a local college as well if they want me to come and talk about AI and construction, which is quite entertaining. Because I've never worked in construction, so I've got to do a bit of a background on that. I'm an AI guy, not a construction guy.

00:25:47 - Tom Welsh
The presentation is going to be quite intense, I think.

00:25:53 - Brandon Hancock
▶ If you want any second eyes on that, happy to provide feedback or anything, just a look. Love education.

---

<!--SEGMENT
topic: Low-Code POC Tools and Document Processing Workflow
speakers: Sam, Brandon Hancock, Mitch
keywords: low-code, proof of concept, GPT, Vertex AI, N8N, Make, Google Docs, RAG, agentic system, council applications, report writing, API, document automation
summary: Sam asks the group for recommendations on low-code tools to quickly build a proof-of-concept for automating council application report writing, where documents must reference regulations and justify submissions. Brandon recommends Make for simple in-and-out document operations and N8N for more complex agentic, multi-iteration workflows, while Mitch suggests hard-coding a demo response to avoid live API dependency during presentations.
-->

00:26:08 - Sam
Man, felt like yesterday we had the last call.

00:26:24 - Sam
The only thing I was thinking of is, does anyone — or what do people use for doing sort of low-code POCs? Because I'm pretty familiar with GPT [tool:ChatGPT] and their kind of customizable stuff, and there's a few other things out there. I've never really used Vertex AI [tool:Vertex AI] or anything like that, but <Q>is there any preferences people go to just to smash something out to wow a noob?</Q>

00:26:56 - Brandon Hancock
<Q>So, out of curiosity, what are you trying to spin up?</Q>

00:27:02 - Sam
<A>Well, it's basically just report writing for someone. So they have these sort of applications they submit to the council to do things. And you kind of pull from some documentation to kind of justify it and meet regulations. So I feel like there's some cheat ways you can do with the kind of pre-built reg stuff. But outside of GPT setup, I'm not really sure who else, because I'm always keen to try new things.</A>

00:27:37 - Brandon Hancock
<A>So real quick, if you're just trying to take in a document, throw it over to AI, give some checks, and then maybe tweak certain things — Make [tool:Make] is very straightforward just for in-and-out operations. But if you're going to want to have some sort of more persistent memory or more — you're kind of going to have to go in N8N if you want to go down that route. ▶ For just very simple, straightforward applications — like, I'm going to pull from Google Docs, I'm going to make sure it meets these criteria, I will update this, and I will write it back, or I'll copy the document, add my new changes, and add it to a new folder — Make is super easy for that. But you could do the exact same thing with N8N, and it gives you the ability to add in more. So if you wanted to have an actual agent to take multiple iterations on it, yeah, you're pretty much going to have to go N8N.</A>

00:28:49 - Brandon Hancock
Hey, I'd be curious to see a demo once you get it all set up and working. I love one of my favorite things on Earth — it's going from, huh, I have an idea, to a day later, oh my God, I did it. I have superpowers.

---

<!--SEGMENT
topic: Scott's Open Web UI Content Platform Build
speakers: Scott Graham, Brandon Hancock
keywords: Open Web UI, virtual private server, full-stack marketing app, script writing, AI filmmaking, workflows, content creation, infrastructure, students
summary: Scott Graham returns after recovering from a hurricane and shares that he is building a private content creation platform by combining Brandon's full-stack marketing app structure with Open Web UI on a virtual private server. The platform is designed for students in his script writing and AI filmmaking program to use their own original content to generate new content, with plans to potentially commercialize it after internal testing.
-->

00:29:24 - Brandon Hancock
Scott, you're up, man. What have you been working on?

00:29:27 - Scott Graham
Long time no see, Brandon.

00:29:36 - Scott Graham
I got hit by a hurricane. That's why I've been gone. I finally recovered from the hurricane, but I've got something hot. So I took the base structure of your full-stack marketing app [tool:Full-Stack Marketing App]. And I'm putting it into a virtual private server sitting next to Open Web UI [tool:Open Web UI] so that we can use our content to create content. We have all our own original content and connect those two things together so that our people can promote their stuff.

00:30:18 - Brandon Hancock
<Q>So out of curiosity, what do you mean on helping people create their own content? Is it like more literary?</Q>

00:30:28 - Scott Graham
<A>We do script writing and AI filmmaking. So we're going to be building workflows on the Open Web UI side that then can go over to a full-stack side and do stuff with it.</A>

00:30:43 - Brandon Hancock
<Q>Are you thinking about being more of a marketplace where people put their stuff and let others get it? Or strictly more internal?</Q>

00:30:52 - Scott Graham
<A>Eventually. Not school, but it's just for our people. So it's just for us. Maybe eventually it'll be a commercial tool, but it's just for our students to start because, you know, it's probably going to be rough and we're going to eat it for a while and make it better. But yeah, I'm almost done with the infrastructure and then the basics are there. It works. And now I just got to build it out and wire it all up.</A>

00:31:25 - Scott Graham
I just want to say thanks and thanks to everyone. I don't always say stuff, but everyone's participation always helps me out. Even if I don't say something, you know, I try to give a thumbs up. But when you solve a problem, it solves one for me. So thank you, everybody, for being so transparent and I appreciate it.

00:31:46 - Brandon Hancock
▶ Yeah, Scott, seriously, I'd love to see a demo at some point of it in action.

---

<!--SEGMENT
topic: Juan's Federal Reserve Web Scraping Presentation Prep
speakers: Juan Torres, Brandon Hancock, Mitch, Richard
keywords: Jupyter Notebook, Google Colab, API key, Gemini, LLM, agentic system, Federal Reserve, web scraping, live stream, LinkedIn, YouTube, VentureX, Plotly, linear regression, demo backup
summary: Juan Torres is preparing for a live in-person and virtual presentation the following day demonstrating an AI agent that web scrapes Federal Reserve data and performs data visualization with linear regression. The group debates the best approach for audience participation — whether to have attendees create their own API keys, hard-code a demo response, or rely on Juan's cloud-deployed application — with Richard recommending a backup demo in case the live API call fails.
-->

00:32:18 - Brandon Hancock
Next up, we got Juan. What's been going on, man?

00:32:25 - Juan Torres
Just prepared for the presentation tomorrow.

00:32:29 - Brandon Hancock
Nervous? Excited?

00:32:31 - Juan Torres
Now I'm nervous. Like last week, I wasn't nervous, but now I'm like — You were cool as a cucumber last week.

00:32:42 - Brandon Hancock
<Q>So is there people already on a wait list or how is this going down?</Q>

00:32:53 - Juan Torres
<A>Through LinkedIn, but for the LinkedIn link, they're going to be able to go into my YouTube stream. And then for the meetup, you have to RSVP to get into the VentureX building. But I think it's just going to be a combination between both virtual and in-person. So everything's set up. Hopefully the internet is going to be good enough to maintain and sustain the live stream. Hopefully that's going to be the case because we're going to be web scraping the Federal Reserve [tool:Federal Reserve data] live. So that's going to be a lot of computers trying to do it at the same time.</A>

00:33:37 - Brandon Hancock
<Q>So out of curiosity — I know last week we talked about finding a free model for everyone. Were you able to test it out with Gemini and I? Were things working well?</Q>

00:33:48 - Juan Torres
<A>I haven't had the chance to do so. I can actually look it up today and see if it's a viable option to share with everybody else. But yeah, they just have to have an API key in their .env file, so everybody can just upload it.</A>

00:34:19 - Brandon Hancock
▶ The thing I was going to suggest is, if it is quick for them to make their own key in like five minutes, that would probably be the best, strictly because they'll have something to use afterwards, and if you were to do it yourself, you're definitely going to hit token rate limits — like, hey, you can only make 10 requests per second, and you just made like 80. So we definitely recommend, if possible, just, like, here's two slides to get your own API key for this.

00:34:47 - Juan Torres
I guess I could do that. The only thing I worry about is that in the process of having to spend the five minutes, a lot of people are going to be left behind, and it's going to be a little bit complex because it's going to be kind of in a fast-paced environment, and that's going to be delaying the process of finishing the presentation and then the workshop in the time span of an hour and a half.

00:35:50 - Brandon Hancock
Mitch, do you have an idea for them?

00:35:54 - Mitch
I tend to fall into this aspect of, like, it needs to be done right. But this is for like a presentation. I might just hard-code in the API result instead of actually just doing an API call. And then if they wanted to actually do an API call, then you could just do that. But I would just hard-code the response. And so it would show an example.

00:36:25 - Juan Torres
You mean like have already the visualization of what the AI agent would carry out normally without the API key?

00:36:35 - Mitch
Yeah. Or just take the response of like what Gemini [tool:Gemini] would say, for example, and then you could just say, demo Gemini response. And then that'd be the example. So you don't actually have to call the API. You would just say, here was a response that I got. And then just duplicate the workbook if you need to say, hey, if you want to duplicate this yourself, here's the more advanced version.

00:37:01 - Juan Torres
I could do that. The only thing is that I already have a component in which we visualize data and create a linear regression model. So the aspect of visualizing data, not through AI, but rather through just coding mechanisms or using Plotly [tool:Plotly]. And at the same time, I'm going to be actually presenting how I'm going to do it myself on my screen. So I don't want to give them a false aspect of agency — I actually want them to carry out the code themselves with an agentic system.

00:37:59 - Richard
<Q>Yeah, I was going to say, you should probably do that anyway while sticking with your first plan, just in case it doesn't work, because that's how demos are.</Q> <A>So just having that as a backup is probably a good idea, just in case it doesn't work live for you. It may be down, a lot of people might be using it. So just food for thought, you might want to still kind of have that as a backup at the very least.</A>

00:38:26 - Juan Torres
Yeah, yeah. No, that's a great suggestion. Actually, I have my AI agent on the cloud on an application. I can actually share this on the chat. And the demonstration itself is going to be represented dynamically through my cloud-based application. So I'm not really worried about a backup option for being able to demonstrate agentic systems doing the work, but rather the question is, how do we get the audience to feel, quote unquote, empowered on the ability to actually execute code directly on the Colab [tool:Google Colab] notebook without having the fantasy of actually doing it?

---

<!--SEGMENT
topic: Cyril's Job Search Progress
speakers: Cyril I, Brandon Hancock
keywords: Alphasize, Elementor, Wine Owners, Bet365, Resolva, job interviews, technical assessment, coding challenge, Ukraine, AI developer roles, multiple offers
summary: Cyril reports completing his fourth and final interview with Alphasize, receiving positive feedback from all three interviewers. He is simultaneously progressing through interview pipelines at five other companies including Elementor, Wine Owners, Bet365, and Resolva, having passed technical assessments and face-to-face rounds at multiple firms. Brandon encourages him to leverage competing offers for negotiation leverage.
-->

00:39:45 - Brandon Hancock
All right. Cyril, you're up next, Mr. One Million Jobs. What's going on?

00:39:54 - Cyril I
I've actually had my final interview for a company called Alphasize [tool:Alphasize] tonight, so it went, and it actually went pretty well because it wasn't neither technical or like face-to-face in Vietnam — quite unusual, because there was a technical manager, there was a company manager, and there was just a hiring agent, and I just had like one hour conversations with all three of them, and it was great. Well, once again they just asked me the same questions over and over again, told me a bit more about the company. To be fair they talked a bit deeper with me about my previous projects, which I spoke to them about, and all of them said, wow, it is really, really impressive, the fact that he was able to do it within the amount of time that he had spent on them, and the fact that I can be part of their company just excites them very much. So they told me that they gave feedback about the interview by the end of this week, but fingers crossed I will be able to get it.

00:41:02 - Brandon Hancock
<Q>So how many interviews for this one company are we at?</Q>

00:41:05 - Cyril I
<A>I think it's fourth.</A>

00:41:08 - Brandon Hancock
Fourth? Okay, I gotcha. I hate how many interviews they make you do. Like three, in my opinion, like max.

00:41:38 - Cyril I
As it has been said, I'm job shopping rather than me trying to play for jobs. So yeah. So one is Elementor [tool:Elementor], which is a local company in York. Second one is Alphasize, which is this company. Third one is Wine Owners, and I'm already on the third stage where I completed technical assessment, and they're just going to get back to me. But they gave me an advantage in the end, and it said that I outperformed 8% of applicants.

00:42:56 - Cyril I
The fourth one is Bet365 [tool:Bet365]. The fifth one is Resolva, just another company. The sixth one is Up to Half, and the second one is another local company in Leeds. So yeah, I have quite a few that I was able to pass questions and once again face-to-face interviews due to the guide that you have provided. So yeah, hopefully I will be able to get at least one of them.

00:43:26 - Brandon Hancock
▶ It sounds like very soon you're going to have multiple offers, and I think that's going to be very cool — like, well, if you want me, they also want me. So can you go up a little bit? That's going to be a very exciting spot to be in very soon.

00:44:00 - Brandon Hancock
▶ And finally, seriously, if it comes down to any — once you get some final offers, if you want anyone to review it or anything like that, happy to look at it for you.

---

<!--SEGMENT
topic: Audiobook Generation with FFMPEG and ElevenLabs
speakers: Richard, Brandon Hancock, Bastian Venegas, Mitch, Scott Graham
keywords: FFMPEG, ElevenLabs, OpenAI text-to-speech, Sesame, audio stitching, multi-voice audiobook, Python, MP3, narrator, voice cloning, Whisper, speech-to-text
summary: Richard asks whether FFMPEG can handle audio manipulation (stitching, volume, muting) and proposes building a pipeline that parses a story script by character, generates per-character voice clips using ElevenLabs, and stitches them into a multi-voice audiobook using FFMPEG. Brandon confirms feasibility and suggests adding silence/pause metadata between chapters. Bastian recommends OpenAI's new text-to-speech models as potentially superior to ElevenLabs for multilingual and emotional range, and Scott recommends the Sesame voice tool.
-->

00:44:25 - Richard
Hey, what's going on, man? I've been a little — I was over in Arizona in a snowstorm and the road got closed down and we did a little detour and the detour got closed down and I ended up parking at a brake check area and some guy crashed into the back of my trailer really badly. Yeah, went underneath — yeah, like his whole family in there and stuff. So yeah, just kind of been dealing with that.

00:45:09 - Richard
<Q>Does FFMPEG [tool:FFMPEG] work with audio?</Q>

00:45:28 - Brandon Hancock
<Q>Yeah. What do you mean by work with audio? Like to do what?</Q>

00:45:33 - Richard
<A>Like to mute it, make it louder? Stitch it together.</A>

00:45:39 - Brandon Hancock
<A>Yeah, 100%.</A>

00:45:42 - Richard
Because what I want to do is — I have a friend. He's been writing this story, and he kind of wants to just do a simple voiceover for the book. But the way he writes it is in scenes and stuff like that. So I said, hey, I can clean that text for you using some Python or something like that, right? Where I can just clean up the text with a little script to get like, voiceover scene one, scene two, and all the stuff that goes with him writing the script. And I was like, you know, I can also probably do like a voiceover with ElevenLabs [tool:ElevenLabs]. And I could, you know, obviously just give all the text to ElevenLabs and have it do it. But I was wondering, is it possible to actually have it break up the script with whose voice goes where? And then maybe use like several different voices from ElevenLabs and FFMPEG put everything together in the order in which it's supposed to go. And then you got like a full-fledged audiobook read with different voices, each character having their own voice and narrator having his own voice and stuff like that.

00:47:00 - Brandon Hancock
<A>Yeah. So the answer is 100% it is possible. And FFMPEG, basically what it allows you to do is just combine files. So especially audio files — I'm assuming you're going to get MP3 out of it. And yeah, they 100% allow that. So like, the main thing is, it sounds like what you're going to do is, per script, per speaker, you're going to generate a sound byte. And then you just need to keep up with the order — basically just number all of them in the order that they occur. Then yes, you 100% can use FFMPEG to continually add at the end.</A>

00:47:40 - Brandon Hancock
▶ The only other thing that I think you would probably want to focus on is pauses — because if not, it's just going to be speaker, speaker, speaker, speaker. So you might want to look at doing something with like pauses or like a few seconds of silence between chapters. Like, every time you do a clip, you probably want to add like a meta tag with it — this is a part of a conversation, so obviously keep it choppy, but if it's like chapter two and it's a chapter title, put like a three-second pause before it, just so it sounds like someone's reading you a book, and not just two robots talking.

00:49:36 - Brandon Hancock
Asako basically said she's done something similar for her podcast project, and you could definitely do multiple voices together. And then Bastian also said he would go with OpenAI's new text-to-speech models [tool:OpenAI TTS], you can customize emotions and various parameters further for like pauses and pace.

00:50:05 - Richard
Yeah, I forgot they just came out with that. So that'd be like a good way to play with that. That'd be a great YouTube video.

00:50:32 - Brandon Hancock
And Scott also dropped something else. It's Sesame [tool:Sesame]. It's basically another voice tool. So that's in the chat. So definitely recommend that as well.

00:50:50 - Richard
I think I'm going to try the new OpenAI model because I do want to play with that.

00:51:00 - Richard
I've been working on an SEO agent that posts blogs directly to Shopify [tool:Shopify], and I've kind of did the B-roll agent. Now I'm working on the second agent, and it does blogs. It pulls in internal links from the blogs that exist on my store now, and it places those in the new blogs that it writes, as well as product images that are relevant to the blog itself. And then creates additional images using Flux [tool:Flux], and then it posts it as a draft, and then I approve it if I like it.

---

<!--SEGMENT
topic: Bastian's Legal AI Tool for Insurance Firm
speakers: Bastian Venegas, Brandon Hancock, Richard, Mitch
keywords: ChatGPT Enterprise, GPT-4o Mini, JSON schema, function calling, insurance contracts, PDF parsing, Excel, single-page application, Windsurf, legal AI, law firm, hourly billing, AI adoption
summary: Bastian Venegas describes building a single-page browser application overnight using Windsurf that converts Excel insurance field data into a JSON schema compatible with a law firm's existing ChatGPT Enterprise integration. The firm uses GPT-4o Mini to search insurance policy PDFs but nobody knows how to generate the required JSON filter. Bastian's tool solves this with a drag-and-drop interface, running entirely in the browser for privacy. The group then debates whether lawyers will adopt AI given hourly billing incentives.
-->

00:52:13 - Brandon Hancock
Well, speaking of Bastian, you're up next, man. So how are all the projects going at the same time? What are we working on?

00:52:23 - Bastian Venegas
Yeah. I was just working with a friend of mine who's a lawyer at a big firm that handles various types of insurances, like for big corporations and buildings and stuff like that. So everything from an earthquake, arson, whatever. And they have a bunch of clients. And she told me they actually have an integration with ChatGPT [tool:ChatGPT Enterprise], like the one they provide for enterprises. But almost no one in her company knows how to use it. So, for example, they have a way to search through PDF, like the contracts for every insurance and all the terms, and they have this JSON that acts as a filter that GPT-4o Mini [tool:GPT-4o Mini] can use to dive into these documents. But I'm sure that's severely under-optimized, and the most important thing is nobody knows who to ask — like even the IT guys don't know how to use it.

00:53:30 - Bastian Venegas
So I just was preparing — I built a single-page application in like a web browser to fit a table that they have for every field of the insurances, like the most common ones. And you can put like these Excel files, and this tool will give you back the JSON schema that actually that GPT is trying to ask, and nobody knows how to give it.

00:54:02 - Bastian Venegas
Yeah, I managed to do this from 5 p.m. until now, so she was pretty amazed, and I told her, like, ask your boss, send me an NDA, I don't care, and we can do this and make it work for all of your coworkers.

00:54:18 - Brandon Hancock
Yeah, no, that's wild that they're not using this stuff, and it's also that you're able to spin up things so quickly. I am curious — this is just a question to the group — I don't know how much lawyers will want to adopt AI, like, strictly because of, like, from my understanding, most lawyers are per hour. Like, it's an hourly-based thing. So their incentive directly corresponds to them not using AI and being as efficient as possible. Because, like, if you've been a divorce lawyer, they're upset if you settle the divorce in an hour. But on the big claim ones, obviously, they're just like, hey, we just get a piece of the settlement. So they want things to go as fast as possible. So I'm very curious to see which — it sounds like you're working with the later ones, the claim ones. And I think they would really love to use AI as much as possible because it directly aligns to their incentives.

00:55:24 - Richard
Yeah, hourly is definitely their choice because that's been the model that has kind of gotten them paid. But there's no one making them do that. So I can certainly see them transitioning from hourly to something that is more efficient, like what he's doing, especially if they're going to make more within less time. And there's all types of lawyers, like title lawyers and stuff like that, that will love to use AI because some of those services are like one-off services. So when they do like to make sure that the title is clean, if you're buying real estate and stuff like that, those title searches, they're one-offs, about $250 a pop. And if they do have to spend any time doing it, then obviously they would much rather use AI.

00:56:32 - Mitch
Yeah, I work with a decent amount of lawyers. Personal injury lawyers, they want to minimize the time, right, on the case. So if there's a fixed output, then they're always incentivized to minimize the time. And if it's hourly, they'll just charge via emails or via automated services — they'll always add more or they'll just add another fixed fee. And there's also no negotiation on those hours. They could even just say, thought about you — and the minimum. They'll always have a minimum hour requirement. So even if they spend 10 minutes, it'll be an hour. So it doesn't matter if it's faster or not. Actually, it's better if it's faster because now they can do five minutes, but minimum billable hour is an hour.

00:57:42 - Bastian Venegas
[Screen share demo] So it has this drag and drop for the Excel file. And I did build an example, which you can download from the same page. Everything runs in the browser, so there's no privacy issues. And you get to write like the fields from the Excel file that you want — the name of the field, the description, the search standout that the GPT will use, and the name of the filter as a whole. So in this case, everything is just recognized. So then you can preview what the filters will be. And it will assume everything is a string because they haven't optimized and they don't want to process like their whole database. And then you can copy this to the clipboard or just download the JSON schema.

01:00:22 - Bastian Venegas
<A>The output is the JSON schema that these guys will feed their GPT-4o Mini version to parse through their complete insurance policy in a PDF or a table format. It uses function calling [tool:function calling], like to search the text again and again.</A>

01:01:01 - Bastian Venegas
I did it in Windsurf [tool:Windsurf]. It took like two iterations, and that was it. I had a pretty good idea what I wanted, so it just did it for me.

---

<!--SEGMENT
topic: Autogen Multi-Agent Podcast Generation
speakers: asako, Brandon Hancock, Paul Miller, Bastian Venegas
keywords: Autogen, Microsoft, ElevenLabs, multi-agent, agent-to-agent conversation, group chat, podcast, text-to-speech, Japanese language, multilingual, OpenAI TTS, Whisper, Python, Next.js, AWS Bedrock Flows, N8N
summary: Asako shares her work using Microsoft's Autogen framework to generate natural-sounding podcast scripts through agent-to-agent conversation between two named hosts, then converting the output to audio via ElevenLabs. She highlights Autogen's group chat feature for preserving conversational context and agenda-based flow control. She raises a challenge with ElevenLabs' poor Japanese language support, prompting Bastian to recommend OpenAI's new TTS models which show dramatically reduced error rates across all languages. Brandon also shares his discovery of AWS Bedrock Flows as an N8N-style visual workflow builder.
-->

01:01:37 - Brandon Hancock
All right. Asako, you are up next.

01:01:40 - asako
Oh, I didn't expect that. My turn. Thank you, guys. I haven't caught up with Aaron, so I didn't do anything about the project with him this week. But meanwhile, I was working for a podcast project. In the past, I created podcasts using scripts generated by OpenAI [tool:OpenAI], but then Aaron suggested me to use a conversational AI to make it more interactive, so I explored options. And at the beginning, I thought about using ElevenLabs, the conversational AI, but then it turns out that it doesn't support agent-to-agent conversation. So I used Autogen [tool:Autogen] by Microsoft, I believe, which does agent-to-agent conversation by text-based. So I generated scripts using Autogen, and then converted to audio using ElevenLabs, and then it's pretty good. The conversation sounded very natural.

01:03:00 - Brandon Hancock
<Q>How did you like Autogen, out of curiosity? I haven't got to play with it, but I was curious what your thoughts were on it.</Q>

01:03:07 - asako
<A>I think it's pretty good.</A>

01:03:27 - Brandon Hancock
I started digging into Bedrock on their multiple agent stuff. I didn't even know Bedrock had Flows [tool:AWS Bedrock Flows]. Did you know that? Like, you could build an N8N-style workflow in Bedrock. I didn't know that.

01:03:52 - Paul Miller
There's a topic for your YouTube video.

01:04:22 - asako
One of the coolest features Autogen has is a group chat functionality, which preserves the previous conversation within the session. So, like, if there are two — for example, in this project, we have Sakura and Peter as podcast hosts — and by using group chat, you can preserve the conversations between two. So, for example, Sakura said something, and Peter understood what she said, and then responded to what previously she said. So, like, the conversation responds very naturally. And then also you can create an agenda within the system prompt. So, like, if you want to make intro first, and then have them talk about article summary, and then key phrase discussion, then you can define how the conversation should flow, and then you can easily customize what you want them to talk. So, yeah, it's very flexible, and it's very easy to set up.

01:06:00 - Brandon Hancock
<Q>Any, so out of curiosity, going back to the code — so is it strict text-to-text, and then you were passing the article summary in?</Q>

01:06:12 - asako
<A>Yeah, it's text-to-text, and then I pass the article summary to the system prompt, and then have them discuss based on the agenda.</A>

01:07:44 - asako
Yeah, actually, I am struggling with the voice. ElevenLabs doesn't have a good Japanese speaking capability, even with the multilingual agent. So someone brought up Sesame or other voice frameworks. <Q>I'm curious if any of the language models have a better capability for multilingual.</Q>

01:08:15 - Brandon Hancock
<Q>Bastian, real quick on the new OpenAI models — do you know how they're multilingual, like their non-English skills are?</Q>

01:08:23 - Bastian Venegas
<A>I think it's better than the previous generation, like across the board. And I saw them show the data — because they released speech-to-text and text-to-speech models separately, but much faster and at a really good price. And they showed like the rate of error was reduced dramatically, like in every language. And even for the — I believe they released a version, like the one that we're going to release and also a smaller one. And both are better than Whisper [tool:Whisper] in the speech-to-text side. So I would expect this to be their attempt at state-of-the-art for the speech generation as well.</A>

---

<!--SEGMENT
topic: AWS Bedrock vs SageMaker; Amazon and Google AI Platform Strategy
speakers: Brandon Hancock, Paul Miller, Bastian Venegas
keywords: AWS Bedrock, SageMaker, Bedrock Flows, Anthropic, Nova models, fine-tuning, N8N, agent deployment, private network, Google, OpenAI, Microsoft, Langchain, LangGraph, production-ready AI, cloud AI platforms
summary: Brandon shares his discovery of AWS Bedrock Flows as a visual N8N-style agent workflow builder and asks Paul and Bastian for their experiences with Bedrock versus SageMaker. Paul praises Bedrock's security architecture and Nova models but warns that some agent builder features can be expensive. Bastian explains SageMaker is better suited for large-scale fine-tuning projects rather than typical agentic workflows. Paul and Brandon agree that the long-term AI platform race will be Google versus Amazon, with Microsoft/OpenAI losing ground, and Brandon announces plans to dedicate focused content months to each platform.
-->

01:09:41 - Brandon Hancock
Real quick, Bastian, Paul — I have a few questions for you guys when it does come to SageMaker [tool:AWS SageMaker] versus Bedrock. Paul, how much have you got to use Bedrock? Are you liking it, not liking it?

01:09:57 - Paul Miller
<A>Yeah, no, I like it a lot because from a client perspective, you just don't have to think about that security and running things up because its whole architecture is just really good. It's got the Nova models [tool:Amazon Nova] are really good and quite price competitive, depending on what you're doing, but they keep adding other foundation models into the mix. They've got that Chinese model in there, but hosted in the U.S., so it's all good.</A>

01:10:35 - Brandon Hancock
<Q>Have you been able to play with any of their agent builders or anything like that?</Q>

01:10:42 - Paul Miller
<A>No, just got to watch those because their billing approach on that is really expensive. And like many things on AWS, there's cheap stuff in there, but there's also some very expensive stuff where they think it's kind of good, but it's not. But I'm not sure on the billing on Flows — how they do the billing. There's always the gotcha with Amazon.</A>

01:11:09 - Brandon Hancock
I gotcha, yeah, because the way they — let me just show real fast — the UI made, I was very shocked with how well it looked, because it feels like N8N. You have flow inputs, you can then throw in either agents, prompts, or just straight up code. Then you could work with knowledge bases. Obviously you're lacking the functionality for easy integrations to third-party services — that's the one thing that's kind of a pain here. But like, I believe you could get around that somehow, like between, you know, just storing your users' keys somewhere. But yeah, at a high level, I thought this was pretty impressive, honestly. And I just didn't even know they had it.

01:12:14 - Paul Miller
Yeah, they've got, with their relationship with Anthropic [tool:Anthropic] — because they have a massive shareholder in Anthropic — so while Microsoft have gone the full OpenAI route, Amazon, I think, is being more strategic, because I don't think OpenAI are really there in terms of great vision. Their stuff is expensive. The models are getting crappier. Like, Amazon, I think the real future game is going to be Google versus Amazon.

01:12:49 - Brandon Hancock
Dude, buying both the stocks? I'm buying both of them. Hand over fist, man.

01:13:00 - Brandon Hancock
Bastian, you said on SageMaker — have you got to, anything that you liked on SageMaker so far?

01:13:08 - Bastian Venegas
<A>I, actually, it's not necessarily something you would use that often. You could get away with Bedrock perfectly because this is — it also has a UI that launched like in August. And I haven't seen that because when I learned something about SageMaker, it was like over a year ago. So they didn't have the UI. They have the SageMaker Studio [tool:SageMaker Studio], which is like an IDE. But the main difference is that you can run fine-tuned models and manage your different servers and functions with more granularity. But if your approach is like an N8N-similar stuff, I think you're pretty far if you go down the SageMaker route. ▶ I think that's for a big company project in production and where you have enough data to fine-tune one of their models. But that's usually not what clients want in this era. So it's not something I would dive super deep in for the current needs of the market.</A>

01:14:34 - Brandon Hancock
I got you. Yeah, I just wanted to dedicate a month strictly to Amazon and another one strictly to Google just because I think that's where it's all going. So I'm just starting to try to get some feelers for what you guys have liked about them so far before diving in to either of them. But yeah, like, it's the part that I think is wild is it really has taken over two years for things to honestly get to where they're production ready. Because up till now it's been like, oh cool, go Langchain [tool:Langchain], but then everyone's like, actually don't go Langchain for production stuff. And then it's like, wait no, they came back with LangGraph [tool:LangGraph] and it's like, well no, it's actually more complicated now. Big boys are coming out with their own tools. So it's just honestly been flip-flop, flip-flop. ▶ So I feel like we're now at a place where Google is starting to really spin their stuff up and AWS has really got to spin their stuff up. And I think mastering the development tools that they're dropping is honestly going to be — if you can master them, the amount of opportunities that will come your way I think are going to be unreal, just because people want to do things on trusted platforms like this.

01:16:31 - Brandon Hancock
Yeah, I mean, so I think what would be interesting, Steve, is from my understanding, you would just spin up a normal app that you would normally do inside of AWS, and then you would just set up some sort of permissions to allow your application to reach and connect to whatever agent or flow you spin up on your VPC and just allow them to talk. So it's still secure, but you're still getting to securely talk to agents. Like that's the kicker. It's like, right now, it is so hard to actually deploy agents in a secure manner. Because like, if you have multiple parties talking together, it's all just done through API requests. But now, with AWS, you could actually kind of keep everything in one private network, which is wild that we're getting to this point.

---

<!--SEGMENT
topic: NVIDIA Digits Personal Supercomputer Discussion
speakers: Richard, Brandon Hancock, Bastian Venegas
keywords: NVIDIA Digits, personal supercomputer, 200 billion parameter model, open-source LLM, Llama 3, NVLink, local inference, home compute, GPU, model fine-tuning, on-premise AI
summary: Richard announces he has reserved an NVIDIA Digits personal supercomputer priced at $3,000, capable of running 200-billion-parameter open-source models locally. The group discusses whether linking two units via NVLink would allow running a 400-billion-parameter model, with Bastian clarifying that while the model would fit across both units, communication latency between chips would reduce inference speed compared to a single unified system. Brandon notes the device would be most cost-justified for long-running projects with constant compute needs.
-->

01:17:04 - Richard
Hey, real quick, man. What about the NVIDIA supercomputer? Anybody reserve it? I reserved mine. It's $3,000. But I mean, 200 billion parameter open-source model running at home on a tiny little supercomputer. I don't know, man. I can't pass it up.

01:17:33 - Brandon Hancock
<Q>What's it called? It's Digits [tool:NVIDIA Digits]?</Q>

01:17:34 - Richard
<A>Yeah, Digits. That was the name of it.</A>

01:17:46 - Brandon Hancock
See, I just — I don't have any long-running projects right now to justify it. But the second I have more long-term projects that are needing constant compute — like, depending on how big the project is and how many people are using it, it 100% could pay for itself. And it's wild that it's just sitting right next to you. And the part that's pretty cool is the amount of training and experimenting you get to do. Like, when I experiment now, I'm like, oof, let's not break the bank. But in your case, like, I'm already all in on this device. Let's do as much as we possibly can.

01:18:33 - Richard
So, yeah, because I was kind of wondering — they had an offer for two of them. And I think you can link them. <Q>And I was going to ask, does that mean that you can run a 400 billion parameter model? Or you would just have two?</Q>

01:18:53 - Bastian Venegas
<A>Yeah, it's faster than Ethernet, but it's not like having them be part of the same system-on-chip. So you will be able to run it and fit it inside. But you will — yeah, the speed will degrade because of the communication — it's a bottleneck. But you will be able to run it and fit it inside. That's the main difference.</A>

01:19:30 - Brandon Hancock
▶ Yeah, you could run — by hooking up two of them — Llama 3 [tool:Llama 3], the 4-billion model, you 100% could do it. But yeah, just like what Bastian's saying, it's probably a little bit slower. But the fact that you can, just at your house.

01:20:18 - Richard
I've reserved it. So it's not for sale yet. They send the email to reserve it and then it was like 200 people in line ahead of me. I had to wait to get on the site. So I guess it was kind of like crashing the site as well. So yeah, there was a wait line, and I reserved it. And when it comes out, then I'm going to purchase it and just see about it.

---

<!--SEGMENT
topic: Session Close and Brandon's Content Plans
speakers: Brandon Hancock
keywords: content creation, video schedule, AWS Bedrock, GCP, tutorials, community, weekly polls, full-time creator
summary: Brandon closes the session by announcing he will officially begin full-time content creation the following week, targeting two to three videos per week with a focus on AWS and Google Cloud AI tooling. He plans to introduce weekly community polls to prioritize tutorial topics based on member needs and encourages the group to flag questions and project ideas.
-->

01:21:39 - Brandon Hancock
All right, guys. Any final questions? If not, I'm going to go get an early dinner tonight and I got to hop back to work. But yeah, so pumped. Next time I see you guys, I will be officially unemployed, a freeloader. Taking out, mooching off my wife. So I'll keep you guys posted. Starting next week, I'm really ratcheting up the content schedule, shooting ideally starting at two and then going to start going up to three videos a week. There's just so much to explore. I feel so bad — I've fallen behind for you guys. So we'll definitely be spinning things up and I will start to do a lot more weekly polls like, hey, what do you want to see about this week? So, yeah, please be on the lookout for that just because if you have questions on stuff, I want to go off and make sure, you know, break everything down into nice videos for you guys. So, yeah, I'm excited. I'll keep you guys posted and I hope you guys have a great rest of your week. See you guys. Bye.

---

=== UNRESOLVED SPEAKERS ===

The following speakers appeared in the transcript but were not present in the SPEAKER_ALIASES context block (which was not supplied):

- **Mitch** — last name unknown; passed through unchanged
- **Sam** — last name unknown; passed through unchanged
- **Richard** — last name unknown; passed through unchanged
- **asako** — last name unknown; passed through unchanged
- **Cyril I** — partial name; passed through unchanged
- **Steve** — referenced by Brandon at 01:16:01 but never formally introduced; may be a chat participant