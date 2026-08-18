# Task Priority Matrix Generator for ChatGPT

## 簡介

The Task Priority Matrix Generator is a free AI prompt that creates a systematic prioritization framework for professionals managing multiple tasks and deadlines. This task priority prompt for ChatGPT evaluates your activities against three dimensions - urgency (time-sensitivity), importance (alignment with objectives), and impact (potential outcome) - then assigns each task to a clear priority level: Critical, High, Medium, or Low. The output includes a markdown table scoring each task, definitions of priority categories, and execution strategies tailored to your project deadline and key objectives. It runs on ChatGPT, Claude, and Gemini, turning unstructured task lists into an actionable plan that balances immediate demands with strategic, high-impact work. Reach for this prompt when you need to decide what to work on first, allocate resources across competing priorities, or communicate task rankings to a team. ● Scores every task on three criteria - urgency, importance, and impact - using a consistent rating scale ● Assigns tasks to four actionable priority levels (Critical, High, Medium, Low) with clear definitions for each ● Provides execution strategies for addressing each priority category, including delegation and deferral guidance ● Recommends how to balance urgent, short-term demands with high-impact strategic work to meet both immediate deadlines and long-term objectives ## Prompt

```
## Role
You are a task prioritization expert who organizes and ranks activities based on urgency, importance, and impact.

## Task
Create a comprehensive prioritization system that evaluates the provided tasks and categorizes them into actionable priority levels. Assess each task against three criteria: urgency (time-sensitivity), importance (alignment with objectives), and impact (potential outcome). Assign each task to a priority level—Critical, High, Medium, or Low—and provide clear rationale and execution strategies for each category.

## Context
Tasks to prioritize:
{{tasks}}

Project deadline: {{deadline}}

Key objectives: {{objectives}}

## Output
1. A markdown table with columns: Task | Urgency | Importance | Impact | Priority Level
2. Rating scale explanation (e.g., 1-5 or Low/Medium/High for each criterion)
3. Priority level definitions:
   - **Critical**: Immediate action required
   - **High**: Schedule within days
   - **Medium**: Address within the current cycle
   - **Low**: Defer or delegate
4. Bullet-point strategies for addressing each priority category
5. Recommendations for balancing urgent demands with high-impact, strategic work to ensure both short-term delivery and long-term success
```

## 用法 / Usage
- 必填變數 / Variables: {{deadline}}、{{objectives}}、{{tasks}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Task Priority Matrix Generator is a free AI prompt that creates a systematic prioritization framework for …
