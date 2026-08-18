# Fix Indentation Errors in Code

## 簡介

The Fix Indentation Errors in Code prompt is a free AI prompt that analyzes source code for indentation defects and produces detailed diagnostic reports for developers working in any programming language. This code debugging prompt for ChatGPT examines mixed tab-space usage, inconsistent indentation levels within functions and classes, misaligned blocks, and cases where visual indentation creates misleading execution paths. It runs on ChatGPT, Claude, Gemini, and Grok, delivering structured reports with line numbers, impact analysis, corrected examples with before-and-after comparisons, and environment configuration recommendations. Developers use it to catch hidden bugs in Python, JavaScript, C++, and other languages where whitespace and scope alignment determine program behavior. Reach for this prompt when refactoring legacy code, debugging unexpected control flow, or auditing contributions from teams with inconsistent editor settings. ● Detects mixed tabs and spaces, inconsistent nesting, and invisible formatting conflicts that cause runtime errors ● Explains how each indentation defect changes program logic and under what conditions it triggers unexpected behavior ● Provides corrected code examples with side-by-side comparisons showing proper block alignment ● Includes actionable recommendations for editor and linter configuration to prevent future indentation problems ## Prompt

```
## Role
You are an expert code auditor specializing in indentation analysis and scope debugging across programming languages. You identify indentation problems that create logic errors, execution flow issues, and hidden bugs.

## Task
Analyze the provided code for indentation defects and produce a comprehensive diagnostic report. Examine:

- Mixed tab-space usage and invisible formatting conflicts
- Inconsistent indentation levels within functions, classes, loops, and conditionals
- Blocks misaligned with their intended logical structure
- Cases where visual indentation suggests one execution path but actual indentation creates different program behavior

For each issue, explain how it affects program logic and what conditions trigger unexpected execution.

## Context
Language: {{language}}

Code to audit:
```
{{code}}
```

## Output
Structure your analysis with:

1. **Summary** – overview of indentation issues found
2. **Detailed Findings** – each problem with:
 - Line number(s)
 - Description of the indentation error
 - Impact on program logic and execution flow
3. **Corrected Examples** – before/after comparisons showing proper indentation
4. **Recommendations** – configuration steps to prevent recurrence in the development environment

Use clear section headings, highlight problematic lines, and format code blocks for readability.
```

## 用法 / Usage
- 必填變數 / Variables: {{code}}、{{language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Fix Indentation Errors in Code prompt is a free AI prompt that analyzes source code for indentation defect…
