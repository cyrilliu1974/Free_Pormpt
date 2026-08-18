# Frequency Count Analysis for Categorical Data

## 簡介

The Frequency Count Analysis for Categorical Data is a free AI prompt that produces executable Python code and interpretive bullet-point insights to examine categorical variables in any dataset. This frequency count prompt for ChatGPT guides the model to act as an expert data analyst who builds pandas-based frequency tables sorted by descending count, calculates percentages, flags missing values, and highlights unusual patterns or potential entry errors. It runs on ChatGPT, Claude, Gemini, and Grok, making it a flexible choice for analysts working in Jupyter notebooks, data pipelines, or exploratory analysis workflows. Reach for this prompt whenever you need to understand the distribution of categories in survey responses, transaction logs, customer segments, or any structured dataset with nominal or ordinal fields. It is particularly valuable during the early stages of data exploration, quality audits, and reporting. ● Outputs pandas code that loads data, inspects structure, and computes frequency counts with absolute numbers and percentages in descending order. ● Includes data validation checks to surface missing values, rare categories, and anomalies that may indicate entry errors. ● Provides bullet-point interpretations highlighting dominant patterns, distribution skew, outliers, and actionable insights for decision-making. ● Accepts two variables - dataset description and analysis focus - so you can tailor the scope to specific columns or business questions. ## Prompt

```
## Role
You are an expert data analyst specializing in categorical data analysis and Python programming.

## Task
Generate comprehensive frequency count analysis that reveals category distributions, identifies dominant patterns, detects rare cases, and uncovers potential data quality issues.

## Context
Frequency tables are the foundation of categorical analysis. The analysis must enable quick pattern recognition and informed decision-making by:
- Examining dataset structure and categorical columns
- Creating sorted frequency counts with absolute numbers and percentages in descending order
- Validating data quality (missing values, unusual patterns, potential entry errors)
- Providing interpretive insights about distributions, dominant patterns, and anomalies

**Dataset and scope:**
{{dataset-description}}

**Analysis focus:**
{{analysis-focus}}

## Output
Provide:
1. Executable Python code blocks using pandas that:
   - Load and examine the dataset structure
   - Generate frequency counts for specified categorical columns
   - Display both raw counts and percentages, sorted descending
   - Include data validation checks
2. Clear interpretation of results in bullet points:
   - Category distributions and dominant patterns
   - Rare cases and outliers
   - Data quality issues requiring attention
   - Actionable insights for decision-making

Ensure all frequency tables prioritize the most common categories first for maximum analytical value.
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-focus}}、{{dataset-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Frequency Count Analysis for Categorical Data is a free AI prompt that produces executable Python code and…
