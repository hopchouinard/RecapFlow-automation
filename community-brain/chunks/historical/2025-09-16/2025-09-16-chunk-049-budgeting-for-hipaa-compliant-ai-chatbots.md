---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Budgeting for HIPAA-Compliant AI Chatbots"
speakers: ["Andrew Nanton", "Brandon Hancock", "Juan Torres", "Ola Oyo"]
chunk_id: "2025-09-16-chunk-049"
---

# Budgeting for HIPAA-Compliant AI Chatbots

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Juan proposes reducing infrastructure costs and enhancing security control by implementing custom logging directly within the code base of his EC2 instances rather than relying on standard AWS on-premise logging services. By managing logs locally through SSH access, he can effectively monitor GPU and LLM stress testing while maintaining precise oversight of his computational expenses.

[00:53:31] Andrew Nanton: Maybe he'll have some better answers for you.
[00:53:34] Ola Oyo: Okay.
[00:53:35] Juan Torres: In terms of my logging mechanism, I take complete control of the environment, and I create my own logging mechanisms without using the on-premise.
[00:53:51] Juan Torres: Because AWS also has a watch, what is it called, watch lock application that allows you to keep your logs.
[00:53:59] Juan Torres: Yeah.
[00:53:59] Juan Torres: And so, I just rather.
[00:54:01] Juan Torres: Have control of the environment and free the login for the test of the GPU stress testing or the LLM stress testing.
[00:54:14] Juan Torres: So, I mean, that's going to create some computational, you know, needs of the instance.
[00:54:21] Juan Torres: But at the end of the day, I know how much I'm going to be incurring in costs more if I allow the application to have it.
[00:54:28] Juan Torres: So, that's why I think I reduce my cost in logging.
[00:54:33] Brandon Hancock: I'm sorry, Juan, do you put the logs directly into your code base?
[00:54:38] Juan Torres: Yeah.
[00:54:39] Juan Torres: So, what you can do is just have, like, control of the EC2 instance in the permanent memory mechanism.
[00:54:50] Juan Torres: And so, through that, whatever Python code you're incurring, if you're going to have a mechanism there, you're going to have a folder in which you can see the logs of each test and then be able...
[00:55:01] Juan Torres: to observe what's the particular pinpoint in your Agentec system or whatever you're trying to test.
[00:55:10] Juan Torres: You just need to make a connection to your SSH, through SSH to whatever Agentec ID you're trying to do.
