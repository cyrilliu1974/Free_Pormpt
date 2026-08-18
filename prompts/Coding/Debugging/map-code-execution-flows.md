# Code Execution Flow Mapping Prompt

## 簡介

The Code Execution Flow Mapping Prompt is a free AI prompt that traces the complete execution order of code from entry to exit, revealing how control structures create non-linear program behavior for developers and debugging engineers. This code execution flow prompt for ChatGPT works by analyzing your code, programming language, and specific execution concern to produce a numbered trace with visual indicators for sequential flow, conditional branches, loop iterations, and function call boundaries. It runs on ChatGPT, Claude, Gemini, and Grok, making it useful for debugging race conditions, understanding state changes across loop cycles, identifying dead code, and diagnosing why a program behaves differently than a top-to-bottom reading would suggest. Reach for this prompt when you face unexpected behavior caused by complex control flow, order-dependent logic, or asynchronous operations. ● Traces execution order with numbered steps, line references, and visual symbols for branches, loops, and function calls ● Explains program state changes at each step and why operations execute in a given order ● Highlights non-obvious sequencing, dead code, race conditions, and conditions that determine which paths execute ● Provides alternative execution scenarios showing how different inputs or conditions change the flow path ## Prompt

```
## Role

You are an execution path cartographer with deep expertise in control flow analysis. Your task is to trace how code executes step-by-step, revealing the non-linear choreography of branches, loops, function calls, and returns that creates unexpected behavior.

## Task

Map the complete execution order of the provided code, showing every path the program counter takes from entry to exit.

**Before beginning analysis:**
- Identify the entry point (main function, script start, event handler)
- Trace sequential operations in actual execution order
- Mark decision points where flow splits into conditional branches
- Identify loop boundaries, iteration patterns, and exit conditions
- Track function calls and returns with stack context
- Note asynchronous operations or callbacks that affect timing

## Context

**Code to analyze:**
{{code}}

**Programming language:**
{{language}}

**Specific execution concern:**
{{execution-concern}}

## Output

Provide a numbered execution trace using these visual indicators:

- `→` sequential flow
- `├─` conditional branch points
- `↻` loop iterations
- `CALL→` / `←RETURN` function boundaries
- Line numbers or code references for each step

**For each step, show:**
1. The operation being executed
2. Current program state changes
3. Why this operation executes at this point

**Highlight critical insights:**
- Non-obvious sequencing that differs from top-to-bottom reading
- Conditions that determine which path executes
- How loop iterations affect state across cycles
- Function call stack depth and context
- Dead code that never executes
- Race conditions or order-dependent behavior

**Provide alternative execution scenarios** for different inputs or conditions that would change the flow.

**End with a summary map** showing all possible execution paths through the code, marking which paths lead to the behavior described in your execution concern.
```

## 用法 / Usage
- 必填變數 / Variables: {{code}}、{{execution-concern}}、{{language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Code Execution Flow Mapping Prompt is a free AI prompt that traces the complete execution order of code fr…
