# Error Message Analysis Prompt for Debugging

## 簡介

The Error Message Analysis Prompt for Debugging is a free AI prompt that systematically dissects error messages and code snippets to reveal root causes and generate clear, actionable fixes for developers. This error message analysis prompt for ChatGPT, Claude, Gemini, and Grok takes a cryptic error message, the surrounding code, your programming language, and development environment, then produces a structured diagnosis covering error breakdown, root cause analysis, plain-language explanation, and step-by-step solutions with code examples. Real-world use cases include troubleshooting runtime exceptions, interpreting compiler warnings, resolving environment-specific bugs, and onboarding junior developers who struggle with technical jargon. It works by parsing file names, line numbers, and error types, locating the exact failure point in the code, and translating technical terminology into accessible language that reveals the underlying behavior rather than surface symptoms. Reach for this prompt when you encounter an unfamiliar error, need to explain a bug to non-technical stakeholders, or want to accelerate debugging workflows across your team. ● Parses error messages into digestible components - file paths, line numbers, error types, and operation contexts - so you know exactly where and why the failure occurred. ● Connects error symptoms to the underlying code behavior, surfacing root causes instead of just describing what broke. ● Delivers plain-language explanations that make technical failures understandable to stakeholders at any skill level. ● Provides step-by-step recommended solutions with code examples, turning diagnosis into immediate action. ## Prompt

```
## Role
You are an expert debugging specialist who systematically analyzes error messages and explains technical failures with clarity and precision.

## Task
Dissect the provided error message and code to identify the exact cause of the failure, then deliver a clear diagnosis with actionable solutions.

## Context
Working in {{programming-language}} within {{development-environment}}.

**Error message:**
{{error-message}}

**Code snippet:**
{{code-snippet}}

## Approach
1. Parse the error message for key components: file names, line numbers, error types, operation contexts
2. Locate the exact failure point in the code structure
3. Identify the operation that triggered the failure
4. Translate technical terminology into plain language
5. Connect error symptoms to underlying code behavior to reveal root causes, not just surface symptoms

## Output
Structure your response with these headings:

**Error Breakdown**
- Dissect each component of the error message

**Root Cause Analysis**
- Explain what actually failed and why

**Plain Language Explanation**
- Describe the problem without jargon

**Recommended Solution**
- Provide step-by-step fixes with code examples where applicable

Use bullet points for clarity and actionability.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-snippet}}、{{development-environment}}、{{error-message}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Error Message Analysis Prompt for Debugging is a free AI prompt that systematically dissects error message…
