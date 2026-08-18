# Project Collaboration Plan Builder for Teams

## 簡介

The Project Collaboration Plan Builder for Teams is a free AI prompt that creates comprehensive project management frameworks for teams of any size working across different project types. This project collaboration prompt for ChatGPT takes your project description and preferred PM tool (Asana, Jira, Monday, or others) and outputs a seven-part plan: project overview with success criteria, team structure with defined roles, task breakdown with dependencies, progress tracking with milestones, communication strategy with meeting cadence, risk management with mitigation steps, and a timeline with key deliverables. It runs on ChatGPT, Claude, Gemini, and Grok, adapting the plan structure to fit your specific project context and tooling environment. Teams use it to kickstart sprints, align cross-functional groups, onboard new project members, or reset stalled initiatives with clear accountability. The prompt is designed for project managers, team leads, and Scrum masters who need a structured starting point rather than building collaboration frameworks from scratch. ● Outputs a numbered plan with seven key sections, from team structure to risk management ● Adapts recommendations to your specified project management tool and team composition ● Includes dependency mapping, accountability assignments, and escalation paths ● Provides milestone definitions, reporting cadence, and clear success criteria ## Prompt

```
## Role
You are an expert project manager specializing in team collaboration and delivery.

## Task
Create a comprehensive project collaboration plan that includes task assignment, progress tracking, and communication strategies. Structure the plan to be adaptable across different project types and team sizes while maximizing efficiency and productivity.

## Context
Project: {{project-description}}

Preferred project management tool: {{pm-tool}}

## Output
Deliver the plan as a numbered list with clear headings covering:

1. **Project Overview** - goal, scope, and success criteria
2. **Team Structure** - roles, responsibilities, and accountability
3. **Task Breakdown** - work packages, dependencies, and assignments
4. **Progress Tracking** - milestones, metrics, and reporting cadence
5. **Communication Strategy** - channels, meeting rhythm, and escalation paths
6. **Risk Management** - potential blockers and mitigation approaches
7. **Timeline & Milestones** - key dates and deliverables

Tailor all recommendations to the specified project management tool and team composition described in the project context.
```

## 用法 / Usage
- 必填變數 / Variables: {{pm-tool}}、{{project-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Project Collaboration Plan Builder for Teams is a free AI prompt that creates comprehensive project manage…
