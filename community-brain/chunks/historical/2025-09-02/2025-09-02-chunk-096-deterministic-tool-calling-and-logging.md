---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Deterministic Tool Calling and Logging"
speakers: ["Brandon Hancock", "Jake Maymar"]
chunk_id: "2025-09-02-chunk-096"
---

# Deterministic Tool Calling and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** To manage intensive tasks like document processing efficiently, Brandon recommends utilizing a queuing system rather than PubSub to control job volume and prevent infrastructure costs from spiraling. He suggests spinning up new agent instances per request to ensure modular workflows and confirms that a queue is the most effective approach for scaling production demands.

[01:53:03] Brandon Hancock: You should be calling like agent kickoff, like if you were using Cray, I would kick off an entire new workflow to handle that response.
[01:53:09] Brandon Hancock: So each request is going to spin up its own version or instance of those agents doing work and then submitting back a response.
[01:53:17] Brandon Hancock: So, but to dive into it deeper, yeah, so when it comes to like PubSub versus your agents, another option definitely recommend is a queue.
[01:53:28] Brandon Hancock: I mean, any, any queuing service would be insanely helpful.
[01:53:33] Brandon Hancock: Um, uh, like just for example, like on the RAG SAS stuff that I was working on for you guys for ShipKit, we have to use queues because document processing is a very intensive job and we're dynamically spinning up containers, depending on how many requests come in, but we only want to just not explode costs.
[01:53:52] Brandon Hancock: We might only allow 20 documents to be processed at the same time.
[01:53:55] Brandon Hancock: So we need a queue to slowly add in as availability comes online.
[01:54:00] Brandon Hancock: So I would try to learn more about what your, uh, what your, uh,
[01:54:03] Brandon Hancock: Production environment looks like to recommend PubSub versus Q, but I think Q is the way to go instead of, yeah, that's what I would recommend probably right now.
[01:54:13] Brandon Hancock: Also, Patrick, love to hear that you bought Magnet.
[01:54:17] Brandon Hancock: It's so funny when my friends say they watch me use a computer, they're like, it just doesn't make sense.
[01:54:22] Brandon Hancock: Things are just hopping around on your screen, like you're not touching stuff.
[01:54:25] Jake Maymar: What's going on?
[01:54:26] Brandon Hancock: It's literally Magnet.
[01:54:27] Brandon Hancock: So that's the best $10, $8 you'll spend on a Mac.
