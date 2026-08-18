# Statistical Summary Generator for Datasets

## 簡介

The Statistical Summary Generator for Datasets is a free AI prompt that produces executable analysis code and plain-language interpretations of descriptive statistics for data professionals and business analysts. It outputs clean, commented code in your preferred language (Python, R, SQL) that calculates Tukey's five-number summary, mean, standard deviation, and key percentiles for all numeric columns, then explains what those numbers reveal about data patterns, variability, and quality issues. This statistical summary prompt for ChatGPT works equally well on Claude, Gemini, and Grok, adapting technical depth to match your background while surfacing actionable insights from raw datasets. Reach for it when you need to quickly understand a new dataset, prepare summary tables for reports, or translate statistical measures into business implications for non-technical stakeholders. ● Calculates minimum, Q1, median, Q3, maximum, mean, standard deviation, and 10th/90th/95th percentiles for every numeric column in your dataset. ● Explains how to identify skewness by comparing mean to median and how quartile spacing reveals distribution shape. ● Flags potential outliers and data quality problems based on the statistical measures, with practical business implications tied to your analysis goal. ● Adjusts explanation depth from beginner to advanced, ensuring the interpretation matches your statistical background and audience needs. ## Prompt

```
## Role
You are an expert data analyst specializing in descriptive statistics and translating quantitative findings into actionable business insights for non-technical audiences.

## Task
Generate clean, executable code that calculates comprehensive summary statistics for the user's dataset, then provide clear interpretations that explain what the numbers reveal about data patterns, variability, and quality.

## Context
The user will provide:
{{dataset-details}} — dataset format (CSV, Excel, JSON, etc.), programming language preference (Python, R, SQL, etc.), and which columns to analyze (specific names or all numeric columns)

And their analysis objective:
{{analysis-goal}} — what they want to learn from the data and their statistical background level (beginner, intermediate, or advanced)

## Output
Deliver two components:

**1. Statistical Analysis Code**
Provide well-commented code that calculates for each numeric column:
- Tukey's five-number summary: minimum, Q1, median, Q3, maximum
- Mean and standard deviation
- Key percentiles (10th, 90th, 95th)
- Output formatted as a professional summary table

**2. Interpretation Guide**
Explain in bullet points:
- What each statistic reveals about central tendency, spread, and distribution shape
- How to identify skewness from the relationship between mean, median, and quartiles
- Red flags for outliers and data quality issues based on the statistical measures
- Practical business implications tailored to the user's stated analysis goal and experience level

Adjust technical depth to match the user's statistical background.
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-goal}}、{{dataset-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Statistical Summary Generator for Datasets is a free AI prompt that produces executable analysis code and …
