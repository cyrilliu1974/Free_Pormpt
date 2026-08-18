# Sales Quota Planning Prompt for ChatGPT

## 簡介

The Sales Quota Planning Prompt for ChatGPT is a free AI prompt that builds realistic, achievable sales quotas for sales managers and operations teams. It analyzes your historical sales data, current market trends, and individual rep performance to create a balanced quota structure that drives results without demotivating your team. This sales quota planning prompt for ChatGPT takes four inputs: your sales team composition, historical sales data, market trends, and the column structure you need. It produces a markdown table with personalized quotas for each team member, plus the key assumptions behind the numbers, practical strategies to help reps hit their targets, and recommended incentive structures for over-performance. The prompt explicitly accounts for seasonality, product lifecycle stages, and economic headwinds or tailwinds. Use it when building quarterly or annual plans, re-balancing territories, or justifying quota decisions to leadership and frontline sellers. ● Tailors quotas to individual rep capabilities and tenure, not one-size-fits-all targets. ● Surfaces the assumptions and risk factors behind each number so stakeholders understand the rationale. ● Delivers actionable coaching strategies and incentive recommendations alongside the quota table. ● Accounts for seasonality, product maturity, and economic conditions in a structured, repeatable way. ## Prompt

```
## Role
You are an expert sales strategist designing realistic, achievable sales quotas.

## Task
Create a comprehensive sales quota plan that balances ambition with attainability. Analyze the provided data to develop quotas tailored to each team member, accounting for seasonality, product lifecycle, and economic conditions. Include strategies for quota attainment and incentive recommendations for exceeding targets.

## Context
**Sales team composition and individual performance:**
{{sales-team-context}}

**Historical sales data:**
{{historical-data}}

**Market trends and economic conditions:**
{{market-trends}}

## Output
Present your quota plan as a markdown table with these columns:
{{column-names}}

After the table, provide:
- Key assumptions underlying the quota structure
- Strategies to help the team achieve their quotas
- Recommended incentives for exceeding targets
```

## 用法 / Usage
- 必填變數 / Variables: {{column-names}}、{{historical-data}}、{{market-trends}}、{{sales-team-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Strategic_Resource&Sprint_Prioritization
- 適用 / Use when: The Sales Quota Planning Prompt for ChatGPT is a free AI prompt that builds realistic, achievable sales quotas…
