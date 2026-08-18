# Monthly Cash Flow Forecast Generator

## 簡介

The Monthly Cash Flow Forecast Generator is a free AI prompt that creates detailed cash flow projections with liquidity risk analysis for finance teams, business owners, and treasury professionals. This cash flow forecast prompt for ChatGPT, Claude, Gemini, and Grok produces a structured markdown table tracking projected inflows, outflows, net cash flow, ending balances, and risk levels across each month of your chosen forecast period. It identifies seasonal patterns, payment timing mismatches, growth-related cash demands, and flags months with negative balances or dangerously low reserves. The output includes detailed commentary on critical periods, actionable recommendations for managing shortfalls or deploying surplus cash, and sensitivity scenarios that model how delayed receivables or unexpected expenses would ripple through your projections. Use it when building quarterly budgets, preparing for growth phases, presenting to stakeholders, or stress-testing your business against cash crunches. ● Calculates running monthly balances and flags periods with negative cash or low reserves ● Analyzes seasonal trends, payment timing gaps, and growth-driven liquidity needs ● Delivers sensitivity scenarios modeling delayed receivables and unexpected cost spikes ● Provides specific, actionable recommendations for managing shortfalls and optimizing surplus months ## Prompt

```
## Role
You are an expert financial analyst and cash flow specialist with experience in corporate treasury and business financial planning.

## Task
Create a comprehensive monthly cash flow forecast that identifies liquidity risks and opportunities. Calculate running balances month by month, identify potential shortfalls, and analyze seasonal patterns, payment timing mismatches, and growth-related cash demands. Flag months with negative balances or low reserves. Provide specific recommendations for managing shortfalls and optimizing surplus periods. Include sensitivity analysis showing how delays in receivables or unexpected expenses could impact projections.

## Context
Business type and industry: {{business-context}}

Current cash balance: {{current-cash-balance}}

Forecast period: {{forecast-period}} months

## Output
Present your analysis as a markdown table with columns: Month | Projected Inflows | Projected Outflows | Net Cash Flow | Ending Balance | Risk Level

Follow the table with:
- Detailed commentary on critical months
- Actionable recommendations for managing identified issues
- Sensitivity scenarios (delayed receivables, unexpected expenses)
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{current-cash-balance}}、{{forecast-period}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Monthly Cash Flow Forecast Generator is a free AI prompt that creates detailed cash flow projections with …
