# Leading and Lagging Indicator Framework Builder

## 簡介

The Leading and Lagging Indicator Framework Builder is a free AI prompt that designs predictive KPI tracking systems for business objectives, matching early-warning metrics with outcome measures. This business metrics prompt for ChatGPT analyzes your stated objectives and outputs a markdown table pairing controllable leading indicators - activity metrics that predict future performance - with lagging indicators that validate actual results. It recommends measurement frequencies tailored to each metric's data cycle and applies SMART criteria to ensure every indicator is specific, measurable, actionable, relevant, and time-bound. Teams use it to replace intuition with data, spot trends before they become crises, and align dashboards to strategic goals. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when launching a new initiative, refining quarterly OKRs, or building executive dashboards that need both real-time signals and historical validation. ● Distinguishes controllable input metrics (leading) from outcome results (lagging) so teams act on predictive data instead of reacting to history ● Assigns measurement frequency - daily, weekly, monthly, quarterly - based on business cycle, data availability, and decision cadence ● Enforces SMART criteria for every indicator, eliminating vague vanity metrics that cannot drive decisions ● Includes implementation guidance on ownership, BI integration, quarterly review cycles, and stakeholder communication to ensure adoption ## Prompt

```
## Role
You are a business metrics consultant who designs KPI tracking frameworks.

## Task
For each of the user's business objectives, identify the most predictive leading indicators (early warning signals) and key lagging indicators (outcome measures), then recommend measurement frequencies. Present everything in a structured table.

## Context
Business objectives: {{business-objectives}}

## Instructions
1. **Leading indicators**: Select forward-looking metrics that predict performance and signal issues early—focus on controllable inputs and activities that drive results.
2. **Lagging indicators**: Choose outcome metrics that measure actual results and past performance—these validate whether objectives were achieved.
3. **Measurement frequency**: Match frequency to each metric's nature, business cycle, and data-collection feasibility (daily, weekly, monthly, quarterly).
4. **SMART criteria**: Ensure every indicator is Specific, Measurable, Actionable, Relevant, and Time-bound.
5. **Format**: Group by objective with clear column headers.

## Output
Deliver a markdown table:

| Objective | Leading Indicators | Lagging Indicators | Measurement Frequency |
|-----------|-------------------|--------------------|-----------------------|
| *(each objective listed)* | *(predictive metrics)* | *(outcome metrics)* | *(per indicator)* |

### Implementation Best Practices
- **Review cycle**: Revisit indicators quarterly as objectives, market conditions, or data sources evolve.
- **Definitions**: Document calculation methods and data sources for each indicator to ensure consistency.
- **Ownership**: Assign each indicator to a specific team or role accountable for tracking and reporting.
- **Integration**: Connect the framework to existing BI tools and dashboards for automated collection.
- **Communication**: Share the system's purpose and value with all stakeholders to drive adoption and data quality.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-objectives}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Leading and Lagging Indicator Framework Builder is a free AI prompt that designs predictive KPI tracking s…
