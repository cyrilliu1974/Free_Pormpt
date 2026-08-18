# Database Schema Generator Prompt for ChatGPT

## 簡介

The Database Schema Generator Prompt for ChatGPT is a free AI prompt that transforms application requirements into production-ready relational database schemas for developers, database architects, and technical leads. This database design prompt for ChatGPT takes your business logic and outputs complete SQL CREATE TABLE statements, entity relationship diagrams, foreign key constraints, normalization through third normal form, and indexing strategies that anticipate growth. It runs on ChatGPT, Claude, Gemini, Grok, and Cursor, applying best practices like single-column primary keys, explicit cascading rules, junction tables for many-to-many relationships, and snake_case naming conventions. Reach for this prompt whenever you need to move from requirements documents to a maintainable schema that avoids redundancy and supports common query patterns. ● Extracts entities and attributes from requirements, applies normalization rules, and generates SQL CREATE TABLE statements with primary keys, foreign keys, constraints, and indexes. ● Produces text-based entity relationship diagrams showing table connections, cardinality, and junction tables for many-to-many relationships. ● Documents design decisions, assumptions, and how the schema handles optional data, audit trails, soft deletes, and future growth beyond stated requirements. ● Follows relational design principles including minimized nullable fields, no derived columns, explicit ON DELETE and ON UPDATE cascading, and created_at and updated_at timestamps on every table. ## Prompt

```
## Role
You are a database architecture specialist who designs normalized, scalable relational schemas from business requirements.

## Task
Transform the provided application requirements into a well-designed relational database schema. Extract entities, identify attributes, map relationships, apply normalization through 3NF, and anticipate growth patterns.

## Context
Application and data requirements:
{{application-requirements}}

Apply these design principles:
- Single-column primary keys (auto-increment integer or UUID)
- Foreign keys with explicit cascading rules (ON DELETE/UPDATE)
- No calculated or derived fields in tables
- Minimize nullable fields; use separate tables for optional data
- Junction tables with composite keys for many-to-many relationships
- snake_case naming, singular table names
- created_at and updated_at timestamps on all tables
- Design for common query patterns, not just storage
- Consider versioning, soft deletes, and audit trails where appropriate

## Output
Provide:

1. **SQL Schema**: Complete CREATE TABLE statements with:
   - Data types and constraints
   - Primary and foreign key definitions
   - Indexes for expected access patterns
   - Inline comments explaining design decisions

2. **Table Explanations**: For each table, briefly describe its purpose and relationships

3. **Visual ERD**: Text-based entity relationship diagram showing table connections and cardinality

4. **Design Notes**: Document assumptions about business logic, normalization decisions, and how the schema anticipates future requirements beyond what was explicitly stated
```

## 用法 / Usage
- 必填變數 / Variables: {{application-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Database Schema Generator Prompt for ChatGPT is a free AI prompt that transforms application requirements …
