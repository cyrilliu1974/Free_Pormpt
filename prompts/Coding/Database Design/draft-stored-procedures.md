# Stored Procedure Generator for T-SQL

## 簡介

The Stored Procedure Generator for T-SQL is a free AI prompt that drafts production-ready stored procedures for database architects and developers working in enterprise environments. This stored procedure prompt for ChatGPT takes your database schema and business requirements, then generates complete T-SQL code with parameter validation, transaction management, comprehensive error handling, and high-performance set-based operations. It runs on ChatGPT, Claude, Gemini, and Grok, producing properly formatted SQL code blocks with inline documentation, security annotations, and performance considerations. Use it when you need to implement complex business logic in SQL Server databases while maintaining security, performance, and maintainability standards. ● Produces set-based operations that avoid cursor overhead and improve query performance ● Includes parameter validation logic to prevent SQL injection and invalid input ● Structures code with try-catch blocks, transaction rollback handling, and meaningful error messages ● Adds inline comments explaining logic, edge cases, indexing considerations, and query plan implications ## Prompt

```
## Role

You are an expert T-SQL database architect specializing in stored procedure design, drawing on set-based query techniques and enterprise optimization patterns.

## Task

Draft production-ready T-SQL stored procedures that implement the specified business logic with modular design, comprehensive error handling, proper transaction management, and high-performance set-based operations.

## Context

You are building for enterprise environments where performance, security, and maintainability are critical. Each procedure must:

- **Validate parameters** to prevent SQL injection and invalid input
- **Use set-based operations** instead of cursors or iterative logic
- **Manage transactions** with appropriate isolation levels and rollback handling
- **Handle errors** with try-catch blocks, meaningful error messages, and logging where appropriate
- **Include inline comments** explaining logic, edge cases, and performance considerations
- **Follow consistent naming conventions** and document all input/output parameters
- **Consider indexing strategies** and query plan implications

Analyze the provided schema for optimal data access patterns, identify potential bottlenecks, and structure code for reusability and long-term maintenance.

## Input

**Database schema:**  
{{database-schema}}

**Business requirements:**  
{{business-requirements}}

## Output

Provide the complete stored procedure code in properly formatted SQL code blocks with:

- Clear section headers (parameter declarations, validation, main logic, error handling)
- Comprehensive inline documentation
- Performance and security annotations where relevant
```

## 用法 / Usage
- 必填變數 / Variables: {{business-requirements}}、{{database-schema}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Stored Procedure Generator for T-SQL is a free AI prompt that drafts production-ready stored procedures fo…
