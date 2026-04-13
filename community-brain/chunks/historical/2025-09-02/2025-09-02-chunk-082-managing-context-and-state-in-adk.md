---
session_date: "2025-09-02"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Managing Context and State in ADK"
speakers: ["Ola Oyo"]
chunk_id: "2025-09-02-chunk-082"
---

# Managing Context and State in ADK

**Session:** Weekly Coaching Call | **Date:** 2025-09-02

**Summary:** Ola Oyo discussed the challenges of integrating a Dockerized Postgres database with ADK and the custom tooling required to feed that data into his models. He concluded by seeking advice on optimizing token usage, noting that passing persistent state between tools has caused his request costs to balloon to 100k tokens.

[01:36:16] Ola Oyo: Is that what I'm hearing?
[01:36:17] Ola Oyo: Yeah, persistent storage is saving to the database.
[01:36:20] Ola Oyo: But I think the major issue that I had then was the examples had SQLite, but I was trying to save to a Postgres database sitting in a Docker container.
[01:36:30] Ola Oyo: Yeah.
[01:36:31] Ola Oyo: So there was just a bit of, you know, tooling that I had to use to do that.
[01:36:35] Ola Oyo: And then also in terms of being able to get, like, data directly from the database also, I've had to do quite a bit of tooling where, through my ORM, I sort of get all of that data ready, and then just sort of, like, mix it and then get it passed to the model, and then the model is then able to go much faster in it.
[01:36:54] Ola Oyo: So that's been pretty much what I've been on to.
[01:36:57] Ola Oyo: The one thing I have seen is an exponential.
[01:37:02] Ola Oyo: a Sorry.
[01:37:03] Ola Oyo: for
[01:37:08] Ola Oyo: So I was just wondering, like, you know, how do you, how do you reduce the number of tokens as you're passing that state from one tool to another, because I've seen my token count for a request go as high as up to 100k tokens, and it's just exponentially growing up, and I'm like, wow, that's huge, because it's quite a huge chunk it's taken in.
