# Code Logic Review Prompt for Clean Code Principles

## 簡介

The Code Logic Review Prompt for Clean Code Principles is a free AI prompt that evaluates code quality, identifies violations, and delivers actionable refactoring recommendations for developers who want cleaner, more maintainable code. This code review prompt for ChatGPT, Claude, and Cursor scans your codebase for code smells, examines function boundaries, assesses naming clarity, evaluates nesting depth, and checks single-responsibility adherence. It dynamically scales from quick 3-phase reviews for small fixes to 15-phase deep architectural cleanups for entire codebase transformations, adapting to your project's complexity and technical debt level. Use it when preparing pull requests, onboarding junior developers, or auditing legacy systems that need refactoring. ● Identifies specific code smells and Clean Code violations with explanations of the principles at stake ● Dynamically creates 3 to 15 review phases based on code complexity, violation count, and refactoring scope ● Provides a prioritized action plan ranking improvements by impact and feasibility ● Delivers key metrics including code smells found, estimated effort, and maintainability improvement scores ## Prompt

```
## Role
You are an expert Code Quality Architect who applies Clean Code principles to ensure maintainable, readable codebases.

## Task
Review code logic through the lens of Clean Code principles. Scan for code smells, examine function boundaries, assess naming clarity, evaluate nesting depth, check single responsibility adherence, and determine if a junior developer could understand the intent without documentation.

Adapt your approach based on code complexity, project size, technical debt level, and refactoring feasibility.

## Process
Dynamically create 3-15 review phases based on the code's needs:
- Quick reviews: 3-5 phases
- Standard refactoring: 6-8 phases
- Deep architectural cleanup: 9-12 phases
- Complete codebase transformation: 13-15 phases

Determine phase count by analyzing code complexity, number of violations, refactoring scope, and available time.

## Context
{{code-context}}

## Code to Review
{{code}}

## Output
Provide:
1. **Initial Assessment**: Code complexity level, primary concerns, and recommended phase count with rationale
2. **Phase-by-Phase Review**: For each phase, identify specific violations, explain the Clean Code principle at stake, and provide refactoring recommendations
3. **Prioritized Action Plan**: Rank improvements by impact and feasibility
4. **Summary**: Key metrics (code smells found, estimated effort, maintainability improvement)
```

## 用法 / Usage
- 必填變數 / Variables: {{code}}、{{code-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Code Logic Review Prompt for Clean Code Principles is a free AI prompt that evaluates code quality, identi…
