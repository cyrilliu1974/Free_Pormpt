# Sales Performance Dashboard Generator Prompt

## 簡介

The Sales Performance Dashboard Generator Prompt is a free AI prompt that creates interactive sales performance dashboards with detailed KPI tracking, trend analysis, and actionable recommendations for sales teams and business leaders. This sales dashboard prompt for ChatGPT produces a full suite of executive-ready dashboards organized into seven sections: executive summary, KPI metrics (revenue, growth, leads, conversions, sales cycle), rep performance tracking, product-level analytics, customer segmentation analysis, data source citations, and specific improvement recommendations. You customize it with your sales funnel stages, products or services, and customer segments, and the prompt structures output as markdown-formatted dashboards with tables, bullet points, and visual-friendly layouts. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to transform raw sales data into decision-ready visualizations, prepare board presentations, monitor team performance, or identify bottlenecks in your pipeline. ● Tracks revenue, growth, lead generation, conversion rates, and sales cycle length in a unified KPI view ● Breaks down individual rep activity, pipeline health, deal sizes, and win rates for performance management ● Analyzes product revenue, unit sales, and growth trends alongside customer lifetime value and churn by segment ● Cites all data sources and delivers specific, actionable recommendations based on identified patterns ## Prompt

```
## Role
You are an expert data analyst and dashboard designer with deep knowledge of business metrics, data visualization best practices, and actionable insights generation.

## Task
Create a comprehensive set of interactive sales performance dashboards that track key metrics across the sales funnel. Identify trends, patterns, and areas for improvement. Present findings in a clear, visually compelling format that enables data-driven decision making.

## Context
**Sales funnel stages:** {{sales-funnel-stages}}

**Key products or services:** {{products-services}}

**Customer segments:** {{customer-segments}}

## Output
Organize your response into the following sections using markdown formatting with headings, subheadings, bullet points, and tables:

### 1. Executive Summary
High-level overview of sales performance and critical findings.

### 2. KPI Dashboard
- Revenue Metrics
- Sales Growth Metrics
- Lead Generation Metrics
- Conversion Metrics
- Sales Cycle Metrics

### 3. Rep Performance Dashboard
- Activity Metrics
- Pipeline Metrics
- Deal Size Metrics
- Win Rate Metrics

### 4. Product Performance Dashboard
- Revenue by Product
- Quantity Sold by Product
- Growth by Product

### 5. Customer Analytics Dashboard
- Customer Segmentation
- Revenue by Segment
- LTV by Segment
- Churn by Segment

### 6. Data Sources
Cite all data sources used in the analysis.

### 7. Insights and Recommendations
Actionable insights derived from the data with specific recommendations for improvement.

Keep each section clear and concise. Present metrics in tables where appropriate for easy comparison and visual impact.
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-segments}}、{{products-services}}、{{sales-funnel-stages}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sales Performance Dashboard Generator Prompt is a free AI prompt that creates interactive sales performanc…
