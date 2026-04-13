---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Building a Portfolio App with RAG"
speakers: ["Alex Wilson", "Brandon Hancock"]
chunk_id: "2025-09-16-chunk-078"
---

# Building a Portfolio App with RAG

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Brandon Hancock recommends consolidating database, vector store, and blob storage needs into a single Supabase instance to simplify development and reduce long-term costs. The discussion concludes with the pair weighing the efficiency of this all-in-one approach against the potential drawbacks of losing multiple distributed free tiers.

[01:28:10] Brandon Hancock: We also get it for a Postgres database, beautiful.
[01:28:14] Brandon Hancock: It's a Postgres database, so we can also use it as a vector store.
[01:28:18] Brandon Hancock: And then the third one is we can use it as a blob store.
[01:28:21] Brandon Hancock: So anytime we want to upload images, documents, anything like that, it's all in one place.
[01:28:25] Brandon Hancock: Because in the past, I have found this painful developing.
[01:28:31] Brandon Hancock: It's like, okay, I'm going to hop over to Neon to look at my database.
[01:28:33] Brandon Hancock: I'm going to hop over to Clerk for Auth.
[01:28:36] Brandon Hancock: I'm going to hop over to Uploading or AWS or Google Cloud for blob.
[01:28:40] Brandon Hancock: And then for like, I'm going to hop over to Pinecone for a vector store.
[01:28:43] Brandon Hancock: I was in six apps and I was like, man, I just want to like, you know, because eventually once your app grows, you're going to not only have to pay on one platform, you got to pay on five, you know?
[01:28:52] Brandon Hancock: So it actually ends up costing less.
[01:28:56] Brandon Hancock: The gotcha is they all give that free tier.
[01:28:59] Brandon Hancock: And then you're like, oh, this is it's completely free.
[01:29:01] Brandon Hancock: But then the second it's not free, you're paying.
[01:29:02] Brandon Hancock: 20 bucks times five, rather than just 20 for everything.
[01:29:06] Brandon Hancock: So that's the, that's the main, main reason why I picked it.
[01:29:10] Alex Wilson: So would you recommend just doing the, I think the Supabase is 25 a month, that $25 a month plan?
