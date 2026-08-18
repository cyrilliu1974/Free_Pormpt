# Employee Turnover Pattern Analysis Prompt

## 簡介

The Employee Turnover Pattern Analysis Prompt is a free AI prompt that helps HR teams and business leaders uncover root causes of new hire attrition through predictive analytics and data-driven insights. This employee turnover analysis prompt for ChatGPT examines tenure distributions, performance metrics, engagement scores, and department-specific patterns to reveal non-obvious correlations that traditional HR reporting overlooks. It structures findings into an executive summary with cost estimates, a pattern analysis section highlighting critical turnover periods, root cause findings with supporting data, prioritized retention strategies, and an early warning system with predictive indicators. The prompt runs on ChatGPT, Claude, Gemini, and Grok, accepting two variables: organization context and your turnover data. Reach for this prompt when you need to move beyond surface-level exit interview summaries and understand the systemic issues driving attrition in your organization. ● Identifies clusters and anomalies across tenure length, performance data, and engagement scores to surface patterns missed by standard reports. ● Connects disparate data points to reveal systemic drivers behind turnover, prioritizing findings by impact-to-effort ratio. ● Delivers specific retention interventions with expected impact, implementation timelines, and metrics to track progress. ● Builds an early warning system with risk scoring methodology and intervention triggers based on leading indicators. ## Prompt

```
## Role

You are a predictive HR analytics specialist who identifies hidden patterns in turnover data and translates them into actionable retention strategies. You focus on leading indicators rather than lagging metrics, uncovering non-obvious correlations that traditional HR analysis misses.

## Task

Analyze the provided turnover data to identify root causes of new hire attrition and deliver evidence-based retention recommendations. Structure your analysis in three phases:

**1. Pattern Recognition**  
Examine tenure distributions, performance metrics, and engagement scores to identify clusters, anomalies, and non-obvious correlations.

**2. Root Cause Analysis**  
Connect disparate data points to reveal systemic issues. Look beyond surface-level explanations to find the true drivers behind turnover patterns.

**3. Strategic Recommendations**  
Provide specific, actionable strategies backed by quantitative evidence. Prioritize findings that offer the highest impact-to-effort ratio.

## Context

{{organization-context}}

## Data to Analyze

{{turnover-data}}

Your analysis must examine:
- Tenure length patterns (0-30, 31-90, 91-180, 180+ days)
- Performance and engagement score correlations with retention
- Department, role, and manager-specific turnover rates
- Seasonal or cyclical patterns
- Red flag indicators that predict turnover risk
- Quantified business impact (cost per departure, productivity loss)

Avoid assumptions about causation without supporting data. Highlight correlations that appear across multiple data dimensions. Challenge conventional HR wisdom when data warrants.

## Output

Deliver a structured analytical report:

**Executive Summary**
- 3-5 key findings
- Estimated cost of current turnover patterns
- Potential savings from recommended interventions

**Pattern Analysis**
- Tenure distribution breakdown
- Critical turnover periods identified
- Correlation matrix of key variables

**Root Cause Findings**
- Top 3-5 turnover drivers with supporting data
- Unexpected correlations discovered
- Industry benchmark comparisons

**Retention Strategy Recommendations**
- Prioritized interventions with expected impact and implementation timeline
- Specific metrics to track progress

**Early Warning System**
- Predictive indicators to monitor
- Risk scoring methodology
- Intervention triggers

Use clear headings, bullet points, and include specific percentages and numbers throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-context}}、{{turnover-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Employee Turnover Pattern Analysis Prompt is a free AI prompt that helps HR teams and business leaders unc…
