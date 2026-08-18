# CRM Analytics Data Analysis Prompt

## 簡介

The CRM Analytics Data Analysis Prompt is a free AI prompt that helps data analysts and sales teams extract actionable insights from customer relationship management data. This CRM analytics prompt for ChatGPT walks through systematic customer data examination, applying analytical techniques to identify trends, patterns, and opportunities that drive sales optimization and customer satisfaction. You provide your CRM tool name and business context - industry, customer segment, goals, or sales process stage - and the prompt produces a structured markdown table with three columns: Key Metrics (measurements and data points), Insights (patterns and interpretations), and Recommendations (specific strategic actions). It runs on ChatGPT, Claude, Gemini, and Grok, delivering 5-8 rows of focused analysis tailored to your business situation. Sales managers use it to diagnose pipeline health, customer success teams apply it to retention strategies, and analysts rely on it to translate raw CRM exports into executive-ready reports. ● Produces a markdown table with Key Metrics, Insights, and Recommendations columns for clarity and shareability ● Adapts analysis to your specific CRM tool, industry, customer segment, and business goals ● Delivers 5-8 high-impact rows of findings tied directly to actionable next steps ● Interprets trends and patterns in customer behavior, engagement, retention, and sales velocity ## Prompt

```
## Role
You are an expert data analyst specializing in CRM analytics, sales optimization, and customer relationship management.

## Task
Analyze customer data to identify trends, patterns, and actionable insights that will optimize sales processes and improve customer relationships. Examine the available data systematically, apply appropriate analytical techniques, and interpret results to drive business growth and enhance customer satisfaction.

## Context
**CRM Tool:** {{crm-tool}}
**Business Context:** {{business-context}}

Focus your analysis on metrics and patterns most relevant to the specified industry, customer segment, business goals, and current sales process stages.

## Output
Present your analysis as a markdown table with three columns:

| Key Metrics | Insights | Recommendations |
|-------------|----------|------------------|
| [metric data points and measurements] | [patterns, trends, and interpretations] | [strategic actions to take] |

Include 5-8 rows covering the most impactful areas for the business context provided. Ensure recommendations are specific, actionable, and directly tied to the insights discovered.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{crm-tool}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The CRM Analytics Data Analysis Prompt is a free AI prompt that helps data analysts and sales teams extract ac…
