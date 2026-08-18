# Design RBAC System

## 簡介

The Design RBAC System is a free AI prompt that generates a complete role-based access control architecture for applications requiring granular permission management and enterprise-grade security. It produces a full-stack implementation including role hierarchy design, database schema with indexes, permission-checking middleware, API route guards, frontend access controls, error handling, testing strategy, and audit logging tailored to your specific technology stack. This RBAC prompt for ChatGPT, Claude, and Cursor transforms a description of your application type, framework, database, and authentication setup into production-ready code that prevents unauthorized access and privilege escalation. Reach for it when you need to add or redesign access control in web, mobile, or SaaS applications, or when security audits reveal inadequate permission boundaries. ● Designs role hierarchies and permission structures that follow the principle of least privilege and prevent both external attacks and internal privilege escalation. ● Provides database schemas with relationships and indexes optimized for performance at scale, plus migration considerations for existing applications. ● Delivers middleware, route guards, and frontend components with code examples in the appropriate language for your stack, plus testing strategies to validate permission boundaries. ● Includes monitoring and audit logging implementations that track access attempts, role changes, and security events for compliance and incident response. ## Prompt

```
## Role

You are a security architect specializing in role-based access control (RBAC) systems. You design implementations that balance strong security boundaries with developer ergonomics and maintainability.

## Task

Design and implement a comprehensive RBAC system for the specified application. Deliver a complete architecture including role definitions, database schema, permission-checking middleware, UI access restrictions, and audit mechanisms.

## Context

The application currently has inadequate authentication with no granular permission controls, allowing unauthorized access to sensitive data and administrative functions. The solution must implement enterprise-grade security while maintaining user experience, scale with application growth, prevent both external attacks and internal privilege escalation, follow principle of least privilege, and be maintainable by the development team.

## Input

{{tech-stack}}
Describe your application type (web/mobile/SaaS), core technologies and frameworks, database system, current authentication setup, and user base size with growth expectations.

## Output

Provide implementation in these sections:

**Role Architecture**: Comprehensive role hierarchy and permission structure design

**Database Schema**: Tables, relationships, and indexes for storing roles, permissions, and user assignments with performance considerations

**Middleware Implementation**: Code examples for permission-checking middleware, hooks, and dynamic authorization logic

**API Route Protection**: Backend route guards and endpoint security patterns specific to the stack

**UI Access Control**: Frontend components and patterns for conditionally rendering elements based on permissions

**Error Handling**: User-friendly error messages and fallback UI for unauthorized access attempts

**Testing Strategy**: Unit and integration tests to validate permission boundaries and prevent privilege escalation

**Monitoring & Audit**: Logging implementation for tracking access attempts, role changes, and security events

**Deployment Checklist**: Security validation steps and migration considerations

For each section, include security rationale explaining why the approach prevents common vulnerabilities. Use clear technical explanations with code examples in the appropriate language for the stack.
```

## 用法 / Usage
- 必填變數 / Variables: {{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Design RBAC System is a free AI prompt that generates a complete role-based access control architecture fo…
