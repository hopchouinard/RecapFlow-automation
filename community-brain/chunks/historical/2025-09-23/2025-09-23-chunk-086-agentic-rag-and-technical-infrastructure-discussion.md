---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Juan Torres"]
chunk_id: "2025-09-23-chunk-086"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** Juan Torres discusses overcoming GPU limitations in Agentic RAG infrastructure by utilizing CPU offloading and memory allocation strategies on EC2 instances. He concludes by detailing his workflow for managing client-side permissions and virtual private clouds to support upcoming local LLM development for tabular data inference.

[01:51:53] Juan Torres: Juan You'll be surprised that you actually need way more GPU in order to handle those.
[01:51:58] Juan Torres: Juan And those have been only for funds.
[01:52:03] Juan Torres: Juan
[01:52:03] Juan Torres: I then have to trade the A10s for financial processing information, but the way I've been trying to go around it is by engaging in CPU offloading, so you can basically set up the EC2 instance to use the, let's say, the A10 has 24 gigabytes of VRAM, and then you have, let's say, 16 gigabytes of CPU, so what you can do is start, set up the environment to upload a lot of the processing power from the CUDA environment to the CPU, and then what you can do, and I've been trying to do in order to maximize the environment's capacity, is apparently you can convert some of the memory, some of the, like, S, S, S, the,
[01:53:03] Juan Torres: memory into actual processing capacity, you can recruit it to in order to handle some of the capacity to, and you can do it permanently, you can, you know, if you're like dealing with 15 gigabytes, 100 gigabytes, or 150, you can recruit a percentage of that memory that you will have in order to just have your files saved there, to basically be used for inferences.
[01:53:33] Juan Torres: So I've just been playing around with EC2 instances for, and the reason that I give myself that flexibility is because I'm running the EC2 instances for my clients, but then a parallel personal EC2 instance, because sometimes I'm dealing with permissions issues, so I just have to know what are some of the permissions that I have to send over to my client in order for him to give me the capacity to give me some
[01:54:03] Juan Torres: changes in EC2 instances, virtual private clouds.
[01:54:08] Juan Torres: And so now, today, I'm actually going forward with the development of downloading LLMs in order to carry some tabular data inferences.
