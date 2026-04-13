---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Juan Torres"]
chunk_id: "2025-09-23-chunk-092"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** The participants discussed whether smaller model parameters yield faster token speeds, concluding that infrastructure bottlenecks—specifically cloud provider hardware limitations—often dictate performance more than model size. Consequently, they shifted from using isolated GPUs on specialized platforms to scalable EC2 instances to better manage cost-efficiency and horizontal scaling requirements.

[02:02:33] Bastian: like bottlenecks, because in theory, if its size is the most...
[02:02:38] Bastian: is the most determined factor, like parameter size, and as long as that fits in your GPU memory and it's just one model for one GPU, and you compare like 8 billion to 20 billion parameters, I see no reason why it would be faster for the...
[02:02:58] Bastian: I mean, I see no reason why it would be harder for us...
[02:03:03] Bastian: Small model to produce more token speed output, unless the bottleneck is somewhere else.
[02:03:13] Juan Torres: That's a really good question, the question of if there is any additional cost of recruiting more instances, given the demands of the specific environment.
[02:03:25] Juan Torres: Because the reason that I can't really rely on one 8.100 in AWS is because they don't offer one single 8.100 GPU.
[02:03:38] Juan Torres: They offer like an EC2 instance with like 8.10, and then 8.10 with more CPU capacity, more CPU capacity.
[02:03:51] Juan Torres: And then it jumps to a bundle of 8.10, and then it jumps to a bundle of 8.100.
[02:03:59] Juan Torres: So I actually carry the cost-benefit for my client, and that's...
[02:04:03] Juan Torres: So recently, we opted for Oculus at the beginning because they were actually offering an 8100 isolated, right?
[02:04:11] Juan Torres: So in the cost-benefit schema, it made sense to go for that option.
[02:04:17] Juan Torres: The problem is that at one point, there were some costs that were not perceived at the beginning.
[02:04:24] Juan Torres: So then that's when we decided to then reorganize around an EC2 instance and then provide the option for scale, horizontal scalability, given the demands of the specific project.
