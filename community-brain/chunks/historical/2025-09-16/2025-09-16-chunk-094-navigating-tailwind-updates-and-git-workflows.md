---
session_date: "2025-09-16"
session_title: "Weekly Coaching Call"
content_tier: "historical"
topic: "Navigating Tailwind Updates and Git Workflows"
speakers: ["Brandon Hancock", "Morgan Cook"]
chunk_id: "2025-09-16-chunk-094"
---

# Navigating Tailwind Updates and Git Workflows

**Session:** Weekly Coaching Call | **Date:** 2025-09-16

**Summary:** Morgan expressed frustration with Git's inability to run tools while directories are ignored, prompting Brandon to clarify the licensing parameters of the code. They concluded that these build issues specifically arise from Morgan’s goal of maintaining a public repository, with Brandon suggesting a Tailwind configuration to properly include source files during compilation.

[01:44:35] Brandon Hancock: Like, the license is, like, you can do whatever you want with it, but just, like, don't publicly share the source code is basically the agreement.
[01:44:42] Brandon Hancock: But build your own apps with it, hey, go for it.
[01:44:44] Brandon Hancock: Knock yourself out.
[01:44:45] Brandon Hancock: It's just not share public, if that makes sense.
[01:44:47] Morgan Cook: So, one of the problems I had was I had originally added it to the GitIgnore.
[01:44:53] Morgan Cook: I'm using Windsurf, and maybe this is a problem with Windsurf.
[01:44:56] Morgan Cook: I don't know.
[01:44:56] Morgan Cook: But the GitIgnore then ignored the directory for any of the commands that were being issued.
[01:45:03] Morgan Cook: So it would create a problem.
[01:45:06] Morgan Cook: I don't want it in my project for the sake of committing to GitHub, but I need it in my project for the sake of the tool to actually run, but it's trying to honor the Git ignore.
[01:45:18] Morgan Cook: So I had the same kind of problem with one of the Tailwind problems, too.
[01:45:24] Brandon Hancock: Tailwind has a solution for that by including a source to include it so it gets compiled when you do your build.
[01:45:31] Morgan Cook: Just some problems to think about.
[01:45:33] Brandon Hancock: No, I thank you for sharing that I am so I'm guessing so you are building a public project.
[01:45:38] Morgan Cook: That's why.
[01:45:40] Brandon Hancock: Yeah, I think okay.
[01:45:42] Brandon Hancock: Okay, cool.
[01:45:43] Brandon Hancock: I can yeah, that's is 99% of all these projects are all been private.
