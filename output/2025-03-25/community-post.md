📝 SUMMARY

This coaching call featured Brandon Hancock's announcement of his transition to full-time content creation, alongside deep technical discussions on enterprise AI platforms, voice synthesis tools, and member project updates ranging from legal tech automation to multi-agent podcast generation. The group explored practical implementations of AWS Bedrock flows, Google Gemini 2.5 Pro's document analysis capabilities, and strategies for deploying AI agents at scale while maintaining security.

💡 KEY INSIGHTS

Brandon announced he is leaving his full-time job to focus exclusively on content creation, with plans to produce tutorials on AWS Bedrock and Google Cloud Platform's Gemini implementations for real-world agentic applications beyond basic N8N automations.

Paul highlighted that Google Gemini 2.5 Pro features a one-million token context window (expanding to two million) and API access, making it particularly effective for analyzing large document sets and code libraries without the restrictions of Notebook LM. He noted it can generate audio descriptions directly from chat mode without needing Notebook LM.

Andrew and Maxim discussed scaling their car dealership AI application to 30,000 users across LATAM, noting they implemented Cloudflare Workers for authentication and are expanding into voice agents for customer support.

Bastian demonstrated a browser-based tool built in Windsurf that converts Excel insurance data into JSON schemas for GPT-4.0 Mini function calling, solving the problem of lawyers not knowing how to structure queries for their existing ChatGPT Enterprise integration.

Asako shared her workflow using Microsoft Autogen for multi-agent text-based conversations between podcast hosts, which preserves conversation context through group chat functionality before converting to audio via ElevenLabs.

Richard announced he reserved an NVIDIA Digits personal AI supercomputer for three thousand dollars capable of running two-hundred-billion parameter open source models locally, with discussion about potentially linking two units for larger models though speed would degrade due to communication bottlenecks.

Tom discussed learning Jest for functional testing after realizing he needed proper test coverage for his code, spending eight hours to produce seven minutes of video content but improving his prompting skills with Cursor in the process.

❓ KEY Q&A

Mitch asked about hosting code via GitHub URLs that appear to run applications. Brandon explained this refers to GitHub Pages, which allows publishing static HTML, CSS, and JavaScript sites directly from repositories using username.github.io domains, ideal for quick project demos without complex deployment.

Sam asked about low-code POC tools for report writing applications involving document analysis and regulatory justification. Brandon recommended Make for simple document processing workflows with Google Docs integration, and N8N for more complex agentic systems requiring persistent memory or multiple iterations on content.

Richard asked whether FFMPEG works with audio for stitching together voice files from multiple characters. Brandon confirmed FFMPEG handles MP3 concatenation and recommended adding meta tags or pauses between clips to avoid robotic transitions when combining multiple speaker segments, suggesting three-second pauses between chapters.

Juan asked about managing API keys for a live workshop where attendees need to run agentic code to web scrape Federal Reserve data. The group debated pre-configured keys versus having attendees create their own, with Mitch suggesting hard-coding example responses as a fallback to avoid rate limits, and Richard recommending backup demos in case of API failures during the live presentation.

🛠️ TOOLS AND CONCEPTS MENTIONED

AWS Bedrock Flows: Visual workflow builder for AI agents similar to N8N discovered by Brandon, allowing secure deployment within AWS infrastructure with flow inputs, agents, prompts, and code blocks

Google Gemini 2.5 Pro: New model with one-million to two-million token context window and API access for document analysis, accessible at gemini.google.com

Neo4j: Graph database technology Paul is studying for knowledge graph implementations and RAG applications

GitHub Pages: Free static site hosting directly from GitHub repositories using username.github.io domains

Jest: JavaScript testing framework Tom learned for functional testing and code coverage

FFMPEG: Command-line tool for audio and video processing including MP3 concatenation and audio manipulation

ElevenLabs: Voice synthesis platform for creating character voices and conversational AI

OpenAI TTS: New text-to-speech models with emotion customization and pacing controls for pauses

Sesame: Voice generation tool recommended by Scott for high-quality voice synthesis

Microsoft Autogen: Multi-agent conversation framework for text-based interactions with group chat functionality that preserves conversation context

NVIDIA Digits: Three-thousand-dollar personal AI supercomputer for running two-hundred-billion parameter models locally

SageMaker versus Bedrock: Discussion on AWS machine learning platforms, with Bedrock preferred for most agentic use cases and SageMaker reserved for fine-tuning with large datasets

📎 SHARED RESOURCES

gemini.google.com: Access point for Google Gemini Advanced with document upload and audio generation capabilities

github.io: Domain structure for GitHub Pages static hosting

🔄 FOLLOW-UPS WORTH EXPLORING

Comparison of AWS Bedrock pricing for flows and agents versus standard API usage, particularly regarding the billing approach for agent builders mentioned by Paul

Testing Google Gemini 2.5 Pro for multilingual voice capabilities as an alternative to ElevenLabs for Japanese language podcast generation requested by Asako

Follow-up on Andrew and Maxim's voice agent implementation for LATAM car dealership customer support scaling to thirty-thousand users

Deep dive into AWS Bedrock's multi-agent orchestration capabilities compared to N8N and other workflow tools

Review of Cyril's job offers and negotiation strategies once final interviews with AlphaSights, Elementor, and other companies conclude

Analysis of NVIDIA Digits performance when linked together for four-hundred-billion parameter models and the practical limitations of the interconnect speed