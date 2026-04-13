---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Jake Maymar", "Juan Torres"]
chunk_id: "2025-09-23-chunk-087"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Juan Torres and Jake Maymar discussed the infrastructure challenges of deploying local LLMs for tabular data inference, specifically noting that while 4-bit quantized 20B parameter models require less VRAM, they have unexpectedly experienced slower inference speeds. The two explored the trade-offs between model size and performance, questioning the technical expectation that quantization should inherently increase speed.

[01:54:08] Juan Torres: And so now, today, I'm actually going forward with the development of downloading LLMs in order to carry some tabular data inferences.
[01:54:23] Jake Maymar: Nice, nice.
[01:54:25] Jake Maymar: So the LMs, are they using, like, KimiK2, or, like, or what sort of?
[01:54:38] Juan Torres: I wish I could use the, are you talking about the 1 trillion parameter model?
[01:54:42] Jake Maymar: Well, I heard the quantized version was pretty good, and then there was, like, but I don't know.
[01:54:49] Jake Maymar: I mean, I, I, I'm just kind of curious to see what models you're using, um, to, to do inference.
[01:54:57] Juan Torres: Right now, for the limited environment, I mean, even when I was deploying the LLM,
[01:55:04] Juan Torres: On an 8100 GPU with 40 gigabytes of VRAM, I was deploying 8 billion parameters, and it was taking a substantial amount of the GPU capacity.
[01:55:22] Juan Torres: And then, like I was saying in the previous call, was using the GPT OSS 20 billion parameter that it's quantized to 4 bits in order to carry some inferences.
[01:55:34] Juan Torres: And it was actually requiring less GPU capacity.
[01:55:38] Juan Torres: But the thing is that it's giving out actual space for slowness.
[01:55:45] Juan Torres: The speed is actually decreasing when it's being quantized.
[01:55:48] Juan Torres: And I know, what's his name?
[01:55:51] Juan Torres: There was someone that was working with Maxim.
[01:55:53] Juan Torres: He was talking about, well, when you quantize it, isn't it supposed to actually go faster?
