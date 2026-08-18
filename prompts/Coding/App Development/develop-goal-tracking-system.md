# Goal Tracking System Architecture Prompt

## 簡介

The Goal Tracking System Architecture Prompt is a free AI prompt that generates end-to-end system designs for goal achievement platforms, built for data scientists, software engineers, and product teams planning productivity applications. This goal tracking system prompt for ChatGPT, Claude, and Gemini produces a six-part technical blueprint: system requirements for goal creation and progress monitoring, a normalized relational database schema with users/goals/milestones/tasks tables, an analytics layer with completion rates and velocity metrics, integration specifications for Notion/Trello/Asana and calendar platforms, security architecture including OAuth 2.0 and GDPR compliance, and a phased implementation roadmap from MVP to advanced features. Real use cases include startups building habit-tracking apps, enterprise teams designing internal OKR platforms, and consultants scoping goal management systems for clients. Reach for this prompt when you need a production-ready system design document rather than just feature lists or wireframes. ● Outputs a normalized data model with entity relationships, attributes, and integrity constraints for goals, milestones, tasks, and progress entries ● Defines key performance metrics like completion rates, velocity trends, and milestone adherence with corresponding visualization types ● Specifies third-party integration requirements for major productivity tools and calendar systems with API synchronization details ● Includes a four-phase implementation roadmap with testing milestones and iteration cycles from MVP to production deployment ## Prompt

```
## Role
You are an expert data scientist and software engineer specializing in goal tracking systems, data analysis, and visualization.

## Task
Design a comprehensive system architecture and implementation plan for a goal achievement tracking platform. The system must enable users to input goals, monitor progress, and generate actionable insights through visualizations and reports.

## Context
Project scope: {{system-name}}
Target audience: {{target-users}}
Core objective: {{primary-goal}}

## Output
Deliver a complete system design covering:

**1. System Requirements**
- Core features: goal creation, progress tracking, milestone management, task breakdown
- User-facing capabilities and technical infrastructure needs
- Focus on usability, robustness, and insight generation

**2. Data Model**
- Database schema including tables for users, goals, milestones, tasks, and progress entries
- Entity relationships and key attributes for each table
- Normalization strategy and data integrity constraints

**3. Analysis and Visualization**
- Key performance metrics: completion rates, velocity trends, milestone adherence, time-to-goal
- Visualization types: progress charts, trend graphs, achievement heatmaps, comparative dashboards
- Actionable insights derived from user behavior patterns

**4. Integration and Compatibility**
- Third-party integrations: major productivity tools (Notion, Trello, Asana) and calendar systems (Google Calendar, Outlook)
- Multi-platform support: responsive web, native mobile (iOS/Android), desktop applications
- API specifications for data synchronization

**5. Security and Privacy**
- Authentication mechanisms (OAuth 2.0, MFA)
- Data encryption (at-rest and in-transit)
- Compliance requirements (GDPR, CCPA)
- Access control and data anonymization strategies

**6. Implementation Roadmap**
- Phase 1: Core MVP features (goal CRUD, basic tracking)
- Phase 2: Analytics engine and visualizations
- Phase 3: Integrations and cross-platform deployment
- Phase 4: Advanced features based on user feedback
- Include testing milestones and iteration cycles throughout
```

## 用法 / Usage
- 必填變數 / Variables: {{primary-goal}}、{{system-name}}、{{target-users}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Goal Tracking System Architecture Prompt is a free AI prompt that generates end-to-end system designs for …
