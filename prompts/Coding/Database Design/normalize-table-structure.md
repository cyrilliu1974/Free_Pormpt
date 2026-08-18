# Database Table Normalization Prompt for ChatGPT

## 簡介

The Database Table Normalization Prompt for ChatGPT is a free AI prompt that analyzes relational database schemas and systematically guides you through normalization to third normal form using Codd's proven framework. This table normalization prompt for ChatGPT examines your existing table structures, identifies first, second, and third normal form violations, explains the real-world consequences of each issue (update anomalies, insertion problems, data redundancy), and generates decomposed table designs with foreign key relationships that preserve data integrity. It produces before-and-after schemas with sample data, SQL migration scripts, validation queries, and implementation guidance tailored to your business context. Works with ChatGPT, Claude, and Gemini for database design and refactoring projects. Designed for database administrators, backend developers, and data engineers who need to eliminate redundancy, resolve functional dependency issues, or restructure legacy schemas while maintaining all original data relationships. ● Maps functional dependencies and identifies partial dependencies, transitive dependencies, repeating groups, and non-atomic values across your schema ● Decomposes tables into normalized structures with foreign key constraints that eliminate insertion, update, and deletion anomalies ● Generates side-by-side comparisons showing original versus normalized schemas populated with the same sample data ● Provides SQL DDL scripts, data migration logic, referential integrity constraints, indexing recommendations, and query impact notes for implementation ## Prompt

```
## Role
Database normalization specialist applying relational theory and normal forms (1NF through 3NF) to eliminate redundancy, update anomalies, and insertion/deletion problems.

## Task
Analyze the provided database table structure and guide step-by-step normalization to third normal form (3NF). Identify violations, explain their real-world consequences, decompose tables to resolve issues, and provide clear before-and-after examples with migration guidance.

## Context
{{table-structure}}

Business context: {{business-context}}

## Analysis Framework

**Step 1: First Normal Form (1NF)**
- Identify repeating groups and multi-valued attributes
- Locate non-atomic values that should be decomposed
- Show how these violations create insertion and update anomalies

**Step 2: Second Normal Form (2NF)**
- Examine composite keys for partial dependencies
- Find non-key attributes that depend on only part of the primary key
- Demonstrate the risks of maintaining these dependencies

**Step 3: Third Normal Form (3NF)**
- Detect transitive dependencies between non-key attributes
- Identify cases where non-key columns depend on other non-key columns
- Explain cascading update problems these create

## Output

**Current Structure Assessment**
- Table schemas with primary keys marked
- Normal form violations identified at each level
- Functional dependencies mapped

**Normalization Process**

For each violation found:
- **Violation**: Specific rule being broken with example
- **Impact**: Concrete anomalies this causes (update/insert/delete)
- **Resolution**: Decomposed table structure that eliminates the problem
- **Integrity**: Foreign key relationships that preserve data connections

**Before & After Comparison**

Show side-by-side:
- Original table(s) with sample data demonstrating the problem
- Normalized table(s) with the same data properly distributed
- Relationship diagram showing how foreign keys connect tables

**Implementation Path**

1. SQL scripts or pseudocode for creating normalized tables
2. Data migration approach to populate new structures
3. Validation queries to confirm lossless decomposition
4. Performance considerations and indexing recommendations
5. Application impact notes for queries that will change

**Practical Considerations**
- Stop at 3NF unless higher normal forms are explicitly needed
- Flag cases where denormalization may be justified for performance
- Ensure all original data relationships remain queryable
- Maintain referential integrity through proper constraints
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{table-structure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Database Table Normalization Prompt for ChatGPT is a free AI prompt that analyzes relational database sche…
