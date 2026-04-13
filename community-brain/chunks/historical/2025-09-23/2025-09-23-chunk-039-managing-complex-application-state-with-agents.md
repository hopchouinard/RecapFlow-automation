---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing complex application state with agents"
speakers: ["Alex Wilson", "Brandon Hancock"]
chunk_id: "2025-09-23-chunk-039"
---

# Managing complex application state with agents

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Alex Wilson is looking for an architectural solution to maintain complex, persistent state for multi-item quotes (bills of materials) as they are processed by a sequence of isolated, interdependent agents. The discussion focuses on identifying the best approach—such as using ADK state or artifacts—to ensure agents can consistently access and update status fields across a large, tabular dataset.

[00:48:21] Brandon Hancock: Quotes can contain up to 100 line items, and the JSON schema has multiple fields per line.
[00:48:27] Brandon Hancock: Do you recommend using ADK state to maintain this across or artifacts?
[00:48:33] Brandon Hancock: So, Alex, do you have, oh, wait.
[00:48:39] Brandon Hancock: I was like, it was your time to shine, I thought you were getting up to run away.
[00:48:44] Brandon Hancock: Do you want hop on your micro fast, just, just to, like, expand on a little bit more of what you're, what you're working on, I would be happy to clear it up.
[00:48:52] Alex Wilson: Yeah, so, like, maybe to define it better, I just, right now I have, like, like, each agent working in isolation, I've just built on their, like, own, so they're, like, going from input to output.
[00:49:01] Alex Wilson: But the outputs and now I'm trying to hook them up together and they need to like persist and be able to maintain around the status of this quote and that quote can be like working on a quote and it can be like a hundred line items in the quote and then that quote obviously from like if you take it like a tabular architecture it's got like each you know columns with fields in it so I'm trying to figure out now how do I like how do I maintain the state around the quote so that each as each agents accessing it there's persistent understanding of where where the status is basically the state of it okay and just to dive in a little bit deeper into it so like in my head like is this like a quote of like a hundred like are we building a house and we have to keep track of like okay the doors are going to cost we need two doors each door is two dollars or like a bill yeah it's like it's like a bill of materials so like okay here's your quote with you know each item and here's how much it you know it should cost it should
