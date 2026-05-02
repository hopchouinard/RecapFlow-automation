=== SESSION ===
date: Not explicitly stated (references Apple event "today," iPhone 16 AI features, recent AWS/GitHub spec-based building announcements)
duration_estimate: ~2 hours 15 minutes
main_themes: ShipKit RAG template demo and development update, member project showcases (RPA agent, AWS GPU infrastructure, restaurant ordering app, 3D product scanning, school logistics app), AI tooling discussions (ADK, Cursor, Gemini CLI, MCP servers, embedding models), community knowledge-sharing on prompting for non-technical audiences, B2B lead generation workflows

---

<!--SEGMENT
topic: Pre-meeting Chatter and Introductions
speakers: Andrew Nanton, Marc Juretus, Paul Miller, Tom Welsh, Juan Torres, Sam, Brandon Hancock
keywords: expert witness, Oregon, introductions, mainly music, architect, demo preparation, ShipKit, sprint, community call structure
summary: Participants exchange informal greetings before the formal session begins. Andrew Nanton mentions ongoing expert witness cases and an upcoming lecture. Brandon Hancock announces he has been sprinting to prepare a demo and sets expectations for the call format: questions first, then round-robin updates.
-->

00:00:00 - Andrew Nanton
I have a couple different expert witness cases going on, and then a lecture that I'm giving at the end of the month.

00:00:13 - Marc Juretus
Nice.

00:00:37 - Marc Juretus
What area are you located in?

00:00:40 - Andrew Nanton
I'm in Oregon.

00:00:44 - Marc Juretus
You ever been to an Oregon game?

00:00:46 - Marc Juretus
No, I haven't.

00:00:49 - Marc Juretus
I need to.

00:02:32 - Paul Miller
Hey, Tom. Good to see you.

00:02:35 - Paul Miller
Hey, Paul. How's it going?

00:02:37 - Paul Miller
Good, good.

00:04:00 - Paul Miller
You've been to mainly music again, Sam, this week?

00:04:05 - Paul Miller
Not this week, no.

00:04:09 - Paul Miller
Find yourself another architect?

00:04:11 - Sam
Yeah, yeah.

00:04:14 - Paul Miller
Find a backing developer and then put myself completely out of the job.

00:04:22 - Brandon Hancock
Guys, I have been sprinting all day to get a demo ready. I needed more time. But I'll still at least show the direction things are going just because I still think it's pretty cool. Just need more time in the day.

---

<!--SEGMENT
topic: ShipKit RAG Template Demo
speakers: Brandon Hancock, Jake Maymar, Hemal Shah
keywords: ShipKit, RAG template, vector store, Google Cloud, document processing, AI course platform, roadmap, phase-based development, OpenAI Assistants, GitHub repository
summary: Brandon Hancock demos the ShipKit RAG template, showing document upload, Google Cloud-based processing instances, and a real-world conversion of the template into an AI-powered course platform. He explains the phase-based roadmap system and invites community contributions. Jake Maymar suggests the community could contribute RAG evaluation workflows as a differentiator.
-->

00:04:56 - Brandon Hancock
All right, guys. We'll do a quick demo. So the thing I've been working on wrapping up is the RAG template. The RAG template's good, but one of the things that I'm trying to do in ShipKit [tool:ShipKit] is showcase how you can take each template and turn it into a real-world app.

00:05:32 - Brandon Hancock
Here's the RAG template. You can go in here, you can upload documents. Once it's done uploading, it'll start spinning up instances in Google Cloud [tool:Google Cloud], which are dedicated to monitoring and processing documents. So videos, images, audio files, everything. It has its own processing part so that it can put everything in a vector store so that you can ask questions.

00:06:38 - Brandon Hancock
You saw the old project, which was Raggy. That's the base template everyone gets. And then I'm doing a complete walkthrough showing how to use all the prompts, templates, roadmaps, everything set up in ShipKit to go to their own custom app. So this is the second RAG project that's in ShipKit. I'm about 70% through the process.

00:07:01 - Brandon Hancock
What's cool is it actually has a course section. I was using the RAG template to help create an AI course. You can go in here, you can actually build a course like a school. For each section, you can upload videos and play videos.

00:07:35 - Brandon Hancock
▶ This exact tool is actually going to be converted into the actual behind-the-scenes thing for ShipKit. You can actually ask questions about anything in the course. So if you ever get questions about ShipKit when you're in ShipKit, you can ask questions. So — what was said about OpenAI Assistants [tool:OpenAI Assistants]?

00:08:15 - Brandon Hancock
That is literally the RAG template out of the box converted into an AI course platform. And in ShipKit, I'll be showing you guys exactly how to do it.

00:08:48 - Brandon Hancock
The way things are set up is I'm at phase seven. ShipKit generates a roadmap for you to literally help you build out each thing. So I'm at phase seven, which is to make the AI chat. You just use the roadmap to help make tasks, and then you go off and actually build all the functionality.

00:09:17 - Brandon Hancock
The walkthroughs are taking way longer than expected, but I think they're going to be super valuable because you'll get to see me run into errors and how I overcome them.

00:12:44 - Jake Maymar
I was almost thinking maybe as ShipKit matures, you could have us sort of contribute an evals kind of thing, workflow. <Q>Because what's so cool about ShipKit and what I think would be a differentiator is us — we're building all these different things and we could start contributing using your templates. Because RAG, there's a whole bunch of different flavors of RAG.</Q>

00:13:22 - Brandon Hancock
<A>It is a GitHub repository [tool:GitHub]. So you can add issues, you can add features. I am excited for that community aspect of it as soon as it goes live.</A>

---

<!--SEGMENT
topic: AI News Sources and Apple Event Reaction
speakers: Brandon Hancock, Hemal Shah
keywords: Matt Wolfe, Theo, Futurpedia, Lenny's newsletter, Apple Intelligence, iPhone 16, YouTube, AI news, spec-based building, AWS, GitHub Copilot
summary: The group discusses recommended AI news sources including Matt Wolfe and Theo on YouTube. Brandon reacts with mixed feelings to Apple's latest AI feature announcements, expressing disappointment that promised iPhone 16 AI features have not materialized. AWS and GitHub's spec-based building tools are briefly mentioned as directionally aligned with ShipKit's approach.
-->

00:10:47 - Brandon Hancock
Paul, your question cracked me up. AWS [tool:AWS] had their tool that came out a little bit ago that does the spec-based building. And then GitHub [tool:GitHub] also has the spec-based building. I mean, it is the direction to go. That's the way code building should happen — you should create specs and tasks. That's literally what ShipKit does. But the one thing that's different is what they're doing is a general solution for all coding tasks, where this is more AI application based.

00:11:42 - Brandon Hancock
<Q>Hamal, besides Lenny's newsletter [tool:Lenny's Newsletter], are there any other recommendations on AI-related news?</Q>

00:12:04 - Hemal Shah
<A>Yeah, Matt Wolfe, Matthew Wolfe.</A>

00:12:06 - Brandon Hancock
Matt Wolfe [tool:Matt Wolfe YouTube]. Yeah. Both of those are my go-to. And then I also like Theo [tool:Theo YouTube]. That's how I learn about everything. If you're not watching Theo on YouTube, he's phenomenal. He does a video every day, so you're always learning something.

00:13:44 - Brandon Hancock
I don't know if you guys got to watch the Apple thing today. I got bummed because I got the iPhone 16 and I was supposed to have all these AI features. So now I can't trust any time they do a new update. Apple — I kind of got unhyped on today's big reveal for all the new Apple stuff.

---

<!--SEGMENT
topic: David's RPA Agent for Government Website
speakers: David, Brandon Hancock, Juan Torres
keywords: RPA agent, robotic process automation, FMCSA, Unified Registration System, mock environment, human-in-the-loop, Selenium, Google ADK, agent development kit, browser agent, loop agent, context window, trucking industry
summary: David presents a project to build an intelligent robotic process agent that navigates a 75-page government (FMCSA) registration website. He has built a mock Unified Registration System for testing. Brandon recommends using Google ADK with a multi-agent loop architecture — a loop agent for page analysis, a browser agent using Selenium for element identification, and a separate agent for data entry — to avoid context window overflow.
-->

00:14:28 - David
I'm creating an intelligent robotic process agent that walks through a government website to fill out an application. It is approximately 75 pages long. Throughout the application process, there are a couple of different stages where I'll need to do a human-in-the-loop or a handoff where my robotic process agent can allow the client to input — or it's scanning a QR code and taking a picture of themselves.

00:15:24 - David
The challenge is that this is a government website. They don't make coding environments for people like us to go and make things to work with their systems. So I don't truly have an environment to test this in. My thought is that I need to recreate the government's Unified Registration System [tool:FMCSA Unified Registration System] — or a mock of it — so that I can have my agent walk through that.

00:16:22 - David
The part I would like advice on is the human-in-the-loop parts. <Q>Do you guys know how to put that into a testing environment so that my agent can get a realistic feel for exactly what it'll be like to walk through? And my goal is to have the testing environment output what the agent did so that I can score it and train the agent on it.</Q>

00:17:07 - David
They are dynamic. For example, in the trucking industry, if a truck driver's vehicle is rated for a certain amount of pounds, they may or may not be required to do additional regulations dependent upon their operating — whether they leave the state, whether they're hauling hazardous cargo, whether they carry more than 15 passengers.

00:18:00 - Brandon Hancock
<A>So here's what I would do if I was using a tool like Agent Development Kit [tool:Google ADK] — I would create a loop agent that goes through a cycle of reviewing a page, analyzing the questions it's being asked, and coming up with the answers. Once it has the answers, it passes that off to a browser agent who is responsible for inputting that data. That browser agent will continually look at the page, figure out where all the HTML elements are. Once it finds an email input field, it pastes in whatever value is provided.</A>

00:21:15 - Brandon Hancock
▶ I just sent you a video in the chat — there's a really good YouTube video that Google created that shows you how to set up a browser agent. In your case, you're basically going to be using Selenium [tool:Selenium] as a web driver. Your agent is going to control the web driver. Set it up to go in a loop: take a screenshot of the page, come up with the answers, pass answers to the browser agent, and the browser agent will first identify where those inputs are, enter inputs, and submit the page.

00:24:44 - Brandon Hancock
▶ The only thing that is bad about that source code — the browser agent is doing too much in every cycle. That is the only issue because you run out of context. So I suggested doing a loop: browser agent one finds the raw text and the exact ID of the email field, saves that to state, passes it to the next agent, and then agent two is the enter-information agent. You have to break it up because if it all happens in one, you'll quickly hit the context limit and it explodes. Separation of concerns: one agent provides answers, one agent finds elements, a third agent enters information and presses submit.

00:23:36 - Juan Torres
<Q>The browser agent — do you create it through ADK or do you use an external tool?</Q>

00:23:49 - Brandon Hancock
<A>The browser agent is just an agent that has tools to use the browser. Behind the scenes, during agent creation, it will have a Selenium instance of your browser already open where your credentials are already put in. And then it has tools such as scrape page, click button, find element, take screenshot of page. That GitHub repository linked to that YouTube video is a fountain of knowledge.</A>

---

<!--SEGMENT
topic: Tom Welsh Update and Cursor Rules Discussion
speakers: Tom Welsh, Brandon Hancock, Ty Wells
keywords: Cursor, cursor rules, context window, De La Rue, networking, Bolt, Claude Code, Gemini CLI, Codex, AI coding tools, automatic rules, manual rules
summary: Tom Welsh shares a networking win — meeting the chairman of De La Rue (which prints 60% of the world's currency) on a train. Brandon raises an open question about Cursor's automatic vs. manual rules settings and their impact on context window costs. Ty Wells mentions Claude Code, Gemini CLI, and Codex CLIs becoming available in Bolt, prompting discussion about past Bolt hackathon frustrations.
-->

00:25:50 - Brandon Hancock
Tom, you're up next, man.

00:25:59 - Tom Welsh
I've not been doing very much AI recently because I've been moving house. The important day is I'm moving on the 18th, so I'm in the new house for the 20th.

00:26:25 - Tom Welsh
I was chatting to a guy on the train two or three days ago. We got chatting about AI and this, that, and the other. Then he dropped his card on me and it turns out he's the chairman of De La Rue. They print 60% of the world's money.

00:26:55 - Tom Welsh
I've got him lined up for a call tomorrow. So we'll see what comes out of that.

00:27:08 - Brandon Hancock
Your superpower is connecting to people.

00:27:39 - Brandon Hancock
Speaking of Cursor [tool:Cursor] really fast — inside of Cursor, you can update your rules to apply intelligently or apply manually. Where it'll be like, "Oh, you're working on a Python file? I'm automatically going to add these 20–30 rules." <Q>I would be curious as you guys go over the next week — which one do you like better? Because I like having explicitly set rules, but it kind of blows up my context window. My Cursor bill is just very high. But I'm writing quality code. Automatic rules or manually set?</Q>

00:28:43 - Ty Wells
My wallet's hurting too. It keeps warning me I'm running out. <Q>But did you guys see Claude Code [tool:Claude Code], the Gemini CLI [tool:Gemini CLI], and Codex [tool:OpenAI Codex] — they bolted up?</Q>

00:29:05 - Brandon Hancock
I've stayed away from Bolt [tool:Bolt]. Who was it that did a Bolt hackathon and said they'll never do that again?

00:29:16 - Ty Wells
I'm just saying those CLIs are going to be available. I will test it. They'll follow my five-minute test.

00:29:26 - Brandon Hancock
After that hackathon, you seemed like a defeated man for a day after all the headaches. But if you get a chance to try it, please let me know. I'd love to hear if it's worth the investment or not.

---

<!--SEGMENT
topic: Andrew Nanton — Local AI, Toga GUI, and Presenting AI to Non-Technical Audiences
speakers: Andrew Nanton, Brandon Hancock, Patrick Chouinard, Paul Miller
keywords: Toga, local LLM, Claude Code, Context7, Google LangExtract, context window, prompting for non-technical users, AI presentation, master prompt, Copilot, prompt templates
summary: Andrew Nanton recommends the Toga Python GUI library for local development and discusses mixed results with local LLM models, preferring cloud APIs for context window reliability. He asks for advice on presenting AI to a non-technical audience. Patrick Chouinard offers the "intelligent intern with zero context" analogy as an effective onboarding frame. Paul Miller emphasizes starting with the right AI chatbot and building a master prompt for professional context.
-->

00:29:53 - Brandon Hancock
Andrew, you're up next, man. What's going on in Andrewland?

00:29:57 - Andrew Nanton
I have been poking around with some more locally running stuff. And I will share that if you need to do some basic, simple, local GUI stuff, I can strongly recommend Beware Toga [tool:Toga]. I'll put a link in. It's pretty basic, but I found it to be pretty good. It's documented well enough that you can get good results out of an LLM with it.

00:30:43 - Brandon Hancock
<Q>Does Context7 [tool:Context7] have their libraries?</Q>

00:30:48 - Andrew Nanton
<A>Claude Code [tool:Claude Code] was pulling it from somewhere else that I haven't used before.</A>

00:30:56 - Brandon Hancock
Yeah, there looks like it does.

00:31:00 - Andrew Nanton
Playing with a little more local AI — mixed results. I still just really can't justify using too many local models over the relatively low cost. And that Google LangExtract [tool:Google LangExtract] project that I was telling you about before, that continues to be really cool. One of the things I'm hoping to do — I don't need super powerful LLM grunt to make that work, but it does need to work over a reasonable context window size. And that's where local seems to fall over.

00:31:54 - Brandon Hancock
▶ At this point, I'm going to pay the $0.10 up to $1 to just get the thing working with Claude rather than spending two hours getting the local model to correct it a thousand times.

00:32:18 - Andrew Nanton
There's one last thing — I'm giving a pretty long presentation on AI, mostly geared toward a non-technical audience. I've had my head so far in LLM world for so long that sometimes it's hard to remember what it's like to not think of the stuff the way that I do. <Q>If any of you have been working with people who are very unfamiliar with these technologies and have suggestions for topics I should make sure I cover, I would love if you would drop that in the chat.</Q>

00:33:09 - Brandon Hancock
<A>▶ Literally just prompting — using AI to build a template to help you do work. You build a template and the template is your SOP to get work done. If it doesn't produce valuable work, you go back and update the template. My friends that are doing it are using it to help write emails, manage inventory — they're building instruction guides so they can hand it to any employee and say, "Anytime you're working with inventory, I already have this prompt."</A>

00:34:15 - Patrick Chouinard
<A>▶ I really go to the most useful trick I give to people in their first ever training: think of the AI as the most intelligent intern you ever worked with, but that just started work and has zero context. If you bring them inside, what would you tell them if you want them to do something? And the nice thing is that intern has a superpower — if you ask them to tell you what they don't know and need from you, they will. This got me a 55-year-old assistant who never went beyond Word able to use Copilot [tool:Microsoft Copilot] in a decent way.</A>

00:35:43 - Patrick Chouinard
And then you get to models and the templates and all of that.

00:35:56 - Paul Miller
▶ The starting journey must be: how do you make sure that you give the context and prompt — in a professional sense, I want to use the AI to help me do my job better — and getting them to build that master prompt where they define what their job is, what the context of how they're going to use the AI chatbot is. And use the right AI chatbot. I've come across so many people that have said, "Oh, I use AI, and it comes up with stupid answers." Which chatbot are you using? "I'm using the free version of such and such."

00:38:34 - Andrew Nanton
▶ Maybe the most important rule of thumb for me is: if you put a lot into it and you expect to get a little bit back, you're probably in good shape. If you put a little bit into it and you expect to get a lot out, you're probably going to have a bad time.

---

<!--SEGMENT
topic: Hemal Shah — ADK Data Reconciliation and Gemini Pricing
speakers: Hemal Shah, Brandon Hancock, Tom Welsh
keywords: Google ADK, ADK Web, Gemini Flash 2.5, LiteLLM, ChatGPT-4o Mini, GCP billing, budget alerts, file attachments, vector store, state management, token cost, context window
summary: Hemal Shah shares progress on a data reconciliation project using Google ADK Web as a UI, noting its out-of-box file upload capabilities. He encounters issues using LiteLLM to swap Gemini Flash for ChatGPT-4o Mini due to file attachment incompatibility. Brandon clarifies that Gemini 2.5 Flash is competitively priced and recommends keeping agent state small to control costs. Tom Welsh shares a Perplexity-sourced tip about ADK context compression.
-->

00:39:05 - Brandon Hancock
Hamal, you're up next, man. What's been going on?

00:39:08 - Hemal Shah
I continued working on a data reconciliation project between two files. Started with thinking about putting UI in place, but I'm amazed with what ADK Web [tool:Google ADK Web] is providing. You can upload files and do so much. I really like all the out-of-box goodies that come with Google ADK [tool:Google ADK].

00:39:46 - Hemal Shah
It was using Gemini 2.5 Flash [tool:Gemini 2.5 Flash]. Up until now, I was using ChatGPT-4o [tool:ChatGPT-4o] or 4o Mini [tool:ChatGPT-4o Mini]. Flash is super expensive, I feel, compared to the other models. I tried to tweak ADK to use LiteLLM [tool:LiteLLM] to go back to the ChatGPT version, but LiteLLM somehow is not working with file attachments with ADK Web. So that was an interesting find.

00:40:28 - Hemal Shah
<Q>I wonder if we can use real ADK Web in production with some username/password security. It comes with so much out of the box from the UI perspective.</Q>

00:40:41 - Brandon Hancock
<A>▶ I'm hoping at some point soon that they have a button that's just like "export ADK chat," and then you could just throw up a chat where you could add it to your website. That would be sick because then you get all the goodness out of the box and don't have to reinvent the wheel.</A>

00:41:22 - Hemal Shah
The worry I had was because of that pricing — Gemini Flash might be expensive. I went to GCP to see if I can put a hard cap on the money spend. In Google, there is no way you can put a threshold, but I found out that there is a way you can work around it by putting a budget alert and having a function to stop the billing.

00:41:53 - Brandon Hancock
<A>▶ The only feedback to give on that is: every time you're having a conversation in ADK, if you're passing in a monster amount of information or state, it's going to charge you for that. So I think one way to cut costs is to make prompts very small, very concise, and make agents very single-purpose. If it is still super excessive, I would really look at whether I'm putting too much in state. In general, 2.5 Flash is pricing-wise one of the lowest comparatively. If you used Claude for that exact same task, your bill would easily be eight to ten times more.</A>

00:43:49 - Brandon Hancock
▶ They have a Flash Lite — I think it's 2.5 Flash Lite. If you want max speed and lowest cost possible, I would look at that.

00:45:16 - Tom Welsh
Apparently, well, Perplexity [tool:Perplexity] says yes, you can compress ADK context. I've shared a link with what Perplexity came back with.

00:45:29 - Brandon Hancock
Oh, that's perfect. James, I know you had the question, so definitely recommend checking out that link.

---

<!--SEGMENT
topic: Juan Torres — AWS GPU Infrastructure for RAG Application
speakers: Juan Torres, Brandon Hancock
keywords: AWS EC2, A10 GPU, PostgreSQL, pgvector, Elastic Beanstalk, VPC, Mistral, open-source LLM, AWS cost calculator, AWS Activate, cold boot, warm boot, horizontal scaling, vertical scaling, AI Engineering book, Chip Huyen
summary: Juan Torres describes building a full AWS infrastructure with an EC2 A10 GPU instance for running 7B–20B parameter open-source models (Mistral), a PostgreSQL database with vector extension for RAG retrieval, and an Elastic Beanstalk frontend — all within a VPC to minimize data transfer costs. He shares an AWS cost calculator tool and the AWS Activate startup credits program. Brandon discusses cold boot vs. warm boot tradeoffs and recommends the AWS Certified Developer certification.
-->

00:45:42 - Brandon Hancock
Next up, Juan, what's going on, man? What fun projects are you working on?

00:45:51 - Juan Torres
I'll try to develop a whole AWS infrastructure [tool:AWS]. With an EC2 instance [tool:AWS EC2], with an A10 GPU that can handle a 7 billion parameter model, 20 billion parameter model — the same ones, Mistral [tool:Mistral] and GPT open-source — with an instance that also has a PostgreSQL [tool:PostgreSQL] database that has the extension to vectorize the data to do the RAG retrieval. And then I'm helping the front-end person develop the Elastic Beanstalk [tool:AWS Elastic Beanstalk] instance in order to deploy the application. And all of it is going to be within the virtual private cloud in order to lower costs of transmitting information between different instances.

00:46:48 - Juan Torres
▶ I wanted to share with people this really cool tool that allows you to cost instances for EC2, or RDS, or Elastic Beanstalk. So this helps me create a budget of what the whole three instances are going to be for my client. I'm expecting an initial cost of $1,000. And if he makes the one-year commitment, it's going to lower to maybe half of that, maybe $500. The biggest expense is going to be the EC2 instance that has the A10 GPU.

00:47:49 - Juan Torres
▶ Aside from that, I was able to save my client $1,000 because he applied to the AWS Activate program [tool:AWS Activate]. As a startup, you can apply for at least $1,000 in credits. So the initial stage of development is all covered. If people are interested in deploying in AWS, I really recommend applying to that program.

00:48:35 - Brandon Hancock
<Q>Does everything need to run 24/7? Or is this a tool they build and then give to customers?</Q>

00:48:50 - Juan Torres
<A>No, it's for customers. So there needs to be a level of readiness. For now, we're going to put it on on-demand just because I want to have a consistent environment in which I can run experiments. But if clients can wait a couple of hours to get their agentic response, then spot instances could actually be a feasible solution.</A>

00:49:41 - Brandon Hancock
<A>▶ The only suggestion I was going to make — there's something called a warm boot versus a cold boot. What a lot of companies will do is say, "We'll spin up to 10 of these monster GPU instances, but when no one's on the platform, we're going to go down to zero." By going down to zero, they're saving a ton of money. But the trade-off is the second that first request comes in, you have a cold boot — for these bigger computers, especially with whatever software and images you're loading, that could lead to three to five minutes just to get the first response.</A>

00:50:49 - Brandon Hancock
▶ Quick recommendation — if you have not done the AWS Certified Developer Program, I would 10 out of 10 recommend it. You're speaking the language, you're doing the things. It looks great on a resume.

00:51:56 - Juan Torres
Have you guys read this book before? It's the AI Engineering by Chip [tool:AI Engineering by Chip Huyen].

00:52:19 - Juan Torres
In San Diego, there's the San Diego Machine Learning Group. I may actually be teaching this book at that group with a machine learning engineer from San Diego. We picked it up because we thought it was theoretically comprehensive. The practical aspect of it, I think it's going to be somewhat abstract. I was debating with my co-teacher how we should approach it — if we should move towards teaching more applicable software-related skills rather than the theoretical whole gamut of AI engineering.

00:53:25 - Brandon Hancock
I read a book very similar — the AI Engineering Bible [tool:AI Engineering Bible]. It's Kindle Unlimited. If you're looking for a cheaper book, that one was decently good. Once again, they're all theoretical.

---

<!--SEGMENT
topic: James Rennie — Gemini CLI MCP Setup and Chat Context Management
speakers: James Rennie, Brandon Hancock, Tom Welsh
keywords: Gemini CLI, MCP, Context7, JSON configuration, API key, Gemini 2.5 Pro, Gemini Flash, context window, chat merging, markdown export, AI docs folder, scratch folder
summary: James Rennie troubleshoots adding the Context7 MCP server to Gemini CLI — the server is found but throws errors. Brandon walks through the JSON configuration, suggesting removal of unnecessary headers. James also asks how to merge context from multiple chat sessions; Brandon demonstrates his practice of exporting chat summaries to markdown files in an AI docs scratch folder and importing them into new sessions.
-->

00:54:42 - James Rennie
I've been trying to add MCP to Gemini CLI [tool:Gemini CLI]. <Q>It doesn't seem to work at all, whatever I'm doing wrong.</Q>

00:55:07 - Brandon Hancock
<A>When you're in Gemini, you can type in MCP, you can see what all tools you have. I think it's MCP add. I think it's looking for a folder inside your code — your root Gemini folder. Whenever I added it there, then I was able to use it.</A>

00:56:11 - James Rennie
Yeah, so I added it there. It finds it. If I do the MCP list, it finds it, no problem. But it just gives errors over and over again. I thought it was the API key, but then I did a shell command using the API key and it worked fine.

00:56:42 - James Rennie
I copied the chat — the JSON layout — and just removed the API key. So I can show you the format I have in the JSON file.

00:57:02 - James Rennie
The Context7 [tool:Context7] one.

00:57:45 - Brandon Hancock
<A>▶ I would just drop the headers if I was you. They're not needed. Lines 5 through 8 — it's a nice to have, but not mandatory. And get rid of that comma on line 4. Then if you save and refresh, it should, fingers crossed, work.</A>

00:58:27 - Brandon Hancock
▶ Gemini CLI — I like what Google's doing because this is a really good open-source project. However, it does need improvements. I think the biggest limitation right now is you pretty much have to use Gemini 2.5 Pro [tool:Gemini 2.5 Pro] to get it to work consistently.

00:58:43 - James Rennie
Yeah, as soon as it runs out and switches to Flash, I'm done using this for today.

00:59:04 - James Rennie
<Q>The other one is more just a workflow question. When you're creating chats — say you have three different chats and you want to take the context of the different chats that you're working through, compress it, and keep moving on — how are people combining their chats?</Q>

00:59:46 - Brandon Hancock
<A>▶ I always have an AI docs folder and I have a scratch folder in there. Whenever I get to a point where I need to take information from chat one, I'll say, "Hey, I'm going to start working with another AI engineer — export everything that was just discussed in this conversation in maximum detail so that the other engineer has context about what we were doing." I do that in both chats. It makes these files, then I open up a new session and say, "Hey, I was just working on these two tasks, read everything you can about it." We have to export chat to a markdown file and then bring it back in the next one. There's not a quick merge button.</A>

01:01:24 - James Rennie
That's exactly what I've been doing. I just created a Gemini learnings file, put it with the date, and then merged all those files into the context.

01:01:34 - Brandon Hancock
Dude, you're getting creative, man. That's awesome.

---

<!--SEGMENT
topic: Paul Miller — 3D Product Scanning for Retail Shelf AI and Conference Speaking
speakers: Paul Miller, Brandon Hancock, Juan Torres, Jake Maymar
keywords: RoboFlow, YOLO model, 3D scanning, augmented reality, Apple ARKit, Swift, Gaussian splats, synthetic data, shelf recognition, consumer goods, conference speaking, master prompt, lead generation, AI life copilot, Claude Code
summary: Paul Miller shares a project using a photo lightbox with a rotating turntable and iPhone to create 3D models of retail products, aiming to generate synthetic training data for a YOLO-based shelf recognition model — eliminating manual RoboFlow annotation. He also shares a YouTube video of someone using Claude Code to manage their entire business life. Jake Maymar connects Paul with his 3D asset company's expertise and mentions Gaussian splats. Paul asks for advice on presenting AI at a C-level consumer goods conference.
-->

01:01:56 - Brandon Hancock
Paul, you're up next.

01:02:06 - Paul Miller
One of my base company products takes photographs and analyzes what's on the shelf and what's happening with products. But it needs a lot of manual training — saying, "Here's what's on the shelf," mapping that to a file, and then putting it back through AI training using RoboFlow [tool:RoboFlow]. It's quite heavily manual. I want to be able to do more offerings, do it cheaper, do it smarter.

01:03:35 - Paul Miller
So can you see my photo here? Inside it is a turntable that rotates a product, and that ties into an iPhone with a Bluetooth control that controls an object turning around in the box. So if I show you the output of that, it creates a three-dimensional object. Here's like a can of peaches.

01:04:34 - Paul Miller
▶ We can put this in a virtual world and adjust the lighting and the randomness of the virtual world, but then get the software to map that out automatically over and over again and then train the other AI model. This photo was created using Swift [tool:Swift] — there's a wonderful Apple library because Apple's doing a lot with augmented reality [tool:Apple ARKit]. They make it really easy — if you give a collection of photos, it can help you make those photos into a three-dimensional object.

01:05:53 - Paul Miller
I went into the supermarket, I bought every product in one category — baked beans and spaghetti in the United Kingdom. We don't have any customers currently in that space, so I thought, let's use that space as the demo environment, buy every product, scan every product, and create a virtual mapping of how accurate it could be.

01:07:00 - Paul Miller
There's a YouTube video where a guy uses Claude Code [tool:Claude Code] to run his life. So instead of using Claude Code to build an app, he's getting it to manage his business life. I thought it was quite an interesting thing — think of all those markdowns that Brandon's got in ShipKit, but instead of getting it to write software, it's getting it to manage all the things you're trying to handle.

01:07:43 - Brandon Hancock
That's so cool. I genuinely think this is the way work's going to go. A lot of people will eventually start working out of IDEs to do their real-life work. Because you need files and AI, MCP to connect to other stuff, and then boom, you can do most work.

01:09:00 - Paul Miller
I've got an opportunity to speak at a conference coming up in November with most of the people that buy our products in the consumer community. I'm not allowed to go there and just pitch our wares. I want to give away some practical ideas. <Q>I'm thinking that master prompt stuff — how can it help an executive in the consumer goods world? How do they become more capable? If anyone's got any ideas for a talk that people are going to take something away from, I'm just there to be a thought leader.</Q>

01:10:26 - Brandon Hancock
<A>▶ I think what you could do is demo some sort of AI prompt — help them do something with their life or make a suite of tools. Like, "Here's a prompt for how I manage email." Take a few ideas from that AI life copilot, showcase how they could use that in their own life, and say, "By the way, if you want all those for free, just head over here and you can grab them all." That way you get their contact information. The best way to get the leads is to give something cool that you get to demo and they're like, "Holy crap, that was cool."</A>

01:14:21 - Jake Maymar
This is one of our companies — it basically makes photoreal assets. The test is if it makes you hungry or not. We do a lot of food. We were like the distributor for Google and others where we basically take their assets and create 3D assets. What would actually increase your quality is you basically do one where it is and then move the camera up and point it down. And when you run it, it's going to look even better.

01:15:23 - Jake Maymar
▶ Gaussian splats [tool:Gaussian Splats] are pretty amazing — you can have a full 3D animation that you can walk around and a full environment as well. I can show you another example of someone doing basically capturing motion, but 3D motion, doing Gaussian splats.

01:12:18 - Paul Miller
▶ The purpose of creating the three-dimensional world is: by creating accurate representations of all the 3D objects, we can take photos of all the different ways those objects can appear on the shelves, and then use those photos plus where we know the objects are to design an advanced version of the YOLO model [tool:YOLO] that accurately identifies the placements of products on the actual shelves. It builds lots of artificial worlds and says, "In this world, these five products are on the top shelf." The end game is to do that without having to manually map where each product is — because if the system that creates the artificial world knows where the products are because it places them, it can create the mapping itself.

---

<!--SEGMENT
topic: Jake Maymar — OpenAI RAG White Paper and Embedding Model Landscape
speakers: Jake Maymar, Brandon Hancock, Andrew Nanton, Ty Wells
keywords: OpenAI RAG, hallucination reduction, training methodology, embeddings, text-embedding-3-small, multimodal embeddings, Gemini, vector store, Claude slowdown, Anthropic funding, Heijen, Unreal Engine, AI avatars
summary: Jake Maymar references an OpenAI white paper on changing model training methodology to reduce hallucinations. Brandon clarifies the current embedding model landscape: OpenAI's text-embedding-3-small is cost-effective for text, but Google Gemini is currently the only provider supporting multimodal (image/video) embeddings. The group also discusses Claude's recent performance degradation and Anthropic's $13B fundraise. A side discussion covers AI avatar tools including Heijen and Unreal Engine.
-->

01:14:03 - Brandon Hancock
Jake, it looks like you're up next, man. What cool projects are you working on?

01:17:24 - Jake Maymar
Just buried, totally buried in this project. I'm hoping, Brandon, when you come up for air that I can ask questions. But yeah, learning a lot, and I feel like everything is heating up at the same time. I'm pretty sure I'm going to be looking for other people pretty soon. <Q>If you know anyone that you would recommend — mostly a full-stack developer — that would be great.</Q>

01:17:00 - Brandon Hancock
<A>Yeah, if you want to ping me with what you're looking for, I can definitely put names together. I think that's the coolest part about the community — it's filled with people all the way from "I've worked at a major C-level company" to "I just saw AI the other day and now I'm excited."</A>

01:17:24 - Jake Maymar
One other question — I was just curious about the OpenAI RAG [tool:OpenAI]. <Q>Did you guys see the white paper that OpenAI announced? Basically, the training of all the models has been like "randomly guess until you get the right answer," and so they're changing the way the models are trained, which supposedly will get rid of hallucinations. Did anyone have any thoughts on that?</Q>

01:18:35 - Brandon Hancock
<A>I can't remember what the pricing is for OpenAI's embeddings for their vector store. Their text embedding three small model [tool:OpenAI text-embedding-3-small] is insanely affordable. The kicker is — great, where do you put them afterwards? That's the hard part.</A>

01:19:00 - Brandon Hancock
▶ Quick thing I'm seeing in the market: OpenAI, if all you're doing is text-based, document-based embeddings, I've absolutely loved working with what they have set up. But if you're doing anything with image and/or video, Google is the only one that has support for multimodal embedding [tool:Gemini multimodal embeddings]. So if you're ever trying to do something that involves images, you pretty much have to go with Gemini at this point to generate those embeddings. I'm pretty much going all in on Gemini stuff right now until more competition comes in.

01:20:39 - Jake Maymar
I do have one question that's sort of tangential. I'm running a lot of different things. I'm doing Cursor, but I'm also doing just regular Claude Desktop [tool:Claude Desktop]. <Q>If anyone's noticed — just using regular Claude, do you see the UI slow down?</Q>

01:20:53 - Ty Wells
<A>Claude is slowed down in Cursor. Outside by itself, it seems to be okay. I had to switch to direct Claude today. But yes, I have noticed it slowed down.</A>

01:21:03 - Jake Maymar
Yeah, I'll be going along and my computer, everything is running fine, but Claude itself — I'll type and wait for it to finish typing. I went through, looked at all my network, looked at all my stuff, everything looks fine.

01:21:51 - Ty Wells
I noticed it around five or six — when people get off work. It just starts to bog down the system. During the day I don't really notice it that much, but after five Central Time, I'm like, "Oh my God, people are here." So that's when I take my break.

01:22:15 - Jake Maymar
And then I know, Andrew, you're using Claude Code. <Q>Do you ever see a slowdown at all?</Q>

01:22:21 - Andrew Nanton
<A>Yeah. I did see that they said the last six weeks they've had degraded performance — some of it for speed, but also for quality. I wonder if they're going to address that for those of us who are paying for it.</A>

01:23:07 - Brandon Hancock
I know they did just raise $13 billion and most of it is supposed to go towards GPUs to help train and deliver for the normal models that we're using. So fingers crossed the second that cash hits the bank account, they start going on a buying spree.

01:41:00 - Mitch
You've got to get an AI clone, man.

01:41:23 - Jake Maymar
There's a lot of puppets. It's a character, but it's a puppet of a person, and that actually does pretty well. Unreal [tool:Unreal Engine] is a tool that a lot of people use to make those puppets.

01:42:33 - Alex Wilson
A lot of people are using Heijen [tool:Heijen], right? That has the avatars.

01:42:36 - Jake Maymar
▶ The problem with Heijen is you don't get the emotions, and so it's not real time. Whereas the Unreal solutions are more real-time solutions. Heijen works, but you have to sculpt it. So it's not a real-time thing — you can basically make the video, and if they're not saying it right, you say, "Say it like this," and it will. But in general, it misses the emotion side of things.

---

<!--SEGMENT
topic: Ty Wells — Bahamas Restaurant Ordering App Launch
speakers: Ty Wells, Brandon Hancock, Hemal Shah
keywords: restaurant ordering app, POS system, Twilio, SMS server, Bahamas, onboarding automation, menu scraping, 5% transaction fee, tablet ordering, Uber Eats alternative, ShipKit, payment processing
summary: Ty Wells demos a fully built restaurant ordering and management system deployed in the Bahamas, built in approximately one month. The app replaces phone-based ordering with a tablet interface, includes a full back-end POS for restaurant operators, and uses a custom SMS server (avoiding Twilio's international costs) for order confirmations. Restaurants are onboarded in 10 minutes by scraping their menu. The business model is 5% per transaction with no upfront cost.
-->

01:23:33 - Brandon Hancock
I think next up is Ty. What cool projects are you working on, man?

01:23:39 - Ty Wells
Still down at the Bahamas — leaving tomorrow. But this is the other product I've shipped. This is a... you can order from different restaurants. But this has a full ordering system. I've built in a complete system on the back end that's being given away for free. Basically, any of these restaurants can use this to manage their system. A lot of them do not use any kind of POS or anything like that.

01:25:32 - Ty Wells
So they could use this if they want to run their entire operations — their entire business system. Suppliers, inventory, they can do whatever they want. This is all basically what they would see on their screen, like a tablet sitting there, like an Uber Eats [tool:Uber Eats] or anything like that.

01:26:15 - Ty Wells
▶ I made it easy for them. If they wanted to change an item, I gave them a whole little thing here — they could search, find new items that match. I can basically onboard a restaurant with their menu in about 10 minutes. My salespeople go out there, they find the restaurant, they onboard the restaurant before they even walk in the door — just from the menu, they scan, and it automatically processes. I've got some workflows on the back end that will pull in their menu, scrape any website, any social media. 10 minutes, boom. Restaurant's on board. Just have training for another 30 minutes, and they're ready to take orders.

01:27:05 - Brandon Hancock
<Q>How does one price this? Is it on a per-order fee?</Q>

01:27:13 - Ty Wells
<A>▶ It's 5% on any transaction. That's it. That's all you pay. So if nobody uses the system or orders anything on your platform, you pay nothing.</A>

01:27:41 - Ty Wells
It has a three-strike system for people that place orders and don't pick up. It's got the full gamut of everything you need to order, but just for delivery. If the market drives them to want payment processing, I've got that built already. I'm just not going to roll out with that because I'm just replacing what they already do, which is to call restaurants.

01:30:17 - Ty Wells
▶ Just so you know — because using Twilio [tool:Twilio] and it's going to come from a non-Bahamian number, which is a different area code and costs more — I use my own SMS server to send messages back and forth to the users. That's how I confirm the sign-up: phone number and a quick PIN. Boom. It takes your card so you can order right to the point.

01:28:35 - Hemal Shah
<Q>Did I hear correctly that it's a phone ordering system where a customer can just call a number and place the order?</Q>

01:28:47 - Ty Wells
<A>No, that's what they do right now. They call the restaurant and have to place the order. The problem is when they're busy during lunch, they just don't pick up the phone. They can only take one order at a time. So this eliminates all of that — all they have to do is see the tablet, accept the order or reject the order if they can't handle it.</A>

---

<!--SEGMENT
topic: Open-Source Embedding Models and Cloud Deployment Tradeoffs
speakers: Brandon Hancock, James Rennie
keywords: open-source embeddings, DocLing, vendor lock-in, cloud infrastructure, scaling, AWS, Vercel timeout, Pydantic, background workers, n8n, Google Cloud Run, ShipKit RAG processor
summary: Brandon responds to James Rennie's question about using open-source embedding models, explaining that while they work well locally, cloud deployment introduces significant infrastructure complexity around scaling, cold boots, and compute costs. He recommends starting with vendor-provided embeddings (OpenAI or Gemini) while learning, and notes that ShipKit's RAG processor already handles scaling groups. He also previews a planned ShipKit addition for pure automation pipelines beyond ADK's chat-plus-workflow model.
-->

01:30:56 - Brandon Hancock
I did want to address James. Going back to open-source embedding models — <Q>James, your question: using open-source embedding models, awesome, it works great locally. The issue you'll run into is the second you go to deploy it, you then have to start to think about a lot of what Juan was talking about earlier — what happens when a customer gives me 100 documents? How do I embed 100 documents? Do you have one computer that just takes one job and works on it? Do you have always 100 instances running 24/7?</Q>

01:31:42 - Brandon Hancock
<A>▶ When you're thinking about doing open source, it makes a ton of sense locally. The second you go to the cloud, you have to start considering development time and enterprise cloud cost. I will say in ShipKit, I was using the small DocLing [tool:DocLing] embedding model. If you turn off vision mode, it actually is super fast. It's just you have to know in advance — I'm going to have to start worrying about cloud infrastructure and scaling based on how many requests I'm getting at any given moment. If you're not as comfortable with it, I would recommend: it's totally fine to be vendor-locked while you're just figuring stuff out. OpenAI, Gemini — the best models out there right now for embedding.</A>

01:32:38 - Brandon Hancock
▶ Quick internal plug — if the idea of scaling AI machines excites you, ShipKit does that whenever we do the RAG processing. All the scaling groups and everything else are already built in for you in the RAG processor. It was the hardest part to figure out to get working consistently, so I have scars from it.

01:40:00 - Brandon Hancock
One other thing I want to mention — what Mitch was doing: he did a really good job of creating an n8n [tool:n8n] workflow. And then the question is, how do I turn that into my own application? How do I actually deploy a real-world application that literally just automates steps one through 20 every single time, very low human interaction? ADK is great at chat plus workflow. But what happens when you literally just need pure automation from end to end — just a background worker? Literally just Pydantic [tool:Pydantic]. There's no need for agents. But it takes longer than the five minutes that Vercel [tool:Vercel] gives you. So that is one other thing I'm going to add to ShipKit.

01:42:49 - Mitch
The difficulty of doing n8n versus Google Cloud Functions — or it's now called Cloud Run [tool:Google Cloud Run] — is very different. So I think that would be a good middle ground — instead of doing this and you don't like this, then do local n8n running.

---

<!--SEGMENT
topic: Alex Wilson — ShipKit Usage Workflow Questions
speakers: Alex Wilson, Brandon Hancock, Jake Maymar, Mitch
keywords: ShipKit, prep templates, cursor rules, AI docs folder, roadmap, Next.js, ADK orchestrator, bug fix template, Git commits, phase-based development, AI clone, Heijen, Unreal Engine
summary: Alex Wilson asks about the correct way to use ShipKit's prep templates and cursor rules, having been building projects from scratch outside the template. Brandon clarifies that ShipKit works best inside an existing template project and walks through the CLI setup flow, prep template question-and-answer process, and roadmap-driven phase development. The group also briefly discusses AI avatar/clone tools for YouTube content creation.
-->

01:32:41 - Brandon Hancock
Alex, you're up next, man. What's going on?

01:32:45 - Alex Wilson
I'm enjoying learning ShipKit. I have a couple of questions. <Q>The method I've been doing is taking your two folders — the cursor rules and the app folder — and doing that outside of the project and having it build the project underneath it. But I noticed in your examples, it looks like you have those inside of the project.</Q>

01:33:24 - Brandon Hancock
<A>Yeah, the way it will work the best is inside of an existing template. The prep template is designed to look through the current code base to be like, "Okay, I know what app you're building, I know what you're trying to do — because I understand what capabilities your application has, I can help you go from a template to a real-world project." If you just dump these AI documents in a different environment that's brand new and fresh, it's not going to know what there's no existing thing to compare to.</A>

01:34:29 - Brandon Hancock
▶ The main things I would use in the meantime are all the development templates — the task template for Next.js [tool:Next.js], Python task template for anything with Python. And if you're doing anything with ADK, you always start with an orchestrator, because it helps you map out the entire workflow. Then as you run into issues, you do an ADK bottleneck analysis, which will figure out what's going wrong with your prompts. And then you make a task template for ADK to go improve this. Outside of that, bug fix is a godsend because half the time AI code just doesn't work.

01:35:42 - Alex Wilson
So I've been doing it backwards. I've been using the prep to actually build the application from the ground up. And that's why it's outside of the actual project. And it's working really well.

01:35:55 - Brandon Hancock
Oh, that's awesome news. I haven't tried it that way. That makes me happy to hear.

01:36:00 - Alex Wilson
<Q>My question with that is — if it's inside, how do you do the prep work if you start from scratch?</Q>

01:36:10 - Brandon Hancock
<A>Eventually there is a ShipKit CLI — you'll run `shipkit ai`, you'll do like `alex-test`. "Oh, you want to make a RAG SaaS application? Cool." It makes a brand new project for you. And then what's cool is that template project is already going to be working, and it already has all the prep templates and all the AI docs. So it's just a working project that's set up for AI right out the gate.</A>

01:38:52 - Brandon Hancock
The way it works is you start off by going through the prep templates. The way it's designed is to ask you questions and then fill in all the dots. For example, if we're trying to build the RAG template, we would start answering questions about who do you help, what does success look like, what capabilities are we trying to build for them. And as you answer the questions, it starts building out documents for you — your North Star documents — what your app does, all your app names and everything else. The second you get done with each prep process, AI has all the context it needs to start building out your application.

01:40:00 - Brandon Hancock
▶ You end up with this roadmap — phase by phase, exactly how to build out your application. What database changes you need to make, what pages you need to make. And then you literally just copy in phase three, open up a new chat, and say, "Please help me build this out."

01:37:49 - Brandon Hancock
▶ Inside of Cursor, there's a template that's amazing for pushing and writing the commit notes. Every time you finish something, literally just run this — it'll analyze everything that you just did and create the right commits for you.

---

<!--SEGMENT
topic: Morgan Cook — School Pickup Logistics App Concept
speakers: Morgan Cook, Brandon Hancock
keywords: school pickup logistics, real-time updates, Next.js, WebSockets, QR code, license plate recognition, topological sorting, queue, Google AI video, KOHP, charter school, MCP servers, Context7, Supabase, time MCP, Sequential Thinking MCP
summary: Morgan Cook describes a school car-line management app he originally built 15 years ago in KOHP that reduced pickup time from 90 minutes to under 15 minutes. He wants to rebuild it with modern real-time push technology and AI-assisted logistics sequencing. Brandon suggests Google's video AI for license plate detection and topological sorting/queue data structures for sequencing. Morgan also asks what MCP servers the group recommends beyond Context7 and Supabase.
-->

01:44:14 - Brandon Hancock
I think next up is Morgan.

01:44:20 - Morgan Cook
Last week, we talked a little bit about different email services. All I'm working on right now — I've got like eight projects I want to start, but I'm not quite ready yet. I've got five or six different profile sites for different people. But then I have actual applications that are going to require some AI.

01:44:47 - Morgan Cook
One of them is an app that I wrote like 15 years ago when my kids were in school at a charter school. One of the problems was it was taking a good hour and a half to two hours to pick up the kids after school, because charter schools are usually set up in a business district — no parking, just chaotic. I had developed this app to automate that process by having an attendant at the curb scan all the car numbers as they're coming in, and then that would send a message to each of the classrooms and display the student picture of who's supposed to leave.

01:45:31 - Morgan Cook
Back then, the only way I could get it to work was to have the browser constantly polling the server. We didn't have really good push technology 15 years ago. So I'm really excited about using some of the automated stuff in Next.js [tool:Next.js] and updating all that automatically.

01:46:04 - Morgan Cook
The AI part is that it's dynamic every day. Each classroom may be right next to the door, or all the way down the hall and takes a long time to get organized. That's where AI would come in — trying to automate the logistics of getting all the students out the door at the same time for each car in the sequence they're supposed to be there.

01:46:51 - Morgan Cook
The app I had written 15 years ago was in KOHP [tool:KOHP], which is a model-view-controller platform. We reduced the time from the hour and a half to almost two hours at the first of the year down to less than 15 minutes to get that school emptied.

01:47:27 - Brandon Hancock
<A>I have not had to do much with an AI video feed. I know out of all tools right now, I think Google's AI — they have a bunch of video AI tools that would probably be your best bang for buck on registering the car number. Just a real-time feed, literally just a camera outside watching cars pass by. It would just detect license plates. Once it detects license plates, it's just real-time shooting them to the database.</A>

01:50:00 - Brandon Hancock
<A>▶ One thing you could do — it's called topological sorting [tool:topological sorting], which basically means: what order of operations do things need to happen in? So if I'm the car in the first spot, that is the first prerequisite. You either need to do a queue or topological sorting — if you have some sort of dependencies like "Brandon's ready for pickup, but before Brandon can get picked up, Jake needs to get picked up" — that is topological sorting. But that could be overkill. It's either a queue or topological sorting, and you wouldn't even have to use AI — just data structures.</A>

01:51:35 - Morgan Cook
<Q>MCPs — besides Context7 [tool:Context7] and Git and maybe Supabase [tool:Supabase], what MCPs are you guys using to assist with your AI development or development in general?</Q>

01:51:49 - Brandon Hancock
<A>▶ The main other one I'd recommend — there's a time library that is super helpful just because AI sucks at time. It's literally just called time. That is the one I use. I hit the MCP in time probably 100 times a day. Those two are the most used. Outside of that, I would be using Slack if I was on a bigger team. I would be using Linear a lot more.</A>

01:52:44 - Brandon Hancock
▶ I love Sequential Thinking [tool:Sequential Thinking MCP] — but just be careful of the context window because it will burn through it. It forces the agent to explain, basically in a chain of thought, its reasoning for something. Very cool if you're stuck on a problem to get the AI to think through it logically.

---

<!--SEGMENT
topic: Patrick Chouinard — SpecKit, Podcast Audio Generator, and Claude for Financial Services
speakers: Patrick Chouinard, Brandon Hancock
keywords: SpecKit, GitHub Copilot, Claude Code, Gemini CLI, NotebookLM, podcast generation, Clara Forge, markdown, audio, Fabric, Daniel Miesler, Claude for financial services, MCP, enterprise AI, financial data feeds
summary: Patrick Chouinard reports his first hands-on app-building experience using GitHub's SpecKit tool with Claude Code, building a NotebookLM-style podcast audio generator for his Clara Forge project in approximately three hours. He shares a YouTube video by Daniel Miesler (creator of Fabric) on building an AI assistant with Claude Code. He also asks if anyone has experience with Claude for Financial Services — an enterprise Claude offering with proprietary MCPs for financial data feeds, governance, and auditing.
-->

01:55:06 - Brandon Hancock
All right, Patrick, you're up.

01:55:11 - Patrick Chouinard
This week, I actually had my first time to work on building an application instead of just teaching about it.

01:55:21 - Patrick Chouinard
I've tested something called SpecKit [tool:SpecKit] from GitHub [tool:GitHub]. Very, very surprised at how well it worked for Claude Code [tool:Claude Code], because it works with Claude Code, Gemini CLI [tool:Gemini CLI], and GitHub Copilot [tool:GitHub Copilot], but I tried it with Claude and it worked extremely well.

01:55:45 - Patrick Chouinard
I was just tired of creating all of my podcast audio from my other project, Clara Forge [tool:Clara Forge]. Every time I create a new markdown file, I create a podcast out of it from NotebookLM [tool:NotebookLM], but there's no API for NotebookLM. So finally this weekend, I bit the bullet and said, "Okay, I'm going to build my own — some kind of NotebookLM, not all the functionality, just the generating audio podcast from it."

01:56:26 - Patrick Chouinard
▶ I had a first version — not fully debugged, but in about three hours, it was at the very least somewhat working end-to-end without too many bugs. I'm pretty surprised that with the help of SpecKit, I ended up creating a project plan and a list of tasks that was good enough for Claude Code to create something that worked.

01:57:37 - Patrick Chouinard
Here's a little YouTube video I've seen this week that I absolutely love. It's from Daniel Miesler [tool:Daniel Miesler]. He's talking about building an AI assistant using Claude Code, and it's extremely interesting. This guy has like a 600 IQ or something. It's the guy behind Fabric [tool:Fabric].

01:58:23 - Patrick Chouinard
<Q>On the business front — did anybody have the chance to work with Claude for Financial Services [tool:Claude for Financial Services]? Because I was asked to evaluate that this week. Basically, it's Claude Enterprise plus a bunch of proprietary MCPs to connect to a bunch of data feeds for financial business, as well as a prompt database specifically for the financial industry, and a lot of stuff for governance and auditing.</Q>

01:58:57 - Brandon Hancock
<A>I haven't. But I would love to — if you get a demo of that, if you could send it to me. That's the one thing — I know how much I am addicted to AI because I use it 24/7. My wife is a consultant and she uses it a lot, but inside ChatGPT. I'm like, "Man, I cannot wait till you guys get your own tool, like a Cursor, like a Claude Code, because the second they get their own tool, they're going to be hooked."</A>

01:59:42 - Brandon Hancock
Dude, that price tag is going to be stupid. Like, they're actually just going to say, "There is no quote, just give us your bank account number and you'll see money leave."

02:00:04 - Patrick Chouinard
I actually even use Claude Code behind the scenes as a headless server for a bunch of what it does. I haven't seen the pricing yet — obviously it's "call to get a quote." It's not something you buy for $200 a month.

02:00:18 - Patrick Chouinard
But if I get anything in terms of a demo, I'm going to share with the group. No worries. As long as it's legal, obviously.

---

<!--SEGMENT
topic: Mitch — Leather Eyepatch B2B Lead Gen, AI Video Automation, and CliftonStrengths Prompting
speakers: Mitch, Brandon Hancock, Jake Maymar, Juan Torres
keywords: Nano Banana, Amazon, Shopify, B2B lead generation, Instantly, Apify, LinkUp, AI video automation, VO, n8n workflow, CliftonStrengths, ChatGPT memory, personality assessment, Russell Brunson, Value Attainment, Idaho AI startup, agency commoditization
summary: Mitch shares progress on a leather eyepatch business using AI-generated product assets, a Shopify store, and a B2B cold email campaign targeting optometrists via Apify scraping, LinkUp for personalization, and Instantly for sending. He met the ex-head of media for Value Attainment at a conference and is exploring selling AI video automation services. He also demonstrates using ChatGPT with CliftonStrengths assessments and memory to generate personalized blind-spot analyses — a workflow that impressed (and slightly threatened) a CliftonStrengths coach.
-->

02:01:03 - Brandon Hancock
All right, Mitch, you're up next, man. What's going on? How's the app land going?

02:01:09 - Mitch
So, if you guys don't know, I sell leather eyepatches. Been big on Nano Banana [tool:Nano Banana] recently. It's crazy how fast these Amazon agencies are becoming commodities and how much AI tooling is really getting a part of them.

02:02:19 - Mitch
I even made a Shopify [tool:Shopify] store. And then I also did a B2B lead gen for the eyepatch — started getting the emails together, getting the emails primed. It started around two weeks ago. I just started sending the emails today. And I got my first response and I sent out my first eyepatch as a sample today. I think I've emailed close to 2,500 people.

02:03:09 - Brandon Hancock
<Q>My understanding — you're scraping with Apify [tool:Apify]? Email list to Instantly [tool:Instantly]?</Q>

02:03:20 - Mitch
<A>Yep.</A>

02:03:28 - Brandon Hancock
<Q>And then Instantly — is it to a form, to a reply? What's the funnel? Are you using Instantly's AI tools?</Q>

02:03:57 - Mitch
<A>There's a specific one that's really good — it's better at doing deep research. It's LinkUp [tool:LinkUp]. LinkUp is the best tool for deep research. It's best known for doing reverse person research. So it's like, "Hey, notice you were the award-winning eye doctor of the year in your city. Congratulations." Stuff like that.</A>

02:05:01 - Mitch
So Tom inspired me to go to an in-person conference. I went there. I met the ex-head of media for Value Attainment [tool:Value Attainment]. And I was talking to him about some stuff. He's business partners with an insurance guy who exited his insurance company for like $50 million. Talking to him about what I'm doing on the content front — all of these videos, they're completely automated by VO [tool:VO]. And he's like, "Oh, have you thought about selling this to businesses?" And I was like, "Not really. But we should." So we'll talk with him tomorrow.

02:06:15 - Mitch
That guy has around a thousand different insurance companies that he coaches on a newsletter basis. So could definitely kill in that area as well.

02:06:23 - Brandon Hancock
<A>▶ I would honestly just build, once you find someone who's crushing it, just build an AI business around them. If they already have distribution, they already have money flowing in and out — every person needs a suite of AI tools for marketing, for video advertisement, for their coaching services. Even if you just take 2% of the value they're generating, it's still a ton of money.</A>

02:09:08 - Mitch
I was showing Russell Brunson's personal coach my AI workflow for CliftonStrengths [tool:CliftonStrengths]. She's a CliftonStrengths advocate. So I was showing her how I use AI to do the personality side of things. You can take someone's CliftonStrengths assessment, screenshot it, and then arrange it. You can see what is their strength, what is their blind spot. And then you can also take this and analyze how someone thinks — get their five steps of how they think and behave. You can do this with you and your team and see where your blind spots are and things you need to hire for.

02:10:33 - Brandon Hancock
▶ What I love to do with ChatGPT [tool:ChatGPT] is — because it knows me — instead of me going through the whole process, I'm like, "Hey, do you know what this is? Yes. Okay. Using everything you know about me, give me mine." So my Enneagram, all my stuff — I just say, "You probably know me better than most people." And it just instantly generates a report. Here's exactly how you think about problems. Here's exactly where you miss stuff.

02:11:28 - Mitch
▶ And you add it to your memory. Then when you add it into your memory, you say, "Here's my blind spots. And I want you to be very aware of when I'm not aware of my blind spots — it's your job to tell me." And after that, it was cooking. It was like, "Hey, this is your fear of this thing."

02:13:41 - Brandon Hancock
▶ One other thing I want to mention — what Mitch was doing with n8n [tool:n8n]: he did a really good job of creating an n8n workflow. And then the question is, how do I turn that into my own application? How do I actually deploy a real-world application that literally just automates steps one through 20 every single time, very low human interaction? ADK is great at chat plus workflow. But what happens when you literally just need pure automation from end to end — just a background worker? Literally just Pydantic. There's no need for agents. But it takes longer than the five minutes that Vercel gives you. So that is one other thing I'm going to add to ShipKit.

02:15:27 - Brandon Hancock
All right, guys, I've got to hop on another call here in just a few minutes. If you guys need anything, please shoot me a message. Happy to help. Alex, I owe you some docs — I will do that after that next call. Look forward to seeing you guys next week and hope y'all have a great rest of your week.

---

=== UNRESOLVED SPEAKERS ===
- Sam (appears at 00:04:05–00:04:14; not in alias map)
- David (appears at 00:14:28 onward; referred to only as "David"; not in alias map)
- Mitch (appears at 01:40:00 onward; referred to only as "Mitch"; not in alias map)
- Morgan Cook (appears at 01:44:20 onward; referred to as "Morgan"; not confirmed in alias map — passed through as "Morgan Cook" based on transcript attribution)