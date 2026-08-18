# ABC Analysis Task Prioritization Prompt

## 簡介

The ABC Analysis Task Prioritization Prompt is a free AI prompt that categorizes project tasks into high, medium, and low priority tiers for project managers and team leads. This task management prompt for ChatGPT guides the model to perform ABC analysis by evaluating each task against impact on project goals, deadline proximity, resource availability, and dependencies. It runs on ChatGPT, Claude, Gemini, and Grok, producing a clean markdown table that sorts tasks into A (high), B (medium), and C (low) priority categories with explanations for each placement. Real use cases include sprint planning, resource allocation decisions, backlog grooming, and helping teams identify bottlenecks before they derail timelines. Project managers, product owners, and team leads reach for this prompt when facing a long task list and needing objective criteria to decide what to tackle first. ● Categorizes tasks into A, B, and C tiers by analyzing impact, urgency, dependencies, and available resources ● Produces a markdown table with task names and explanations for why each belongs in its assigned priority tier ● Includes a summary of prioritization rationale and recommended sequencing for high-priority A-tier tasks ● Accepts custom task lists, project goals, and resource constraints to tailor the analysis to your specific project context ## Prompt

```
## Role
You are an expert project manager conducting an ABC analysis for task prioritization.

## Task
Categorize the provided tasks into three priority tiers (A, B, C) based on their importance and urgency. Analyze each task considering:
- Impact on project goals
- Deadline proximity and constraints
- Resources required versus resources available
- Dependencies and bottlenecks

Create a prioritization system that optimizes workflow and resource allocation.

## Context
**Tasks:**
{{task-list}}

**Project goals:**
{{project-goals}}

**Available resources and deadlines:**
{{resources-and-deadlines}}

## Output
Present your analysis as a markdown table with three columns:

| A (High Priority) | B (Medium Priority) | C (Low Priority) |
|-------------------|---------------------|------------------|

For each task, include:
- Task name
- Brief explanation of its categorization (why it belongs in that tier)

After the table, provide a summary of the prioritization rationale and any recommended sequencing for the A-tier tasks.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-goals}}、{{resources-and-deadlines}}、{{task-list}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The ABC Analysis Task Prioritization Prompt is a free AI prompt that categorizes project tasks into high, medi…
