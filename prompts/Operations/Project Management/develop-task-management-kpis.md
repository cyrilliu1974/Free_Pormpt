# Task Management KPI Development Prompt

## 簡介

The Task Management KPI Development Prompt is a free AI prompt that builds custom performance measurement frameworks for organizations evaluating their task management systems. This task management KPI prompt for ChatGPT, Claude, and Gemini creates a complete set of key performance indicators tailored to your client context. It outputs a structured table where each KPI includes a clear name, definition explaining what it measures and why, a practical measurement approach, a specific target value, and an importance rating. The prompt enforces SMART criteria and balances predictive indicators with outcome metrics, making it ideal for management consultants, operations managers, and project leaders who need to quantify productivity, efficiency, user adoption, and business impact. Reach for this prompt when you need to move from subjective assessments to data-driven evaluation of task management tools, or when stakeholders require objective reporting on system performance. ● Enforces SMART criteria so every indicator is specific, measurable, achievable, relevant, and time-bound ● Balances leading indicators that predict future performance with lagging indicators that report actual outcomes ● Provides a markdown table format ready for stakeholder presentations and documentation ● Aligns all metrics with the client's unique business goals and industry context ## Prompt

```
## Role
You are a senior management consultant specializing in performance measurement for task management systems.

## Task
Develop a comprehensive set of KPIs tailored to the client's task management system. For each KPI, provide:

1. **Name** – Clear, concise identifier
2. **Definition** – What it measures and why it matters
3. **Measurement** – Calculation method or data collection approach
4. **Target** – Desired performance level
5. **Importance** – Critical/Moderate/Low priority rating

## Context
{{client-context}}

Ensure all KPIs are:
- **SMART** (Specific, Measurable, Achievable, Relevant, Time-bound)
- Balanced between leading indicators (predictive) and lagging indicators (outcomes)
- Aligned with the client's business objectives
- Practical to measure without excessive complexity
- Focused on productivity, efficiency, user engagement, and business impact

## Output
Present the KPIs in a markdown table:

| KPI Name | Definition | Measurement | Target | Importance |
|----------|------------|-------------|--------|------------|
| ... | ... | ... | ... | High/Medium/Low |
```

## 用法 / Usage
- 必填變數 / Variables: {{client-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Task Management KPI Development Prompt is a free AI prompt that builds custom performance measurement fram…
