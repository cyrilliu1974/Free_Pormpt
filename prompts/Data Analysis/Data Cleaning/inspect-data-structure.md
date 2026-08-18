# Data Structure Inspection Prompt for Python and R

## 簡介

The Data Structure Inspection Prompt for Python and R is a free AI prompt that performs systematic code-based analysis to reveal the complete anatomy of a dataset for data scientists and analysts. It generates executable inspection code following tidy data principles - each variable forms a column, each observation forms a row, and each type of observational unit forms a table - then interprets structural findings to guide data readiness decisions. This data structure inspection prompt for ChatGPT works across ChatGPT, Claude, Gemini, and Grok, producing Python or R code blocks that examine dimensions, data types, memory usage, missing value patterns, and representative samples to surface data quality concerns before modeling or visualization. Reach for this prompt when inheriting a new dataset, auditing data pipelines, or preparing data for downstream analysis in any programming environment. ● Generates ready-to-execute code blocks that examine dataset shape, column names, data types, and memory footprint in your chosen language. ● Calculates non-null counts and missing data patterns across all variables, flagging completeness issues before analysis. ● Extracts head, tail, and random samples to uncover structural inconsistencies, encoding errors, and unexpected values. ● Delivers interpretive readiness insights with bulleted recommendations for cleaning, transformation, or format adjustments. ## Prompt

```
## Role
You are an expert data scientist specializing in data structure inspection following tidy data principles: each variable forms a column, each observation forms a row, and each type of observational unit forms a table.

## Task
Perform a comprehensive data structure inspection that reveals the complete anatomy of a dataset through systematic code-based analysis.

## Context
Dataset format: {{dataset-format}}
Programming language: {{programming-language}}
Analysis goals: {{analysis-goals}}

## Process
1. **Confirm the dataset** - Request upload/path and verify format compatibility
2. **Structural foundation** - Generate code to examine dimensions, column names, data types, and memory usage
3. **Missing value analysis** - Calculate non-null counts and missing data patterns across all variables
4. **Representative sampling** - Extract and display head, tail, and random samples to identify inconsistencies, patterns, or data quality issues
5. **Readiness assessment** - Provide interpretive insights about what the structural analysis reveals for downstream analysis

## Output
Structure your response with:
- Clear code blocks ready to execute
- Explanatory section headers (## Structural Overview, ## Missing Data Profile, ## Sample Inspection, ## Readiness Insights)
- Actionable findings in bullet points highlighting structural issues, data quality concerns, and recommended next steps
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-goals}}、{{dataset-format}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Data Structure Inspection Prompt for Python and R is a free AI prompt that performs systematic code-based …
