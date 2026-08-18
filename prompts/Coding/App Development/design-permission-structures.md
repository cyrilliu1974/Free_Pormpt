# Role-Based Access Control System Design Prompt

## 簡介

The Role-Based Access Control System Design Prompt is a free AI prompt that creates secure, scalable permission structures for applications managing complex team access patterns. This RBAC design prompt for ChatGPT walks through user type identification, role definition, permission mapping, inheritance patterns, and edge-case handling to prevent permission sprawl as organizations grow. It produces a role hierarchy map, permission matrix, implementation guidelines, edge-case handlers for temporary access and contractor expiration, and security validation checkpoints aligned with least-privilege principles. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering structured output that security architects and development teams can implement directly. Reach for this prompt when your application is scaling beyond flat permission models, adding contractors or partners, or facing audit compliance requirements that demand clear role boundaries and permission traceability. ● Maps user responsibilities to granular permissions (view, create, edit, delete, archive) across all resource types. ● Establishes parent-child role inheritance flows that minimize redundancy and maintain audit trails. ● Addresses temporary elevated access, cross-functional collaboration, contractor expiration, and delegation patterns. ● Validates designs against least-privilege, role clarity, inheritance logic, scalability, and default-restrictive security principles. ## Prompt

```
## Role

You are a security architecture specialist designing scalable Role-Based Access Control (RBAC) systems that prevent permission sprawl through maintainable hierarchies.

## Task

Design a comprehensive RBAC permission structure for the application described below. Assign permissions to roles rather than individuals, ensuring the system scales efficiently as teams expand with employees, contractors, and partners while maintaining security and audit compliance.

Analyze the application context step by step: identify user types and their responsibilities, map required actions to resources, define clear role boundaries, establish inheritance patterns, and address edge cases for temporary or cross-functional access.

## Context

{{application-context}}

The application faces exponential growth where flat permission models create security vulnerabilities and audit risks. Modern collaborative environments require fluid access patterns that adapt to contractors, partners, and temporary staff without creating permission chaos or role explosion.

## Output

Deliver the permission structure organized into these sections:

### Role Hierarchy Map
Visual tree structure showing parent-child role relationships and inheritance flows.

### Permission Matrix
Table mapping roles against granular permissions (view, create, edit, delete, archive) for each resource type.

### Implementation Guidelines
Numbered deployment steps including patterns for maintaining flexibility while ensuring security.

### Edge Case Handlers
Address special scenarios:
- Temporary elevated access (time-boxed privilege escalation)
- Cross-functional collaboration (project-based permissions)
- Contractor access expiration
- Delegation patterns (vacation coverage, approval chains)

### Security Checkpoints
Validate against:
- **Principle of Least Privilege**: Users receive minimum necessary permissions
- **Role Clarity**: Non-overlapping purposes mapped to real responsibilities
- **Inheritance Logic**: Clear parent-child permission flows with explicit override rules
- **Scalability**: New user types fit existing roles 80% of the time
- **Audit Trail**: Every permission traces to business justification
- **Default Restrictive**: Explicit grants required; no implicit access

Include practical examples for each role definition showing real-world permission scenarios.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Role-Based Access Control System Design Prompt is a free AI prompt that creates secure, scalable permissio…
