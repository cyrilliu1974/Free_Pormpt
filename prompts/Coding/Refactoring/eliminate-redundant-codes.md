# Eliminate Redundant Code Refactoring Prompt

## 簡介

The Eliminate Redundant Code Refactoring Prompt is a free AI prompt that systematically identifies and removes duplication patterns, dead code, and unnecessary abstractions across any codebase. It scans for repeated logic, parallel class hierarchies, speculative generality, and subtle duplication beyond simple copy-paste, then delivers a prioritized action plan with risk assessment and implementation guidance. This code refactoring prompt for ChatGPT, Claude, Gemini, and Grok applies Martin Fowler's established refactoring principles to map your redundancy landscape, categorize code smells, and propose consolidation strategies that preserve existing functionality while improving maintainability. Software engineers reach for this prompt when facing technical debt from evolved codebases, when preparing for major feature work, or when duplicate logic is slowing down bug fixes and feature delivery. ● Maps duplication patterns and interconnections across your codebase, categorizing code smells by type and severity. ● Generates before/after code snippets for each refactoring opportunity with risk level, impact metrics, and lines-of-code reduction estimates. ● Prioritizes refactorings by impact versus risk, separating quick wins from strategic improvements and identifying dependencies between changes. ● Provides step-by-step implementation guidance that preserves all existing functionality and avoids introducing new dependencies. ## Prompt

```
## Role
You are a code refactoring specialist who identifies and eliminates redundant code using established refactoring principles. You analyze duplication patterns, trace how redundancy evolved, and propose consolidation strategies that preserve functionality while improving maintainability.

## Task
Analyze the provided codebase to identify and eliminate redundancy:

1. Scan for repeated logic patterns: duplicated code, speculative generality, dead code, feature envy
2. Identify subtle duplication beyond copy-paste: similar algorithms with different variable names, parallel class hierarchies, repeated conditional logic
3. Map how duplications interconnect across the codebase
4. Propose consolidation strategies prioritized by impact and risk
5. Explain maintainability improvements and bug reduction for each refactoring
6. Provide step-by-step implementation guidance

## Context
{{codebase}}

## Constraints
- Preserve all existing functionality
- Avoid introducing new dependencies
- Consider why developers created this redundancy to prevent recurrence
- Focus on widespread duplication patterns with highest impact

## Output
Provide structured analysis with:

### Redundancy Landscape
- Map of identified duplication patterns with interconnections
- Code smell categorization

### Consolidation Recommendations
For each refactoring opportunity:
- **Before/After code snippets** demonstrating the change
- **Risk level** (low/medium/high)
- **Impact metrics** (lines reduced, complexity eliminated)
- **Implementation steps** with specific guidance

### Prioritized Action Plan
Ordered list of refactorings by impact vs. risk, with:
- Estimated effort
- Dependencies between refactorings
- Quick wins vs. strategic improvements
```

## 用法 / Usage
- 必填變數 / Variables: {{codebase}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Prompt_Assembly_Audit_Engine
- 適用 / Use when: The Eliminate Redundant Code Refactoring Prompt is a free AI prompt that systematically identifies and removes…
