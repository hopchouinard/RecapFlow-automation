---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Patrick Chouinard"]
chunk_id: "2025-09-23-chunk-096"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** The participants discussed using agentic RAG with vision capabilities to process complex documents containing tables and graphics that standard text-based embeddings struggle with. They concluded that a hybrid approach—integrating standard text chunks with additional image context at inference time—is a viable solution, though they noted that current document intelligence tools remain inconsistently stable.

[02:09:00] Bastian: So I think those that need, like, a deeper understanding...
[02:09:04] Bastian: Sending on, like, the domain, knowledge domain, yeah, I think, like, agents with vision is basically the way to go for those concrete, like, pages, but then you will lose the benefit of the embedding or you will have to, like, handle that a bit separately, so that's another trade-off.
[02:09:25] Patrick Chouinard: Exactly, and it's not really doable in, not real-time, but while the user is waiting, basically.
[02:09:31] Bastian: Yeah, but something that you could do is, like, actually, if you have documents like this, which, yeah, they contain some hard graphics but are mostly text, for example, a book of some domain-like business or stuff like that, you could maybe, like, do the chunking, do the embeddings for everything text-related, and just have the model bring the images as additional context for it to analyze at inference time.
[02:09:59] Bastian: I think that could work.
[02:10:02] Patrick Chouinard: Yeah, when it's image, it's not...
[02:10:04] Patrick Chouinard: hard because you can have a text description of what the image is, and you can chung that, but a table, it's really specific.
[02:10:11] Bastian: Yeah, tables and graphics and stuff like that, but I'd like to have the model bring those to at inference time to analyze it and use them to improve the answer so it receives like the rag input, the chunks it retrieved, but also like, oh, yeah, this document has also these images, do you want me to add these to the analysis?
[02:10:33] Bastian: And have like some idea of where in the text they go, so which is related to whatever topic, for example.
[02:10:43] Patrick Chouinard: Okay, right now we're using document intelligence, but honestly, it's not the most stable thing in the world.
