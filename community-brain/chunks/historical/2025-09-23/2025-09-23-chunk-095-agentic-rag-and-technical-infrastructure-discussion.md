---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Patrick Chouinard"]
chunk_id: "2025-09-23-chunk-095"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Bastian and Patrick discussed the limitations of traditional chunking for complex financial tables, concluding that such content is often unreadable when processed via standard OCR methods. Instead, they proposed separating these complex pages from the rest of the document and using LLMs with advanced vision capabilities to interpret the data directly.

[02:07:34] Bastian: I've cut some of these models, like, yeah, like, define that, uh, what looks like your, uh, most typical use cases, and, and of course, if you can, like, uh, like, front load some of the processing, like, pre-processing the, the, the, PDFs can make sense in some cases.
[02:07:52] Patrick Chouinard: Yeah, because a lot of the problem we've encountered, because we're, we build our own, uh, RAG system, and, uh, it's for financial industry, and they have a lot of very complex table that have, uh, and, uh,
[02:08:04] Patrick Chouinard: Merge column, merge rows, merge cell part of the table, and chunking makes it almost unreadable.
[02:08:12] Patrick Chouinard: It's extremely complex to chunk it in a way that the LLM will understand, oh, those two cells are actually reporting to those two rows.
[02:08:21] Bastian: I think it's borderline impossible for that type of document.
[02:08:27] Bastian: I think those should be handled, like, separately.
[02:08:31] Bastian: Like, maybe, like, okay, I have, like, this 30-page PDF, but there are, like, these four pages that are super heavy on graphics and stuff like that, and super technical.
[02:08:41] Bastian: And I think those would benefit more, like, from an LLM with very good vision capability, instead of trying to chunk it, like, with traditional OCR, which is what Doug Lynn and all this stuff do, like, under the hood.
[02:08:56] Bastian: They may have better, faster models, but it's still, like, the same technique.
[02:09:00] Bastian: So I think those that need, like, a deeper understanding...
