# CSV Merger Code Generator Prompt

## 簡介

The CSV Merger Code Generator Prompt is a free AI prompt that produces executable merge code for data integration specialists working with multiple CSV files that have mismatched schemas, varying headers, and quality issues. This CSV merger prompt for ChatGPT analyzes your CSV file structures, identifies alignment columns with confidence scores, and generates fully commented code that validates schema compatibility before merging. It handles header variations (case differences, spacing, special characters), implements your specified duplicate removal logic, and creates an audit trail documenting every transformation. The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing code that explicitly handles missing values, preserves original data types unless conversion is necessary, and includes row-level validation to catch merge errors. Real use cases include consolidating sales data from regional offices, merging customer records from acquired companies, and combining experimental datasets with inconsistent naming conventions. Reach for this prompt when you need to merge CSV files with incompatible structures and want production-ready code that documents every decision and flags potential quality issues. ● Displays schema comparison tables showing column names, data types, and sample values for each CSV file before merging ● Identifies potential join columns with confidence scores and flags column name conflicts where the same name contains different data ● Generates executable code with inline comments documenting all transformation decisions, duplicate handling, and data type conversions ● Produces a data quality report highlighting type coercion warnings, merge conflicts, suspicious patterns, and row-level validation results ## Prompt

```
## Role
You are a data integration specialist merging CSV files while preserving data integrity and following Tidy Data principles (each variable is a column, each observation is a row, each type forms a table).

## Task
Generate code to merge multiple CSV files with inconsistent structures, varying headers, and potential quality issues. Analyze schema compatibility, identify alignment columns, handle variations, and preserve integrity throughout.

## Context
{{csv-files-and-context}}

Describe your CSV files: paste content samples, provide file locations, or describe structure. Include known key columns for alignment and duplicate-handling preference (keep first, last, all, or custom logic).

## Process

1. **Schema Analysis**: Display each file's structure—column names, data types, sample values—in a comparison table.

2. **Alignment Strategy**: Identify potential join columns with confidence scores. Flag column name conflicts (same name, different data).

3. **Merge Code Generation**: Produce executable code that:
   - Validates schema compatibility before merging
   - Handles header variations (case, spacing, special characters)
   - Implements specified duplicate removal logic
   - Handles missing values explicitly—never silently drops or fills without documenting
   - Preserves original data types unless conversion is necessary and logged
   - Creates an audit trail of all transformations
   - Includes row-level validation to catch merge errors
   - Documents all decisions with inline comments

4. **Execution Summary**: Report source row counts, duplicates removed, and data type conversions performed.

5. **Data Quality Report**: Highlight potential issues—type coercion warnings, merge conflicts, suspicious patterns.

## Output

**File Analysis**
- Schema comparison table

**Alignment Strategy**
- Identified join columns and logic

**Merge Code**
- Fully commented, reproducible script

**Summary Statistics**
- Source row counts, duplicates handled, conversions applied

**Data Quality Warnings**
- Issues detected during merge

**Preview**
- First 10 rows of merged dataset
```

## 用法 / Usage
- 必填變數 / Variables: {{csv-files-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The CSV Merger Code Generator Prompt is a free AI prompt that produces executable merge code for data integrat…
