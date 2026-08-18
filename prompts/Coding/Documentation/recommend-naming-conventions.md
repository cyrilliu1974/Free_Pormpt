# Naming Convention Guidelines for Code Documentation

## 簡介

The Naming Convention Guidelines for Code Documentation is a free AI prompt that creates tailored naming standards for software development teams working in any programming language. This naming convention prompt for ChatGPT, Claude, Gemini, and Grok analyzes your language ecosystem and project context to produce structured guidelines covering variables, functions, classes, and file structures. It delivers pattern rules, concrete examples, anti-patterns with explanations, and rationale grounded in readability and maintainability principles. Development teams use it to establish consistent coding standards before starting new projects, during code review process improvements, or when onboarding engineers to existing codebases. The prompt adapts to language idioms - whether you're working in Python, TypeScript, Rust, or any other language - and addresses common pitfalls specific to that ecosystem. ● Produces pattern-based rules for variables, constants, parameters, functions, methods, classes, interfaces, types, files, and directories tailored to your language. ● Includes 3-4 positive examples and 2-3 anti-patterns with explanations for each code element type, making standards immediately actionable. ● Addresses language-specific pitfalls and idiomatic conventions so guidelines align with ecosystem best practices. ● Balances descriptiveness with conciseness and explains the readability rationale behind each pattern to build team understanding. ## Prompt

```
## Role
You are a software architect specializing in naming conventions and code maintainability. Apply principles that create self-documenting, intent-revealing code.

## Task
Create comprehensive, language-specific naming convention guidelines for {{programming-language}} that reduce cognitive load and improve code readability across the team.

## Context
Project context:
{{project-context}}

Good naming conventions balance descriptiveness with conciseness while honoring language idioms. Consistent patterns reduce onboarding time and make codebases intuitive to navigate.

## Process
1. If {{project-context}} lacks critical details about the development environment, existing patterns, or team constraints, ask 2-3 clarifying questions
2. Analyze the language ecosystem and common idioms for {{programming-language}}
3. Create guidelines covering variables (including constants and parameters), functions/methods, classes/interfaces/types, and files/directories

## Output
Structure your guidelines with:

### [Code Element Type]
- **Pattern**: The convention rule
- **Examples**: 3-4 good examples
- **Anti-patterns**: 2-3 examples to avoid, with brief explanation why
- **Rationale**: Why this pattern works (readability, intent, maintenance)

For each section, address common pitfalls specific to {{programming-language}} and how consistent naming reduces ambiguity. Prioritize patterns that make code self-documenting and align with the {{project-context}} constraints.
```

## 用法 / Usage
- 必填變數 / Variables: {{programming-language}}、{{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Naming Convention Guidelines for Code Documentation is a free AI prompt that creates tailored naming stand…
