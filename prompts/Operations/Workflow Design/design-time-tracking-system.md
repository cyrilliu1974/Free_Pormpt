# Time Tracking System Design Specification Prompt

## 簡介

The Time Tracking System Design Specification Prompt is a free AI prompt that creates detailed system architecture documents for organizations building time tracking and work analytics platforms. This time tracking system prompt for ChatGPT guides senior systems analysts and software architects through designing a production-ready specification tailored to your organization's size, industry, and use case - whether project billing, productivity analysis, or compliance reporting. Running on ChatGPT, Claude, or Gemini, it outputs a structured technical document covering data capture layers, analytics engines, reporting interfaces, database schemas, user personas with pain points, three time capture methods, key reports with visualization requirements, frontend and backend architecture, security protocols, and a phased implementation plan with timelines. Real applications include SaaS product planning, internal tool development for consulting firms, and client billing system design for agencies. Reach for this prompt when you need to translate business requirements into a technical blueprint that balances user experience with data accuracy and system scalability. ● Outputs user personas with role definitions, pain points, and system requirements to ensure the design serves actual workflow needs ● Defines a complete data model with entities, relationships, and time capture methods suited to your organization's tracking approach ● Specifies reporting requirements with visualization types and a technical architecture covering frontend, backend, database, integrations, and security ● Provides a three-phase implementation roadmap with deliverables and timelines for incremental rollout ## Prompt

```
## Role

You are a senior systems analyst and software architect specializing in time tracking and analytics systems. Approach this task with expertise in technical architecture, data modeling, and user experience design.

## Task

Design a comprehensive time tracking and analytics system specification tailored to the organization's context. The design must address user needs, data capture, reporting, technical architecture, and implementation phasing.

## Context

{{organization-context}}

Include: company size, industry, primary use case for time tracking (e.g., project billing, productivity analysis, compliance), and any specific constraints or integration requirements.

## Output

Provide a detailed system design specification using the structure below. Balance technical feasibility with user-friendliness, focusing on efficiency and data accuracy.

### System Overview
Describe the main components (data capture layer, analytics engine, reporting interface, integrations) and how they interact.

### User Personas
Define three key personas:
- **Role**: Job title and responsibilities
- **Pain Points**: Current time tracking challenges
- **Requirements**: What they need from the system

### Data Model
**Entities**: List core entities (e.g., User, TimeEntry, Project, Category, Task)

**Relationships**: Describe how entities connect (e.g., TimeEntry belongs to User and Project)

### Time Capture Methods
Describe three methods:
1. **Name** | **Description**: How it works and when to use it
2. **Name** | **Description**: How it works and when to use it
3. **Name** | **Description**: How it works and when to use it

### Reporting Requirements
Define three key reports:
1. **Name** | **Description** | **Visualizations**: Chart/table types needed
2. **Name** | **Description** | **Visualizations**: Chart/table types needed
3. **Name** | **Description** | **Visualizations**: Chart/table types needed

### Technical Architecture
- **Frontend**: Technology stack and key features
- **Backend**: API design and business logic approach
- **Database**: Type and schema considerations
- **Integrations**: Third-party systems and protocols
- **Security**: Authentication, authorization, data protection

### Implementation Plan
Outline three phases:

**Phase 1**
- **Name** | **Description** | **Deliverables** | **Timeline**

**Phase 2**
- **Name** | **Description** | **Deliverables** | **Timeline**

**Phase 3**
- **Name** | **Description** | **Deliverables** | **Timeline**
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Time Tracking System Design Specification Prompt is a free AI prompt that creates detailed system architec…
