# Sales Forecasting Prompt for ChatGPT

## 簡介

The Sales Forecasting Prompt for ChatGPT is a free AI prompt that helps sales analysts and business leaders project future revenue through structured data analysis. This sales forecasting prompt for ChatGPT guides the model to examine historical sales patterns, identify seasonal variations, evaluate current market conditions, and incorporate customer behavior insights into revenue projections. It runs on ChatGPT, Claude, and Gemini, producing a markdown table that breaks down each time period with projected sales figures, the key factors influencing performance, and specific strategies to capitalize on opportunities or mitigate risks. Sales teams use it to move from spreadsheet guesswork to narrative-driven forecasts that explain the "why" behind the numbers. Reach for this prompt when you need to translate raw sales history and market intelligence into a clear, defensible forecast that stakeholders can act on. ● Structures forecasts as a four-column table: Time Period, Projected Sales, Influencing Factors, and Strategies. ● Integrates historical trends, seasonality, market dynamics, and customer segment behavior into each projection. ● Generates actionable strategies row-by-row to maximize performance and address identified risks. ● Accepts custom variables for product/service, forecasting period, and business intelligence context. ## Prompt

```
## Role
You are an expert sales analyst conducting accurate sales forecasting through structured data analysis.

## Task
Analyze historical data, market trends, and customer insights to project future sales. Examine past sales patterns, identify seasonality, evaluate current market conditions and emerging trends, and incorporate customer behavior insights to refine projections. Develop strategies to capitalize on opportunities and mitigate risks.

## Context
**Product/Service:** {{product-service}}

**Forecasting Period:** {{time-period}}

**Business Intelligence:**
{{business-intelligence}}

*Include: key market factors, primary customer segments, and a brief summary of historical sales data (trends, growth patterns, seasonal variations).*

## Output
Present your forecast as a markdown table with 4 columns:

| Time Period | Projected Sales | Influencing Factors | Strategies |
|-------------|-----------------|---------------------|------------|

Each row should provide a comprehensive overview of the sales forecast for that time period, covering projected figures, the key factors driving or constraining sales, and actionable strategies to maximize performance.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-intelligence}}、{{product-service}}、{{time-period}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Minimalist_Entrepreneurship_Execution · First_Customer_Acquisition_Engine
- 適用 / Use when: The Sales Forecasting Prompt for ChatGPT is a free AI prompt that helps sales analysts and business leaders pr…
