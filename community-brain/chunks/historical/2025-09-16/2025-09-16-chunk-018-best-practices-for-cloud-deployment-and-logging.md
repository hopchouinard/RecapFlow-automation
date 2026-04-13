---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Best Practices for Cloud Deployment and Logging"
speakers: ["Brandon Hancock", "Marc Juretus"]
chunk_id: "2025-09-16-chunk-018"
---

# Best Practices for Cloud Deployment and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Marc and Brandon discussed the architecture for a Railway-hosted FastAPI/LangChain application, specifically debating whether to use Supabase APIs or direct Postgres connection strings. Brandon concluded that a shared database approach—where applications interact via a common Postgres backend rather than sending data between each other—is the faster and more secure architectural choice.

[00:17:48] Marc Juretus: So I'll do that on railway with Lang chain and land graph.
[00:17:50] Marc Juretus: I will ask you this though.
[00:17:54] Marc Juretus: Is the best way for using Supabase and I'm going to use fast API.
[00:18:00] Marc Juretus: It's best off to use the actual Postgres connection string as opposed to the APIs for security reasons.
[00:18:07] Marc Juretus: Is that a more secure way of going at it to get into data?
[00:18:11] Brandon Hancock: Yeah.
[00:18:12] Brandon Hancock: So the question, I'll restate the question, which is at the end of the day, for most real world AI applications, you end up with a database and multiple sub applications.
[00:18:23] Brandon Hancock: So in Mark's scenario, he's probably going to have a web application.
[00:18:27] Brandon Hancock: Cool.
[00:18:28] Brandon Hancock: That's running somewhere.
[00:18:29] Brandon Hancock: He's going to have a Python application of some part, Langchain, Cure AI, something.
[00:18:33] Brandon Hancock: And usually you have to get both of these applications to, you know, listen to each other.
[00:18:38] Brandon Hancock: So there's multiple paradigms.
[00:18:40] Brandon Hancock: Paradigm one is your Python application.
[00:18:44] Brandon Hancock: Every time it needs something, it sends it to your front end.
[00:18:46] Brandon Hancock: It sends it to your Next.js application.
[00:18:48] Brandon Hancock: That's paradigm one.
[00:18:49] Brandon Hancock: Paradigm two is they actually do not talk to each other directly at all.
[00:18:54] Brandon Hancock: Everything is shared in a common shared database, which is I think you will have much
[00:19:00] Brandon Hancock: It'll be faster, more secure.
