# Cash Flow Scenario Forecasting Prompt

## 簡介

The Cash Flow Scenario Forecasting Prompt is a free AI prompt that generates three-scenario cash flow projections to help business leaders model uncertainty and plan for multiple financial outcomes. This cash flow scenario prompt for ChatGPT builds side-by-side forecasts across optimistic, realistic, and pessimistic cases over 12 months, calculating monthly cash positions, cumulative runway, and critical thresholds where reserves drop to 90-day, 60-day, or 30-day levels. You provide baseline financials and scenario assumptions - revenue drivers, expense variability, growth rates, seasonality - and the prompt returns a comparison table, detailed monthly breakdowns for each scenario, flagged decision points, and concrete risk mitigation strategies with trigger conditions. It runs on ChatGPT, Claude, Gemini, and Grok, turning raw assumptions into structured forecasts that guide hiring, fundraising, and cost decisions. Reach for this prompt when you need to quantify downside risk, communicate financial ranges to stakeholders, or prepare contingency plans before cash constraints force reactive choices. ● Compares optimistic, realistic, and pessimistic monthly cash flows with cumulative runway for each scenario. ● Identifies exact months and cash levels that trigger hiring freezes, funding needs, or expansion opportunities. ● Highlights the variables driving cash variability and flags early warning indicators for worst-case trajectories. ● Provides 3-5 risk mitigation strategies with implementation steps and the conditions that activate each one. ## Prompt

```
## Role
You are a financial scenario planner specializing in cash flow forecasting, uncertainty modeling, and risk assessment for business leaders.

## Task
Create a comprehensive three-scenario cash flow forecast comparing optimistic, realistic, and pessimistic outcomes over a 12-month period. Identify critical decision points, cash position ranges, break-even thresholds, and provide risk mitigation strategies.

## Context
Business context and baseline financials:
{{financial-baseline}}

Scenario parameters (revenue assumptions, expense variability, growth rates, seasonality factors, and any other drivers unique to each scenario):
{{scenario-assumptions}}

For each scenario (optimistic, realistic, pessimistic):
- Calculate monthly cash positions and cumulative runway
- Identify when cash reserves reach critical thresholds (90-day, 60-day, 30-day runway)
- Highlight the key variables driving cash flow variability
- Flag months requiring major decisions (hiring freezes, funding needs, expansion triggers)

## Output
Deliver your analysis in this structure:

### Executive Summary
One-paragraph overview of the cash position range and primary risks across scenarios.

### Scenario Comparison Table
| Month | Optimistic | Realistic | Pessimistic | Decision Trigger |

### Scenario 1: Optimistic (Best-Case)
- Monthly revenue, expenses, net cash flow
- Cumulative cash position
- Growth/investment opportunities unlocked

### Scenario 2: Realistic (Base-Case)
- Monthly revenue, expenses, net cash flow
- Cumulative cash position
- Operational considerations

### Scenario 3: Pessimistic (Worst-Case)
- Monthly revenue, expenses, net cash flow
- Cumulative cash position
- Survival tactics and required interventions

### Critical Thresholds & Decision Points
Bullet list of specific cash levels or months when action is required.

### Risk Mitigation Strategies
3-5 concrete recommendations with trigger conditions and implementation steps.

### Contingency Planning
Pre-planned responses for if the pessimistic scenario begins materializing (early warning indicators, cost reduction levers, funding options).
```

## 用法 / Usage
- 必填變數 / Variables: {{financial-baseline}}、{{scenario-assumptions}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Structured_Analytical_Decomposition
- 適用 / Use when: The Cash Flow Scenario Forecasting Prompt is a free AI prompt that generates three-scenario cash flow projecti…
