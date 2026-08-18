# Educational Attrition Analysis Method Designer

## 簡介

The Educational Attrition Analysis Method Designer is a free AI prompt that creates tailored retention analytics frameworks for schools, colleges, and universities. This attrition analysis prompt for ChatGPT guides data analysts through designing comprehensive methods that identify key dropout and turnover factors - student attrition, faculty departures, administrative retention - and pairs each with the most appropriate analytics technique (survival analysis, cohort comparison, logistic regression, predictive modeling). The prompt produces a markdown table mapping attrition factors to analysis methods and the strategic insights each yields, calibrated to your institution's available data sources and team expertise. Use it when launching retention initiatives, auditing existing programs, or building dashboards for enrollment and HR leadership. ● Maps student dropout, faculty turnover, and staff retention to evidence-based analytics techniques suited to your data maturity. ● Outputs a three-column table (Attrition Factor | Analysis Technique | Insights) for immediate implementation by analytics or institutional research teams. ● Adapts recommendations to your technical expertise level, whether descriptive reporting or advanced predictive modeling. ● Prioritizes data-driven, decision-ready insights that enrollment managers, provosts, and HR directors can act on. ## Prompt

```
## Role
You are an expert data analyst specializing in attrition analysis for the education sector.

## Task
Design a comprehensive attrition analysis method using advanced data analytics techniques. Identify key attrition factors specific to the education industry, determine the most appropriate analysis technique for each factor, and explain the insights each technique yields. Cover student dropout rates, faculty turnover, administrative staff retention, and other relevant areas. Ensure the method is data-driven, actionable, and provides decision-makers with valuable strategic insights.

## Context
Institution and scope: {{institution-and-concern}}

Available resources: {{data-sources-and-expertise}}

Success criteria: {{desired-outcome}}

## Output
Present your comprehensive attrition analysis method in a markdown table with three columns:

| Attrition Factor | Analysis Technique | Insights |

Each row must provide clear, concise, and actionable information tailored to the institution context and available data. Prioritize techniques that match the specified technical expertise level and can be implemented with the available data sources.
```

## 用法 / Usage
- 必填變數 / Variables: {{data-sources-and-expertise}}、{{desired-outcome}}、{{institution-and-concern}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Educational Attrition Analysis Method Designer is a free AI prompt that creates tailored retention analyti…
