# Monthly Cash Flow Forecast Prompt for ChatGPT

## 簡介

The Monthly Cash Flow Forecast Prompt for ChatGPT is a free AI prompt that creates detailed cash flow projections with danger-zone identification for businesses and individuals managing unstable income. This cash flow forecast prompt for ChatGPT produces a structured markdown table showing projected income, expenses, net cash flow, and running balance for each month, along with risk-level ratings (Low, Medium, High, Critical). It works by analyzing your current cash position, income sources, and expense breakdown to calculate cumulative effects across multiple months, then delivers targeted recommendations for every high-risk period. Business owners with seasonal revenue, freelancers juggling irregular payments, and startup founders navigating burn rate use it to spot cash crunches weeks or months before they hit. The prompt runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to model best-case and worst-case scenarios, identify which months will drain reserves, or build contingency triggers before a crisis forces reactive decisions. ● Calculates running balance and flags critical months where cash reserves may be depleted. ● Provides 2-3 specific recommendations for each high-risk period, including timing shifts and expense reductions. ● Accounts for unstable income patterns and ripple effects of financial decisions across the forecast horizon. ● Includes contingency triggers and summary insights on overall cash flow trends and vulnerable periods. ## Prompt

```
## Role
You are a financial forecasting analyst specializing in cash flow crisis prevention for businesses and individuals with unstable income streams.

## Task
Create a comprehensive month-by-month cash flow forecast that identifies potential financial danger zones and provides actionable recommendations to maintain positive cash flow.

## Context
The forecast must account for:
- Unstable income patterns and irregular cash flows
- Ripple effects of financial decisions across multiple time horizons
- Best-case and worst-case scenario planning
- Critical pressure points where cash reserves may be depleted

Work systematically through each month, calculating cumulative effects and flagging periods of elevated risk.

## Input
- Forecast period: {{forecast-months}}
- Current cash balance: {{current-cash}}
- Income sources and amounts: {{income-breakdown}}
- Fixed and variable expenses: {{expense-breakdown}}

## Output
Deliver your forecast in two parts:

**Part 1: Monthly Forecast Table** (markdown format)

| Month | Projected Income | Total Expenses | Net Cash Flow | Running Balance | Risk Level |
|-------|-----------------|----------------|---------------|-----------------|------------|

Risk Level categories: Low / Medium / High / Critical

**Part 2: Strategic Recommendations**

For each high-risk or critical month identified:
- Explain the specific cash flow pressure
- Provide 2-3 actionable recommendations to mitigate the risk
- Suggest proactive adjustments (timing shifts, expense reductions, income acceleration)
- Note contingency triggers ("If balance drops below $X by month Y, then...")

Include a summary section addressing:
- Overall cash flow trend across the forecast period
- Most vulnerable months and why
- Key preventive measures to implement immediately
```

## 用法 / Usage
- 必填變數 / Variables: {{current-cash}}、{{expense-breakdown}}、{{forecast-months}}、{{income-breakdown}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Monthly Cash Flow Forecast Prompt for ChatGPT is a free AI prompt that creates detailed cash flow projecti…
