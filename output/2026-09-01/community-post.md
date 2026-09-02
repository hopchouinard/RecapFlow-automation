📝 SUMMARY

This week's builder/founder coaching call, led by Brandon Hancock, packed in cost-optimization strategy, agentic architecture patterns, and hands-on go-to-market playbooks. Brandon shared updates on EMS SOAP (slow enterprise sales, active fundraising, aggressive LLM cost-cutting) and his new 30-day challenge project Listio, while Patrick Chouinard gave a deep tour of his personal "agentic OS" built on Proxmox, Hermes, and a markdown-based knowledge graph. The rest of the call was hands-on peer coaching: architecture advice for Hemal's e-commerce AI co-pilot, a full GTM and fundraising playbook for Juan's AI photo booth, cold-outreach troubleshooting for Shakur, and career-positioning strategy for Varun.

💡 KEY INSIGHTS

• Treat falling model costs as a strategic weapon: when a model gets 10x cheaper, reinvest the savings into 10x more product value (integrity checks, live QA) rather than pocketing margin. Expect this reset cycle every 6–8 months.

• Model swaps can deliver 100x savings: Brandon ran the same classification task on DeepSeek v4 Flash for $3 vs. $350 on a frontier model — same intelligence, fraction of the cost.

• A true agent reasons and acts in a loop; a pipeline of sequential LLM calls that just streams an answer is not "agentic." The distinction matters for architecture decisions.

• Adversarial test sets first: before building any conversational system, generate ~100 adversarial synthetic conversations (easy, confusing, prompt-injection) with expected outcomes. Hemal lost two weeks skipping this step.

• Start with the simplest architecture (one agent, many tools), measure failure modes, and only add orchestrators/sub-agents when failure data justifies the complexity.

• Loop engineering: run agents through repeated cycles of hypothesis → experiment → analyze → fix → retest, journaling every experiment to a markdown file so context survives compaction. Review early cycles yourself, then let it run autonomously overnight.

• Use cheap Chinese models (GLM, DeepSeek, Qwen) for internal experimentation; reserve American models (GPT-5.5, Gemini) for production-facing or HIPAA-regulated work.

• Specialize sub-agents and keep the chief-of-staff lean: the main agent should know the user deeply and delegate execution to specialists who carry their own tools and knowledge.

• Emulation before innovation: when directing AI on unfamiliar tasks like outreach copy, have it copy a proven playbook almost verbatim instead of "being creative."

• VCs now explicitly test whether a competitor could clone your app in a weekend. Physical products, proprietary datasets, and domain-expert judgment are far harder to clone — and judgment-at-scale across thousands of edge cases is still AI's moat gap.

• For engineers, public content is the highest-leverage career move: one viral in-public challenge video can outperform thousands of job applications.

❓ KEY Q&A

Q: For a multi-capability AI co-pilot (Q&A, buy, search), should I use an orchestrator with sub-agents or a planner/executor?
A (Brandon): Don't decide up front. Generate ~100 adversarial test conversations, start with one agent and many tools, run the eval set, identify failure modes, then iteratively test more complex architectures — using cheap models for the loop and strong models for production.

Q: Which models for the experiment loop if I'm limited to American models?
A (Brandon): Use a strong thinking model (Opus/5.6-tier) for the orchestrating agent — slower is fine since it runs overnight — and the cheapest fast model (Gemini 3.6 Flash or GPT-5.5 no-thinking) for the user-facing responder.

Q: Is "loop engineering" just a prompt that keeps going until a criterion is met?
A (Brandon): Yes. Review the first few cycles to correct its judgment, then let it run autonomously, logging every experiment to a markdown file so it can recover context after compaction.

Q: Big visual dashboard vs. a simple JSON file plus daily email for a personal OS?
A (Patrick): Simple is fine if you're just managing email and meetings. But once many sub-tools, CLIs, and MCPs run on infrastructure you don't touch daily, you need visualization just to remember what exists. Build the GUI last — it's purely an aggregator/launcher.

Q: How do you observe non-deterministic agent pipelines?
A (Juan/Brandon/Hemal): Build a lightweight containerized test client: register each adversarial input as a row, capture each agent-to-agent output, with an optional debug mode showing full reasoning. Connect it to the same database and toggle it on for dev/test only.

Q: Is DuckDB a vector store?
A (Paul/Daniel): No — it's a columnar, file-based query layer that sits on top of LanceDB for fast structured queries, used to pre-format data per metric category for agentic querying.

Q: My automated outreach is getting zero replies — what's wrong?
A (Brandon/Daniel/Varun): Check whether the offer delivers obvious ROI, increase follow-ups (the money is in the follow-up), make AI copy sound human by feeding it voice-transcribed natural phrasing, and A/B test subject lines and copy to isolate whether email, offer, or volume is broken.

Q: Should I pivot away from specializing in the Google stack for my job search?
A (Brandon): Keep the direction, change the tactic — build public "challenge" videos proving skill through a transparent problem-solving journey (e.g., "handle 1,000 customer queries with AI for under a dollar"), give away all code, and treat it as a repeatable, time-boxed format.

Q: Can I replicate deep self-reflection thinking in a single prompt within ShipKit task templates?
A (Brandon): No shortcut — break the SDLC into discrete skills/artifacts: plan mode → detailed task template → a "poke holes" critique skill → execution → review, with each step saving an artifact.

🛠️ TOOLS AND CONCEPTS MENTIONED

• T3 Code — interface aggregating Claude Code and Codex sessions across machines; Patrick and Shakur are heavy users
• Hermes — Patrick's multi-profile agent framework (chief-of-staff default plus specialist sub-agents)
• InfraKnowledge — Patrick's markdown knowledge graph tracking infra inventory, policy, and dependencies
• Prometheus / Grafana / Loki — Patrick's self-hosted observability stack
• GLM 5.3 / DeepSeek v4 Flash — cheap Chinese models Brandon uses for classification and experimentation
• Instantly — cold email platform central to the group's outreach (rule of thumb: 1 domain + 5 accounts ≈ 150 sends/day, ~2-week warm-up)
• LanceDB + DuckDB — vector store plus columnar query "intelligence layer" powering Paul and Daniel's BI systems
• Cerebras — fast hosted inference Paul uses for real-time chat over BI data
• Claude Design — rapid UI/landing page generation from backend specs
• ShipKit — Brandon's product teaching agent-driven rapid app development
• Blackbox — Scott's open-source Mac IDE/agent harness with agentic browser, iOS simulator, and phone companion app
• vidIQ — Chrome extension for spotting outlier/viral YouTube videos
• ccusage — CLI for tracking daily token usage across Codex/Claude/Grok
• Key concepts: loop engineering, adversarial test-set-first development, the chief-of-staff pattern, emulation before innovation, and Brandon's "1,000 customers before a single line of code" rule

📎 SHARED RESOURCES

Anthropic's Building Effective Agents guide (agent architecture starting point):
https://www.anthropic.com/engineering/building-effective-agents

Scott Rippey's Blackbox repo (free and open to test):
https://github.com/scott-rippey/cc-blackbox-app

ccusage token usage tracker:
https://github.com/ccusage/ccusage

Daniel's write-up on DuckDB as an intelligence layer atop LanceDB:
https://github.com/dzivkovi/video-intel/ (see intelligence-layer.md)

"Unslop" skill for cleaning up Opus responses:
https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md

Instantly's YouTube channel (cold email best practices):
https://www.youtube.com/@InstantlyAI/videos

SerpAPI (cheap Google Place data for lead lists):
https://serpapi.com/

vidIQ Chrome extension:
https://chromewebstore.google.com/detail/vidiq-vision-for-youtube/

Tiny Seed accelerator application:
https://apply.tinyseed.com/

Clerky (Delaware C-Corp setup):
https://www.clerky.com/

Video warning against standard Delaware C-Corp structures (Twilio founder example):
https://youtu.be/7VKliOQXQ9M

ShipKit:
https://www.shipkit.ai/

Daily-follow YouTube channels recommended by Patrick:
https://www.youtube.com/@AndrejKarpathy
https://www.youtube.com/@NateBJones

🔄 FOLLOW-UPS WORTH EXPLORING

• Brandon and Patrick are meeting Thursday to explore Patrick's multi-model code-review cycle for potential use in EMS SOAP's SDLC
• Bastian's ACP integration PR for T3 Code — Patrick will be invited to the repo
• Juan is executing the full GTM playbook: burner domains + Instantly campaigns, a landing page via Claude Design + Vercel, and Tiny Seed/YC applications with a C-Corp via Clerky
• Varun is publishing his first public "challenge" YouTube video within roughly three weeks
• Shakur is revamping his Google-review-reply offer (lower price, dashboard, more volume, manual control) after zero replies
• Scott is releasing his iOS companion app via TestFlight, formalizing his HYROX partnership agreement, and keeping his Blackbox repo free/open
• Morgan is building a 450-lead prospect list for Class2Curb.com using the outreach method discussed on the call
• Brandon will share EMS SOAP fundraising updates and, once funded, resume regular YouTube content and update ShipKit with newer techniques