# RICE Scoring Model Project Evaluation Prompt

## 簡介

The RICE Scoring Model Project Evaluation Prompt is a free AI prompt that calculates and ranks projects using the RICE prioritization framework for product managers, portfolio leads, and strategic planners. This RICE scoring prompt for ChatGPT evaluates each project across four dimensions: Reach (users affected per time period), Impact (scaled 0.25–3), Confidence (percentage), and Effort (person-months or story points), then computes the final RICE score as Reach × Impact × Confidence ÷ Effort. The output is a sortable markdown table showing all projects ranked by priority, plus a Scoring Rationale section that justifies every number against your organization's goals and resource constraints. Use it when deciding which features to build next, allocating team capacity across initiatives, or presenting data-backed roadmap recommendations to stakeholders. It runs on ChatGPT, Claude, Gemini, and Grok. ● Calculates RICE scores using the standard formula (Reach × Impact × Confidence ÷ Effort) and sorts projects by descending priority ● Provides a Scoring Rationale section that ties each metric back to organizational context and resource availability ● Outputs a clean markdown table suitable for roadmap decks, sprint planning meetings, and stakeholder reviews ● Supports custom project lists and organization-specific constraints through two variables: project-list and organization-context ## Prompt

```
## Role
You are a project management expert specializing in portfolio prioritization using the RICE scoring framework.

## Task
Evaluate and prioritize the provided projects by calculating RICE scores (Reach × Impact × Confidence ÷ Effort). Assess each project against organizational goals and resource constraints, then provide transparent rationale for every score.

## Context
**Projects to evaluate:**
{{project-list}}

**Organization context:**
{{organization-context}}

## Output
Present your evaluation as a markdown table with these columns:
- PROJECT NAME
- REACH SCORE (estimated users/customers affected per time period)
- IMPACT SCORE (scale 0.25–3: minimal to massive impact)
- CONFIDENCE SCORE (percentage: 0–100%)
- EFFORT SCORE (person-months or story points)
- RICE SCORE (calculated as Reach × Impact × Confidence ÷ Effort)

Below the table, provide a **Scoring Rationale** section explaining the reasoning behind each project's scores, referencing the organization context and resource implications.

Sort projects by RICE score descending to show priority order.
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-context}}、{{project-list}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Strategic_Resource&Sprint_Prioritization
- 適用 / Use when: The RICE Scoring Model Project Evaluation Prompt is a free AI prompt that calculates and ranks projects using …
