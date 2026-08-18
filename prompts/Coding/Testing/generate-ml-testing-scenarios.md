# ML Testing Scenario Generator for AI Systems

## 簡介

The ML Testing Scenario Generator is a free AI prompt that creates structured test scenarios across the testing pyramid for machine learning engineers and QA teams. It produces a markdown table of test cases organized by level (unit, integration, end-to-end), each with input conditions, expected outcomes, failure indicators, and business impact analysis. This ML testing prompt for ChatGPT, Claude, Gemini, and Grok applies testing pyramid methodology to catch unique ML failure modes like silent data drift, cascading pipeline dependencies, and gradual performance erosion. Reach for it when you need to design test coverage that addresses typical operation, boundary conditions, error handling, performance under load, data quality issues, and user interaction edge cases for any ML system. ● Generates unit tests for component-level validation, integration tests for pipeline dependencies, and end-to-end tests for complete workflows ● Specifies exact input conditions, expected outcomes, observable failure signatures, and production impact for each scenario ● Covers the full failure spectrum including data drift detection, performance degradation, error handling, and boundary conditions ● Outputs a structured markdown table that testing teams can immediately convert into test suites ## Prompt

```
## Role

You are an ML testing architect designing comprehensive test scenarios that catch failures across the testing pyramid: unit, integration, and end-to-end levels.

## Context

ML systems exhibit unique failure modes: data drift degrades models silently, pipeline dependencies cascade failures, and performance erodes gradually before sudden collapse. Effective test coverage must address typical operation, boundary conditions, error handling, performance under load, data quality issues, and user interaction edge cases.

## Task

Generate structured testing scenarios for the ML system described below. Apply the testing pyramid methodology:

- **Unit tests**: granular component-level validation
- **Integration tests**: pipeline and dependency interactions
- **End-to-end tests**: complete workflow validation

For each scenario, specify:

- Exact input conditions that trigger the test
- Expected outcome
- Observable failure signatures teams can monitor
- Business impact if the failure reaches production

**System specification:**

{{ml-system-spec}}

## Output

Structure your response as a markdown table with these columns:

| Test Level | Scenario Type | Input Conditions | Expected Outcome | Failure Indicators | Business Impact |

Group scenarios under clear headings:

### Unit Tests
### Integration Tests
### End-to-End Tests

Cover the full failure spectrum: typical operation, boundary conditions, error handling, performance degradation, data quality issues, and user interaction patterns.
```

## 用法 / Usage
- 必填變數 / Variables: {{ml-system-spec}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The ML Testing Scenario Generator is a free AI prompt that creates structured test scenarios across the testin…
