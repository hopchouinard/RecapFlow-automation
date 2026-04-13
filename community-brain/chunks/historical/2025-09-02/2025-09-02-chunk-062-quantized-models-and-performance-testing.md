---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Quantized Models and Performance Testing"
speakers: ["Brandon Hancock", "Juan Torres"]
chunk_id: "2025-09-02-chunk-062"
---

# Quantized Models and Performance Testing

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Brandon Hancock and Juan Torres discussed the historical challenges of using quantized open-source models for tool calling, noting that while older versions struggled with generating valid JSON, newer iterations like Mistral and GPT-based OSS models show potential for improvement. Consequently, Torres plans to incorporate tool access into his future performance testing to evaluate how these current models handle those specific tasks.

[01:14:16] Brandon Hancock: Okay, I have a few questions for you because I love that you're digging into this.
[01:14:20] Brandon Hancock: I have not got to go deep into, like, the open source models since, like, Crew AI days, so a few questions for you.
[01:14:27] Brandon Hancock: So, tool calling, how is tool calling performing for you on these models?
[01:14:32] Brandon Hancock: Because I know at the time, like, Llama 2, very early Llama 3, was really struggling with tool calling.
[01:14:39] Brandon Hancock: Like, you would literally see the tool call, and you're like, that's gibberish.
[01:14:42] Brandon Hancock: Like, it really wasn't even actual valid JSON, so we had to build in all sorts of safeguards, because the models weren't there yet.
[01:14:49] Brandon Hancock: So, how are the Mistral and the new GPT OSS performing, like, tool-wise?
[01:14:56] Juan Torres: A tool calling, that's actually a parameter that I haven't used, that I haven't tested.
[01:15:02] Juan Torres: So that's a really good suggestion, because at one point, we're going to be giving tools to these open source models, and I actually need to start giving them the access to tools in order for them to perform that kind of task.
[01:15:15] Brandon Hancock: So that's really good.
[01:15:17] Brandon Hancock: Yeah, I would just be curious for science, because old school, these models, eight months ago, really struggled.
[01:15:26] Brandon Hancock: Six months ago, really struggled.
[01:15:28] Brandon Hancock: But I know you could see it in each iteration, they got better.
[01:15:32] Brandon Hancock: So I'm pumped.
[01:15:33] Brandon Hancock: I'm thinking you'll see really good results.
[01:15:34] Brandon Hancock: I'm very optimistic for the GPT one, but hey, you'll let us know, man.
