# SQLite Database Loader From CSV Generator

## 簡介

The SQLite Database Loader From CSV Generator is a free AI prompt that produces a complete Python system to convert CSV files into properly normalized, indexed, and constrained SQLite databases for database architects and data engineers. This SQLite database loader prompt for ChatGPT, Claude, and Cursor analyzes your CSV data, infers optimal column types, applies normalization principles, defines primary and foreign key constraints, creates strategic indexes based on your query patterns, and validates every row during import with detailed logging. You provide descriptions of your CSV files and their relationships, validation rules, expected query patterns, and NULL-handling requirements, and the prompt generates annotated Python code plus schema documentation that explains every design decision. Use it when you need to transform raw CSV exports into production-ready relational databases with referential integrity, domain validation, and optimized read performance. ● Infers INTEGER, REAL, TEXT, BLOB, and NULL types by sampling CSV data and detecting numeric, date, boolean, and text patterns ● Generates normalized schemas with primary keys, foreign key relationships, NOT NULL constraints, and CHECK constraints for domain validation ● Creates indexes on primary keys, foreign keys, and query-critical columns while balancing read performance against write overhead ● Validates all rows against constraints during import, logs successful inserts and constraint violations separately, and reports row numbers with specific failure reasons ● Produces markdown schema documentation tables listing every table, column, data type, constraint type, and indexing rationale with inline code comments ## Prompt

```
## Role

You are a database architect and data engineer specializing in relational database design, normalization, and SQLite implementation.

## Task

Generate a complete Python system that converts CSV files into a properly normalized, indexed, and constrained SQLite database with validation reporting.

## Context

{{csv-files-and-relationships}}

{{validation-requirements}}

## Requirements

**Data type inference**
- Sample CSV data to determine optimal SQLite column types (INTEGER, REAL, TEXT, BLOB, NULL)
- Handle numeric, date, boolean, and text pattern detection
- Preserve precision and range requirements

**Schema design**
- Apply normalization principles (minimize redundancy, ensure referential integrity)
- Define primary keys for all tables
- Create foreign key constraints based on the described relationships
- Add NOT NULL constraints where business rules require values
- Implement check constraints for domain validation

**Indexing strategy**
- Index all primary and foreign keys
- Add indexes for columns used in anticipated queries: {{expected-query-patterns}}
- Balance read performance against write overhead

**Data validation and import**
- Validate all rows against defined constraints during import
- Handle NULL values according to: {{null-handling-rules}}
- Log successful imports and constraint violations separately
- Report row numbers and specific validation failures

**Documentation**
- Comment all code explaining logic and design decisions
- Generate schema documentation describing tables, columns, relationships, and constraints

## Output

Deliver:

1. **Complete Python code** with:
   - CSV analysis and type inference functions
   - Schema generation with proper constraints
   - Data validation and import logic
   - Detailed logging and error reporting
   - Inline comments explaining each component

2. **Schema documentation table** in markdown format:

| Table Name | Column Name | Data Type | Constraints | Index Strategy |
|------------|-------------|-----------|-------------|----------------|

Include all tables, columns, constraint types (PK, FK, NOT NULL, CHECK), and indexing rationale.
```

## 用法 / Usage
- 必填變數 / Variables: {{csv-files-and-relationships}}、{{expected-query-patterns}}、{{null-handling-rules}}、{{validation-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Skills_Catalog_Node_Extractor
- 適用 / Use when: The SQLite Database Loader From CSV Generator is a free AI prompt that produces a complete Python system to co…
