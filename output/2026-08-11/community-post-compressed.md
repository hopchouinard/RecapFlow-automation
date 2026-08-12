📝 SUMMARY

This week's call centered on the evolution from single AI assistants to "chief of staff" multi-agent architectures, featuring Patrick Chouinard's enterprise rollout of 2000+ Claude licenses. Members converged on two-tier systems where coordinator agents delegate to implementers via shared repositories. Key discussions covered governance patterns, measuring real ROI versus vanity metrics, managing model verbosity, overcoming organizational resistance to AI coding, database migrations for real-time apps, and enterprise adoption tactics.

💡 KEY INSIGHTS

The "assistant" model collapses at scale. Patrick described how coordinating many Claude assistants consumes more time than it saves, leading his team to create a two-tier architecture: Claude Cowork acts as "chief of staff" coordinating with Claude Code as "implementer" through a shared local Git ledger. This reduces humans to pure decision-makers rather than message relays.

Surface decisions, wins, and progress—not just noise. Ty Wells noted that showing only problems creates demoralizing interfaces. Effective chief-of-staff agents should highlight successes alongside escalations, not just raw agent output.

Set explicit time budgets. Paul Miller emphasized that agent tasks without deadlines can silently balloon from one hour to four, cascading delays. Decisive time constraints prevent runaway context windows.

Opus 5 requires verbosity management. Multiple attendees flagged Opus 5 as unusually chatty. Mitigations include Matt Pocock's "wait, what?" skill to detect confusing output and Patrick's discovery that sarcastic, personality-driven prompts produce shorter, clearer responses.

Governance belongs in skills, not documents. At enterprise scale, Patrick's team enforces tech stack constraints and approved integrations through mandatory onboarding skills rather than policy documents, preventing users from requesting unsanctioned API keys.

Measure ROI by value delivered, not volume. Token spend, PR counts, and lines of code are easily gamed. Real ROI must judge solution quality per token, citing cases where lower token usage delivered far more business value than higher usage.

The "living specification" reframe. Patrick's team labels AI-generated HTML prototypes as "living specifications" with embedded structured comments that downstream agents parse into functional specs, avoiding scope confusion with stakeholders.

Swap projects to convert skeptics. When developers resist AI coding, swapping their project with an AI-aided colleague's (same team context, different deliverables) provides undeniable evidence. Resistance often stems from fear of replacement rather than stubbornness, particularly when non-technical staff can now build competing prototypes that threaten previous "black box" ownership.

Convex.dev removes sync plumbing. Morgan evaluated Convex for its native reactive sync, eliminating manual socket management needed with Supabase. Bastian noted that proper indexing keeps costs low even at scale, contrasting with high bills only from unoptimized queries.

❓ KEY Q&A

Q: Why migrate from Supabase to Convex?
A: Convex offers built-in real-time sync where all subscribed clients see updates instantly without manual refresh or socket handling, critical for multi-tenant apps with live classroom updates.

Q: How risky is Convex billing?
A: With proper indexing to avoid excessive raw database calls, costs stay low. The highest known bill (Theo's T3Chat at $6-7k monthly) stems from hundreds of thousands of transactional chat users, not typical application patterns.

Q: How should enterprises measure AI coding ROI?
A: Avoid volume metrics like tokens or PRs, which Claude can game by generating useless output. Judge by delivered solution quality and value per token. One developer using $800 in tokens delivered half a year's worth of work, while another using $2,000 delivered only three shallow solutions.

Q: In the developer swap test, did developers lack context?
A: No, both were on the same team with existing familiarity. Only the specific deliverables were swapped, isolating tool impact from project knowledge.

Q: Does Claude Enterprise provide usage data?
A: Yes, the enterprise admin layer exposes an API mirroring the console, though the compliance API (exposing every prompt) carries heavy legal restrictions. The gap between Teams and Enterprise license control is substantial.

Q: Do you recommend Honcho for memory management?
A: Yes. Patrick has run it for three months on roughly $27, using it approximately 12 hours daily. It pre-analyzes memory before storing and re-injects only specific context needed for each question rather than dumping entire memory windows.

🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Cowork: Chief of staff coordination layer sitting above implementer agents.
Claude Code: The implementer agent executing coding and JIRA work, reporting back to shared repositories.
Opus 5: Claude model flagged as unusually verbose by multiple attendees; requires specific mitigation strategies.
Matt Pocock's Skills: "Teach" and "wait, what?" skills for onboarding and detecting confusing verbose output.
Honcho.ai: Memory-reasoning layer that pre-analyzes and selectively injects context rather than full memory dumps.
Convex.dev: Reactive backend-as-a-service with built-in sync, being evaluated to replace Supabase for real-time multi-tenant apps.
WorkOS: Auth provider integrating with Convex for multi-tenant social logins, free up to approximately one million users.
Hermes: Personal and business assistant system built by Scott, used by Ryan C and Patrick for admin, calls, and scheduling.
Whisperflow, Fathom, Otter: Meeting transcription tools with varying reliability for speaker detection and video handling.
Verif/VERIFF: Biometric ID and face-verification API for logistics authentication.
Entra ID: Azure AD used to manage Claude license groups at enterprise scale.
Living Specifications: Reframing AI-generated HTML prototypes as specifications with embedded structured comments for downstream parsing.

📎 SHARED RESOURCES

class2curb.com — Morgan's carpool pickup product for testing and referrals.
data-terrain-showcase.vercel.app/t/the-holding-pool-ws8r19 — Ty Wells' visualization tool showing Morgan's class2curb data.
github.com/openai/codex-plugin-cc — Codex plugin for Claude Code.
convex.dev — Convex backend platform homepage.
honcho.dev — Honcho.ai memory layer platform.
ericscouler.com/projects/church-of-claude — Humorous project link.
diamandis.com/podcast — Peter Diamandis' Moonshots podcast recommended by Alex.
youtube.com/@MoonshotsClips — Moonshots YouTube clips.
youtube.com/@aiDotEngineer — AI Engineer channel.
youtube.com/@alejandro_ao — Practical AI implementation channel recommended by Bastian.
youtube.com/@HealthyGamerGG — ADHD-focused coaching channel recommended by Bastian.
linkedin.com/posts/juan-torres-ai-engineering_i-made-a-game-its-called-ai-booth-activity... — Juan Torres' AI Booth project.
score.org — Business and funding advice resource suggested for Juan Torres.

🔄 FOLLOW-UPS WORTH EXPLORING

Morgan to decide this week whether to rewrite the Carpool app backend on Convex before onboarding additional schools, estimating a four-day rewrite.
Morgan to connect directly with Bastian for Convex and WorkOS implementation guidance.
Patrick to develop separate Claude style templates for chief of staff versus implementer roles to reduce verbosity.
Juan Torres to prepare funding pitch for September round and explore revenue-share venue partnerships versus traditional equity investment.
Paul Miller and Juan Torres to meet regarding funding and partnership strategy.
Ryan C to onboard thirty existing clients into the Hermes assistant system.
Ryan C and Patrick to compare notes on Hermes configurations and multi-profile setups offline.
Scott to demo his in-progress Mac-based coding tool replacement upon returning from holiday.