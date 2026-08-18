# Project Tracking Table Generator for Task Management

## 簡介

The Project Tracking Table Generator for Task Management is a free AI prompt that creates organized task tables for project managers who need to break down work into actionable items with priorities, deadlines, and team assignments. This project tracking prompt for ChatGPT builds a markdown-formatted table containing five critical-path tasks tailored to your specific project. It runs on ChatGPT, Claude, Gemini, and Grok, automatically assigning priority levels (High, Medium, Low) based on importance and urgency, setting realistic deadlines in MM/DD/YYYY format, and matching tasks to team members based on skills and capacity. Use it when launching a new project, reorganizing an existing initiative, or clarifying deliverables for your team. ● Breaks projects into 5 measurable, actionable tasks that cover critical aspects ● Assigns objective priority ratings based on importance and urgency, not guesswork ● Sets realistic deadline dates and matches tasks to appropriate team members ● Outputs clean markdown tables ready to paste into Notion, GitHub, Confluence, or Slack ## Prompt

```
## Role
You are an expert project manager who plans, organizes, and oversees successful project execution by breaking work into manageable tasks, setting priorities and deadlines, and assigning responsibilities based on team skills and capacity.

## Task
Create a project tracking table with 5 tasks that comprehensively cover the key aspects of {{project-name}}. Include:

- **Task**: Brief, specific, measurable, and actionable description
- **Priority**: High, Medium, or Low (assigned objectively based on importance and urgency)
- **Deadline**: Realistic due date formatted as MM/DD/YYYY
- **Assigned To**: Team member best suited by skills, experience, and current workload

Focus on critical-path tasks. Avoid micromanagement—give team members autonomy.

## Output
Provide the table in markdown format:

| Task | Priority | Deadline | Assigned To |
|------|----------|----------|-------------|
| [task description] | [High/Medium/Low] | [MM/DD/YYYY] | [team member] |
| [task description] | [High/Medium/Low] | [MM/DD/YYYY] | [team member] |
| [task description] | [High/Medium/Low] | [MM/DD/YYYY] | [team member] |
| [task description] | [High/Medium/Low] | [MM/DD/YYYY] | [team member] |
| [task description] | [High/Medium/Low] | [MM/DD/YYYY] | [team member] |
```

## 用法 / Usage
- 必填變數 / Variables: {{project-name}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Project Tracking Table Generator for Task Management is a free AI prompt that creates organized task table…
