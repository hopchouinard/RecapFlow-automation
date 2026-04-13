---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Juan Torres"]
chunk_id: "2025-09-23-chunk-090"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Bastian and Juan discussed infrastructure bottlenecks related to CPU-to-GPU latency during horizontal scaling and the impact of NVIDIA interconnects on performance. They concluded that isolating processes—specifically moving chunking tasks to a separate instance from the inference pipeline—is the most optimal architectural approach for Agentic RAG systems.

[01:59:03] Bastian: And I think in those cases, you might actually find a bottleneck where the CPU is not fast enough to load the model into the GPU, and that's a bottleneck that's not trivial, I mean, it depends, that's the only, like, when does a processor, a CPU matter for ML loads that run in GPU, well, it's just like to give it the instructions to load the model into the, into the memory.
[01:59:33] Bastian: So, if, if you are doing horizontal scaling and those instances are cold, you will pay that cost upfront for every, every instance you, you spawn, and that's the difference with, like, the other kind of scaling, not horizontal, I'm sorry, but what's it called, but then the model fits and you just spawn more instances, right, and, and then you don't pay that bottleneck for the CPU, you paid only once.
[02:00:01] Bastian: Uh, and the other thing that Kenny.
[02:00:04] Bastian: Obviously, they have these very optimized racks, so to speak, but the actual cables that link the GPUs are also a factor that weighs into, and maybe more modern GPUs, I'm just supposing, they may have better link methods developed by NVIDIA and such.
[02:00:26] Juan Torres: Are you facing that bottleneck yourself?
[02:00:30] Bastian: Not, no, but it's part of the things I had to study when I was considering using a GPU for the chunking in Chipkit.
[02:00:40] Juan Torres: Oh, yeah.
[02:00:41] Juan Torres: Well, for the chunking, are you kind of like isolating the processing of the chunking and the rack into another instance, or are you doing it in the same instance in which you're going to have the inference pipeline?
[02:00:57] Bastian: I went through, like, every option.
[02:00:59] Bastian: I think the most optimal way would be to use a GPU and only have...
