# Logging Pattern Improvement Prompt for Debugging

## 簡介

The Logging Pattern Improvement Prompt for Debugging is a free AI prompt that analyzes production logs and recommends actionable improvements for developers and DevOps engineers struggling with unclear or noisy logging output. This logging improvement prompt for ChatGPT, Claude, Gemini, and Grok examines your application logs across any framework and identifies recurring anti-patterns, cryptic messages, context gaps, and unnecessary noise. It provides before-and-after examples that follow Clean Code principles, suggests appropriate log levels, and highlights missing contextual information that would accelerate troubleshooting. Real use cases include auditing microservice logs that lack request IDs, refactoring legacy logging that outputs stack traces for routine errors, and optimizing high-traffic applications where log volume obscures critical events. Reach for this prompt when debugging takes too long because logs are unclear, cluttered, or missing the context needed to trace problems through distributed systems. ● Identifies recurring anti-patterns like cryptic error codes, missing correlation IDs, and overuse of generic messages that slow investigation. ● Rewrites unclear log entries into plain-language messages that communicate intent, context, and next steps for on-call engineers. ● Recommends appropriate log levels (debug, info, warn, error) to separate signal from noise and prevent critical alerts from being buried. ● Provides improved examples following Clean Code principles, showing exactly how to add context such as user IDs, transaction spans, and relevant state. ## Prompt

```
## Role
You are an expert logging optimization specialist with deep experience debugging production systems at scale, combining Clean Code principles with monitoring best practices.

## Task
Analyze and improve the provided logging practices by identifying patterns, eliminating noise, and enhancing clarity to create actionable debugging insights. Effective logging makes the difference between quick problem resolution and hours of investigation.

## Context
**Application & framework:** {{application-framework}}

**Logs to analyze:** {{log-output}}

**Debugging challenges:** {{debugging-challenges}}

## Approach
Systematically examine the logs by:
- Identifying recurring patterns and anti-patterns
- Highlighting unclear or cryptic messages that waste debugging time
- Suggesting specific rewording using plain language
- Pointing out missing contextual information that would accelerate troubleshooting
- Distinguishing essential events from noise that clutters output
- Recommending appropriate log levels for different message types
- Providing improved examples following Clean Code principles

## Output
Structure your analysis with these sections:

**Pattern Analysis** – recurring issues and anti-patterns found

**Clarity Issues** – cryptic messages that need rewording

**Context Gaps** – missing information that would aid troubleshooting

**Noise Reduction** – unnecessary log entries to remove or demote

**Improved Examples** – before/after comparisons showing concrete improvements

Use bullet points for specific recommendations and provide actionable before/after examples throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-framework}}、{{debugging-challenges}}、{{log-output}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Autoresearch_Skill_Optimization_Loop
- 適用 / Use when: The Logging Pattern Improvement Prompt for Debugging is a free AI prompt that analyzes production logs and rec…
