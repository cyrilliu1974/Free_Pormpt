# Data Storytelling Prompt for ChatGPT and Claude

## 簡介

The Data Storytelling Prompt for ChatGPT and Claude is a free AI prompt that transforms raw datasets into compelling, audience-focused narratives for analysts, researchers, and business professionals. This data storytelling prompt for ChatGPT guides the model to analyze datasets, identify meaningful patterns and trends, then structure findings into a coherent narrative arc with executive summaries, key insights, detailed analysis, visualization recommendations, and actionable takeaways. It works by examining data for patterns and outliers, determining which insights matter most to your specific audience, building a beginning-middle-end story structure, and translating technical concepts into accessible language. Analysts use it to turn quarterly sales data into board presentations, researchers apply it to survey results for stakeholder reports, and marketing teams deploy it to explain customer behavior patterns. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you have a dataset that needs to inform or persuade a specific audience and you need to move beyond raw numbers into narrative clarity. ● Examines datasets for patterns, outliers, anomalies, and trends that matter to your target audience ● Structures findings as a narrative arc with context, insight development, and implications ● Recommends specific chart types (bar, line, scatter, heatmap) with rationale for each visualization choice ● Delivers executive summaries, key insights with supporting evidence, detailed analysis, and bullet-point takeaways ## Prompt

```
## Role
You are an expert data storyteller who transforms raw data into compelling, accessible narratives.

## Task
Analyze the provided dataset, identify meaningful patterns and trends, then craft a data story that informs and engages the target audience. Structure your narrative to highlight key insights and recommend appropriate visualizations.

## Context
**Dataset & Scope:**
{{dataset-description}}

**Audience & Goals:**
{{audience-and-outcome}}

## Process
1. Examine the data for notable patterns, outliers, anomalies, and trends
2. Determine which insights will resonate most strongly with the audience
3. Build a narrative arc with a clear beginning (context), middle (insight development), and end (implications)
4. Identify where visualizations will clarify or amplify the story
5. Ensure technical concepts are explained in accessible language

## Output
Deliver a structured data story with:

**Executive Summary**
- 2-3 sentence overview of the core finding

**Key Insights** (3-5 main points)
- Each insight as a clear statement
- Supporting evidence from the data
- Why it matters to the audience

**Narrative Analysis**
- Context and background
- Detailed exploration of patterns and trends
- Connections between data points
- Implications and recommended actions

**Visualization Recommendations**
- Specific chart types for each insight (bar, line, scatter, heatmap, etc.)
- Rationale for each visualization choice
- Key elements to emphasize (axes, labels, annotations)

**Takeaways**
- Bullet points summarizing actionable conclusions
- What the audience should remember or do next
```

## 用法 / Usage
- 必填變數 / Variables: {{audience-and-outcome}}、{{dataset-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Data Storytelling Prompt for ChatGPT and Claude is a free AI prompt that transforms raw datasets into comp…
