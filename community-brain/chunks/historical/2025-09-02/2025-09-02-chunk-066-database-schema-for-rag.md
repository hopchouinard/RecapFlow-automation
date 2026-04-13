---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Database Schema for RAG"
speakers: ["Brandon Hancock"]
chunk_id: "2025-09-02-chunk-066"
---

# Database Schema for RAG

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Brandon Hancock advises simplifying the database schema for RAG by storing document chunks and their associated embeddings directly within a single table rather than creating extra tables. He concludes that using tools like `pgvector` allows for efficient storage of these embeddings as simple numeric arrays alongside the raw text content.

[01:19:48] Brandon Hancock: All right, too many, too many windows for place.
[01:19:53] Brandon Hancock: One second, I'll show this.
[01:19:57] Brandon Hancock: But long story short, it just creates a column, actually, and within the column.
[01:20:02] Brandon Hancock: It is designed to be an embedding, which is nothing more.
[01:20:05] Brandon Hancock: An embedding is nothing more than an array of numbers.
[01:20:07] Brandon Hancock: So that's why I'm like, man, having to add a whole extra table just to store that information is a ton.
[01:20:16] Brandon Hancock: So yeah, let me show you this, because this is really that's all that's happening under the hood.
[01:20:19] Brandon Hancock: So I think this could hopefully save you some, save some complexity.
[01:20:23] Brandon Hancock: Okay.
[01:20:24] Brandon Hancock: Yeah, so, so this is where, like, here's literally what you would actually build in your database.
[01:20:33] Brandon Hancock: You would create a document chunk.
[01:20:35] Brandon Hancock: And all a chunk is, is it is referring to the document it came from, the actual raw content.
[01:20:43] Brandon Hancock: You want to make sure you say that as a text field.
[01:20:46] Brandon Hancock: If you're in AWS land, you're probably going to have to just say, like, it's a, I can't remember the exact fields you can use, but don't, just do a very high character count, or if they have the text field.
[01:20:55] Brandon Hancock: From there, this is it.
[01:20:58] Brandon Hancock: I think you add PG vector, all it's doing is it's saying, oh.
[01:21:02] Brandon Hancock: So I'm going to save 15,000 or 1,536 integers or floats in an array, and that's it.
