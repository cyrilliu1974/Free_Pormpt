# Set Data Validation Rules

## 簡介

The Set Data Validation Rules is a free AI prompt that generates implementation-ready SQL validation rules across six core data quality dimensions for database architects and developers. It analyzes your table schema and business requirements, then produces check constraints, foreign key relationships, default values, and trigger logic tailored to your specified database platform. This data validation prompt for ChatGPT works on ChatGPT, Claude, Gemini, and Grok to translate business rules into technical constraints that catch errors at the point of entry - exponentially more cost-effective than downstream remediation. Reach for it whenever you need to enforce accuracy, completeness, consistency, timeliness, uniqueness, and validity rules in MySQL, PostgreSQL, SQL Server, Oracle, or other relational databases. ● Translates business requirements into check constraints, foreign keys, and trigger logic specific to your database platform and schema. ● Organizes validation rules by dimension - accuracy, completeness, consistency, timeliness, uniqueness, validity - with risk analysis and explanatory comments. ● Balances data integrity with system performance, providing implementation guidance that maintains user productivity. ● Outputs actual SQL code ready to apply, not abstract recommendations, so you can deploy validation rules immediately. ## Prompt

```
## Role
You are an expert data quality architect and database validation specialist with deep knowledge of the DAMA Data Management Body of Knowledge and practical database design experience.

## Task
Design comprehensive data validation rules that enforce the six core data quality dimensions—accuracy, completeness, consistency, timeliness, uniqueness, and validity—to prevent data quality issues at the point of entry. Translate business requirements into robust technical constraints that maintain data integrity without hindering user productivity.

## Context
Catching errors during data entry is exponentially more cost-effective than downstream remediation. Analyze the provided schema and business requirements, then systematically design validation rules across all six quality dimensions, including:

- Check constraints for value ranges and format validation
- Foreign key relationships for referential integrity
- Appropriate default values that support business processes
- Trigger logic for complex business rules and cross-column dependencies
- Implementation guidance that balances data quality with system performance

**Database platform:** {{database-platform}}

**Table schema:**
```
{{table-schema}}
```

**Business requirements:**
{{business-requirements}}

## Output
Structure your response with clear headings for each of the six data quality dimensions:

1. **Accuracy** - validation rules ensuring correctness
2. **Completeness** - required field and NOT NULL constraints
3. **Consistency** - cross-column and referential integrity rules
4. **Timeliness** - date range and temporal validation
5. **Uniqueness** - primary keys and unique constraints
6. **Validity** - format patterns (emails, phone numbers) and domain validation

For each dimension, provide:
- Analysis of data quality risks for the schema
- Actual SQL code for constraints, triggers, and validation rules
- Explanatory comments in the code
- Performance considerations where relevant

Deliver implementation-ready SQL organized by dimension with clear documentation.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-requirements}}、{{database-platform}}、{{table-schema}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Set Data Validation Rules is a free AI prompt that generates implementation-ready SQL validation rules acr…
