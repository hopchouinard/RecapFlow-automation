---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Jake Maymar", "Paul Miller"]
chunk_id: "2025-09-23-chunk-076"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Paul and Jake discussed the risks of cloud infrastructure costs, specifically contrasting the lack of hard budget caps in Google Cloud with Amazon’s ability to automatically stop services when limits are reached. They concluded that establishing reliable, controlled resource access is a priority for their upcoming Agentic RAG MVP and future deployments.

[01:36:39] Paul Miller: It's like, that scares the bejesus out of me.
[01:36:44] Paul Miller: Give me any of those hosts where I say, alright, I'm getting a host, I'm getting four cores, I'm getting a whole lot of disk, and I'm getting controlled access to GPU, and I have a cap.
[01:36:58] Paul Miller: That's kind of what I want when I'm doing an experiment.
[01:37:01] Paul Miller: And we're getting a...
[01:37:03] Paul Miller: um, MVP out there.
[01:37:05] Jake Maymar: Yeah, no, I totally agree.
[01:37:07] Jake Maymar: And, and it's, you know, I'm curious, I, I'm really looking forward to sort of when we start talking about the deployments and everything, just, you know, because I saw you had the alerts, but they didn't seem like it was a way to basically restrict, like hard restrict.
[01:37:24] Paul Miller: Uh, it doesn't, that doesn't work with Google.
[01:37:27] Paul Miller: A Google alert, you get the next day.
[01:37:31] Jake Maymar: So, wow, so there's the bill.
[01:37:34] Paul Miller: Yeah, it's not like Amazon.
[01:37:37] Paul Miller: Amazon, you get an alert, and you could set a budget limit, and it just stops, the service just stops.
[01:37:43] Paul Miller: Right, right.
[01:37:44] Paul Miller: Google, it just keeps, it's, oh, we'll process the alerts once a night, and then the next day you get the bill and the alert.
[01:37:54] Jake Maymar: Ooh.
[01:37:55] Jake Maymar: Yeah, that's, that's painful.
[01:37:57] Paul Miller: That's very, that's, I'd be really interested for you to, for you Bastian,
