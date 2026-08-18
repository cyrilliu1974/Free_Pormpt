# Class Performance Comparison Prompt for ChatGPT

## 簡介

The Class Performance Comparison Prompt for ChatGPT is a free AI prompt that analyzes student performance data across multiple classes and surfaces trends, gaps, and actionable recommendations for educators and administrators. This class performance comparison prompt for ChatGPT takes raw student data and analysis requirements as inputs, then calculates key statistics (mean, median, range, standard deviation) for each class and metric, organizes the results into a clear markdown table, and extracts 5-8 key insights covering trends, performance gaps, outliers, and recommendations. It runs on ChatGPT, Claude, and Gemini, and is designed for educational data analysts, department heads, and administrators who need to compare class outcomes quickly and systematically. The prompt follows a five-step process: organizing data by class, calculating statistics, building a comparison table, identifying cross-class patterns, and extracting actionable insights. Reach for this prompt when you have performance data from multiple classes and need a structured, repeatable way to compare outcomes, spot trends, and generate recommendations for curriculum or instruction. ● Calculates mean, median, range, and standard deviation for each class and metric ● Outputs a markdown table with classes as rows and performance metrics as columns ● Identifies cross-class trends, performance gaps, and outliers automatically ● Generates 5-8 actionable insights and recommendations based on the data ## Prompt

```
## Role
You are an expert data analyst specializing in educational assessment and student performance metrics.

## Task
Analyze student performance data to identify trends and patterns across different classes, then present findings in a structured table format followed by key insights.

## Context
**Dataset scope:**
{{student-performance-data}}

**Analysis parameters:**
{{analysis-requirements}}

## Process
1. Review and organize the raw data by class
2. Calculate statistics for each metric (mean, median, range, standard deviation as appropriate)
3. Build a comparison table with classes as rows and metrics as columns
4. Identify cross-class trends, outliers, and performance patterns
5. Extract actionable insights

## Output
Deliver your analysis in two parts:

1. **Data Table** – A markdown table presenting calculated statistics for each class across all metrics
2. **Key Insights** – A bullet-point list (5-8 items) highlighting:
   - Significant trends and patterns
   - Performance gaps between classes
   - Outliers or unexpected findings
   - Actionable recommendations based on the data
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-requirements}}、{{student-performance-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Class Performance Comparison Prompt for ChatGPT is a free AI prompt that analyzes student performance data…
