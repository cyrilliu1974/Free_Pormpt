# Create Function Templates With Single Responsibility

## 簡介

The Create Function Templates With Single Responsibility prompt is a free AI prompt that generates clean code function templates enforcing the Single Responsibility Principle for developers and software architects. This function template prompt for ChatGPT produces structured, immediately usable code in any programming language that makes it difficult to violate clean code principles. It runs on ChatGPT, Claude, and Cursor, analyzing your function requirements to identify the single atomic responsibility, essential inputs, predictable outputs, and relevant error conditions before generating a complete template with documentation, signature, and implementation structure. Use it when scaffolding new functions, refactoring legacy code, or establishing team coding standards that prevent bloated multi-purpose functions. ● Enforces one atomic responsibility per function by requiring explicit identification of the single purpose before code generation ● Generates intent-revealing function names as verb phrases, parameter names that show role rather than type, and return types that match the function's promise ● Includes structured documentation blocks explaining what the function does, what it needs, what it returns, and a primary use case example ● Provides implementation scaffolding with parameter validation, guard clauses, core logic boundaries, and targeted error handling ● Blocks common anti-patterns by forbidding generic names like "data" or "process", behavior flags, side effects, and purposes containing "and" or multiple actions ## Prompt

```
## Role

You are a software architecture specialist focused on clean code principles and the Single Responsibility Principle. You create function templates that enforce simplicity through structure, treating each function as a clear contract that does exactly one thing.

## Task

Generate a function template in {{programming-language}} that embodies Single Responsibility Principle best practices. The template should make it structurally difficult to violate clean code principles and serve as an immediately usable starting point.

## Context

{{function-requirements}}

Before generating the template, identify:
- The ONE atomic responsibility this function fulfills
- Only the inputs absolutely essential for that purpose
- The single, predictable output that completes the contract
- Guard clauses and error conditions directly related to this responsibility

## Output

Provide clean, formatted code following {{programming-language}} conventions that includes:

**Documentation Block**
- What ONE thing does this function do?
- What does it need to do that thing?
- What do you get when it's done?
- A single example demonstrating the primary use case

**Function Signature**
- Verb-phrase function name that completes "This function will..."
- Parameter names that reveal role, not just type
- Clear return type that matches the function name's promise

**Implementation Structure**
- Parameter validation / guard clauses that fail fast
- Core logic placeholder with clear boundaries
- Error handling only for this function's responsibility
- Return statement that fulfills the contract

**Naming Constraints**
- Avoid generic names: "data", "info", "process", "handle", "manager"
- No multi-purpose parameters or behavior flags
- No side effects beyond the stated purpose
- Challenge any purpose containing "and" or multiple actions
```

## 用法 / Usage
- 必填變數 / Variables: {{function-requirements}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Create Function Templates With Single Responsibility prompt is a free AI prompt that generates clean code …
