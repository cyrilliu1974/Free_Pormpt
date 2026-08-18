# Education Performance Metric Dashboard Builder

## 簡介

The Education Performance Metric Dashboard Builder is a free AI prompt that creates comprehensive dashboard specifications for education data analysts and institutional leaders. This education dashboard prompt for ChatGPT walks you through selecting relevant performance metrics - student achievement, enrollment trends, retention rates, resource allocation - and pairs each with appropriate data sources, visualization types, and actionable insight guidance. It outputs a markdown table with four columns (Metric, Data Source, Visualization, Insights) so you can move directly from concept to implementation. The prompt runs on ChatGPT, Claude, Gemini, and Grok, and adapts to K-12 schools, universities, district offices, or training programs by accepting variables for institution type, focus areas, timeframe, and available tools. Reach for this prompt when you need to design a performance dashboard from scratch, standardize reporting across departments, or translate raw educational data into stakeholder-ready visuals. ● Selects metrics tied directly to educational outcomes and institutional goals. ● Matches each metric to accessible, relevant data sources for your context. ● Recommends visualization types that surface patterns and trends immediately. ● Provides interpretive guidance so stakeholders can turn data into decisions. ## Prompt

```
## Role
You are an expert education data analyst designing performance metric dashboards for the education sector.

## Task
Create a comprehensive dashboard specification that tracks and analyzes key educational performance data points. For each metric, identify the data source, recommend an effective visualization type, and provide interpretive guidance.

## Context
{{institution-and-audience}}

{{focus-areas}}

{{timeframe-and-tools}}

## Requirements
1. Select metrics directly relevant to educational performance and outcomes
2. Match each metric to appropriate, accessible data sources
3. Choose visualizations that make patterns and trends immediately clear
4. Include actionable insights that translate data into decisions
5. Ensure the design adapts to different educational contexts and user needs

## Output
Present your dashboard specification as a markdown table with these columns:

| Metric | Data Source | Visualization | Insights |

Each row must represent one complete performance metric with all four elements filled in.
```

## 用法 / Usage
- 必填變數 / Variables: {{focus-areas}}、{{institution-and-audience}}、{{timeframe-and-tools}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Education Performance Metric Dashboard Builder is a free AI prompt that creates comprehensive dashboard sp…
