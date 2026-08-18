# Class Attendance Trend Analysis Prompt

## 簡介

The Class Attendance Trend Analysis Prompt is a free AI prompt that helps educators and data analysts discover meaningful patterns in student attendance records. This attendance analysis prompt for ChatGPT guides language models through systematic examination of attendance data, looking for day-of-week variations, seasonal trends, correlations with assessments or events, and cohort differences. It runs on ChatGPT, Claude, and Gemini, applying statistical validation methods to ensure findings are reliable and actionable. The output is a ranked markdown table showing the most impactful patterns first, complete with supporting evidence and magnitude assessments. Schools use it to understand why attendance drops on Fridays, how weather affects turnout, or whether certain student groups need targeted interventions. Reach for this prompt when you have attendance records and need to move beyond raw numbers to discover the story behind participation trends. ● Examines time-based variations including day-of-week, seasonal, and calendar-driven attendance fluctuations ● Identifies correlations between attendance and external factors such as exams, events, or environmental conditions ● Applies statistical validation methods to distinguish genuine trends from random variation ● Delivers findings in a customizable markdown table format ranked by impact and significance ## Prompt

```
## Role
You are an expert data analyst specializing in educational attendance patterns.

## Task
Analyze class attendance data to identify significant trends, patterns, and correlations. Examine recurring behaviors, notable fluctuations, and relationships with external factors. Use statistical validation to ensure your findings are reliable.

## Context
**Data scope:** {{attendance-data-description}}

**Analysis focus:** {{analysis-parameters}}

Look for patterns such as:
- Day-of-week or time-of-day variations
- Seasonal or calendar-based trends
- Correlation with events, assessments, or external factors
- Cohort or demographic differences
- Improvement or decline trajectories

## Output
Present your findings as a markdown table with {{number-of-columns}} columns: {{column-names}}.

Each row should represent one distinct trend or pattern. Include:
- Clear description of the pattern
- Supporting statistical evidence
- Magnitude or significance of the trend
- Actionable insights where applicable

Prioritize the most impactful findings first.
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-parameters}}、{{attendance-data-description}}、{{column-names}}、{{number-of-columns}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Class Attendance Trend Analysis Prompt is a free AI prompt that helps educators and data analysts discover…
