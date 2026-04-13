---
session_date: "2025-09-23"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Agentic RAG and technical infrastructure discussion"
speakers: ["Bastian", "Paul Miller", "Ty Wells"]
chunk_id: "2025-09-23-chunk-082"
---

# Agentic RAG and technical infrastructure discussion

**Session:** Weekly Coaching Call | **Date:** 2025-09-23

**Summary:** The group discussed deployment strategies for Agentic RAG, noting that while Docker and Kubernetes provide a standard hosting framework, the primary technical burden lies in the initial OCR and chunking processes rather than query inference. Consequently, they concluded that system performance should be optimized for the resource-heavy front-loading of data rather than the retrieval phase.

[01:45:47] Paul Miller: To the point, and I, I don't know if everyone else does it this way.
[01:45:51] Paul Miller: I always start with, uh, Docker.
[01:45:54] Paul Miller: I've got a whole lot of back office hosts in Docker.
[01:45:58] Paul Miller: So I've got local Docker.
[01:45:59] Paul Miller: I've got my hosted, hosted Docker in.
[01:46:03] Paul Miller: in DigitalOcean, and then I've got stuff I've put into Google or Amazon, and I think if you follow Kubernetes or Docker approach, surely that would have been the best practice of deployment and hosting, rather than trying to code it, or is he just trying to leverage the No, it's not a host, it's the vector embedding part that is done, through their embedding models, because they're the only ones that can do the video, and the, you know, all the different types of images, and, like, all the different types, so, you're just doing a query to the embedding requests, right, and doing that reverse lookup, but it still ran on the Vercel app.
[01:46:53] Paul Miller: Right.
[01:46:54] Ty Wells: Right.
[01:46:54] Ty Wells: Yeah.
[01:46:55] Ty Wells: don't think there's any load, there's not much load, just the initial vectorization of whatever content, and then, yeah, you're
[01:47:03] Ty Wells: You're just accessing it.
[01:47:05] Bastian: If I can comment on just a caveat, actually, what's most, the most demanding process is by far chunking and the OCR process.
[01:47:15] Bastian: It's not, it's not the query part or inference, if we, if you will.
[01:47:20] Bastian: It's actually the part where you like front load all these files and you can, of course, update them afterwards.
