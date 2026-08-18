# Test Data Generator for Boundary and Edge Cases

## 簡介

The Test Data Generator for Boundary and Edge Cases is a free AI prompt that produces systematic test datasets covering boundaries, equivalence partitions, and critical edge cases for QA teams and test engineers. This test data generation prompt for ChatGPT applies formal testing strategies - boundary value analysis and equivalence partitioning - to create 15–25 structured samples that expose input validation flaws, constraint violations, and business logic weaknesses. It runs on ChatGPT, Claude, Gemini, and Grok, returning a markdown table that maps each sample to its test category, expected behavior, boundary type, and risk level. Use it to test web forms, APIs, database schemas, file parsers, or any system where input ranges and data constraints matter. Reach for this prompt when you need fast, comprehensive test coverage that balances thoroughness with practical usability for both automated suites and manual QA workflows. ● Covers minimum, maximum, just-below, and just-above threshold values to catch off-by-one and range errors. ● Generates representative samples from valid, invalid, empty, and null equivalence classes. ● Includes special characters, format violations, overflow conditions, and encoding issues. ● Explains each sample's purpose and risk level, making findings actionable for development teams. ## Prompt

```
## Role
You are a test data architect specializing in boundary value analysis and equivalence partitioning. Design comprehensive test datasets that expose edge cases, invalid states, and system vulnerabilities across input validation, data constraints, and business logic.

## Task
Generate realistic test data samples that systematically cover:
- Boundary conditions: minimum values, maximum values, just-below and just-above threshold points
- Equivalence classes: representative samples from valid, invalid, empty, and null partitions
- Edge cases: special characters, format violations, overflow conditions, encoding issues
- Critical business scenarios specific to the application domain

For each test sample, explain what scenario it validates and why it matters for system integrity.

## Context
{{system-under-test}}

Apply testing strategies appropriate to the application type, data constraints, and risk profile. Ensure coverage is thorough yet practical for development teams working with automated test suites and manual QA processes.

## Output
Structure your test data as a markdown table:

| Test Category | Test Data Sample | Expected Behavior | Boundary Type | Risk Level |
|---------------|------------------|-------------------|---------------|------------|

Group rows under clear section headers for each equivalence class and boundary condition set. Include 15–25 samples that span the full range of critical testing scenarios.
```

## 用法 / Usage
- 必填變數 / Variables: {{system-under-test}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Skills_Catalog_Node_Extractor
- 適用 / Use when: The Test Data Generator for Boundary and Edge Cases is a free AI prompt that produces systematic test datasets…
