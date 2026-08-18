# Test Coverage Strategy and Gap Analysis Prompt

## 簡介

The Test Coverage Strategy and Gap Analysis Prompt is a free AI prompt that analyzes your codebase and produces a prioritized testing roadmap focused on preventing production failures. You provide your existing code and known gaps, and the prompt returns organized test scenarios grouped by category: critical business logic, integration points, error handling, boundary conditions, and high-risk areas. This test coverage prompt for ChatGPT, Claude, Gemini, and Grok helps QA engineers and developers move beyond arbitrary line-coverage metrics toward behavior-driven testing that protects revenue-critical flows and user experience. Reach for this prompt when you inherit a codebase with sparse tests, when production incidents reveal blind spots, or when you need to justify testing priorities to stakeholders who understand business impact better than coverage percentages. ● Identifies critical business flows tied to revenue, user sign-up, payments, and core features that must not break in production. ● Surfaces integration vulnerabilities where APIs, databases, and third-party services interact unpredictably under load or failure conditions. ● Highlights missing boundary-condition tests for null inputs, maximum limits, concurrent access, and edge cases that cause real-world crashes. ● Pinpoints error-handling gaps in retry logic, timeout behavior, and fallback paths that determine whether a system degrades gracefully or fails catastrophically. ## Prompt

```
## Role
You are an expert test strategist focused on behavior-driven testing and meaningful coverage. You identify critical gaps in test suites—edge cases, integration vulnerabilities, and business-logic risks that cause real-world failures—rather than chasing arbitrary coverage percentages.

## Task
Analyze the provided codebase and generate a structured test coverage plan that prioritizes:
- Critical business flows that drive revenue and user experience
- High-risk areas: external dependencies, complex algorithms, state management
- Boundary conditions, error paths, and failure modes
- Integration points where components interact unpredictably

## Context
{{codebase-and-gaps}}

## Output
Organize your response with clear headings for each coverage category (Critical Business Logic, Integration Points, Error Handling, Boundary Conditions, High-Risk Areas). Under each heading, provide specific, actionable test scenarios in bullet-point format. Focus on tests that prevent production incidents, not on maximizing line-coverage metrics.
```

## 用法 / Usage
- 必填變數 / Variables: {{codebase-and-gaps}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Test Coverage Strategy and Gap Analysis Prompt is a free AI prompt that analyzes your codebase and produce…
