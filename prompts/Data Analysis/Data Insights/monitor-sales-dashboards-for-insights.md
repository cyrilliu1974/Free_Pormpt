# Sales Dashboard Analysis Prompt for Data Insights

## 簡介

The Sales Dashboard Analysis Prompt for Data Insights is a free AI prompt that transforms raw sales data into actionable performance recommendations for sales analysts, revenue operations teams, and business leaders. This sales dashboard analysis prompt for ChatGPT examines your sales data to identify trends, patterns, and anomalies across critical metrics including conversion rates, average deal size, sales cycle length, and customer acquisition cost. It runs on ChatGPT, Claude, Gemini, and Grok, outputting a structured markdown table that pairs each insight with its corresponding KPI and a concrete action plan. Use it when you need to move beyond raw dashboard numbers and translate metrics into specific optimization strategies tailored to your industry and target market. ● Examines key sales metrics including conversion rates, average deal size, sales cycle length, and customer acquisition cost to identify performance drivers and bottlenecks. ● Surfaces trends, patterns, and anomalies that might be missed in routine dashboard reviews, contextualized for your specific industry and target market. ● Pairs every data insight with the relevant KPI and a concrete action plan, closing the gap between analysis and execution. ● Outputs findings in a markdown table format that is ready to present to stakeholders or integrate into sales review meetings. ## Prompt

```
## Role
You are an expert sales analyst specializing in performance optimization through data-driven insights.

## Task
Analyze the provided sales data to uncover actionable insights that will improve sales performance. Examine trends, patterns, and anomalies across key metrics including conversion rates, average deal size, sales cycle length, and customer acquisition cost. For each insight, identify the relevant KPI and develop a specific action plan.

## Context
{{sales-data}}

Industry: {{industry}}
Target market: {{target-market}}

## Output
Deliver your analysis as a markdown table with three columns:

| Insight | Metric/KPI | Action Plan |
|---------|------------|-------------|

Each row must contain:
- **Insight**: A clear, concise finding from the data
- **Metric/KPI**: The specific metric or KPI the insight relates to
- **Action Plan**: A concrete, actionable recommendation to optimize sales performance based on the insight

Provide 5-8 rows of high-impact insights with their corresponding metrics and action plans.
```

## 用法 / Usage
- 必填變數 / Variables: {{industry}}、{{sales-data}}、{{target-market}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Minimalist_Entrepreneurship_Execution · First_Customer_Acquisition_Engine
- 適用 / Use when: The Sales Dashboard Analysis Prompt for Data Insights is a free AI prompt that transforms raw sales data into …
