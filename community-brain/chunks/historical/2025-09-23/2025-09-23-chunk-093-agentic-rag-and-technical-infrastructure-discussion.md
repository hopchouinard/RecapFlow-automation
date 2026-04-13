---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Jake Maymar", "Juan Torres", "Patrick Chouinard"]
chunk_id: "2025-09-23-chunk-093"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** The team discussed optimizing infrastructure for Agentic RAG by shifting to EC2 instances for better horizontal scalability, with Bastian suggesting that adjusting CPU and RAM configurations could reduce latency to the first token. Additionally, the conversation shifted to technical challenges regarding document processing, specifically how to effectively chunk complex PDFs containing merged table cells.

[02:04:24] Juan Torres: So then that's when we decided to then reorganize around an EC2 instance and then provide the option for scale, horizontal scalability, given the demands of the specific project.
[02:04:38] Juan Torres: Um, but that's, that's a really good, that's a really good interest.
[02:04:42] Bastian: Maybe if you took the CPU, you could, you could see like some quick, uh, wins and, and have like sort of, uh, quickly estimate on a more optimal point.
[02:04:51] Bastian: Because, uh, maybe if you go, uh, like one step, uh, below, it's just the same, or maybe if you go like one step higher, you get like, I don't know, like 20%, uh, less, uh, later.
[02:05:04] Bastian: Latency to the first token, I think that's what could be, I think speed, like in tokens per second, shouldn't change too much once it's loaded into the GPU or the cluster of GPUs, but the latency to the first token, I think that should be very influenced by the CPU and traditional RAM for its capacity to load this into the GPU and how they are connected through the different links.
[02:05:29] Bastian: So that's where I would look if you have a problem, like from latency to first, from question to first token, and then, yeah, the other thing I know I really have an explanation if it's like, once it's loaded in a GPU, it's slower than a bigger model, then I don't know.
[02:05:49] Juan Torres: Yeah, those are really good questions.
[02:05:53] Jake Maymar: So, Bastian, Patrick had a question about the, how you managed chunking.
[02:05:59] Jake Maymar: in the ship kit.
[02:06:01] Patrick Chouinard: Yeah, specifically about, uh,
[02:06:04] Patrick Chouinard: If you had to test with very complex PDF, especially including complex table with merge cell, because they're held to chung properly.
