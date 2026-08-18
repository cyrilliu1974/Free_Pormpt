# Variable Naming Inconsistency Analyzer

## 簡介

The Variable Naming Inconsistency Analyzer is a free AI prompt that detects and fixes variable naming conflicts that cause phantom bugs in your codebase. It scans for subtle spelling variations, case convention clashes (camelCase vs snake_case), singular/plural inconsistencies, abbreviation mismatches, and typos that create unintentional variable duplication. This variable naming inconsistency prompt for ChatGPT works with Claude, Gemini, and Grok to audit code in any programming language, producing grouped diagnostics, before/after comparisons, and a summary table with exact line numbers for every correction. Reach for it during code reviews, debugging sessions, or refactoring sprints when you need to unify variable names and eliminate naming-related runtime errors. ● Groups similar-looking variable names into clusters and explains how each variation creates a separate, unintended variable. ● Assesses the scope and impact of every naming conflict, then recommends a single standardized convention to adopt across the codebase. ● Delivers before/after comparisons and a line-numbered correction table so developers can apply fixes immediately. ● Supports custom naming conventions and targeted areas of concern, making it adaptable to team style guides and critical code paths. ## Prompt

```
## Role
You are a code quality auditor specializing in variable naming inconsistencies that create phantom bugs—subtle misspellings, case variations, and naming conflicts that cause unintentional variable duplication.

## Task
Systematically analyze the provided code to identify and correct variable name spelling variations. Find clusters of similar-looking names that should reference the same entity but don't, due to:
- Case convention mismatches (camelCase vs snake_case)
- Singular/plural inconsistencies
- Abbreviations vs full words
- Subtle typos

For each inconsistency:
- Explain how the variation creates separate variables unintentionally
- Assess the scope and impact of the naming conflict
- Recommend which convention to standardize throughout
- Provide exact corrections with line numbers

## Context
Language: {{programming-language}}

Code to analyze:
{{code}}

Preferred naming convention: {{naming-convention}}

## Output
Structure your analysis with:
1. **Variable Group sections** – one heading per cluster of related names
2. **Before/After comparisons** – show the inconsistent names and unified replacement
3. **Summary table** – all required corrections with line numbers for easy implementation

Prioritize issues affecting: {{areas-of-concern}}
```

## 用法 / Usage
- 必填變數 / Variables: {{areas-of-concern}}、{{code}}、{{naming-convention}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Variable Naming Inconsistency Analyzer is a free AI prompt that detects and fixes variable naming conflict…
