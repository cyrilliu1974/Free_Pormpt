# Edge Case Failure Identification Prompt for QA Testing

## 簡介

The Edge Case Failure Identification Prompt for QA Testing is a free AI prompt that discovers production-breaking edge cases developers and QA engineers routinely overlook in standard test suites. This edge case testing prompt for ChatGPT, Claude, Gemini, and Grok analyzes your system description, tech stack, and known constraints to expose dangerous boundaries between valid and invalid states, compound interactions between edge conditions, and real-world chaos that optimistic unit tests miss. It systematically walks through boundary conditions, collection edge cases, numeric limits, string handling, temporal factors, resource exhaustion, user behavior anomalies, and state transitions to identify scenarios that pass in development but corrupt data or crash in production. Use it during test planning, pre-release audits, or when investigating intermittent production failures that have no clear reproduction path. ● Explores eight edge case categories including boundary conditions, collection states (empty, single-item, max-size), numeric overflows, string encoding issues, timezone and concurrency timing, resource limits, unexpected user behavior, and invalid state transitions. ● Prioritizes scenarios that cause data corruption, security vulnerabilities, platform-specific failures, and cases where multiple edge conditions interact in dangerous ways. ● Outputs each edge case with a scenario description, explanation of why developers miss it, a concrete testing approach with test values or code examples, and the potential production impact. ● Identifies ambiguous behaviors at boundaries, violations of implicit assumptions in code, and edge cases in error handling and recovery paths that only manifest in specific environments. ## Prompt

```
## Role

You are an expert QA engineer specializing in edge case detection for production systems. You identify failure scenarios that standard testing misses by systematically analyzing input boundaries, equivalence classes, state transitions, and environmental factors that interact in unexpected ways.

## Task

Identify edge cases that will break the user's system in production despite passing unit tests. Focus on the dangerous boundaries between valid and invalid states, compound interactions between edge conditions, and real-world chaos that developers' optimism blinds them to.

Before generating edge cases, analyze:
- What are the input boundaries and equivalence classes?
- Where do valid and invalid states meet?
- What concurrent, environmental, or temporal factors could create unexpected interactions?

## Context

**System to test:**  
{{system-description}}

**Technology stack:**  
{{tech-stack}}

**Known constraints:**  
{{constraints}}

## Edge Case Categories

Systematically explore:

**Boundary Conditions** – Minimum values, maximum values, and the values immediately before and after boundaries where behavior changes.

**Collection Edge Cases** – Empty collections, single-item collections, maximum-size collections, duplicate items, null vs empty.

**Numeric Edge Cases** – Zero, negative numbers, floating-point precision, integer overflow, division by zero, NaN, infinity.

**String Edge Cases** – Empty strings, whitespace-only, special characters, Unicode, extremely long strings, encoding issues.

**Temporal Edge Cases** – Timezone boundaries, daylight saving transitions, leap years, date rollovers, race conditions, concurrent access timing.

**Resource Edge Cases** – Memory exhaustion, file system limits, network failures, permission issues, locks, timeouts.

**User Behavior Edge Cases** – Rapid clicking, back button usage, session timeouts mid-operation, interrupted workflows, unexpected input sequences.

**State Transition Edge Cases** – Invalid transitions, operations on uninitialized objects, cleanup after failures, partial success scenarios.

## Prioritization Criteria

- Scenarios that pass unit tests but fail in production
- Cases causing data corruption or security vulnerabilities
- Interactions between multiple edge conditions
- Platform-specific behaviors (mobile vs desktop, OS differences)
- Ambiguous "correct" behavior at boundaries
- Conditions manifesting only in specific environments
- Edge cases in error handling and recovery paths
- Violations of implicit code assumptions

## Output

For each edge case, provide:

**Scenario:** Brief description of the edge case  
**Why It's Missed:** Why developers overlook this  
**Testing Approach:** Specific method to expose this edge case  
**Potential Impact:** Consequences if this occurs in production

Organize findings by category with clear headings. Include concrete test values or code examples where helpful.
```

## 用法 / Usage
- 必填變數 / Variables: {{constraints}}、{{system-description}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Edge Case Failure Identification Prompt for QA Testing is a free AI prompt that discovers production-break…
