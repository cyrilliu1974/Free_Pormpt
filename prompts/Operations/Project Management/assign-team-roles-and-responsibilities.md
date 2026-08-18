# Assign Team Roles and Responsibilities Prompt

## 簡介

The Assign Team Roles and Responsibilities Prompt is a free AI prompt that creates balanced team structures by matching members' capabilities with project needs for project managers and team leads. This team role assignment prompt for ChatGPT analyzes your project goals, timeline, and team composition to produce a detailed markdown table mapping each member to specific roles, responsibilities, and delivery windows. It runs on ChatGPT, Claude, and Gemini, taking three inputs - project name, team members with their skills and experience, and project goals with timeline - and returns not just assignments but also workload balance rationale, collaboration strategies, and risk mitigation plans. Use it when launching a new initiative, restructuring a team, or onboarding members to ensure skills are utilized effectively and no one is over- or under-allocated. ● Produces a role-responsibility matrix in markdown table format with timeline columns ● Includes balance rationale explaining how assignments leverage individual strengths ● Suggests 2-3 collaboration strategies tailored to the team structure ● Identifies potential challenges and mitigation strategies for the staffing plan ## Prompt

```
## Role
You are an expert project manager creating a team management structure that assigns roles and responsibilities based on members' skills, experience, and interests.

## Task
Analyze the project requirements and team composition, then match each member with appropriate roles and responsibilities. Create a balanced assignment structure that leverages individual strengths and aligns with project goals.

## Context
**Project:** {{project-name}}

**Team composition:** {{team-members}}
(For each member, include their name, key skills, experience level, and relevant interests or preferences)

**Project goals and timeline:** {{project-goals-timeline}}
(Describe what the project aims to achieve and the overall timeframe or key milestones)

## Output
Provide a structured markdown table with these columns: Role | Responsibilities | Team Member | Timeline

Below the table, include:
- **Balance rationale:** Brief explanation of how assignments leverage strengths and distribute workload
- **Collaboration strategies:** 2-3 specific approaches for effective team communication and coordination
- **Potential challenges:** Key risks and mitigation strategies for the team structure
```

## 用法 / Usage
- 必填變數 / Variables: {{project-goals-timeline}}、{{project-name}}、{{team-members}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Assign Team Roles and Responsibilities Prompt is a free AI prompt that creates balanced team structures by…
