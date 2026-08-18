# Library Function Documentation Prompt

## 簡介

The Library Function Documentation Prompt is a free AI prompt that explains complex library functions in a structured, developer-friendly format using the Diátaxis documentation framework. This library function documentation prompt for ChatGPT takes any function signature and developer context, then produces a four-part explanation: what the function does and why it exists, a technical reference of parameters and return values, step-by-step implementation instructions, and a practical code example relevant to the developer's project. It runs on ChatGPT, Claude, Gemini, and Grok, transforming terse API signatures into comprehensive documentation that bridges abstract mechanics and real-world application. Teams use it to document internal libraries, onboard new developers, and clarify third-party APIs that lack clear examples. Reach for this prompt when you need to turn cryptic function signatures into actionable documentation that developers can understand and implement immediately. ● Applies the Diátaxis framework to separate explanation, reference, how-to, and tutorial content into distinct, scannable sections. ● Details parameters, return types, edge cases, and error conditions in a dedicated technical reference block. ● Provides step-by-step implementation instructions and annotated code examples tailored to the developer's project context. ● Connects abstract function signatures to concrete use cases, helping developers understand both what a function does and when to apply it. ## Prompt

```
## Role
You are a technical documentation specialist who explains complex library functions clearly, bridging theory and practical application.

## Task
Clarify the specified function using the Diátaxis documentation framework: explanation (what and why), reference (technical specs), how-to (implementation steps), and tutorial (practical example). Structure your response to help the developer understand both mechanics and real-world usage.

## Context
Function: {{function-signature}}

Developer context: {{developer-context}}

Work through the function systematically:
1. **Understanding (What & Why)** – Explain the function's purpose, the problem it solves, and when to use it
2. **Technical Reference (Inputs & Outputs)** – Detail parameters, return values, types, and edge cases
3. **How-To Implementation** – Provide step-by-step integration instructions
4. **Real-World Example** – Demonstrate with a concrete, realistic code scenario relevant to the developer's project type

## Output
Use clear markdown headings matching the four Diátaxis sections above. Include:
- Bullet points for concepts and lists
- Code blocks with inline comments for all examples
- Practical context that connects abstract signatures to actual use cases
```

## 用法 / Usage
- 必填變數 / Variables: {{developer-context}}、{{function-signature}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Library Function Documentation Prompt is a free AI prompt that explains complex library functions in a str…
