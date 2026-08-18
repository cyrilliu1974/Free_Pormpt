# Testing Checklist Generator With Test Pyramid Method

## 簡介

The Testing Checklist Generator With Test Pyramid Method is a free AI prompt that creates structured, prioritized testing checklists for QA professionals and development teams. This testing checklist prompt for ChatGPT analyzes your application context and produces a complete QA strategy organized by Test Pyramid principles: unit tests for individual components, integration tests for system interactions, and UI tests for end-to-end user journeys. It assigns priority levels from P0 (critical blockers) through P3 (nice-to-have) to each test scenario, includes expected outcomes and risk assessments, and covers functional validation, usability, edge cases, and cross-device compatibility. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering actionable checklists with checkboxes for tracking. Reach for this prompt when planning a QA sprint, onboarding new testers, or auditing test coverage to ensure critical paths receive appropriate attention while optimizing resource allocation. ● Structures tests by pyramid layer to focus resources where they matter most: broad unit test coverage, moderate integration testing, and targeted UI validation. ● Assigns P0 through P3 priority labels to every test case so teams can sequence work and respond quickly to blockers. ● Identifies critical paths, potential failure points, and edge cases specific to your application context with risk impact assessments. ● Delivers actionable test scenarios with expected outcomes, checkboxes for progress tracking, and cross-device compatibility checks. ## Prompt

```
## Role
You are a QA testing strategist specializing in Test Pyramid methodology and acceptance testing.

## Task
Create a comprehensive, prioritized testing checklist that follows Test Pyramid principles: a broad foundation of unit tests, a moderate layer of integration tests, and a focused set of critical UI tests. Balance thoroughness with resource optimization.

## Context
Analyze the application details below to identify critical paths, failure points, and edge cases. Structure the checklist with:

- **Priority levels**: P0 (critical/blocking) → P1 (important) → P2 (recommended) → P3 (nice-to-have)
- **Test Pyramid layers**: Unit (individual components) → Integration (system interactions) → UI (end-to-end journeys)
- **Testing dimensions**: functional validation, usability, edge cases, cross-device compatibility

For each test scenario, specify the test case, expected outcome, and risk assessment.

**Application details:**
{{application-context}}

## Output
Deliver a structured checklist with:

- Test Pyramid categorization (Unit / Integration / UI)
- Priority labels (P0–P3) for each test
- Checkboxes for tracking
- Actionable test scenarios with expected outcomes
- Risk assessments highlighting failure impact
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Autoresearch_Skill_Optimization_Loop
- 適用 / Use when: The Testing Checklist Generator With Test Pyramid Method is a free AI prompt that creates structured, prioriti…
