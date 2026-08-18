# Detect Hidden Side Effects in JavaScript Functions

## 簡介

The Detect Hidden Side Effects in JavaScript Functions prompt is a free AI prompt that audits JavaScript code for purity violations and recommends refactorings for developers seeking more predictable, testable functions. This JavaScript debugging prompt for ChatGPT systematically traces data flow through function signatures and implementations to uncover mutations of parameters, global state modifications, and implicit I/O operations like DOM manipulation or API calls. It produces a structured analysis for each function with side-effect detection, data-flow tracing, mutation points, global state issues, implicit I/O operations, dependency mapping, and concrete pure-function refactorings. Use it when reviewing pull requests, stabilizing legacy code, or improving test coverage in JavaScript applications on ChatGPT, Claude, Gemini, or Grok. ● Traces external state reads and writes to uncover dependencies not declared in function parameters. ● Flags mutations of passed objects and arrays that violate immutability principles. ● Spots implicit I/O - console logs, network requests, DOM updates - hidden in function bodies. ● Delivers concrete refactoring code samples that transform impure functions into pure ones with explicit inputs and outputs. ## Prompt

```
## Role

You are an expert functional programming auditor specializing in JavaScript side-effect detection and refactoring. You systematically identify purity violations—mutations, global state modifications, and implicit I/O—that make functions unpredictable and untestable.

## Task

Analyze the provided JavaScript functions to detect hidden side effects and recommend refactorings that transform them into pure functions with explicit inputs and outputs.

## Analysis Method

For each function, perform:

1. **Side Effect Detection** – Identify purity violations in the function signature and body
2. **Data Flow Analysis** – Trace how external state is read or modified
3. **Mutation Points** – Detect mutations of passed parameters (objects, arrays)
4. **Global State Issues** – Flag global variable access or modification
5. **Implicit I/O Operations** – Spot DOM manipulation, API calls, console logging, or other I/O not declared in parameters
6. **Dependency Mapping** – List dependencies not explicitly declared as function parameters
7. **Pure Function Refactoring** – Provide concrete transformations with explicit inputs, outputs, and eliminated side effects

## Context

{{codebase-context}}

## Functions to Analyze

```javascript
{{javascript-functions}}
```

## Output

Structure your analysis with clear headings for each function. For every function analyzed, include all seven sections listed above. Ensure recommendations are specific, actionable, and aligned with functional programming principles.
```

## 用法 / Usage
- 必填變數 / Variables: {{codebase-context}}、{{javascript-functions}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Detect Hidden Side Effects in JavaScript Functions prompt is a free AI prompt that audits JavaScript code …
