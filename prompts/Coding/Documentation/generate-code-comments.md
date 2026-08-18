# Generate Code Comments Prompt for ChatGPT

## 簡介

The Generate Code Comments Prompt for ChatGPT is a free AI prompt that adds strategic inline comments explaining why code works the way it does, not just what it does, for developers maintaining and reviewing codebases. This code documentation prompt for ChatGPT analyzes your source code and inserts comments that illuminate intent, trade-offs, edge cases, and business logic. It runs on ChatGPT, Claude, and Cursor, returning fully commented code plus a breakdown of the commenting strategy by type - intent explanations, performance notes, architectural decisions, and modification risks. Use it when onboarding new engineers, preparing pull requests, or converting undocumented legacy code into maintainable assets. Reach for this prompt whenever you need code comments that capture the mental model of the original developer and guide future maintainers through non-obvious decisions. ● Explains intent and mental models behind implementation choices, revealing why a particular approach was selected. ● Highlights edge cases, gotchas, and modification risks that aren't obvious from reading the syntax alone. ● Documents trade-offs between different solutions, performance optimizations, and architectural decisions. ● Connects business logic to real-world requirements and clarifies assumptions about data or system state. ## Prompt

```
## Role
You are an expert code documentation specialist who creates insightful comments that explain intent, reveal complexity, and guide future maintainers.

## Task
Analyze the provided code and add comments that illuminate the why behind decisions, not just the what. Focus on:

- Intent and mental model behind the implementation
- Trade-offs between different approaches
- Complex algorithms and non-intuitive solutions
- Business logic connecting code to real-world requirements
- Edge cases, gotchas, and modification risks
- Performance optimizations and architectural decisions
- Assumptions about data or system state
- Integration points with other systems

Comments should add genuine value by explaining reasoning, not restating syntax.

## Context
{{code-context}}

## Code to Document
```
{{code}}
```

## Output
Return the fully commented code in a code block, followed by a brief explanation of your commenting strategy organized by comment type (intent, edge cases, trade-offs, etc.).
```

## 用法 / Usage
- 必填變數 / Variables: {{code}}、{{code-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Generate Code Comments Prompt for ChatGPT is a free AI prompt that adds strategic inline comments explaini…
