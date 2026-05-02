=== SESSION ===
date: unknown (transcript contains no explicit date)
duration_estimate: ~26 minutes
main_themes: RAG architecture and hallucination mitigation, vector database re-encoding costs, web scraping for data pipelines, data engineering's role in AI development, portfolio/freelance career development, MCP tooling

---

<!--SEGMENT
topic: Introductions and Upcoming Presentation
speakers: Juan Torres, Jake Maymar
keywords: banking concentration, agentic systems, data engineering, San Diego, live stream, portfolio, data science video, GitHub, Brandon, feedback
summary: Juan Torres introduces an upcoming in-person presentation in San Diego on banking concentration and agentic systems, with plans to live stream it. The conversation touches on Juan's data science video project, which has been delayed due to workload and constructive feedback from a community member named Brandon. Both speakers reflect on the value of early critical feedback.
-->

00:00:00 - Juan Torres
Man, your data science stuff is pretty cool.

00:00:03 - Juan Torres
Thank you. Yeah.

00:00:05 - Juan Torres
Actually, today I was planning to share an event I'm going to be presenting on the concentration of banking with the agentic systems and the engineering components.

00:00:17 - Juan Torres
So we're sharing it with you.

00:00:19 - Juan Torres
I'm planning to do a live stream because it's in San Diego.

00:00:23 - Juan Torres
So for folks that may want to be in the meetings, I'll make the link available.

00:00:31 - Jake Maymar
Cool. Very, very cool. <Q>So are you getting a lot of traction? How's that going?</Q>

00:01:00 - Juan Torres
<A>The video — it's kind of like a byproduct of the whole project and I haven't published it yet, just because I've been really busy with other projects. And I was planning to continue working on the project, and then Brandon made really good recommendations and annotations to the video. So I'm planning to maybe redo it and then try to integrate a lot of his constructive criticisms.</A>

00:01:42 - Jake Maymar
He really does know really, really good points. He's also a very kind person. He wouldn't tell you anything he wouldn't tell himself. And so it may sound like critical feedback, but man, you want to hear that now. You don't want to hear that like years later when you're trying to get funding. ▶ It's so nice to have it at the very beginning.

00:02:24 - Juan Torres
Yeah, it's awesome. And I was really thinking of doing his program, but the thing is I have so many projects right now.

00:02:37 - Jake Maymar
It's crazy. Everything is just accelerating. I love the idea and I would totally be part of it, but yeah, I'm a little jealous of people that are in it — they're going to just skyrocket.

---

<!--SEGMENT
topic: Assessment Tool and RAG Architecture Overview
speakers: Juan Torres, Jake Maymar
keywords: assessment tool, relational communication, NLP, RAG, retrieval augmented generation, vector database, re-ranker, judge, hallucinations, cosine similarity, scoring
summary: Jake describes a communication skills assessment tool that tracks user scores over time and uses a RAG system to generate improvement activities. Juan asks about the distinction between a RAG database and a vector database, prompting Jake to explain how vanilla RAG differs from a RAG pipeline augmented with re-rankers and judges to reduce hallucinations.
-->

00:03:08 - Jake Maymar
<Q>What are you working on?</Q> Oh, well, you know this assessment tool — here, I'll put the link in the chat.

00:03:46 - Jake Maymar
<A>Basically it's an assessment tool where you test yourself on some sort of increment, either daily or weekly, and then try to improve your relational communication skills.</A>

00:04:05 - Juan Torres
<Q>So are you using NLP in order to assess the communication style of people?</Q>

00:04:15 - Jake Maymar
<A>You know, it's kind of funny with assessments — it's essentially a score, right? It's a series of questions that you ask the participants. And then depending on how they answer, you use all of that data to create historical projections and forecasting. And then I also have a RAG database [tool:RAG] that's taking all of the suggestions and creating activities that will help them increase their score as well.</A>

00:05:00 - Juan Torres
<Q>What is the difference between the RAG database and a vector database?</Q>

00:05:10 - Jake Maymar
<A>That's a fair question. Often when you take something and just create a vector database [tool:vector database] out of it, you're going to get hallucinations — you could do cosine similarity, you could do a whole bunch of different things, but you're going to get hallucinations. If you do RAG, vanilla RAG, you'll probably also get hallucinations. But if you do RAG where you have a re-ranker, and then you have a judge, and you have all these other things looking at it — essentially saying don't hallucinate — and you're pulling directly from not only a vector database but an actual database to verify the content, chances are you're going to get something that's fairly accurate.</A>

00:06:13 - Jake Maymar
The problem with RAG is it's just a term — retrieval augmented generation — but now the term, if you add all this stuff in, has become a way to mitigate hallucinations, which is the biggest reason you use it.

00:06:35 - Jake Maymar
In theory, you'd be able to ask an LLM [tool:LLM] a question and it would give you the answer. You can query a database and get a response — if it's in that database, it's going to come back. The problem is if you query an LLM, you'll get a response, but you don't know if it's accurate, and it does cosine similarities — this response is really similar to this one — and it doesn't match either one exactly.

00:07:11 - Jake Maymar
And the hallucinations come from that "in general it matches." Instead of saying the sky is blue, it says green. Now, it says the sky is blue in your vector database, but it says it's green. Technically that's kind of close, because it's close to blue. But the reality is it's supposed to be blue — it's deterministic, it needs to be blue, but you get probabilistic and it's green.

00:07:55 - Jake Maymar
▶ In healthcare, that matters a lot. That's part of the reason I have these RAGs — it's basically drug interactions, and you ask it questions and then it looks at the database and the vector database and other headers, and then it comes back with the result.

---

<!--SEGMENT
topic: Hallucination Mitigation and Model Drift
speakers: Juan Torres, Jake Maymar
keywords: hallucinations, synthetic data, evals, model drift, prompt drift, system drift, GPT-4o mini, OpenAI, Claude, re-encoding, pharmaceutical data, API drift
summary: Jake explains his evaluation methodology for catching hallucinations, using synthetic data and adversarial prompts. He introduces the concept of prompt drift, model drift, and system drift as compounding challenges when building production RAG systems, using GPT-4o mini as a cost-effective but evolving model example. The segment highlights why maintaining stable LLM-based systems is difficult.
-->

00:08:22 - Juan Torres
<Q>How do you verify the answers for your system?</Q>

00:08:28 - Jake Maymar
<A>Classic evaluations are the best. So you do a whole bunch of synthetic data, then you generate a whole bunch of in-theory responses, and then you run those responses along with hallucination-inducing questions — questions that should generate hallucinations — and then you tune to make sure that it doesn't keep giving you hallucinations, or at least mitigates them.</A>

00:09:01 - Jake Maymar
▶ It's very hard to get rid of hallucinations. The reason it's so hard is you have prompt drift, you have model drift, and then you have system drift.

00:09:11 - Jake Maymar
A lot of people don't think about that. Like, I like to use GPT-4o mini [tool:GPT-4o mini] — it's a very hard model to use, but I'm using it because it costs nothing. It's super fast.

00:09:52 - Jake Maymar
But they keep updating GPT-4o mini. When I started using it, it was kind of rough — not very good, kind of weird. Now it's really refined, very fast, gets way better results. But the problem is all my prompts and all my system worked with that earlier model, and I can't freeze that model.

00:10:22 - Jake Maymar
And then you have other systems on top of that. If you're pulling pharmaceutical data, that changes from time to time. So everything becomes dynamic — I'm pulling in new data, I have a new model, and then some other API calls I'm doing also drift. ▶ It's very, very hard to make sure you have a rock-solid solution when working with LLMs.

00:11:00 - Jake Maymar
So the best way is to have constant evals that run in the background. The problem is if you're running Claude [tool:Claude] 3.7, that's very expensive. So now you have to do evals and embeddings on a very expensive model.

00:11:18 - Jake Maymar
I've been talking with Sebastian and Brandon and Paul — and there's someone whose name I'm forgetting — but they're really good with evals. So you basically run evals, create all your synthetic data, and you're constantly testing against that.

00:12:13 - Jake Maymar
Going back to using OpenAI [tool:OpenAI] models — when you vectorize and tokenize everything, currently you have to re-vectorize everything if you add a substantial amount to the vector database. You have to re-encode it.

00:12:48 - Jake Maymar
You would think you could just append parts of it. But what happens is that appended part doesn't relate to the rest — it's indexing everything, figuring out the similarities. If you append it, those things are similar to each other but don't have any relation to the rest.

00:13:23 - Jake Maymar
That's where graph databases come in — like Neo4j [tool:Neo4j]. ▶ But basically you have to re-encode everything. If you have an expensive encoder, you have to pay for that, and if the data is dynamic, it becomes very brittle. ▶ If you can get to a point where it's a stable dataset that isn't changing much, then RAG works pretty well.

---

<!--SEGMENT
topic: Web Scraping and Data Pipeline for RAG
speakers: Juan Torres, Jake Maymar
keywords: web scraping, Crawl4AI, ETL, HTML selectors, markdown, Federal Reserve, pharmaceutical data, data cleaning, garbage in garbage out, automation, Plotly Dash
summary: Jake describes his web scraping pipeline for gathering pharmaceutical data, using tools like Crawl4AI to convert HTML to markdown before extracting selectors. Juan shares his own ETL-based scraping approach for Federal Reserve data. Both discuss the importance of data cleaning before ingestion into a RAG system, emphasizing the "garbage in, garbage out" principle.
-->

00:14:16 - Juan Torres
<Q>Are you scraping your information, or do you have an API?</Q>

00:14:19 - Jake Maymar
<A>Yeah, that's actually how I get it. I'll scrape a couple of different pharmaceutical companies as well as aggregators, and just get a big jumble, then sort through that jumble either manually or using different automations to sort through the noise. Then from there, build a pretty solid database. And from that database, I create a RAG system and vectorize it.</A>

00:15:00 - Jake Maymar
▶ Garbage in, garbage out. If you scrape something and you have advertising or extra stuff or weird formatting and you're not cleaning the data, that noise gets encoded into your RAG and causes confusion. ▶ You really want to have really clean data in, and then of course you get clean data out.

00:15:33 - Jake Maymar
<Q>Are you using AI in order to automate the web scraping process?</Q>

00:15:36 - Jake Maymar
<A>Yes. I was using Crawl4AI [tool:Crawl4AI]. Brandon had a really nice tutorial. There are a couple of other methods out there, but they're all kind of the same. Once you get the page to markdown, you look for selectors, and from the selectors you extract what you need.</A>

00:16:01 - Juan Torres
Yeah, that's what I did for the Federal Reserve [tool:Federal Reserve data] — I just used old-school ETL scripting. I was thinking, maybe there's a module or a system that — yeah, you give it the HTML code and then it helps you identify the table or the specific parameters within that code.

00:16:35 - Jake Maymar
Exactly. The old-school methods work. If you want to scrape LinkedIn [tool:LinkedIn], you just figure out their selectors — the only problem is they keep updating their selectors, so every time you access the site, they update everything.

00:17:00 - Juan Torres
I'm working with a government bureaucracy that's not very innovative, so they don't update their webpage and data much. So I have a non-dynamic web scraping process.

00:17:15 - Jake Maymar
▶ Yeah, that's fantastic — because I can't tell you how many of my scrapers no longer work. That's what happens.

---

<!--SEGMENT
topic: Juan's Freelance Goals and Banking Concentration Project
speakers: Juan Torres, Jake Maymar
keywords: banking concentration, freelance, data science, contract work, AI development, political economy, econometrics, Plotly, Dash, Charming Data, Adam Schroeder, San Diego data science community
summary: Juan outlines his goal of securing contract work in data engineering, data science, and AI development. He describes the banking concentration project as a research initiative in political economy and econometrics that has gained recognition from the San Diego data science community and was featured by Plotly. Jake affirms the value of data science skills in the current AI landscape.
-->

00:17:34 - Juan Torres
<Q>What are the next steps once you have your site and video ready?</Q>

00:17:34 - Juan Torres
<A>I do want to do contracted work doing the engineering, data science, and AI development work. That's my main goal.</A>

00:18:05 - Juan Torres
The concentration of banking project — is it a client-based project or just a portfolio project? It's really a research project. It's more political economy, econometrics, research. But even despite the fact that it has no monetary implications, it has been receiving a really good reception by the data science community here in San Diego and in other parts.

00:18:54 - Juan Torres
Do you know Dash [tool:Plotly Dash] — the web development framework? So it's like — let me send it to the web — so these guys at Plotly [tool:Plotly]... yes, yes, they liked it so much they actually put it right there in their — awesome, congratulations!

00:21:47 - Jake Maymar
▶ Data science is in a weird place right now, and coding and development is in a weird place too. A lot of people think AI is solving all these problems. But I think if you can show that you still need data science and you still need to evaluate things, you're going to be in great shape.

00:21:53 - Juan Torres
Yeah. And I feel like data engineering specifically is going to still be a really important component of AI development. Because if you don't have really good data for your agents or your models, then you're not going to be able to develop really high-level abstract analysis by AI at all.

00:22:23 - Juan Torres
▶ A lot of people are overlooking the necessity of engineering, because AI is the shinier thing right now. But a lot of the projects I'm working on — do you know Adam Schroeder, the guy who manages the Charming Data [tool:Charming Data] YouTube channel?

00:23:04 - Juan Torres
Yeah, so we get together as a group of people and develop database applications. And a lot of this work, despite the fact that we integrate agentic systems or AI tools of analysis — it doesn't work if you don't have the engineering component that feeds all that stuff into your data web application. ▶ That's why engineering is still quintessential to everything else.

---

<!--SEGMENT
topic: MCP Tooling and Santiago / Underfitted Resource
speakers: Juan Torres, Jake Maymar
keywords: MCP, Model Context Protocol, Santiago, Underfitted, YouTube, Twitter, data science education, model spin-up, practical applications
summary: Jake shares a resource from data science educator Santiago (YouTube channel: Underfitted) demonstrating how to spin up a model using MCP (Model Context Protocol) for practical applications. Juan mentions blocking social media to avoid distraction, so Jake provides a YouTube link instead of a Twitter link. The segment closes with brief wrap-up and plans to reconnect Thursday.
-->

00:24:19 - Jake Maymar
I like this guy Santiago [tool:Underfitted / Santiago YouTube channel] — pretty cool data science guy, and a really nice guy too. I like him explaining this MCP [tool:MCP (Model Context Protocol)].

00:24:38 - Juan Torres
<Q>Have you seen Santiago's stuff?</Q>

00:24:41 - Jake Maymar
It's on Twitter. Let me see if I can get you one that's not on Twitter. Here you go — this is a YouTube link. [link:Underfitted YouTube channel]

00:24:50 - Juan Torres
I just have some social media sites blocked so I don't get distracted.

00:25:01 - Juan Torres
Yeah, I got it here. It's Underfitted.

00:25:06 - Jake Maymar
Yeah, his name is Underfitted now — it's Santiago. I haven't actually gone through his YouTube. But yeah, he's great. Very, very accessible. Foundational stuff, but also some really brilliant practical applications.

00:25:43 - Jake Maymar
▶ He shows here how you can basically spin up a model using MCP and do just about anything you want to do with it. Pretty cool.

00:26:01 - Jake Maymar
You'll totally get it when you see it — like, oh, that's cool. Well, hey, man, it's great talking with you. I look forward to seeing where you're going. It looks like you're already going to pretty cool places. I guess I will talk to you on Thursday.

00:26:15 - Juan Torres
Definitely, Jake. Take care.

00:26:19 - Jake Maymar
Take care. Talk to you. Bye.

00:26:20 - Juan Torres
Bye.

---

=== UNRESOLVED SPEAKERS ===

No speaker alias map was provided in the `SPEAKER_ALIASES` context block (the template variable was not populated). The following speaker names appear in the transcript and have been passed through unchanged:

- **Juan Torres**
- **Jake Maymar**
- **Brandon** (referenced by both speakers as a community member who provides feedback and tutorials; not a direct speaker)
- **Sebastian**, **Paul** (mentioned by Jake as contacts knowledgeable about evals; not direct speakers)
- **Adam Schroeder** (referenced as manager of the Charming Data YouTube channel; not a direct speaker)
- **Santiago** (referenced as creator of the Underfitted YouTube channel; not a direct speaker)