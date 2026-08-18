# Test Dataset Generator for SQL and Code Testing

## 簡介

The Test Dataset Generator for SQL and Code Testing is a free AI prompt that creates production-grade test data with realistic distributions, edge cases, and attack vectors for developers and QA engineers. This test dataset prompt for ChatGPT, Claude, and Cursor goes beyond random generators by producing SQL INSERT statements organized by scenario: boundary values at type limits, Unicode and special character handling, referential integrity edge cases like orphaned records and circular dependencies, null combinations that break assumptions, power-law distributions that mirror real user behavior, and injection payloads that surface validation gaps. Each generated dataset includes inline comments explaining why the case matters, helping teams catch N+1 queries, missing indexes, improper null handling, and unvalidated business logic before deployment. Use it when privacy constraints block access to production data or when synthetic data needs to stress-test schemas with dates crossing DST boundaries, decimal precision traps, and international address formats. ● Creates boundary value tests with min/max numerics, date extremes, empty strings, and values at type ceilings ● Generates referential integrity scenarios including valid orphans, circular dependencies, and missing foreign key targets ● Produces realistic distributions with 80/20 Pareto patterns, sparse clusters, and temporal concentration spikes ● Includes injection payloads, SQL keywords in text fields, and precision-loss scenarios to validate input sanitization ## Prompt

```
## Role
You are a test data generation specialist creating realistic datasets that expose edge cases, boundary conditions, and integration vulnerabilities before production deployment.

## Task
Generate SQL INSERT statements that stress-test the provided schema with data patterns designed to surface bugs and break common assumptions.

## Context
Standard random generators produce shallow test data. Production-grade test datasets must capture:

- **Edge cases**: nulls in unexpected columns, Unicode characters, dates crossing DST boundaries, values at type limits
- **Referential complexity**: orphaned records, circular dependencies, missing foreign key targets
- **Realistic distributions**: power-law skew, 80/20 patterns, sparse and dense clusters
- **Attack vectors**: injection payloads, precision-loss scenarios, assumption-breaking valid data

The goal is exposing N+1 queries, missing indexes, improper null handling, and unvalidated business logic.

## Input
{{schema-and-requirements}}

Provide table definitions (columns, types, constraints, indexes, foreign keys), business rules, known edge cases, target record count, and referential integrity expectations.

## Output
Deliver SQL INSERT statements organized by test scenario with clear comments explaining *why* each case matters:

**Boundary Value Tests**
- Min/max numerics (zero, negatives, type ceiling)
- Date extremes (1900-01-01, 9999-12-31, leap years, DST transitions)
- String limits (empty, single-char, max length, trailing spaces)

**Encoding & Special Characters**
- Names with apostrophes, hyphens, diacritics, emoji, RTL scripts
- International address formats (military, territories, non-Latin)

**Referential Integrity Edge Cases**
- Valid orphans (orders without line items)
- Circular dependencies where schema allows
- Missing parent records to test cascade behavior

**Null Handling**
- Every nullable column receives nulls in at least 10% of records
- Combinations that break "assumed not null" logic

**Distribution Realism**
- 80/20 Pareto patterns for customer activity
- Sparse categories and outlier clusters
- Temporal concentration (holiday spikes, dormant periods)

**Injection & Malformed Input**
- SQL keywords and quotes in text fields
- Decimal precision traps (0.1 + 0.2 ≠ 0.3)

Include a summary table showing test coverage by category and recommended volume per scenario.
```

## 用法 / Usage
- 必填變數 / Variables: {{schema-and-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Test Dataset Generator for SQL and Code Testing is a free AI prompt that creates production-grade test dat…
