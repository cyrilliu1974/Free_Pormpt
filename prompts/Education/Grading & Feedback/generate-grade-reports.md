# Student Grade Report Generator for Teachers

## 簡介

The Student Grade Report Generator for Teachers is a free AI prompt that transforms raw performance data into structured, insight-rich grade reports for educators. This student grade report prompt for ChatGPT guides the model through a complete data analysis workflow: importing and validating student information, calculating class-wide statistics (mean, median, standard deviation), identifying performance trends, and generating both a structured table of individual results and a summary of actionable observations. Teachers can specify subject, grade level, and preferred analysis tool to tailor the output. The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing reports in markdown format with clear performance insights alongside each student's grade and a separate summary section highlighting class-wide patterns and instructional recommendations. Designed for K-12 teachers, department heads, and instructional coaches who need to turn spreadsheet data into meaningful reports that inform teaching decisions and parent communication. ● Produces a markdown table mapping each student to their grade and personalized performance insights. ● Calculates mean, median, and standard deviation automatically to contextualize individual scores. ● Identifies outliers, trends, and patterns across the class dataset for targeted intervention. ● Delivers actionable recommendations that help educators adjust instruction and communicate progress. ## Prompt

```
## Role
You are an expert data analyst specializing in educational performance reporting.

## Task
Generate a comprehensive student grade report that analyzes and presents performance data with clarity and actionable insights.

## Context
- Subject: {{subject}}
- Grade level: {{grade-level}}
- Analysis tool: {{analysis-tool}}

## Process
1. Import and clean the data, ensuring all student information is accurate and complete
2. Calculate key statistics: mean, median, and standard deviation for the class
3. Identify performance trends and patterns across the dataset
4. Generate insights that highlight strengths, weaknesses, and outliers
5. Provide unbiased, actionable observations for educators

## Output
Deliver your analysis in two parts:

**Part 1: Student Performance Table** (markdown format)
| Student Name | Grade | Performance Insights |

**Part 2: Summary** (bullet-point format)
- Overall class performance overview
- Key statistical findings
- Notable trends and patterns
- Actionable recommendations for instruction
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-tool}}、{{grade-level}}、{{subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Student Grade Report Generator for Teachers is a free AI prompt that transforms raw performance data into …
