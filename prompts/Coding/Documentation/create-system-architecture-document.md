# System Architecture Document Generator

## 簡介

The System Architecture Document Generator is a free AI prompt that produces comprehensive technical architecture documentation for developers, architects, and system administrators. This system architecture prompt for ChatGPT walks through eleven structured sections - executive summary, system overview, architectural goals, patterns and styles, component breakdowns, data models and flow, integration points, security architecture, scalability strategies, deployment infrastructure, and appendices. You provide a high-level system description, and the prompt returns a markdown-formatted document complete with placeholders for diagrams, detailed component interactions, and technical specifications. Teams use it to document microservices platforms, SaaS applications, internal tools, and infrastructure designs. It runs on ChatGPT, Claude, and Gemini. Reach for this prompt when you need to formalize architecture decisions, onboard new engineers, prepare for design reviews, or create stakeholder-facing technical documentation. ● Covers eleven core sections from executive summary through deployment and appendices ● Outputs markdown with headings, bullet lists, and diagram placeholders for immediate use ● Explains technical terms on first use and maintains consistency across sections ● Supports documenting microservices, monoliths, cloud platforms, and hybrid systems ## Prompt

```
## Role
You are an expert technical architect creating a comprehensive system architecture document for technical stakeholders including developers, architects, and system administrators.

## Task
Produce a complete system architecture document covering purpose, components, interactions, data model, integration points, security, scalability, and deployment.

## Context
System to document:
{{system-description}}

The document must be clear, well-structured, and accessible to technical audiences. Use diagrams and illustrations to enhance understanding. Explain technical terms when first introduced. Maintain consistency and coherence throughout.

## Output
Deliver a markdown-formatted document with these sections:

### 1. Executive Summary
Summarize the system's purpose, scope, and key architectural decisions.

### 2. System Overview
Provide a high-level description of the system, its main components, and their interactions.

### 3. Architectural Goals and Constraints
Discuss the goals, requirements, assumptions, and constraints shaping the architecture.

### 4. Architectural Patterns and Styles
Describe the architectural patterns, styles, and principles employed in the system design.

### 5. System Components
For each component, include:
- Name
- Detailed description of responsibilities and key features
- Interactions with other components and external systems
- Diagram illustrating internal structure and interactions

### 6. Data Model and Flow
- Describe the data model: key entities, relationships, and data stores
- Illustrate data flow through the system: sources, transformations, and destinations
- Include detailed diagrams showcasing data model and flow

### 7. Integration and Interfaces
- Describe internal component integration and communication
- Detail external interfaces, APIs, and integration points
- Include diagrams illustrating integration and interface architecture

### 8. Security Architecture
Discuss security measures, authentication, authorization, and data protection mechanisms.

### 9. Scalability and Performance
Describe how the architecture supports scalability, performance optimization, and capacity planning.

### 10. Deployment and Infrastructure
Provide an overview of deployment architecture, infrastructure requirements, and deployment processes.

### 11. Appendices
Include additional diagrams, technical specifications, or supporting documentation as needed.

Use headings, subheadings, bullet points, numbered lists, and tables to enhance readability throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{system-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The System Architecture Document Generator is a free AI prompt that produces comprehensive technical architect…
