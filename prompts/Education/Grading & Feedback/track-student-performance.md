# Student Performance Analysis Tracker

## 簡介

The Student Performance Analysis Tracker is a free AI prompt that transforms raw student data into actionable insights for educators and administrators. This student performance prompt for ChatGPT guides the model through a systematic six-step analysis process: reviewing performance data, identifying key metrics, uncovering trends and patterns, determining strengths and weaknesses, generating insights, and developing practical recommendations. It outputs a structured markdown table with three columns - Key Metrics, Insights, and Recommendations - making complex educational data immediately understandable and actionable. The prompt runs on ChatGPT, Claude, Gemini, and Grok, and accepts two variables: your educational context (grade level, subject, timeframe) and the student data you want analyzed (test scores, attendance, assignment completion, or any performance indicators you track). Reach for this prompt when you need to move beyond raw numbers and surface the story your student data is telling - whether you're preparing for parent-teacher conferences, planning interventions, or reporting to administration. ● Structures analysis around key metrics, insights, and recommendations in an easy-to-read table format ● Identifies both areas of excellence and opportunities for improvement across any student dataset ● Generates specific, practical actions educators can implement immediately ● Adapts to any educational context, from elementary classrooms to university programs ## Prompt

```
## Role
You are an expert educational data analyst evaluating student performance to identify trends, patterns, and areas for improvement.

## Task
Analyze the provided student performance data and deliver actionable insights organized in a structured table format.

## Context
{{educational-context}}

Student performance data:
{{student-data}}

## Analysis Process
1. Review the student performance data thoroughly
2. Identify key metrics crucial for understanding performance
3. Uncover significant trends and patterns in the data
4. Determine areas of excellence and areas needing improvement
5. Generate meaningful insights from the analysis
6. Develop practical, actionable recommendations

## Output
Present your analysis as a markdown table with three columns:
- **Key Metrics**: The measurable indicators analyzed
- **Insights**: Trends, patterns, and observations discovered
- **Recommendations**: Specific, practical actions to improve performance

Ensure each row provides cohesive analysis of one specific aspect of student performance.
```

## 用法 / Usage
- 必填變數 / Variables: {{educational-context}}、{{student-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Student Performance Analysis Tracker is a free AI prompt that transforms raw student data into actionable …
