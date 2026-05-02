📝 SUMMARY

This coaching call covered advanced AI-assisted development workflows, enterprise implementation strategies, and practical tool demonstrations. Patrick shared his work with SpecStory for extracting training materials from AI chat logs and building research pipelines with Gemini CLI. Ty showcased ShipKit Studio, a GUI wrapper for project scaffolding, and a voice-based learning application. Brandon provided strategic guidance on productized services, prompt engineering education, and enterprise AI deployment with proper security considerations. New members Glenn and Ryan shared their transitions into AI development, while Lan and David received technical advice on handling large-scale real estate data and ERP system integration respectively.

💡 KEY INSIGHTS

Patrick argued that when models lack training examples for specific workflows, developers should build the "brain" (prompts and logic) first, then use Cloud Code to construct the scaffolding around it. He demonstrated this by creating a research pipeline with Gemini CLI for search and HTML generation, storing components in Supabase, and having Cloud Code tie everything together.

Ty revealed ShipKit Studio, a web application that transforms the ShipKit CLI workflow into a visual interface with wireframing capabilities, database schema visualization, and planned E2B integration for browser-based code deployment. He also demonstrated a voice-first learning application using ElevenLabs that adapts content complexity based on user expertise level.

Brandon emphasized that developers should view skills as "small employees who are specialists at one outcome," building AI agents for repetitive tasks like YouTube title generation, email drafting, and social media management. He noted that AI adoption in enterprises will likely happen "bottom up," automating operational tasks before strategic ones.

Glenn, a veteran mobile developer since 2010, noted that AI represents a "complete reset" where everyone starts at the same level regardless of prior experience. He predicted that traditional mobile apps and website frontends will disappear within five years, replaced by AgentOS and contextual widgets.

Patrick highlighted that Claude for Financial Services is uniquely positioned for enterprise ERP integration because it provides audit trails and SOC compliance features that standard models lack, with contractual guarantees that data won't be used for training.

❓ KEY Q&A

Tom asked about the difference between specs and tasks. Patrick explained that in SpecKit, a spec represents the overall specification including user stories and requirements, while tasks are sub-items within those specs.

Prem asked about PostHog project structure for different environments. Brandon recommended using a single project with filters to exclude localhost traffic from dashboards, or using the PostHog MCP to automatically create these filters via natural language.

Prem asked about learning Playwright for testing. Brandon recommended IndieDevDan's YouTube tutorials and explained how to use Playwright as an MCP tool for UI testing and mobile responsiveness checks. Scott shared a document clarifying the relationships between slash commands, MCPs, agents, and skills.

Lan asked about handling 50 million real estate records and whether to use CSV, Parquet, or relational databases. Brandon and Patrick suggested starting with Excel pivot tables for exploration, then moving to Postgres with the PostGIS extension for geographic indexing. For the existing Python/Pandas codebase, Brandon recommended treating it as a seeding script for a new Supabase project rather than refactoring the entire brownfield application.

David asked about enterprise AI deployment for ERP systems like NetSuite. Brandon recommended starting with read-only MCP servers to prevent rogue AI actions, using Claude for Financial Services for audit trails, and eventually migrating to LangGraph for production agent orchestration. Patrick warned about data residency issues with Bedrock in certain geographic regions.

🛠️ TOOLS AND CONCEPTS MENTIONED

SpecStory: VS Code and Cursor extension that exports AI chat logs to markdown files for extracting rules and creating training documentation.

Gemini CLI: Command line interface for Google's Gemini models, used by Patrick for automated search and content generation pipelines.

Cloud Code Max: The $200 subscription tier for Claude Code, which Patrick adopted after hitting the five-hour limit on the $100 plan.

ShipKit/SpecKit: Development frameworks where SpecKit is used for internal applications and ShipKit for external products. Ty built ShipKit Studio as a GUI wrapper around ShipKit workflows.

ElevenLabs: Voice generation platform used in Ty's adaptive learning application for narrating lessons and quizzes.

E2B: Sandbox environment for executing code in the browser, which Ty is integrating for cloud-based project deployment.

PostHog: Analytics platform discussed for tracking application events, with recommendations to filter development traffic using the PostHog MCP.

Playwright: Browser automation tool used for end-to-end testing and mobile responsiveness verification through MCP integration.

MCP (Model Context Protocol): Standard for connecting AI agents to external tools and APIs, discussed extensively for ERP integration.

LangGraph: Enterprise framework for building production agent workflows, recommended for corporate environments requiring complex orchestration.

Claude for Financial Services: Enterprise version of Claude with built-in audit trails, SOC compliance, and data isolation guarantees.

PostGIS: Postgres extension for geographic data handling, recommended for Lan's real estate application to efficiently query properties by location.

Pandas: Python data analysis library capable of handling large datasets (50M+ records) for local data processing before database migration.

🔄 FOLLOW-UPS WORTH EXPLORING

Patrick committed to reporting back on his Cloud Code Max usage scores after a week of heavy usage to benchmark the $200 plan's limits.

Ty plans to complete the E2B integration for ShipKit Studio to enable browser-based code deployment without touching the CLI, potentially allowing non-technical users to launch full applications.

Brandon and Glenn agreed to schedule a deeper discussion in December about the future pivot of mobile development to AI agents and the disappearance of traditional frontends.

The group consensus on AI's trajectory: A dedicated session to predict where AI development will shift in 2025-2026, particularly regarding backend systems versus UI generation.

Lan's data architecture: Migrating 50M real estate records from text/CSV files into a proper Postgres/PostGIS database structure with Supabase as the backend.

David's enterprise implementation: Building a proof-of-concept NetSuite MCP server with read-only permissions and exploring LangGraph for production deployment in a financial services environment.

Ryan's productized service: Scaling the social media management application from handling 2-3 clients to 20-30 clients using the automated Claude/Zapier integration.

Brandon's "Prompt Dojo" concept: A potential SaaS offering to train developers on prompt engineering by grading their prompts against optimal solutions and teaching missing concepts.