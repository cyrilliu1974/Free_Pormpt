# Database Naming Convention Standardization Prompt

## 簡介

The Database Naming Convention Standardization Prompt is a free AI prompt that analyzes existing database schemas and produces a complete naming standardization plan aligned with ISO 11179 guidelines for database architects and platform engineers. This database naming convention standardization prompt for ChatGPT and Claude takes your schema export, platform details, and deployment context to identify inconsistencies across tables, columns, indexes, and constraints, then generates phased rename scripts with full rollback mechanisms and dependency tracking. Use it when inheriting legacy systems, merging databases after acquisition, or reducing technical debt that slows developer onboarding and increases maintenance overhead. This prompt is for database architects, schema engineers, and platform teams who need to enforce consistent naming standards across enterprise databases without breaking existing application integrations. ● Performs deep analysis of current schemas to surface mixed-case styles, plural/singular conflicts, abbreviation abuse, and semantic ambiguity across all object types. ● Establishes ISO 11179-compliant naming rules tailored to your platform, covering case conventions, pluralization, abbreviation guidelines, and semantic clarity requirements. ● Generates SQL rename scripts grouped by dependency chains, complete with backup procedures, rollback commands, and validation queries to confirm compliance. ● Delivers a phased implementation roadmap that prioritizes low-risk objects first and maps application compatibility risks to minimize downtime. ## Prompt

```
## Role

You are an expert database architect and ISO 11179 standards specialist with enterprise-scale schema standardization experience.

## Task

Analyze the provided database schema and create a comprehensive naming standardization plan that follows ISO 11179 guidelines while ensuring zero disruption to existing applications.

## Context

Inconsistent naming conventions create technical debt, reduce developer productivity, and increase maintenance costs. Common issues include mixed case styles, plural/singular variations, abbreviation misuse, and missing semantic clarity.

Work through this systematically:

1. **Analyze** the current schema to identify naming inconsistencies and anti-patterns
2. **Establish** clear ISO 11179 compliant naming rules (case conventions, pluralization standards, abbreviation guidelines, semantic clarity requirements)
3. **Prioritize** the implementation plan by grouping related objects to minimize application impact
4. **Generate** comprehensive rename scripts with proper dependency handling, backup procedures, and rollback mechanisms
5. **Provide** validation queries to verify naming compliance and establish ongoing governance procedures

## Input

**Database platform:** {{database-platform}}

**Schema and objects:** {{schema-export}}

**Application dependencies and deployment constraints:** {{deployment-context}}

## Output

Structure your response with these sections:

### Current State Analysis
- Naming inconsistencies identified
- Anti-patterns and their impact
- Dependency map

### Proposed Naming Standards
- Unified naming convention framework with specific rules for tables, columns, indexes, constraints, and other database objects
- ISO 11179 compliance details

### Implementation Roadmap
- Phased rollout plan prioritized by risk and impact
- Application compatibility strategy

### SQL Scripts
- Rename scripts with rollback procedures
- Validation queries
- Backup and recovery procedures

Use proper markdown headings and code blocks for clarity and implementation readiness.
```

## 用法 / Usage
- 必填變數 / Variables: {{database-platform}}、{{deployment-context}}、{{schema-export}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Database Naming Convention Standardization Prompt is a free AI prompt that analyzes existing database sche…
