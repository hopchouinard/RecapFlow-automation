---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Quantized Models and Performance Testing"
speakers: ["Brandon Hancock", "Juan Torres"]
chunk_id: "2025-09-02-chunk-061"
---

# Quantized Models and Performance Testing

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Juan Torres is exploring a decision tree strategy to optimize GPU resource allocation by comparing Mistral (16-bit) and GPT-OSS (4-bit quantized) models. He concluded that while the 4-bit quantization process makes GPT-OSS slower in tokens per second, the model maintains superior reasoning capabilities compared to Mistral.

[01:12:29] Juan Torres: So we're thinking of bringing a decision tree in the accounting application to use more, a more reserved model, like OOS, in order to carry out tasks when the big GPU from A100 is not available quick because their servers are requesting that GPU through several users, so it's an on-demand GPU really, right?
[01:12:56] Juan Torres: So now I have to make a strategy for my client to be able to utilize.
[01:13:00] Juan Torres: make sure.
[01:13:02] Juan Torres: Lower models compared to Mistral, for example, because I was making an A-B test in between Mistral and GPT-OSS.
[01:13:10] Juan Torres: And despite the fact that Mistral is an 8 billion parameter and GPT-OSS is a 20 billion parameter, GPT is actually performing slower.
[01:13:22] Juan Torres: And the reason that it's performing slower than the 8 billion parameter is because it's quantized to a 4-bit quantization, while Mistral is quantized to 16-bits.
[01:13:34] Juan Torres: So the quantization process is slowing the performance of a GPT, despite the fact that it has more parameters, which was not surprising.
[01:13:45] Juan Torres: I always knew that the quantization process was going to affect the performance.
[01:13:48] Juan Torres: It doesn't decrease the accuracy in the reasoning complex tasks completion.
[01:13:58] Juan Torres: In some ways, it's actually better than Mistral.
[01:14:00] Juan Torres: So… But it's…
[01:14:02] Juan Torres: Definitely slower, and so when you ask the question of why is it using less tokens per second, like about 15 tokens per second, it's because it's actually a quantized model, so it's going to be performing at that level, yeah.
[01:14:16] Brandon Hancock: Okay, I have a few questions for you because I love that you're digging into this.
