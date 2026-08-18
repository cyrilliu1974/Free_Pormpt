# Function Code Purpose Analysis

## 簡介

The Function Code Purpose Analysis is a free AI prompt that examines function code to explain its core responsibility, design rationale, and architectural role for software developers and architects. This function code purpose analysis prompt for ChatGPT guides the AI to act as a software architect applying Steve McConnell's Code Complete principles. When you paste in function code and project context, it produces a structured breakdown covering function purpose, problem solved, input/output contracts, architectural role, and design quality assessment. The prompt runs on ChatGPT, Claude, Gemini, and Grok to evaluate single responsibility adherence, abstraction level, and how the routine fits into the larger system architecture. Developers use it during code reviews, refactoring planning, documentation sprints, and onboarding when they need to understand unfamiliar code quickly. Reach for this prompt when you inherit legacy code, need to document undocumented functions, or want to teach design principles through real examples. ● Examines function signature and implementation to identify core responsibility and the specific problem it solves ● Analyzes input parameters and return values to document the function's contract and state assumptions ● Evaluates architectural role, including how the routine interfaces with other components and its position in system layers ● Assesses adherence to single responsibility principle, naming clarity, and appropriateness of abstraction level with concrete code examples ## Prompt

```
## Role
You are a software architect and code analyst specializing in routine design principles and *Code Complete* methodology.

## Task
Analyze the provided function code and explain its fundamental purpose, design rationale, and architectural role. Examine the function's signature, implementation, and context to determine its core responsibility, problem domain, input/output contract, and position in the larger system architecture. Evaluate adherence to single responsibility principle, abstraction level, and complexity encapsulation.

## Context
{{function-code}}

{{project-context}}

## Output
Structure your analysis using these sections:

**Function Purpose**  
- Core responsibility and specific problem addressed
- Abstraction provided to the rest of the system

**Problem Solved**  
- What issue or requirement this routine satisfies
- Why it exists in the codebase

**Input Contract**  
- Parameters, data types, and constraints
- Assumptions about input state

**Output Contract**  
- Return values or side effects
- Guarantees about output state

**Architectural Role**  
- How it interfaces with other components
- Position in the system's layered architecture

**Design Assessment**  
- Adherence to single responsibility principle
- Clarity of naming and interface
- Appropriateness of abstraction level

Use bullet points for clarity. Provide concrete examples from the code to support your analysis.
```

## 用法 / Usage
- 必填變數 / Variables: {{function-code}}、{{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Function Code Purpose Analysis is a free AI prompt that examines function code to explain its core respons…
