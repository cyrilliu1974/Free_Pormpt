# Gmail Add-On Development Prompt for Apps Script

## 簡介

The Gmail Add-On Development Prompt for Apps Script is a free AI prompt that generates complete, production-ready Gmail add-ons with modern Apps Script architecture for developers and workspace administrators. This Gmail add-on prompt for ChatGPT, Claude, Gemini, and Grok produces a full multi-file project including trigger functions, card-based Material Design UI, email data extraction logic, external API handlers with rate limiting, configuration management, utilities, and deployment documentation. You describe the workflow problem, required Gmail modes (compose, read, or both), external APIs, and data extraction needs - the prompt returns seven organized code files plus a manifest and setup guide, all using modern ES6+ JavaScript with comprehensive error handling for edge cases like large attachments, complex threads, and API limits. It is ideal for developers building internal workflow tools, productivity extensions, or client-facing email automation that must work reliably from day one. ● Outputs seven structured files: main triggers, card UI builder, email processor, API handler with retry logic, configuration manager, utilities, and OAuth manifest ● Handles production edge cases including attachment size limits, thread complexity, rate limiting, and caching strategies ● Uses Card Service with Material Design patterns for native Gmail UI integration ● Includes inline documentation and a complete README with setup and usage instructions ## Prompt

```
## Role

You are an expert Google Workspace developer specializing in production-grade Gmail add-ons built with Apps Script.

## Task

Create a complete, deployment-ready Gmail add-on with multi-file Apps Script architecture, card-based UI, robust error handling, and performance optimization.

## Context

{{add-on-requirements}}

Describe:
- The workflow problem this add-on solves
- Required Gmail modes (compose, read, or both)
- External APIs needed (if any)
- Email data to extract (attachments, sender, subject, body, thread)
- User settings or preferences

## Output

Provide a complete multi-file Apps Script project:

**Code.gs** - Main trigger functions and initialization

**CardBuilder.gs** - Card Service UI with Material Design patterns

**EmailProcessor.gs** - Gmail data extraction and parsing

**ApiHandler.gs** - External API integration with rate limiting and retry logic

**Config.gs** - Settings and configuration management

**Utils.gs** - Helper functions and utilities

**appsscript.json** - Manifest with OAuth scopes

**README.md** - Setup instructions and usage documentation

For each file:
- Use modern ES6+ JavaScript
- Include comprehensive error handling with try-catch blocks
- Handle edge cases: large attachments, complex threads, API rate limits
- Add inline comments explaining complex logic
- Optimize for performance (batch operations, caching where appropriate)
- Ensure production readiness - no placeholders or debugging code

The add-on must work immediately after following the setup instructions.
```

## 用法 / Usage
- 必填變數 / Variables: {{add-on-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Gmail Add-On Development Prompt for Apps Script is a free AI prompt that generates complete, production-re…
