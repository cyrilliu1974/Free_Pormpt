# Project Management System Design Prompt

## 簡介

The Project Management System Design Prompt is a free AI prompt that creates a comprehensive task dependency tracking system specification tailored to any project type, from software development to construction or event planning. This project management system prompt for ChatGPT generates an implementation-ready specification covering eleven critical areas: stakeholder requirements, project constraints, dependency types (finish-to-start, start-to-start, finish-to-finish, resource dependencies), functional requirements, ASCII UI mockups, data model schemas, REST API endpoints, integration points, performance benchmarks, and security protocols. It runs on ChatGPT, Claude, Gemini, and Grok, adapting every section to the unique characteristics of your project type rather than delivering generic templates. Use it when you need to design a dependency tracker that reflects real-world constraints like regulatory compliance, team distribution, or timeline pressures specific to your industry. ● Identifies stakeholders by role and maps their specific tracking system requirements ● Defines dependency relationship types relevant to the project category and provides visualization strategies ● Delivers data model schemas with entities, attributes, and relationships in clear notation ● Specifies REST API endpoints with HTTP methods, request/response formats, and parameters for task operations ● Addresses performance requirements, integration points, and security protocols appropriate to project scale ## Prompt

```
## Role
You are a project management expert specializing in task dependency tracking systems across industries.

## Task
Design a comprehensive task dependency tracking system specification tailored to the project type provided. The specification must be actionable, specific to the project's unique needs, and ready to guide implementation.

## Context
Project type: {{project-type}}

The system should address the unique stakeholders, constraints, dependency patterns, and objectives inherent to this project type. Cover both functional requirements (what the system does) and non-functional requirements (performance, security, integration).

## Output
Deliver a complete specification with these sections:

**1. Project Type**
Brief description of the project category and its characteristics.

**2. Key Stakeholders**
List primary stakeholders (roles, not names) and their specific requirements for the tracking system.

**3. Project Constraints**
Identify constraints typical of this project type: timeline pressures, resource limits, regulatory requirements, technical debt, team distribution, etc.

**4. Dependency Types**
Define the dependency relationships relevant to this project (finish-to-start, start-to-start, finish-to-finish, start-to-finish, resource dependencies, external dependencies).

**5. Tracking System Requirements**
Numbered list of functional requirements: task creation, dependency mapping, visualization, notification rules, conflict detection, reporting capabilities.

**6. UI Mockup**
ASCII diagram showing the main interface layout for dependency visualization and management.

**7. Data Model Specification**
Define entities (Task, Dependency, Project, Resource), their attributes, and relationships. Use clear schema notation.

**8. API Specification**
List REST endpoints with HTTP methods, request/response formats, and key parameters for task and dependency operations.

**9. Integration Points**
Identify systems this tracker must integrate with (calendar tools, communication platforms, resource management, reporting tools) and integration methods.

**10. Performance Requirements**
Specify response times, concurrent user capacity, data volume limits, and scalability needs appropriate to the project scale.

**11. Security Considerations**
Address authentication, authorization (role-based access), data encryption, audit logging, and compliance requirements relevant to the project type.

Be specific and avoid generic advice. Tailor every section to the unique characteristics of the project type provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-type}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Project Management System Design Prompt is a free AI prompt that creates a comprehensive task dependency t…
