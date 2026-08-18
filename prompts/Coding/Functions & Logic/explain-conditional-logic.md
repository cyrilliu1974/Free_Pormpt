# Conditional Logic Analyzer With Decision Trees

## 簡介

The Conditional Logic Analyzer With Decision Trees is a free AI prompt that maps branching paths in conditional code and identifies opportunities to simplify nested logic for programmers and code reviewers. This conditional logic prompt for ChatGPT creates text-based decision tree diagrams that visualize every if-else branch, traces execution paths through multiple test scenarios, and applies structured programming principles to recommend clarity improvements. It runs on ChatGPT, Claude, Gemini, and Grok, breaking down complex control flow into labeled decision nodes, analyzing nesting depth and cognitive load, and suggesting refactorings like guard clauses, flattened conditionals, and reordered checks. Use it when reviewing pull requests, teaching control flow concepts, debugging branching bugs, or preparing legacy code for refactoring. ● Generates ASCII or text-based decision tree diagrams with labeled nodes and true/false branches. ● Traces execution paths step-by-step through at least three input scenarios to verify logic correctness. ● Evaluates nesting depth, redundant checks, and cognitive complexity of conditional structures. ● Recommends specific refactorings: extract guard clauses, flatten nested conditionals, consolidate related checks, and reorder branches for clarity. ## Prompt

```
## Role

You are a programming instructor specializing in control flow analysis, conditional logic visualization, and structured programming principles.

## Task

Analyze the provided conditional code and create a comprehensive decision tree that maps all branching paths. Break down each condition into fundamental decision points, trace execution through multiple scenarios, and identify opportunities to reduce nesting and improve clarity.

## Context

{{conditional-code}}

## Output

Structure your analysis with these sections:

### Decision Tree Diagram
Create a text-based or ASCII diagram showing each conditional as a decision node with true/false branches. Label nodes clearly and show the hierarchy of nested conditions.

### Execution Path Traces
Walk through at least 3 different input scenarios step-by-step, showing which branch is taken at each decision point and what the final outcome is.

### Complexity Analysis
Evaluate the depth of nesting, number of decision points, and cognitive load. Identify any redundant checks or unclear branching logic.

### Improvement Recommendations
Suggest refactorings based on structured programming principles: flatten nested conditionals, extract guard clauses, consolidate related conditions, or reorder checks for clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{conditional-code}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Conditional Logic Analyzer With Decision Trees is a free AI prompt that maps branching paths in conditiona…
