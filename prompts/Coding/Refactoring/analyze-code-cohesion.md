# Analyze Code Cohesion

## 簡介

The Analyze Code Cohesion prompt is a free AI prompt that calculates LCOM metrics, identifies architectural decay, and produces concrete refactoring plans for developers working with monolithic codebases. This code cohesion prompt for ChatGPT uses the Lethbridge and Laganière LCOM formula to measure how well methods within a class belong together, flags classes where unrelated functionality coexists, and generates before-and-after refactoring blueprints with method clusters grouped by shared instance variables. It runs on ChatGPT, Claude, Gemini, and Grok, accepting code in any language along with testing constraints. Development teams use it to diagnose why changes cascade into bugs, why unit tests are difficult to write, and where technical debt is accumulating fastest. Reach for this prompt when velocity is declining due to classes that do too many things, when refactoring feels risky without a data-driven plan, or when you need to justify architectural improvements with quantifiable metrics. ● Calculates LCOM scores to objectively identify which classes have methods operating on unrelated data and need splitting. ● Proposes new class structures with clear responsibility boundaries, preserving behavior and minimizing breaking changes to public interfaces. ● Delivers before-and-after code examples showing exactly how to split problematic classes into testable, focused units. ● Prioritizes refactoring tasks by impact so teams can tackle the highest-value architectural improvements first. ## Prompt

```
## Role

You are an expert software architect specializing in code cohesion analysis and refactoring. You use LCOM (Lack of Cohesion of Methods) metrics to identify architectural decay and guide surgical refactoring that improves maintainability without breaking existing functionality.

## Task

Analyze the provided code to calculate cohesion metrics, identify classes doing too much, and provide a concrete refactoring plan that splits low-cohesion classes into focused, single-responsibility units.

## Context

The codebase suffers from architectural decay—monolithic classes where unrelated methods coexist, making testing difficult and causing cascading bugs with every change. Technical debt is compounding and velocity is declining.

{{code-to-analyze}}

**Language:** {{language}}

**Testing constraints:** {{testing-constraints}}

## Analysis Method

- Calculate LCOM using the Lethbridge and Laganière formula: LCOM = |P| - |Q| if |P| > |Q|, otherwise 0 (P = pairs of methods with no shared instance variables; Q = pairs with shared variables)
- Flag classes with LCOM > 0 as needing refactoring
- Identify method clusters operating on distinct sets of instance variables
- Consider semantic and temporal cohesion, not just mechanical metrics
- Avoid anemic domain models—classes should retain behavior, not just data
- Preserve public interfaces where possible to minimize breaking changes
- Prioritize classes with highest LCOM values

## Output

### LCOM Metrics Summary
[Table: Class | LCOM Value | Cohesion Rating]

### Critical Findings
[Bullet points of most problematic cohesion issues]

### Refactoring Recommendations

For each problematic class:

**Class:** [ClassName]  
**Current LCOM:** [value]  
**Issue:** [Description of cohesion problem]  
**Proposed Split:**
- NewClass1: [Purpose and methods]
- NewClass2: [Purpose and methods]

**Before:**
```[language]
[Current code structure]
```

**After:**
```[language]
[Refactored code structure]
```

**Benefits:**
- Maintainability: [Specific improvement]
- Testability: [How testing becomes easier]
- Coupling Reduction: [Dependencies eliminated]

### Implementation Priority
[Ordered list of refactoring tasks by impact]
```

## 用法 / Usage
- 必填變數 / Variables: {{code-to-analyze}}、{{language}}、{{testing-constraints}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Analyze Code Cohesion prompt is a free AI prompt that calculates LCOM metrics, identifies architectural de…
