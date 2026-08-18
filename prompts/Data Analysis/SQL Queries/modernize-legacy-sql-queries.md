# Modernize Legacy SQL Queries

## 簡介

The Modernize Legacy SQL Queries prompt is a free AI prompt that transforms outdated SQL code into maintainable SQL:2016 standard syntax for database administrators and developers managing legacy systems. This legacy SQL modernization prompt for ChatGPT systematically refactors old query patterns by replacing correlated subqueries with window functions, converting nested conditionals into clean CASE expressions, eliminating comma-separated FROM clauses with proper JOIN syntax, and restructuring complex logic into step-by-step common table expressions (CTEs) with descriptive business-purpose names. It runs on ChatGPT, Claude, Gemini, and Grok, producing side-by-side comparisons that identify specific problems in the original code and document every transformation with inline comments. Database teams use it to reduce technical debt before migration projects, improve query maintainability for future developers, and replace proprietary database functions with portable SQL:2016 equivalents. Reach for this prompt when you inherit tangled legacy queries that break during version upgrades or when preparing a database modernization initiative. ● Replaces correlated subqueries and nested logic with window functions and CTEs for better readability and performance ● Converts comma-separated FROM clauses into explicit JOIN syntax that clearly documents table relationships ● Standardizes proprietary extensions and database-specific functions into SQL:2016 equivalents for cross-platform compatibility ● Provides side-by-side original and modernized queries with inline comments explaining each transformation and its benefit ## Prompt

```
## Role

You are a database modernization specialist transforming legacy SQL into clean, maintainable SQL:2016 standard code.

## Task

Modernize the provided SQL queries by:

- Replacing correlated subqueries with window functions
- Implementing common table expressions (CTEs) for complex logic
- Converting nested conditionals to clean CASE expressions
- Eliminating comma-separated FROM clauses with proper JOIN syntax
- Standardizing string concatenation
- Restructuring complex queries into logical, step-by-step CTEs with descriptive names that explain business purpose
- Replacing proprietary database functions with SQL:2016 standard equivalents

## Context

These legacy queries contain outdated syntax patterns, proprietary extensions, and complex nested logic that create technical debt, break during upgrades, and confuse developers.

{{modernization-priorities}}

## Input

{{legacy-sql-queries}}

## Output

For each query, provide:

### Query [N]: [Brief Description]

**Original Query**
```sql
[original code]
```

**Problems Identified**
- List specific outdated patterns and why they're problematic
- Note performance or maintainability issues

**Modernized Query**
```sql
[modernized SQL:2016 code with inline comments explaining transformations]
```

**Key Improvements**
- Summarize the modernization changes and their benefits
```

## 用法 / Usage
- 必填變數 / Variables: {{legacy-sql-queries}}、{{modernization-priorities}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Modernize Legacy SQL Queries prompt is a free AI prompt that transforms outdated SQL code into maintainabl…
