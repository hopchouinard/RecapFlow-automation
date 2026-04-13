---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Juan Torres", "Ty Wells"]
chunk_id: "2025-09-23-chunk-088"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Juan Torres discussed troubleshooting unexpected latency issues with quantized models in high-capacity environments, noting that the models performed slower than expected relative to their size. To address this for future scalability, he plans to test model performance on smaller 24GB GPUs and implement a horizontal scaling strategy using multiple instances.

[01:55:53] Juan Torres: He was talking about, well, when you quantize it, isn't it supposed to actually go faster?
[01:56:00] Juan Torres: And the reason that it's supposed to go faster is if it's like, how...
[01:56:03] Juan Torres: Well, the reason that it's going slow in the first place, it's because it's actually having a very limited environment.
[01:56:13] Juan Torres: And so when you quantize it, you actually give it space in order to go at a more sustainable pace.
[01:56:19] Juan Torres: But in my case, the issue is not GPU capacity.
[01:56:24] Juan Torres: The problem is that compared to other unquantized models, it is relatively slower.
[01:56:31] Juan Torres: So that's why he was basically having this, like, you know, he was perplexed by the fact that it was going slower than an 8 billion parameter model, that it's quantized to 16 bits.
[01:56:46] Ty Wells: So did he find, did he figure it out, how to resolve that, or not?
[01:56:52] Juan Torres: Well, both of them actually work pretty effectively in an 8.100 GPU, 40 gigabyte environment.
[01:57:00] Juan Torres: But now, what's happening is that...
[01:57:03] Juan Torres: We're transitioning from that kind of environment to an 810, 24-gigabyte environment, and I'm going to carry some tests in order to see if the models can run successfully in a more restricted GPU environment, because what's going to happen is, in order to make it scalable, I'm going to have to engage in a scaling group of recruiting several 810s in a group, in a bundle of horizontal scaling.
[01:57:40] Juan Torres: It's called horizontal scaling because you have the recruiting of several instances of a computational unit across a similar, across the same EC2 instance, versus vertical scaling, in which you actually go on a hierarchy of EC2 instances, that is, of computational computational units, and computational units, it's
