# Gantt Chart Builder for Project Planning

## 簡介

The Gantt Chart Builder for Project Planning is a free AI prompt that creates visual project timelines with task dependencies, deadlines, and critical path identification for project managers and team leads. This Gantt chart prompt for ChatGPT produces a markdown table showing task names, start dates, end dates, and dependencies organized chronologically. It analyzes your project scope to identify the critical path, flag scheduling conflicts, surface resource allocation issues, and highlight key milestones. The prompt works across ChatGPT, Claude, and Gemini, making it accessible regardless of your preferred text model. Use it when launching new initiatives, coordinating cross-functional teams, or presenting timelines to stakeholders who need a clear view of project phasing. ● Outputs a markdown table with task names, start/end dates, and dependencies in chronological order ● Identifies and explains the critical path to help prioritize high-impact activities ● Flags scheduling conflicts and resource constraints before they derail timelines ● Includes a reading guide so stakeholders can interpret the chart without training ## Prompt

```
## Role
You are an expert project manager creating a Gantt chart for project planning and prioritization.

## Task
Develop a comprehensive Gantt chart that visually represents task durations, dependencies, and deadlines in a clear table format. Organize all tasks chronologically, identify dependencies, highlight the critical path, and flag any scheduling conflicts or resource allocation issues.

## Context
{{project-scope}}

## Output
Deliver a markdown table with the following columns:
- Task Name
- Start Date
- End Date
- Dependencies

Below the table, include:
1. A brief explanation of how to read the Gantt chart
2. Critical path tasks highlighted and explained
3. Any identified scheduling conflicts or resource constraints

Ensure all key milestones and deadlines are clearly visible in the timeline.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-scope}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Gantt Chart Builder for Project Planning is a free AI prompt that creates visual project timelines with ta…
