# CSV Import System Design Prompt

## 簡介

The CSV Import System Design Prompt is a free AI prompt that produces step-by-step implementation guides for building production-grade CSV import functions with pandas, database transactions, and validation logic for data engineers and Python developers. This CSV import prompt for ChatGPT, Claude, and Cursor walks you through seven critical components: file format validation, data type checking, constraint validation against your database schema, batch processing strategies for large files, atomic transaction management, real-time progress feedback, and logging infrastructure. You provide your database schema, CSV structure, and file size context, and the AI returns runnable Python code examples with explanatory bullet points for each section. Real-world use cases include importing customer records into PostgreSQL, bulk-loading product catalogs with data integrity checks, and migrating legacy CSV exports into modern databases without risking partial imports or corruption. Reach for this prompt when you need to build or refactor a CSV import pipeline that must handle edge cases, prevent data corruption through all-or-nothing commits, and deliver clear error messages pinpointing problematic rows. ● Row-by-row validation against database constraints with specific error reporting including row numbers and issues ● Atomic transaction management ensuring all-or-nothing imports to prevent partial data corruption ● Batch processing strategies and progress tracking optimized for large file sizes ● Detailed logging infrastructure and audit trails for debugging and compliance ## Prompt

```
## Role
Expert data engineer specializing in production CSV import systems with pandas, database transactions, and data validation.

## Task
Provide a complete, step-by-step implementation guide for a production-ready CSV import function covering:

- CSV parsing with pandas
- Row-by-row validation against database constraints
- Comprehensive error reporting with specific row numbers and issues
- Atomic database transactions (all-or-nothing imports)
- Progress tracking for large files
- Detailed logging and audit trails
- File format and data type validation
- Batch processing strategies
- Rollback mechanisms on failure
- User-friendly progress feedback

## Context
Data corruption from partial imports can be catastrophic. Every aspect must prioritize atomicity, validation, and clear error reporting to ensure data integrity.

{{database-schema}}
{{csv-structure}}
{{file-size-and-environment}}

## Output
Structure your implementation guide with these sections, each containing complete runnable code examples in code blocks plus explanatory bullet points:

1. **File Format Validation** - Code with edge case handling
2. **Data Type Checking** - Implementation and type coercion strategies
3. **Constraint Validation** - Database-specific validation logic
4. **Batch Processing Strategy** - Performance optimization for the specified file sizes
5. **Transaction & Rollback Management** - Atomic import guarantees
6. **Progress & Error Reporting** - Real-time user feedback mechanisms
7. **Logging Infrastructure** - Audit trail and debugging support

Provide production-ready Python code with pandas and appropriate database libraries.
```

## 用法 / Usage
- 必填變數 / Variables: {{csv-structure}}、{{database-schema}}、{{file-size-and-environment}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The CSV Import System Design Prompt is a free AI prompt that produces step-by-step implementation guides for b…
