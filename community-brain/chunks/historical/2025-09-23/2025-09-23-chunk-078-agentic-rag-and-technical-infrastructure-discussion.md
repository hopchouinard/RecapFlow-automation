---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Jake Maymar"]
chunk_id: "2025-09-23-chunk-078"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Bastian explained that while containerization makes Agentic RAG systems technically portable, varying cloud-specific configurations like cold starts and CPU scaling make cross-platform deployment complex and unsupported. Consequently, the group concluded they will focus on peer-to-peer knowledge sharing regarding deployment strategies and platform-specific troubleshooting to navigate these infrastructure challenges.

[01:39:58] Bastian: But I think this has to do with your question about...
[01:40:03] Bastian: Deploying in other clouds, in theory, you can, because it's all containerized, but I don't think, if I were Brandon, I wouldn't necessarily offer support to help you set this up in Amazon, for example, because it's really, this is the pain, it's not just like what you guys were talking about a few months ago, the real issue is the deployment and getting it to work within the constraints of this particular cloud and system.
[01:40:33] Bastian: In spite of all having equivalent services, like the parameters that you will use are, even they have different names, even if they might do the same.
[01:40:44] Bastian: So for example, if you're going to handle like cold starts or boost CPU and start up for the containers, like all these variables are more nuanced than minimum instances and maximum instances.
[01:40:56] Bastian: But yeah, those are the key drivers.
[01:40:58] Jake Maymar: Nelisa,.D.: Yeah, that makes sense.
[01:41:01] Jake Maymar: sense.
[01:41:02] Jake Maymar: I think.
[01:41:03] Jake Maymar: think what's going to be interesting is we're all going to be running these systems, and so we're all going to, I mean, I'll definitely share notes on, you know, costs and what I'm doing and deployment strategies and all those things, and I definitely will have an AWS deployment, I'll probably also have an Azure deployment, I'm sure other people will have that too, so that's what I'm really excited, I really feel like this is going to be a really great focus tool for the group, where we're like building these things and kind of sharing notes and kind of understanding less about the support, less more of like sharing notes, you know, okay, well, this deployment doesn't really work on this platform, you know, or it works, just make sure don't do this kind of thing.
[01:41:47] Jake Maymar: Oh, no worries.
