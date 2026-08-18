# SQL Migration Generator for Laravel Schema Changes

## 簡介

The SQL Migration Generator for Laravel Schema Changes is a free AI prompt that creates production-ready migration files for database schema evolution in Laravel applications. This Laravel migration prompt for ChatGPT, Claude, and Cursor analyzes your current database structure and requested changes, then generates timestamped PHP migration files with complete up() and down() methods, proper foreign key sequencing, and inline risk warnings. Each migration includes rollback logic, constraint management to maintain referential integrity, and deployment notes that specify dependencies and expected duration. The prompt follows Laravel conventions by isolating one logical change per file, applying foreign keys only after referenced tables exist, and separating complex data transformations from schema changes. Reach for this prompt when you need to evolve database schemas safely in production environments, ensure every change can be reversed cleanly, or coordinate multi-step migrations across development teams. ● Analyzes schema dependencies and flags risks such as NOT NULL columns on existing tables or circular foreign key references ● Generates chronologically ordered migration files with Laravel Schema builder syntax and descriptive timestamps ● Includes complete rollback procedures in every down() method to enable safe reversions in production ● Provides deployment notes specifying which migrations require manual backups, multi-step execution, or maintenance windows ## Prompt

```
## Role
You are a database migration architect specializing in Laravel schema evolution, designing production-grade migrations that maintain data integrity and enable safe rollbacks.

## Task
Create timestamped Laravel migration files for the requested schema changes. Each migration must include:

- Atomic up() and down() methods
- Proper constraint management and referential integrity
- Inline comments explaining critical steps
- Rollback strategies for each transformation
- Sequencing that minimizes downtime

## Context
Analyze the provided database structure and required changes to identify dependencies and risks. Design migrations following Laravel conventions:

- One logical change per migration file
- Foreign keys applied after referenced tables exist
- Indexes named consistently
- Data transformations separated from schema changes when complex
- Safe defaults for new NOT NULL columns on existing tables

{{schema-and-changes}}

## Output
Provide migration files in chronological order with:

1. **Filename**: `YYYY_MM_DD_HHMMSS_descriptive_name.php`
2. **up() method**: Schema changes with inline risk warnings
3. **down() method**: Complete reversal logic
4. **Deployment notes**: Sequence dependencies, expected duration, rollback procedure

Use Laravel's Schema builder syntax. Flag any changes requiring manual data backups or multi-step deployments.
```

## 用法 / Usage
- 必填變數 / Variables: {{schema-and-changes}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Adaptive_Checkpoint_System
- 適用 / Use when: The SQL Migration Generator for Laravel Schema Changes is a free AI prompt that creates production-ready migra…
