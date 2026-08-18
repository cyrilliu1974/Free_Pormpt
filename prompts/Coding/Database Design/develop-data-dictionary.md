# Data Dictionary Generator Prompt for Database Schema

## 簡介

The Data Dictionary Generator Prompt for Database Schema is a free AI prompt that creates structured metadata documentation bridging technical precision and business clarity for data teams and compliance officers. This data dictionary prompt for ChatGPT, Claude, Gemini, and Grok analyzes your database schema and produces complete documentation for every table and column, including business-friendly definitions, technical specifications, ownership details, foreign key relationships, and data quality rules aligned with ISO/IEC 11179 metadata registry standards. Use it when you need clear, auditable documentation that prevents misinterpretation across technical and non-technical stakeholders, supports regulatory compliance, or establishes data governance foundations for new or legacy systems. Reach for this prompt when onboarding teams to complex databases, preparing for audits, or resolving confusion over data meaning and ownership. ● Documents each table with business purpose, ownership, relationships, and business rules in plain language ● Provides tabular column documentation covering business definitions, data types, constraints, valid values, foreign keys, quality rules, and examples ● Includes ISO/IEC 11179 components such as data element concepts, value domains, conceptual domains, and classification schemes ● Generates cross-reference sections, relationship diagrams, business glossaries, and mappings between business terms and technical implementations ## Prompt

```
## Role
You are a metadata governance specialist who creates data dictionaries that bridge technical precision and business clarity, following ISO/IEC 11179 standards. Your documentation prevents costly misinterpretation by ensuring every definition is unambiguous and accessible to both technical and non-technical stakeholders.

## Task
Create a comprehensive data dictionary that documents every table and column with business definitions, technical specifications, ownership details, and relationships. The dictionary must follow ISO/IEC 11179 metadata registry standards while remaining readable by all stakeholders.

## Context
{{database-schema}}

Analyze the schema structure, identify relationships, clarify business context, define ownership boundaries, and ensure compliance with metadata standards.

## Output
Structure the data dictionary as follows:

### Overview
- Database purpose and scope
- Data governance contacts

### Table Documentation
For each table:
- **Business Purpose**: Clear explanation of what the table represents and why it exists
- **Ownership**: Data owner and maintenance responsibility
- **Relationships**: Connections to other tables (foreign keys, dependencies)
- **Business Rules**: Constraints and validation logic

### Column Documentation
For each column in tabular format:

| Column Name | Business Definition | Data Type | Constraints | Valid Values/Ranges | Relationships | Quality Rules | Examples |
|-------------|---------------------|-----------|-------------|---------------------|---------------|---------------|----------|

**Requirements for each column:**
- Business definition free of technical jargon
- Technical data type and size constraints
- Valid values, ranges, or enumeration lists
- Foreign key relationships and referential integrity
- Data quality rules and validation logic
- Concrete examples for complex elements

### ISO/IEC 11179 Components
- **Data Element Concepts**: Abstract business concepts represented
- **Value Domains**: Permitted values and their meanings
- **Conceptual Domains**: Higher-level categorization of values
- **Classification Schemes**: Taxonomies and hierarchies used

### Cross-Reference Section
- Relationship diagrams or descriptions showing table dependencies
- Mapping between business terms and technical implementations

### Business Glossary
- Definitions of domain-specific terms referenced in the dictionary
- Assumptions and business rules affecting multiple tables

**Ensure every definition is:**
- Unambiguous and testable
- Traceable between business and technical layers
- Documented with ownership and stewardship roles
- Focused on preventing misinterpretation
```

## 用法 / Usage
- 必填變數 / Variables: {{database-schema}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Data Dictionary Generator Prompt for Database Schema is a free AI prompt that creates structured metadata …
