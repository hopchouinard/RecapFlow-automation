---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Database Schema for RAG"
speakers: ["Brandon Hancock", "Juan Torres"]
chunk_id: "2025-09-02-chunk-067"
---

# Database Schema for RAG

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Brandon Hancock advises storing vector embeddings directly within the existing database table rather than creating a separate database or table. He concludes by emphasizing the importance of indexing these fields to optimize RAG query performance from O(n) to O(log n).

[01:21:02] Brandon Hancock: So I'm going to save 15,000 or 1,536 integers or floats in an array, and that's it.
[01:21:09] Brandon Hancock: So I really wouldn't make a whole extra table just to store.
[01:21:14] Brandon Hancock: I wouldn't make a whole extra database to store what could have been done in a single table.
[01:21:20] Brandon Hancock: So that would be a final recommendation.
[01:21:22] Brandon Hancock: And the very last thing is you want to make sure you index your table.
[01:21:27] Brandon Hancock: I can't remember if I can show indexes in here.
[01:21:29] Brandon Hancock: But you just want to make sure you allow indexing on this field right here to speed up your RAG queries.
[01:21:37] Brandon Hancock: That's the final thing I'd say.
[01:21:40] Brandon Hancock: Just because if not, every query is going to take O of n time versus O of log n time.
[01:21:45] Brandon Hancock: So that's my, like, deep dive into RAG.
[01:21:50] Brandon Hancock: Sorry if I got nerdy, but I just want to make sure you, I've been working so much on the RAG sub recently.
[01:21:56] Brandon Hancock: So just want to make sure you don't say, I've wasted so much time.
[01:22:01] Brandon Hancock: So steal my lessons.
[01:22:01] Brandon Hancock: That's great.
[01:22:02] Brandon Hancock: Yeah, perfect.
[01:22:04] Brandon Hancock: That's great.
[01:22:05] Brandon Hancock: you have questions, happy to dive deeper into it.
[01:22:08] Juan Torres: Awesome.
[01:22:09] Brandon Hancock: Thank you.
[01:22:09] Brandon Hancock: Okay.
[01:22:10] Brandon Hancock: Of course.
