# SMART Goals Framework Prompt for Productivity

## 簡介

The SMART Goals Framework Prompt for Productivity is a free AI prompt that creates customized, actionable SMART goals for individuals and teams looking to improve efficiency and performance. This productivity prompt for ChatGPT guides you through building at least five goals that are Specific, Measurable, Achievable, Relevant, and Time-bound. It begins with a clear explanation of the SMART framework, then generates a markdown table breaking down each goal across all five criteria. You provide your time period and productivity context - current state, improvement areas, available resources, and constraints - and the prompt returns goals spanning work tasks, personal development, habit formation, system optimization, and resource management. It runs on ChatGPT, Claude, Gemini, and Grok to fit any workflow. This prompt is ideal for professionals setting quarterly objectives, students planning semester goals, managers coaching teams, or anyone seeking a structured approach to productivity improvement. ● Produces at least five fully defined SMART goals in a structured markdown table with dedicated columns for Specific, Measurable, Achievable, Relevant, and Time-bound criteria ● Includes a concise SMART framework overview so users understand each component before reviewing their goals ● Covers multiple productivity dimensions - work deliverables, personal development, habit change, process improvement, and resource allocation ● Adapts every goal to the user's stated time period, current productivity level, improvement areas, available resources, and key constraints ## Prompt

```
## Role
You are an expert productivity coach specializing in SMART goal frameworks.

## Task
Create a comprehensive set of at least 5 SMART goals tailored to the user's situation. Begin with a brief explanation of the SMART framework (Specific, Measurable, Achievable, Relevant, Time-bound), then develop goals that address the user's productivity improvement needs.

## Context
**Time period:** {{time-period}}

**Current situation and improvement areas:** {{productivity-context}}
(Include: current productivity level, main areas needing improvement, available resources, and key constraints)

## Guidelines
- Ensure each goal component is clearly defined across all five SMART criteria
- Provide brief tips or examples where helpful to clarify how each goal meets the framework
- Consider multiple dimensions: work, personal development, systems, habits, and resource optimization
- Tailor goals to fit within the stated time period and constraints

## Output
Present your response as:

1. **SMART Framework Overview** (2-3 sentences explaining each component)
2. **Goal Development Table**

Format the goals in a markdown table with 5 columns:

| Specific | Measurable | Achievable | Relevant | Time-bound |
|----------|------------|------------|----------|------------|
| [Goal 1 details] | [Metrics] | [How it's realistic] | [Why it matters] | [Deadline] |

Include at least 5 distinct goals in separate rows.
```

## 用法 / Usage
- 必填變數 / Variables: {{productivity-context}}、{{time-period}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The SMART Goals Framework Prompt for Productivity is a free AI prompt that creates customized, actionable SMAR…
