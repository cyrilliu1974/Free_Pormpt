# Grant Budget Proposal Builder

## 簡介

The Grant Budget Proposal Builder is a free AI prompt that creates detailed, professionally formatted budget proposals for grant applications across any sector. This grant budget prompt for ChatGPT takes your project context - grant type, business type, requested amount, project duration, and goals - and produces a comprehensive budget table with relevant expense categories, clear descriptions, and appropriate dollar amounts. It runs on ChatGPT, Claude, Gemini, and Grok, delivering a markdown-formatted proposal with an introduction explaining how the budget supports your project goals, followed by an organized three-column table and a summary total. Researchers, nonprofit managers, consultants, and business owners use it to translate project plans into fundable financial requests that meet funder requirements and industry norms. ● Produces a professional markdown budget table with categories, line-item descriptions, and dollar amounts tailored to your grant type and business sector. ● Includes an introductory paragraph that explains how the budget aligns with stated project goals and grant objectives. ● Generates a summary row to confirm that itemized expenses match the total requested amount. ● Adapts to any grant context - research, nonprofit program, business development, capital projects, or operational funding. ## Prompt

```
## Role
You are an expert financial planner specializing in grant application budgets.

## Task
Develop a comprehensive budget proposal that strengthens a grant application. Create a detailed, professionally structured budget with clear expense categories, thorough descriptions, and appropriate amounts that align with grant objectives and industry standards.

## Context
**Grant and project details:** {{grant-and-project-context}}
(Include: grant type, business type, total requested amount, project duration, and specific project goals)

Identify budget categories relevant to this grant type and business. For each category, describe proposed expenses that directly support the project goals and fit within the grant's parameters and limitations.

## Output
Provide a brief introduction explaining the budget's alignment with project goals, followed by a markdown table with three columns:

| Budget Category | Description | Amount |
|-----------------|-------------|--------|

After the table, include a summary row showing total expenses and confirm it matches the requested amount.
```

## 用法 / Usage
- 必填變數 / Variables: {{grant-and-project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Grant Budget Proposal Builder is a free AI prompt that creates detailed, professionally formatted budget p…
