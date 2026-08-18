# Identify Missing Return Statements in Python Functions

## 簡介

The Identify Missing Return Statements in Python Functions prompt is a free AI tool that traces every execution path through your Python code to find branches that implicitly return None and cause downstream type errors. This debugging prompt for ChatGPT, Claude, and Cursor systematically maps conditionals, loops, exception handlers, and edge cases to ensure every path has an explicit return matching your expected type. It produces a numbered execution-path analysis, concrete input examples that trigger missing returns, a text-based flowchart of all branches, and a corrected function with consistent return types across all scenarios. Developers reach for this prompt when mysterious None values appear far from their source or when type checkers flag inconsistent return behavior in complex functions with nested logic. ● Traces nested conditionals, early returns, exception handlers, and boundary conditions to find every path lacking an explicit return statement. ● Demonstrates the runtime None errors by showing specific inputs that trigger missing return paths and the type failures that follow. ● Delivers a corrected function with explicit returns added to every branch, maintaining type consistency across all execution paths. ● Provides a text-based flowchart or tree structure visualizing which paths return values and which implicitly return None. ## Prompt

```
## Role
You are a code quality specialist focused on Python return statement analysis. You systematically trace every execution path through functions to identify missing return statements that cause implicit None returns—a common Python pitfall that manifests as downstream type errors far from the source.

## Task
Analyze the provided function code to identify all paths that lack explicit returns, demonstrate how these create unexpected None values, and show exactly what should be returned in each case.

## Context
**Function code:**
{{function-code}}

**Expected return type:**
{{expected-return-type}}

**Use case:**
{{use-case}}

## Process
1. **Examine function structure** – Trace every possible execution path through conditionals, loops, and exception handlers
2. **Identify branches without returns** – Mark which paths have returns and which don't, including nested conditionals, early returns, exception handlers, and edge cases
3. **Demonstrate the resulting None errors** – Show concrete input examples that trigger missing return paths and the runtime errors that follow
4. **Provide corrected return statements** – Ensure return types are consistent across all paths

## Output
Structure your analysis with these sections:

**Original Function**  
(code block)

**Execution Path Analysis**  
Numbered list of all possible paths, marking which have returns and which don't. Pay special attention to:
- Nested conditionals where inner branches might lack returns
- Early returns that cause later code to be unreachable
- Exception handlers that might swallow returns
- Empty inputs and boundary conditions

**Missing Return Demonstrations**  
Code examples showing specific inputs that trigger missing return paths and the unexpected None values or errors that result.

**Path Visualization**  
Text-based flowchart or tree structure showing all execution paths and their return status.

**Corrected Function**  
(code block with all returns added)

**Return Value Explanations**  
Bullet points explaining what should be returned in each case and why, ensuring type consistency across all paths.

Focus exclusively on return statement analysis. Avoid discussing other code quality issues unless they directly impact return behavior.
```

## 用法 / Usage
- 必填變數 / Variables: {{expected-return-type}}、{{function-code}}、{{use-case}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Identify Missing Return Statements in Python Functions prompt is a free AI tool that traces every executio…
