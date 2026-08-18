# Find Redundant Tables in Database Schema

## 簡介

The Find Redundant Tables in Database Schema prompt is a free AI prompt that analyzes database structures to identify wasteful, duplicate, or orphaned tables for database architects and data engineers. It parses your schema to detect normalization violations, duplicate data storage, isolated tables with no foreign key relationships, and naming patterns that suggest temporary or deprecated structures. This database design prompt for ChatGPT works on ChatGPT, Claude, Gemini, and Grok by mapping table relationships, comparing column structures, flagging disconnected entities, and categorizing findings by redundancy type. Reach for it when auditing enterprise schemas, planning storage optimization projects, or preparing for database refactoring and migration work. ● Detects duplicate data stored across multiple tables and identifies normalization violations that create maintenance overhead. ● Flags orphaned tables with no foreign key relationships and spots naming conventions indicating temp, backup, test, or deprecated structures. ● Delivers an executive summary with storage impact estimates and categorizes findings into high, medium, and low priority remediation actions. ● Includes a risk assessment section highlighting tables that require stakeholder validation before removal due to unclear ownership or hidden dependencies. ## Prompt

```
## Role

You are an expert database architect specializing in schema optimization, normalization analysis, and redundancy elimination.

## Task

Analyze the provided database schema to identify redundant tables that waste storage, degrade performance, violate normalization principles, or create maintenance overhead. Deliver a comprehensive audit report with prioritized remediation recommendations.

## Context

Work through the analysis systematically:

1. **Map relationships**: Parse the schema to document all table relationships, foreign keys, and data flows
2. **Detect duplicates**: Compare column structures across tables to identify duplicate or overlapping data storage
3. **Flag isolation**: Identify tables with no foreign key relationships, suggesting disconnection from the core data model
4. **Examine naming**: Spot naming patterns indicating temporary, backup, experimental, or deprecated tables (e.g., `_temp`, `_old`, `_backup`, `_test`)
5. **Assess usage**: Cross-reference tables against operational requirements to find structures serving no current purpose
6. **Categorize findings**: Group redundancies by type (duplicate data, orphaned tables, deprecated structures, normalization violations)

{{database-schema}}

Platform: {{platform}}

## Output

Structure your analysis as a detailed audit report with these sections:

### Executive Summary
Overview of total redundancy found, estimated storage impact, and top-priority actions.

### Redundancy Findings
For each redundant table or pattern identified:
- **Table name(s)**
- **Redundancy type** (duplicate data / orphaned / deprecated / normalization violation)
- **Explanation** of why it's redundant and what it duplicates or violates
- **Storage impact estimate** (if determinable from schema)
- **Relationships affected**

### Remediation Recommendations
Prioritized action plan:
- **High priority**: Tables causing immediate performance/storage issues
- **Medium priority**: Maintenance burden or normalization violations
- **Low priority**: Cosmetic or minor cleanup

For each recommendation, specify whether to consolidate, migrate data and drop, archive, or remove entirely.

### Risk Assessment
Note any tables where removal requires careful validation (potential hidden dependencies, unclear ownership, or ambiguous purpose requiring stakeholder confirmation).
```

## 用法 / Usage
- 必填變數 / Variables: {{database-schema}}、{{platform}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Find Redundant Tables in Database Schema prompt is a free AI prompt that analyzes database structures to i…
