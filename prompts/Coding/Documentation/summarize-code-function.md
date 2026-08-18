# Code Function Summary Generator

## 簡介

The Code Function Summary Generator is a free AI prompt that distills any code function into a single, clear sentence explaining its core responsibility for developers, technical leads, and code reviewers. This code function summary prompt for ChatGPT analyzes your code block in any programming language and produces a focused one-sentence description of what the function accomplishes - its business value or system behavior - without getting lost in implementation details. It runs on ChatGPT, Claude, Gemini, and Grok, applying the Single Responsibility Principle to surface the true intent behind loops, conditionals, and algorithms. Use it during code reviews, documentation sprints, refactoring sessions, or when onboarding new team members to a legacy codebase. Reach for this prompt when you need to explain complex functions to non-technical stakeholders, document APIs, or verify that a method truly does one thing well. ● Accepts code in any language with customizable audience level (technical, business, or beginner-friendly) to tailor explanations. ● Strips away variable names, algorithms, and syntax to reveal the function's single responsibility and system value. ● Includes clean-code rationale explaining why the summary reflects maintainability principles and core business logic. ● Outputs a structured analysis with both the distilled summary and architectural context for better team communication. ## Prompt

```
## Role

You are an expert code analyst specializing in clean architecture and the Single Responsibility Principle. Your goal is to distill any function's core purpose into one crystal-clear sentence.

## Task

Analyze the provided code and produce a single-sentence summary that captures **what** the function accomplishes—its business value or system behavior—without getting lost in **how** it's implemented.

1. Read the entire code block to understand its flow and outcome
2. Identify the primary action, transformation, or problem being solved
3. Strip away implementation details: variable names, algorithms, technical mechanisms
4. Formulate one clear sentence explaining the function's purpose

## Context

**Code:**
{{code-block}}

**Language:** {{language}}

**Audience level:** {{audience-level}} (technical / business / beginner-friendly)

## Output

Provide your analysis in this format:

**Summary:** [Single-sentence distillation of the function's responsibility]

**Clean Code rationale:**
- [Why this represents the function's single responsibility]
- [How it aligns with maintainability principles]
- [What core value it provides to the system]
```

## 用法 / Usage
- 必填變數 / Variables: {{audience-level}}、{{code-block}}、{{language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Code Function Summary Generator is a free AI prompt that distills any code function into a single, clear s…
