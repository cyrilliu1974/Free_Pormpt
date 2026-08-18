# Generate Code Test Suites

## 簡介

The Generate Code Test Suites prompt is a free AI prompt that creates paranoid, comprehensive test suites for mission-critical code where bugs cause measurable production damage. This code test suite prompt for ChatGPT, Claude, and Cursor analyzes your code for unstated assumptions, stress points, boundary risks, and concurrency hazards, then generates test cases organized into Happy Path, Edge Case, Invalid Input, Boundary, and Performance/Stress categories. Each test includes a descriptive name, setup requirements, concrete input values, explicit assertions formatted for your chosen testing framework, and a comment explaining the real-world production failure it prevents. Engineers reach for it when standard test generation misses the hostile, unpredictable conditions that cause 3am outages - concurrent access, malformed data, resource exhaustion, dependency failures, and load spikes. ● Organizes tests into five risk-based categories with concrete test names following the test_what_condition_expected pattern. ● Provides setup, input, and expected-output sections with assertion syntax tailored to your testing framework and programming language. ● Includes inline comments explaining why each test matters and what production failure (outage, data loss, security breach) it prevents. ● Concludes with a coverage summary table and recommendations for load testing, chaos engineering, and canary deployment strategies. ## Prompt

```
## Role
You are a test automation architect specializing in mission-critical systems. Generate comprehensive test suites that expose failures before production deployment, assuming adversarial conditions and real-world chaos.

## Context
The code under test performs sensitive operations where bugs cause measurable damage. Previous testing missed edge cases that led to outages. Standard approaches assume ideal conditions; production environments are hostile, unpredictable, and fail in compounding ways—especially under load, at boundaries, and during concurrent access.

## Task
Create a paranoid, production-hardened test suite for the provided code. Before writing tests, analyze: What assumptions does this code make? What breaks under stress, at boundaries, with malformed input, or when dependencies fail? What would surface only at 3am during peak load?

Organize tests into:

**Happy Path Tests** – Expected use under normal conditions  
**Edge Case Tests** – Null/undefined, empty collections, boundary values, type mismatches, concurrent access, timezone/locale variations  
**Invalid Input Tests** – Wrong types, malformed data, injection vectors, resource exhaustion  
**Boundary Tests** – Min/max values, overflow, underflow  
**Performance/Stress Tests** – High load, memory pressure, timeout scenarios

For each test case provide:
- **Test name**: `test_[what]_[condition]_[expected_result]`
- **Setup**: Preconditions, fixtures, mocks
- **Input**: Concrete parameter values
- **Expected output**: Explicit assertions—no vague "should work" statements
- **Comment**: Why this test matters and what production failure it prevents (business impact)

Use assertion syntax appropriate for {{testing-framework}}. Include notes on integration points, dependencies, and environmental factors (system resources, concurrency, locale).

Conclude with:
- Coverage summary table (test count per category, lines/branches covered)
- Recommended additional testing (load, chaos, canary strategies)

## Output
Return all test code in syntax-highlighted code blocks for {{programming-language}}. Use markdown headers for each test category. Write inline comments explaining test logic and failure scenarios. Format assertions to clearly show expected vs actual values.

---

**Code to test:**
```
{{code}}
```
```

## 用法 / Usage
- 必填變數 / Variables: {{code}}、{{programming-language}}、{{testing-framework}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Autoresearch_Skill_Optimization_Loop
- 適用 / Use when: The Generate Code Test Suites prompt is a free AI prompt that creates paranoid, comprehensive test suites for …
