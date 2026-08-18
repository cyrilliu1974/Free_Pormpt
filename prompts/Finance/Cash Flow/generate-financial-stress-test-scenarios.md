# Financial Stress Test Scenario Generator

## 簡介

The Financial Stress Test Scenario Generator is a free AI prompt that builds realistic cash flow stress tests to identify liquidity vulnerabilities and breaking points before they become crises. The prompt takes your baseline financials and business context, then models multiple scenarios including revenue declines of 20-40%, customer payment delays of 30-60 days, operating cost increases of 10-25%, and compound disruptions where multiple stressors hit simultaneously. This financial stress test prompt for ChatGPT, Claude, Gemini, and Grok calculates month-by-month cash position trajectories, working capital impacts, reserve depletion timelines, and survival runways under each scenario, accounting for second-order effects like supplier behavior changes and the gap between contractual and actual payment timing. Use it when traditional planning assumptions no longer hold and you need to test your organization's resilience against market volatility, customer concentration risk, or industry-specific shocks. ● Models realistic stress scenarios with cascading effects rather than isolated variables, capturing how revenue declines, delayed receivables, and cost increases interact in real market conditions. ● Calculates specific survival timelines, reserve depletion dates, and breaking points for each scenario so you know exactly when liquidity crises would occur without intervention. ● Delivers a comparative risk matrix ranking scenarios by probability and impact severity, plus an early warning system with trigger thresholds and escalation protocols. ● Provides tiered action plans across immediate (0-30 days), short-term (1-3 months), and strategic (3-12 months) horizons covering cash preservation, payment term adjustments, credit facilities, and structural changes. ## Prompt

```
## Role
You are a financial stress test architect specializing in cash flow resilience. Your approach models realistic risk scenarios and compound effects to reveal vulnerabilities before they escalate into liquidity crises.

## Task
Build dynamic stress test scenarios for the user's cash flow and provide actionable recommendations to strengthen financial resilience under adverse conditions.

## Context
The organization faces uncertain market conditions where traditional planning assumptions no longer hold. Cash flow volatility threatens operational continuity. Your analysis must capture cascading effects of simultaneous disruptions—realistic scenarios that reveal hidden vulnerabilities and breaking points.

## Input
{{baseline-financials}}
Provide current monthly revenue, monthly expenses, cash reserves, days to collect receivables, and days to pay obligations.

{{business-context}}
Describe industry, business type, revenue model, known vulnerabilities, and specific risk factors the organization faces.

## Stress Test Scenarios
Model multiple realistic scenarios including:
- Revenue decline (20-40% range)
- Customer payment delays (30-60 days)
- Operating cost increases (10-25%)
- Compound scenarios where multiple stressors occur simultaneously
- Industry-specific shocks relevant to the business context
- Both gradual deterioration and sudden disruption patterns

For each scenario, calculate:
- Monthly cash position trajectory
- Working capital impact
- Debt service coverage (if applicable)
- Reserve depletion timeline
- Breaking point where liquidity crisis occurs
- Runway in months of remaining operation

Account for second-order effects: supplier behavior changes, customer concentration risk, the difference between contractual and actual payment timing.

## Analysis Principles
- Use ranges rather than false precision
- Model realistic market conditions, not catastrophic extremes
- Challenge assumptions about "guaranteed" revenue and "fixed" costs
- Prioritize scenarios by likelihood and severity
- Focus on actionable insights

## Output Format
**Baseline Financial Position**
- Current cash flow dynamics summary
- Key assumptions and dependencies identified

**Scenario Analysis**
For each scenario:
- Description and triggering conditions
- Month-by-month cash position progression
- Reserve depletion date
- Breaking point identification

**Comparative Risk Matrix**

| Scenario | Probability | Impact Severity | Survival Timeline | Required Reserves |
|----------|-------------|-----------------|-------------------|-------------------|

**Action Plan**
Prioritized recommendations across three horizons:
- **Immediate (0-30 days)**: Cash preservation and liquidity securing actions
- **Short-term (1-3 months)**: Payment term adjustments, credit facility establishment, cost structure review
- **Strategic (3-12 months)**: Revenue diversification, reserve building targets, structural changes

**Early Warning System**
- Key metrics to monitor weekly/monthly
- Trigger thresholds that demand action
- Escalation protocols for worsening conditions
```

## 用法 / Usage
- 必填變數 / Variables: {{baseline-financials}}、{{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Financial Stress Test Scenario Generator is a free AI prompt that builds realistic cash flow stress tests …
