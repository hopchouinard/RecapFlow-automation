---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Best Practices for Cloud Deployment and Logging"
speakers: ["Brandon Hancock", "Marc Juretus"]
chunk_id: "2025-09-16-chunk-020"
---

# Best Practices for Cloud Deployment and Logging

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Brandon Hancock recommends centralizing database interactions by creating a dedicated Python database service to manage CRUD operations for all application components, specifically using Supabase/Postgres. Additionally, the call clarifies that a CRM is essential for growing businesses to track customer information, manage sales pipelines, and handle communications.

[00:20:18] Brandon Hancock: Usually what will happen is you'll have to make something like this.
[00:20:24] Brandon Hancock: Let me share my screen really fast.
[00:20:27] Brandon Hancock: Yeah, usually in your Python project, you'll create something called like a database service and the database service is going to be using, so in our case, we're using Postgres because Supabase is using Postgres, so you basically just say like, hey, here's all my information from my database, here's like my database passwords and everything.
[00:20:50] Brandon Hancock: And at this point, you have one database service that all the different components of your application can reach out to.
[00:20:56] Brandon Hancock: So for example, like at the end of the day, your database just needs to be able to like insert data.
[00:21:00] Brandon Hancock: Read data, edit data, delete data, so you basically just have one database service that handles everything, and then you just build custom functions on top of this, that's the usual, you know, being nice and being good programmers would do, so hopefully that makes sense.
[00:21:19] Marc Juretus: And I just have one small quick question, so I see Ty's talking about that, Paul and CRM, and I forgot the gentleman wearing the hoodie, they're talking about the CRMs.
[00:21:30] Marc Juretus: In a nutshell, is that just the customer relationship management, where you have, like, you're keeping data, sending emails, what is the whole summary of what a CRM is, in your mind?
[00:21:40] Brandon Hancock: Yeah, everything that you just said, which is basically like, as a software business grows, you need to keep up with how many customers you have, what is their information, where are they in the sales pipeline journey, you need a way to contact them.
[00:21:54] Brandon Hancock: So it's basically just all things related to knowing about your customers, where they're at, and then having the ability.
[00:22:00] Brandon Hancock: remember is, and
