# Sales Initiative ROI Calculator Prompt

## 簡介

The Sales Initiative ROI Calculator Prompt is a free AI prompt that calculates and presents Return on Investment analysis for sales programs, campaigns, and initiatives. This sales initiative ROI prompt for ChatGPT takes your revenue figures, implementation costs, customer acquisition expenses, and timeframe, then applies standard financial formulas to compute ROI percentages across multiple dimensions. It delivers results as a markdown table showing each metric's value and ROI percentage, followed by a written summary with key insights and decision-making implications. Sales leaders use it to evaluate campaign performance, justify budget requests, and compare initiative effectiveness across quarters. Designed for sales operations teams, financial analysts, and revenue leaders who need consistent, professional ROI reporting without manual spreadsheet work. ● Applies standard ROI formulas automatically - ((Revenue - Cost) / Cost) × 100 - to revenue, implementation costs, and customer acquisition figures ● Outputs a three-column markdown table (Metric, Value, ROI Percentage) that copies cleanly into reports and presentations ● Includes a narrative summary section highlighting overall ROI assessment, key observations, and business implications ● Accepts custom timeframes so you can analyze initiatives by month, quarter, campaign duration, or fiscal year ## Prompt

```
## Role
You are a financial analyst specializing in sales initiative performance measurement.

## Task
Calculate and present the Return on Investment (ROI) for a sales initiative using provided financial data.

## Context
Analyze the following:
- Sales initiative: {{sales-initiative}}
- Revenue generated: {{revenue-generated}}
- Cost of implementation: {{cost-of-implementation}}
- Customer acquisition cost: {{customer-acquisition-cost}}
- Analysis timeframe: {{timeframe}}

Calculate ROI percentage for each relevant metric using standard financial formulas: ROI = ((Revenue - Cost) / Cost) × 100.

## Output
Deliver your analysis as:

1. **Markdown table** with three columns:
   - Metric (e.g., Overall Initiative ROI, Customer Acquisition Efficiency)
   - Value (dollar amounts or key figures)
   - ROI Percentage

2. **Summary section** below the table containing:
   - Overall ROI assessment
   - Key insights and observations
   - Implications for decision-making
```

## 用法 / Usage
- 必填變數 / Variables: {{cost-of-implementation}}、{{customer-acquisition-cost}}、{{revenue-generated}}、{{sales-initiative}}、{{timeframe}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Structured_Analytical_Decomposition
- 適用 / Use when: The Sales Initiative ROI Calculator Prompt is a free AI prompt that calculates and presents Return on Investme…
