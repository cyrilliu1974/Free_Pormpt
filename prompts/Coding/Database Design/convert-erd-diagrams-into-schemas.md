# ERD to Database Schema Converter

## 簡介

The ERD to Database Schema Converter is a free AI prompt that translates Entity-Relationship Diagrams into complete, executable DDL statements for database architects and engineers. This ERD to SQL schema prompt for ChatGPT, Claude, and Cursor analyzes entity structures, relationship cardinality (one-to-one, one-to-many, many-to-many), and business constraints, then generates organized CREATE TABLE statements, foreign key constraints, junction tables for complex relationships, indexes, and inline documentation. Database architects use it to accelerate schema development for PostgreSQL, MySQL, SQL Server, Oracle, and other systems while maintaining referential integrity and enforcing business rules through explicit constraints. The prompt accepts an ERD diagram description, target database system, and preferred naming convention, then outputs production-ready code structured into logical sections. Reach for this prompt when you need to convert conceptual data models into deployable schemas without losing critical relationship definitions or constraint logic. ● Transforms every entity into properly typed tables with primary keys and appropriate column definitions ● Maps one-to-many and many-to-many relationships into foreign key constraints and junction tables with composite keys ● Generates explicit CHECK, UNIQUE, and NOT NULL constraints that enforce business rules at the schema level ● Produces indexes for foreign key columns and inline comments documenting complex cardinality or constraint rationale ## Prompt

```
## Role
You are a database architecture specialist who translates ERD diagrams into production-ready schemas, preserving all relationships, constraints, and cardinality rules.

## Task
Convert the provided ERD into complete, executable DDL statements that maintain data integrity and business logic.

Analyze before generating:
- Each entity and its attributes
- All relationships and their cardinality (1:1, 1:N, M:N)
- Constraints that enforce business rules
- Naming patterns that preserve business context

## Context
{{erd-diagram}}

Target database: {{database-system}}

Naming convention: {{naming-convention}}

## Output
Provide executable DDL organized as:

**1. Table Definitions**
- CREATE TABLE statements with all columns and explicit data types
- Inline PRIMARY KEY declarations

**2. Foreign Key Constraints**
- All FOREIGN KEY constraints with proper REFERENCES
- ON DELETE/ON UPDATE rules where business logic requires them

**3. Junction Tables**
- Tables for many-to-many relationships with composite primary keys

**4. Additional Constraints**
- UNIQUE, CHECK, NOT NULL constraints
- Business rules not covered by referential integrity

**5. Indexes**
- CREATE INDEX statements for foreign key columns

**6. Documentation**
- Inline comments (--) explaining complex business logic, non-obvious constraints, or cardinality enforcement

Ensure:
- Every entity becomes a properly named table
- Cardinality rules are enforced through schema design
- All constraints are explicit and production-ready
- The schema is immediately executable on the specified database system
```

## 用法 / Usage
- 必填變數 / Variables: {{database-system}}、{{erd-diagram}}、{{naming-convention}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The ERD to Database Schema Converter is a free AI prompt that translates Entity-Relationship Diagrams into com…
