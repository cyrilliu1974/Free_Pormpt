# Virtual Project Documentation Template Generator

## 簡介

The Virtual Project Documentation Template Generator is a free AI prompt that creates structured, comprehensive project templates for teams managing virtual or remote work initiatives. This project documentation prompt for ChatGPT takes your project overview and team details and outputs a complete template with seven core sections: project overview, team structure with communication plans, scope definition with in/out boundaries, budget breakdowns, risk management with mitigation strategies, ongoing update logs, and formal closure documentation. It runs on ChatGPT, Claude, and Gemini, making it ideal for project managers, technical writers, and team leads who need consistent, professional documentation that scales across project types and team sizes. The template is designed to support collaboration from kickoff through final sign-off, with clear sections for meeting minutes, change requests, and status reports. ● Outputs seven structured sections including scope, budget, risk, team roles, and closure protocols ● Includes built-in communication plans, escalation paths, and reporting structures for remote teams ● Adapts to any project type or size by customizing the project-overview and team-details variables ● Facilitates sign-off workflows with acceptance criteria, deliverable verification, and lessons learned documentation ## Prompt

```
## Role
You are an expert technical writer and project manager creating comprehensive virtual project documentation templates.

## Task
Generate a detailed, well-structured project documentation template that covers all essential project management aspects and facilitates team collaboration. The template must be adaptable to various project types and sizes.

## Context
Project details:
{{project-overview}}

Team structure:
{{team-details}}

## Output
Deliver the documentation as a complete template with the following sections:

### Project Overview
- Project Name: [from project-overview]
- Project Description: [from project-overview]
- Project Objectives: [from project-overview]
- Project Stakeholders: [from project-overview]
- Project Timeline:
  - Start Date: [from project-overview]
  - End Date: [from project-overview]
  - Milestones: [from project-overview]

### Project Team
- Team Members: [from team-details, including name, role, responsibilities, and contact info for each member]
- Communication Plan: [specify meeting cadence, communication channels, escalation paths, and reporting structure]

### Project Scope
- In Scope: [define boundaries and included work]
- Out of Scope: [explicitly list excluded items]
- Deliverables: [list all project outputs]
- Acceptance Criteria: [define success metrics and sign-off requirements]

### Project Budget
- Budget Overview: [total budget and funding sources]
- Cost Breakdown: [itemized costs by category]
- Budget Approval: [approval authority and process]

### Risk Management
- Potential Risks: [identify and categorize risks by likelihood and impact]
- Mitigation Strategies: [preventive actions for each risk]
- Contingency Plans: [response procedures if risks materialize]

### Project Updates
- Status Reports: [weekly/monthly progress summaries]
- Meeting Minutes: [decisions, action items, and attendees]
- Change Requests: [scope change log with approvals]

### Project Closure
- Final Deliverables: [completed outputs with verification]
- Lessons Learned: [successes, challenges, and recommendations]
- Project Sign-Off: [formal acceptance and closure documentation]

Ensure all sections are clearly organized, easy to navigate, and support ongoing collaboration throughout the project lifecycle.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-overview}}、{{team-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Virtual Project Documentation Template Generator is a free AI prompt that creates structured, comprehensiv…
