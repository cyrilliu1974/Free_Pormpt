# Source Code Commenting Prompt for ChatGPT

## 簡介

The Source Code Commenting Prompt for ChatGPT is a free AI prompt that adds clear, structured documentation comments to existing code for software developers and engineering teams. This source code commenting prompt for ChatGPT analyzes your code and inserts inline comments, block comments, and header documentation that explain what each component does, why architectural decisions were made, how complex algorithms work, and where edge cases may occur. It runs on ChatGPT, Claude, and Cursor, preserving your original code while layering in maintainability-focused documentation. Real use cases include onboarding new team members to legacy codebases, preparing open-source projects for external contributors, and documenting internal tools before handoff. Reach for this prompt when you need to retrofit undocumented code, prepare a pull request for review, or create educational examples that explain implementation choices alongside working logic. ● Inserts inline comments for line-level clarification and block comments for functions, classes, and modules using correct language-specific syntax. ● Explains architectural rationale, algorithm complexity, and potential gotchas that aren't obvious from reading the code alone. ● Adapts comment depth and terminology to match your target audience, from junior developers to senior maintainers. ● Returns fully functional code with zero logic changes - only documentation added - so you can commit or deploy immediately. ## Prompt

```
## Role
You are an expert software developer specializing in code documentation and maintainability.

## Task
Add clear, informative comments to the provided source code. Comments should explain:
- What each component does
- Why architectural and implementation decisions were made
- Complex logic and algorithms
- Potential edge cases and gotchas
- Important considerations for maintenance and extension

Tailor comment style and depth to the target audience's experience level.

## Context
{{code-and-language}}

{{documentation-focus}}

## Output
Return the original code with inline comments and block comments added using the correct syntax for the language. Structure comments according to these conventions:
- Inline comments for line-level clarification
- Block comments for functions, classes, and complex sections
- Header comments for modules and major components

Preserve all original code functionality; only add documentation.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-language}}、{{documentation-focus}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Source Code Commenting Prompt for ChatGPT is a free AI prompt that adds clear, structured documentation co…
