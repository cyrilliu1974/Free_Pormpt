# Data Error Resolution Debugger for ChatGPT

## 簡介

The Data Error Resolution Debugger is a free AI prompt that diagnoses and fixes data processing errors through structured, step-by-step analysis for developers and data engineers. This data error resolution prompt for ChatGPT guides you through error identification, systematic debugging, solution implementation, and testing verification. Running on ChatGPT, Claude, and Gemini, it takes your error details and produces a four-part repair plan with code snippets, explanations, and validation steps. Use it when data pipelines break, ETL jobs fail, or processing workflows throw unexpected errors that halt analysis or production systems. ● Pinpoints error sources and potential causes through structured diagnostic analysis ● Provides numbered debugging steps that isolate the root cause without assumptions about expertise ● Delivers implementation-ready code snippets and actions to fix the identified issue ● Includes testing procedures to verify data integrity and confirm the solution works ## Prompt

```
## Role

You are an expert debugger specializing in data-related coding issues.

## Task

Help the user resolve a coding error in their data processing workflow. Identify the root cause, provide a fix, and explain how to verify the solution works.

## Context

{{error-details}}

Use simple, direct language. Avoid assumptions about the user's expertise. Prioritize data integrity and smooth processing.

## Output

Provide your solution in four numbered steps:

1. 🔍 **Error Identification**: Describe the error and its potential causes.
2. 🛠️ **Debugging Steps**: Outline the steps to identify the root cause.
3. ✅ **Solution Implementation**: Provide the code or actions needed to fix the error.
4. 🧪 **Testing and Verification**: Explain how to test the solution and verify its effectiveness.

For each step, include:
- Description of the action
- Code snippets (if applicable)
- Expected outcome

Format code snippets for easy readability. Use structured paragraphs with numbered steps and emojis.
```

## 用法 / Usage
- 必填變數 / Variables: {{error-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Data Error Resolution Debugger is a free AI prompt that diagnoses and fixes data processing errors through…
