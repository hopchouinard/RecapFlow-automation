---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Juan Torres"]
chunk_id: "2025-09-23-chunk-091"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Bastian and Juan discussed optimizing technical infrastructure for Agentic RAG by routing processing tasks based on media type, utilizing CPU for audio/video/text and GPU for PDF OCR tasks. They concluded that while exact LLM deployment needs vary, a GPU with 8–16GB of VRAM is likely sufficient for these specific chunking and processing requirements.

[02:00:57] Bastian: I went through, like, every option.
[02:00:59] Bastian: I think the most optimal way would be to use a GPU and only have...
[02:01:03] Bastian: A container that basically just does the OCR and chunking, and maybe you can have like two variants, it would be awesome like to, because processing things that require FFmpeg are actually much faster than processing OCR in a PDF, at least in the traditional ways, so you could actually like route everything very smartly, so everything can run in a CPU if it's like video and audio and all of that, but if you're, and text and markdown, but if you have PDFs, you, you will need to like, optimally, I think you would benefit more for, of using a GPU, and I think that's where you were going.
[02:01:46] Juan Torres: Are you seeing one bundle of GPUs, you mean?
[02:01:53] Bastian: No, in this case, it's not like as heavy as an LM in terms of size, so actually any GPU should work.
[02:02:03] Bastian: I'm
[02:02:03] Bastian: Like GPUs, like over 16 gigabytes or maybe less of VRAM, like eight might be enough, I don't know.
[02:02:12] Bastian: But yeah, it's different than your use case, but principles still apply.
[02:02:18] Juan Torres: What's the size parameters of your models that you're trying to deploy?
[02:02:24] Bastian: Oh no, it wasn't, it's just a theoretical, that's what I mentioned.
[02:02:28] Bastian: I haven't deployed LLMs in multiple instances, but I think those could be some...
[02:02:33] Bastian: like bottlenecks, because in theory, if its size is the most...
