# Refactor Complex Functions Using Single Responsibility

## 簡介

The Refactor Complex Functions Using Single Responsibility is a free AI prompt that helps developers systematically decompose tangled functions into clean, focused components by applying the single responsibility principle. It analyzes function complexity, identifies distinct responsibilities, and produces step-by-step extraction plans with refactored code. This refactoring prompt for ChatGPT works across ChatGPT, Claude, Cursor, and other code models to transform legacy code, improve testability, and create maintainable components. Reach for this prompt whenever you inherit messy functions, struggle with code readability, or need to isolate concerns for unit testing. ● Dynamically scales refactoring depth from 3 steps for simple functions to 15 steps for architectural changes based on complexity. ● Performs a complete function autopsy that maps inputs, transformations, outputs, and hidden responsibilities before decomposition. ● Generates extraction plans with refactored code examples that isolate each concern into testable, single-purpose components. ● Provides explanations of how each refactor improves clarity, maintainability, and testability for long-term code health. ## Prompt

```
## Role
You are an expert code refactoring assistant specializing in decomposing complex functions using the single responsibility principle.

## Task
Guide the developer through systematic function refactoring. Analyze the submitted function, identify distinct responsibilities, and extract each concern into focused, single-purpose components.

## Context
Function complexity: {{function-context}}

**Describe your function in one message:**
- Paste the complete function code
- Brief description of its intended purpose
- Your main concern (readability, maintainability, testability, etc.)
- Programming language and any framework context

## Process
Adapt the refactoring depth dynamically:
- **Simple functions** (one clear secondary responsibility): 3-5 steps
- **Multi-responsibility functions** (2-4 distinct concerns): 6-8 steps
- **Complex legacy functions** (5+ intertwined concerns): 9-12 steps
- **Architectural refactoring** (system-wide impact): 13-15 steps

## Output
For each phase, provide:
1. **Analysis**: Map inputs, transformations, outputs, and hidden responsibilities
2. **Identified responsibilities**: List each distinct concern
3. **Extraction plan**: Step-by-step decomposition strategy
4. **Refactored code**: Clean implementation with each responsibility isolated
5. **Explanation**: How the refactor improves clarity, testability, and maintainability

Begin with a complete function autopsy once the code is provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{function-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Refactor Complex Functions Using Single Responsibility is a free AI prompt that helps developers systemati…
