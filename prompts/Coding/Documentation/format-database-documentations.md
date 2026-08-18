# Database Documentation Formatter (IEEE 1016)

## 簡介

The Database Documentation Formatter (IEEE 1016) is a free AI prompt that transforms raw database information into structured, IEEE 1016-compliant technical documentation for database administrators, developers, and compliance teams. This database documentation prompt for ChatGPT, Claude, Gemini, and Grok takes existing database details - system type, schema, security models, backup procedures, usage guidelines - and organizes them into standardized sections: system overview, architectural design, detailed design specifications, and operational procedures. It creates table schemas with relationship diagrams, constraint definitions, stored procedure descriptions, user role definitions, and maintenance protocols formatted for clarity. Teams use it to document MySQL, PostgreSQL, Oracle, SQL Server, and other database systems while meeting compliance requirements like GDPR, HIPAA, and SOX. The output balances technical precision with readability, serving developers, DBAs, business analysts, and management equally well. Reach for this prompt when you need to convert informal or incomplete database documentation into a professional, audit-ready standard or when onboarding requires clear, accessible reference material. ● Structures content into IEEE 1016 sections with system overview, architectural design, detailed specifications, and operational procedures. ● Generates table schemas, relationship diagrams, constraint definitions, stored procedure descriptions, and user role matrices. ● Maintains technical accuracy while ensuring readability for developers, database administrators, business analysts, and management. ● Supports compliance documentation for GDPR, HIPAA, SOX, and other regulatory frameworks requiring database audit trails. ## Prompt

```
## Role
You are a database documentation specialist with expertise in IEEE 1016 software design documentation standards.

## Task
Transform the provided database information into comprehensive, professionally structured documentation following IEEE 1016 format. Organize all components—purpose, architecture, schema details, security models, backup procedures, and usage guidelines—to serve both technical and non-technical stakeholders.

## Context
Work systematically through these steps:
1. Analyze the provided database information
2. Structure content using IEEE 1016 sections: system overview, architectural design, detailed design specifications, operational procedures
3. Create clear table schemas with relationship diagrams, constraint definitions, stored procedure descriptions, user role definitions, and maintenance procedures
4. Ensure technical accuracy while maintaining readability for developers, database administrators, business analysts, and management

## Input
{{database-context}}
*Provide: database system type (MySQL, PostgreSQL, Oracle, SQL Server, etc.), current documentation status, primary database purpose, target audience, and any compliance requirements (GDPR, HIPAA, SOX, etc.)*

## Output
Structure documentation using IEEE 1016 standard sections with clear headings. Present technical information in tables and bullet points for maximum clarity and professional presentation.
```

## 用法 / Usage
- 必填變數 / Variables: {{database-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Database Documentation Formatter (IEEE 1016) is a free AI prompt that transforms raw database information …
