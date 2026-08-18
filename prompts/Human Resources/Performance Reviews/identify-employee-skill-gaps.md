# Employee Skill Gap Analysis Prompt

## 簡介

The Employee Skill Gap Analysis Prompt is a free AI prompt that systematically extracts skill deficiencies from performance reviews and maps them to targeted development activities for HR professionals and managers. This skill gap analysis prompt for ChatGPT works by parsing performance review text, categorizing findings across six competency areas (communication, technical skills, teamwork, leadership, problem-solving, and time management), then matching each identified gap to specific training interventions drawn from your organization's available resources. It runs on ChatGPT, Claude, Gemini, and Grok, producing a structured report that quotes evidence from the review, prioritizes gaps by impact on role effectiveness, and ensures recommendations align with both employee career goals and organizational objectives. Use it when conducting performance review cycles, planning individual development plans, or allocating training budgets based on documented need rather than assumption. ● Extracts skill gaps with supporting evidence quoted directly from performance review text ● Categorizes deficiencies across communication, technical, teamwork, leadership, problem-solving, and time management domains ● Matches each gap to specific interventions (workshops, mentoring, online courses, seminars) from your training catalog ● Prioritizes recommendations by severity, role impact, and alignment with development goals ## Prompt

```
## Role
You are a performance review analyst specializing in identifying skill gaps and recommending targeted development interventions.

## Task
Analyze the provided performance review to extract specific skill gaps, then recommend prioritized training and development activities that address each gap.

## Context
Performance Review:
{{performance-review}}

Employee Role and Responsibilities:
{{role-and-responsibilities}}

Available Training Resources:
{{training-resources}}

Development Goals:
{{development-goals}}

## Process
1. Read the performance review closely, noting all comments on competencies, achievements, and improvement areas
2. Categorize findings into themes: communication, technical skills, teamwork, leadership, problem-solving, and time management
3. For each category, identify specific instances indicating skill deficiencies or improvement opportunities
4. Extract concrete examples from the review that evidence each gap
5. Match each skill gap to appropriate interventions (workshops, online courses, mentoring, on-the-job training, external seminars) drawing from available training resources
6. Prioritize gaps by severity and impact on role effectiveness and organizational objectives
7. Ensure recommendations align with the employee's development goals and career trajectory

## Output
Deliver a structured report containing:

**Identified Skill Gaps**
- List each gap with supporting evidence quoted or paraphrased from the performance review
- Organize by category

**Recommended Development Activities**
- For each skill gap, specify training or development interventions
- Prioritize by urgency and impact
- Reference available training resources where applicable

**Summary**
- Key findings and top-priority recommendations
- Alignment with employee development goals and organizational needs

Make all recommendations clear, actionable, and specific to the employee's context.
```

## 用法 / Usage
- 必填變數 / Variables: {{development-goals}}、{{performance-review}}、{{role-and-responsibilities}}、{{training-resources}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Employee Skill Gap Analysis Prompt is a free AI prompt that systematically extracts skill deficiencies fro…
