# Task Batching Strategy Builder for Workflow Optimization

## 簡介

The Task Batching Strategy Builder for Workflow Optimization is a free AI prompt that creates systematic task grouping strategies to enhance productivity and streamline any workflow. This task batching prompt for ChatGPT analyzes your workflow context and produces a two-part deliverable: a strategic overview explaining how tasks should be grouped based on interdependencies and resource constraints, plus a detailed markdown table categorizing at least five tasks by complexity and time requirements. It runs on ChatGPT, Claude, and Gemini, making it practical for project managers, operations teams, and anyone managing complex workflows who need to identify bottlenecks and optimize resource allocation. The prompt examines task interdependencies, assesses complexity levels, and provides time estimates tailored to your specific workflow context. ● Systematically categorizes tasks into logical batches based on interdependencies and resource needs ● Assesses task complexity levels to support better planning and resource allocation decisions ● Estimates time requirements for each task category to prevent bottlenecks and scheduling conflicts ● Delivers both strategic rationale and a structured table format for immediate implementation ## Prompt

```
## Role
You are a task management expert specializing in task batching strategies that enhance productivity and streamline workflow.

## Task
Create a systematic task batching strategy for the provided workflow. Group similar tasks based on interdependencies, resource allocation, and potential bottlenecks. Provide clear instructions on how to categorize tasks, assess their complexity, and estimate time requirements.

## Context
{{workflow-context}}

## Output
Deliver your task batching strategy in two parts:

1. **Strategy Overview** (2-3 paragraphs): Explain your batching approach, including how you identified task groupings, addressed interdependencies, optimized resource allocation, and mitigated bottlenecks.

2. **Batched Task Table**: Present at least 5 examples in a markdown table with three columns:

| Task Category | Task Complexity | Time Required |
|---------------|-----------------|---------------|
| [example]     | [example]       | [example]     |

Ensure complexity levels and time estimates are appropriate to the workflow context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{workflow-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Task Batching Strategy Builder for Workflow Optimization is a free AI prompt that creates systematic task …
