# Comparison Operator Error Analyzer for Code Debugging

## 簡介

The Comparison Operator Error Analyzer for Code Debugging is a free AI prompt that systematically identifies logical errors in code caused by incorrect comparison operators, assignment misuse, and logical expression mistakes. This comparison operator debugging prompt for ChatGPT walks through conditional statements, loop conditions, and logical expressions to find errors like assignment operators (=) used instead of comparison (==, ===), reversed relational operators (> vs <), type compatibility issues, and logical operator mistakes (&& vs ||). It runs on ChatGPT, Claude, Gemini, and Grok, delivering structured error reports with problematic code snippets, explanations of what the incorrect operator actually does versus what was intended, corrected versions, and root-cause analysis tailored to your experience level. Developers reach for this prompt when their code passes syntax checks but produces unexpected behavior due to subtle logical mistakes. ● Detects assignment operators mistakenly used in conditionals (= instead of == or ===) that silently change program behavior. ● Identifies reversed relational operators and logical operator errors that cause loops and conditionals to behave opposite to intent. ● Provides side-by-side incorrect and corrected code snippets with plain-language explanations of what each operator actually does. ● Tailors root-cause analysis and prevention tips to the developer's stated experience level, from beginner to advanced. ## Prompt

```
## Role
You are an expert code reviewer specializing in comparison operator errors—logical mistakes that pass syntax checks but break functionality.

## Task
Systematically analyze the provided code for comparison operator errors. For each mistake, explain what the incorrect operator does versus what was intended, provide the corrected version, and clarify why the error occurs.

## Focus Areas
- Conditional statements, loop conditions, and logical expressions
- Assignment operators (`=`) used instead of comparison (`==`, `===`)
- Reversed relational operators (`>` vs `<`, `>=` vs `<=`)
- Type compatibility issues causing unexpected comparisons
- Logical operator mistakes (`&&` vs `||`, `!` placement)

## Context
**Code Submission:**
{{code-submission}}

*Include: programming language, code snippet, intended behavior, actual unexpected behavior, and your experience level.*

## Output
Structure your response:

### Error [N]: [Brief Label]
**Incorrect Code:**
```
[problematic line(s)]
```

**Problem:** What the current operator actually does

**Correction:**
```
[fixed line(s)]
```

**Why This Happens:** Root cause and prevention tips tailored to the stated experience level

---

If no comparison operator errors are found, state that clearly and check for related logical issues that might cause the described symptoms.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-submission}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Comparison Operator Error Analyzer for Code Debugging is a free AI prompt that systematically identifies l…
