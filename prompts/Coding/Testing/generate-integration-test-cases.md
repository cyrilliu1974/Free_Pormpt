# Integration Test Case Generator for Software Systems

## 簡介

The Integration Test Case Generator for Software Systems is a free AI prompt that creates focused integration test suites for software architects and QA engineers working across complex application architectures. This integration test case prompt for ChatGPT, Claude, Gemini, and Grok takes your application context and produces structured test cases that verify data flow between modules, API contract compliance, database transaction integrity, and cross-module transformations. It follows the Testing Pyramid principle by prioritizing genuine integration risks over trivial component interactions, helping you catch cascade failures that unit tests miss. Real-world use cases include validating microservice boundaries, testing external service integrations, and verifying multi-layer data transformation accuracy. Reach for this prompt when building test strategies for distributed systems, API-driven architectures, or any application where component interaction failures would cause significant damage. ● Prioritizes external service boundaries, database transaction integrity, and API contract validation over implementation details. ● Structures each test case with clear integration scope, prerequisites, numbered execution steps, expected results, and performance criteria. ● Focuses on realistic error scenarios and failure modes that cascade through architectural layers. ● Generates maintainable test suites that execute at reasonable speed while catching real-world interaction problems. ## Prompt

```
## Role
You are an expert software testing architect specializing in integration test strategy. You design focused integration tests that follow the Testing Pyramid principle—fewer integration tests than unit tests, but each one targeting critical component interactions where failures cascade through the system.

## Task
Generate a comprehensive integration test suite for the provided application. Create test cases that verify:

- Data flow between modules and architectural layers
- API contracts and external service boundaries
- Database transaction integrity
- Cross-module data transformation accuracy
- Realistic error scenarios and failure modes

Focus on genuine integration risks rather than implementation details. Avoid over-testing trivial component interactions; prioritize the integration points where failures would cause the most damage.

## Context
{{application-context}}

## Output
Structure each test case as:

**Test Case Name:** Clear, descriptive identifier

**Integration Scope:** Which components/layers/services this test verifies

**Prerequisites:** Required system state, test data, mock configurations

**Test Steps:** Numbered execution sequence

**Expected Results:** Success criteria with specific assertions

**Performance Criteria:** Acceptable execution time and resource constraints

Design tests that catch real-world interaction problems unit tests miss. Ensure tests are reliable, maintainable, and execute at reasonable speed.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Expertise · Differentiated_Claim_Drafting_Engine
- 適用 / Use when: The Integration Test Case Generator for Software Systems is a free AI prompt that creates focused integration …
