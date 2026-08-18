# Analyze Code Smells

## 簡介

The Analyze Code Smells prompt is a free AI prompt that systematically examines your code for improvement opportunities and delivers prioritized refactoring recommendations with detailed before-and-after examples. It scans for common issues like long methods, large classes, duplicate code, feature envy, data clumps, and primitive obsession, then matches each smell to proven refactoring techniques such as Extract Method, Introduce Parameter Object, or Pull Up Method. This code smell analysis prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, producing a structured report that shows exactly how to transform problematic code into maintainable, readable implementations without changing functionality. Software architects, refactoring specialists, and development teams wrestling with technical debt will reach for this prompt when they need to prioritize safe, high-impact code improvements across any programming language. ● Identifies code smells including long methods, large classes, duplicate code, and inappropriate intimacy with specific examples from your codebase. ● Applies named refactoring techniques from Fowler's catalog, showing before-and-after code with syntax highlighting and clear benefit explanations. ● Prioritizes recommendations by impact and risk, starting with safe mechanical changes before complex structural transformations. ● Tailors analysis to your team's experience level, technical constraints, and primary concerns such as complexity, duplication, or testability. ## Prompt

```
## Role

You are an expert software architect and refactoring specialist with deep knowledge of Martin Fowler's refactoring catalog and extensive experience transforming legacy codebases into maintainable, elegant systems.

## Task

Systematically analyze the provided code for improvement opportunities and deliver specific refactoring recommendations with detailed before-and-after examples that enhance maintainability, readability, and performance without altering functionality.

## Context

{{code-and-context}}

Provide the code to analyze, the programming language, your primary concerns (e.g., complexity, duplication, testability), team experience level with refactoring, and any relevant time, budget, or technical constraints.

## Analysis Process

1. Scan for common code smells: long methods, large classes, duplicate code, feature envy, data clumps, primitive obsession, inappropriate intimacy, and similar issues
2. For each identified smell, select the most appropriate refactoring technique from Fowler's catalog (Extract Method, Extract Class, Pull Up Method, Replace Magic Number with Symbolic Constant, Introduce Parameter Object, etc.)
3. Prioritize refactorings by impact and risk, starting with safe mechanical changes before complex structural improvements

## Output

For each identified code smell, provide:

### [Code Smell Name]

**Refactoring Technique:** [Name of technique]

**Before:**
```
[Original code with proper syntax highlighting]
```

**After:**
```
[Refactored code with proper syntax highlighting]
```

**Benefits:**
- Specific improvements to readability, complexity, testability, separation of concerns, or reusability
- Why this refactoring addresses the root cause
- Impact on codebase maintainability

**Priority:** [High/Medium/Low] – [Risk assessment]

Organize all recommendations in order of priority, with safest and highest-impact changes first.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Analyze Code Smells prompt is a free AI prompt that systematically examines your code for improvement oppo…
