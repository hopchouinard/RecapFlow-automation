---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Jake Maymar", "Juan Torres"]
chunk_id: "2025-09-23-chunk-089"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Juan Torres recommends horizontal scaling over vertical scaling for the project's infrastructure to prioritize GPU capacity rather than unnecessary CPU expansion. The team concludes that while horizontal scaling effectively manages GPU "real estate" for large models, they acknowledge a potential bottleneck involving CPU load times during model deployment.

[01:57:40] Juan Torres: It's called horizontal scaling because you have the recruiting of several instances of a computational unit across a similar, across the same EC2 instance, versus vertical scaling, in which you actually go on a hierarchy of EC2 instances, that is, of computational computational units, and computational units, it's
[01:58:03] Juan Torres: It's to have more capacity as you go over, right?
[01:58:06] Juan Torres: So here, horizontal scaling, we're just recruiting the same 810 GPUs across several, you know, one or two or three of them, right?
[01:58:17] Juan Torres: And the reason that I'm recommending for horizontal scaling is because what we're trying to recruit here is GPU real state instead of CPU real state.
[01:58:29] Juan Torres: And if you go over, you were to out for the vertical scaling, you will be basically not maximizing the GPU real state, and you will be more or less getting more CPU capacity.
[01:58:44] Jake Maymar: Man, Juan, that's amazing.
[01:58:46] Jake Maymar: Oh, go ahead.
[01:58:46] Bastian: Sorry.
[01:58:48] Bastian: Juan, I was going to ask a question just to confirm.
[01:58:50] Bastian: So if I understand correctly, horizontal scaling is traditionally used in ML models because when the model doesn't fit in your, like, one instance, so you do horizontal...
[01:59:03] Bastian: And I think in those cases, you might actually find a bottleneck where the CPU is not fast enough to load the model into the GPU, and that's a bottleneck that's not trivial, I mean, it depends, that's the only, like, when does a processor, a CPU matter for ML loads that run in GPU, well, it's just like to give it the instructions to load the model into the, into the memory.
