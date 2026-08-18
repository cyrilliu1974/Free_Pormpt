# Student Engagement Analysis Prompt for LMS Data

## 簡介

The Student Engagement Analysis Prompt for LMS Data is a free AI prompt that analyzes learning management system engagement metrics to identify trends and generate actionable recommendations for educators and data analysts. This student engagement prompt for ChatGPT examines core indicators including login frequency, session duration, assignment completion rates, forum participation, and peer interaction patterns across any specified student population and timeframe. It runs on ChatGPT, Claude, Gemini, and Grok, processing data from Canvas, Blackboard, Moodle, or any LMS platform to surface meaningful patterns like seasonal variations, cohort differences, and correlations between engagement types. The prompt outputs a clean markdown table with three columns: Engagement Metric, Trend, and Recommendation, making it easy to present findings to faculty, administrators, or instructional designers. Reach for this prompt when you need to transform raw LMS analytics into evidence-based strategies for improving student participation and learning outcomes. ● Analyzes login patterns, content engagement, assignment submissions, and discussion forum activity across any student cohort and time period. ● Surfaces correlations between different engagement types and identifies anomalies that may indicate at-risk learners. ● Generates 5-8 prioritized recommendations with specific actions tied directly to observed trends. ● Adapts to any LMS platform and accepts custom metrics like video watch time, quiz attempts, or mobile access rates. ## Prompt

```
## Role
You are an educational data analyst specializing in learning management system engagement patterns.

## Task
Analyze student engagement data to identify trends and patterns, then develop actionable recommendations to improve engagement and learning outcomes.

## Context
**Data scope:**
- Learning management system: {{lms-name}}
- Student population: {{student-group}}
- Analysis period: {{timeframe}}
- Institution context: {{institution-type}}

**Core engagement indicators to examine:**
- Login frequency and session duration
- Time spent on platform and content types
- Assignment completion rates and submission patterns
- Forum participation and peer interaction
- {{additional-metrics}}

Identify meaningful patterns across these metrics, considering seasonal variations, cohort differences, and correlations between different engagement types.

## Output
Present your analysis as a markdown table with three columns:

| Engagement Metric | Trend | Recommendation |
|-------------------|-------|----------------|

Each row should provide:
- **Engagement Metric**: The specific indicator analyzed
- **Trend**: Clear description of the observed pattern (increases, decreases, correlations, anomalies)
- **Recommendation**: Specific, actionable step to address the trend and improve outcomes

Include 5-8 key metrics in your analysis, prioritizing those with the strongest patterns or greatest impact on learning outcomes.
```

## 用法 / Usage
- 必填變數 / Variables: {{additional-metrics}}、{{institution-type}}、{{lms-name}}、{{student-group}}、{{timeframe}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Student Engagement Analysis Prompt for LMS Data is a free AI prompt that analyzes learning management syst…
