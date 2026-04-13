---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Paul Miller"]
chunk_id: "2025-09-23-chunk-077"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Paul and Bastian discussed the feasibility of hosting the Shipkit stack outside of Google Cloud, with Bastian noting that Google’s infrastructure allows for predictable, usage-based scaling that drops to zero when idle. They concluded that while costs are transparent and manageable, overall expenses depend primarily on the configured user queue limits and instance scaling settings.

[01:37:57] Paul Miller: That's very, that's, I'd be really interested for you to, for you Bastian,
[01:38:03] Paul Miller: Your thoughts on, because you've had a little bit more exposure on the looking at the Shipkit stack, is it something that we can do with a host, with a different type of hosting partner other than Google?
[01:38:19] Paul Miller: Is that going to be an option with Shipkit?
[01:38:27] Bastian: I don't really know, I wouldn't like to talk in Brandon's place, but what I can tell you is that the costs in Google Cloud are pretty, like, you can know upfront how much it will cost, at least have, like, minimums and maximums, so you can, like, have a really complete idea.
[01:38:55] Bastian: I mean, basically, the version I was working, at least, it was run in CPU.
[01:39:03] Bastian: So you basically just, like Brandon mentioned, minimal instances is zero, so it scales back to zero.
[01:39:10] Bastian: And so baseline costs are nothing, basically.
[01:39:15] Bastian: But the costs come when you add users, and that depends on how much vCPU you have, RAM, and the maximum instances.
[01:39:29] Bastian: And then you only, like, since they charge basically in time that you use the virtual machines, it's very predictable.
[01:39:42] Bastian: I mean, of course, if you set, like, maximum instances to, like, 20 versus 10 or 30, then your costs will be very variable.
[01:39:51] Bastian: But it all depends on how you, like, run the queue for your users, and you can obviously customize that further.
[01:39:58] Bastian: But I think this has to do with your question about...
