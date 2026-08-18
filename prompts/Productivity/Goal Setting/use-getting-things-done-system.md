# Getting Things Done (GTD) System Implementation Guide

## 簡介

The Getting Things Done (GTD) System Implementation Guide is a free AI prompt that builds a customized GTD methodology roadmap for professionals looking to structure their task management workflow. This GTD prompt for ChatGPT asks you to describe your current productivity level, main challenges, preferred task management tools, work environment, and long-term goals, then delivers a structured markdown table covering all five core GTD phases: Capture, Clarify, Organize, Reflect, and Engage. Each column includes specific actions, recommended techniques, and best practices adapted to your exact toolset and work style. The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing a ready-to-follow implementation plan rather than generic advice. Use it when you know the Getting Things Done framework but need a personalized blueprint that respects your existing apps, constraints, and productivity pain points. ● Breaks down Capture, Clarify, Organize, Reflect, and Engage into actionable steps matched to your preferred tools ● Integrates your work environment, challenges, and long-term goals into every phase of the guide ● Outputs a scannable markdown table format for quick reference and implementation ● Provides best practices and efficiency tips specific to your productivity profile, not boilerplate GTD theory ## Prompt

```
## Role
You are a productivity expert specializing in the Getting Things Done (GTD) methodology.

## Task
Create a comprehensive GTD implementation guide tailored to the user's workflow. Break down the five core phases—Capture, Clarify, Organize, Reflect, and Engage—with actionable instructions, techniques, and best practices for each.

## Context
User's productivity profile:
{{productivity-context}}

(Include: current productivity level, main challenges, preferred task management tools, work environment, and long-term goals)

## Output
Present the guide as a markdown table with 5 columns: **CAPTURE**, **CLARIFY**, **ORGANIZE**, **REFLECT**, and **ENGAGE**.

For each phase column, include:
- Specific actions to take
- Recommended tools and techniques
- Best practices and tips to maximize efficiency

Ensure the guidance integrates the user's preferred tools and addresses their specific challenges and environment.
```

## 用法 / Usage
- 必填變數 / Variables: {{productivity-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Getting Things Done (GTD) System Implementation Guide is a free AI prompt that builds a customized GTD met…
