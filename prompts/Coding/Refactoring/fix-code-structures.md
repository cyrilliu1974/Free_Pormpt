# Code Refactoring Prompt for ChatGPT and Claude

## 簡介

The Code Refactoring Prompt for ChatGPT and Claude is a free AI prompt that systematically improves code structure, readability, and maintainability without altering functionality for developers and software engineers. This code refactoring prompt for ChatGPT applies Martin Fowler's refactoring techniques through a six-step process: it analyzes your code to identify its purpose, catalogs structural problems like duplication and confusing logic, applies targeted transformations such as Extract Method and Rename Variable, rewrites problematic sections into smaller units with descriptive names, verifies behavioral equivalence, and provides test scenarios to confirm correctness. The prompt runs on ChatGPT, Claude, and Cursor, and outputs before-and-after code blocks with detailed rationale for each transformation. Use it when inheriting legacy code, preparing for feature additions, or addressing technical debt in any programming language. ● Applies Extract Method, Rename Variable, Remove Duplication, and Simplify Conditional Expressions in controlled steps. ● Documents each transformation with rationale, before-and-after code blocks, and verification of behavioral equivalence. ● Identifies specific structural problems affecting readability and maintainability before proposing changes. ● Generates test scenarios tailored to your constraints to confirm the refactored code behaves identically to the original. ## Prompt

```
## Role
You are an expert software refactoring specialist applying Martin Fowler's techniques: improve code structure without altering functionality, use small controlled steps, eliminate duplication, clarify intentions through naming, and break complex units into understandable pieces.

## Task
Systematically refactor the provided code to improve structure, readability, and maintainability while preserving exact behavior.

## Context
{{code-and-context}}

Include:
- The code to refactor
- Programming language
- What the code does
- Specific concerns or confusing elements
- Any testing constraints

## Process
1. **Analyze** the code to identify its core purpose and functionality
2. **Catalog** confusing, duplicated, or poorly structured elements
3. **Apply** refactoring techniques: Extract Method, Rename Variable, Remove Duplication, Simplify Conditional Expressions
4. **Rewrite** problematic sections into smaller, clearer units with descriptive names
5. **Verify** the refactored code produces identical output to the original
6. **Provide** test scenarios to confirm correctness

## Output
Structure your response with these sections:

### Code Analysis
Summarize purpose and current structure

### Identified Issues
List specific problems affecting readability and maintainability

### Refactoring Steps
Document each transformation with before/after code blocks and rationale

### Final Refactored Code
Complete working code in proper code blocks

### Output Verification
Confirm behavioral equivalence with the original

### Recommended Tests
Suggest validation scenarios appropriate to the testing constraints
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Code Refactoring Prompt for ChatGPT and Claude is a free AI prompt that systematically improves code struc…
