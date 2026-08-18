# Revenue Forecasting Prompt for Financial Analysis

## 簡介

The Revenue Forecasting Prompt for Financial Analysis is a free AI prompt that builds detailed revenue projections for companies using historical data, market analysis, and customizable forecasting methodologies. This revenue forecasting prompt for ChatGPT works with Claude, Gemini, and Grok to produce markdown tables showing key financial metrics across specified time periods, accompanied by assumptions, risk factors, and upside scenarios. You specify the company name, forecast period, forecasting method (trend analysis, regression, moving averages, etc.), and the key metrics you need tracked (revenue growth rate, CAGR, market share, unit economics, or custom KPIs). The prompt analyzes historical performance, identifies primary revenue drivers, incorporates external factors like competitive landscape and seasonality, then formats everything into a professional table with metric explanations and executive-ready commentary. Financial analysts, FP&A teams, and business strategists reach for it when building board presentations, investor decks, or strategic planning documents that require transparent, assumption-based revenue models. ● Produces markdown tables with time periods as columns and key metrics as rows, formatted for reports and presentations ● Incorporates user-specified forecasting methods (time-series analysis, regression models, bottom-up builds, or hybrid approaches) ● Identifies revenue drivers, external market conditions, competitive dynamics, and seasonality impacts ● Includes metric explanations, forecast assumptions, risk factors, and upside scenarios for transparent financial modeling ## Prompt

```
## Role
You are an expert financial analyst specializing in revenue forecasting and business intelligence.

## Task
Create a detailed revenue forecast for the specified company using the provided forecasting method. Analyze historical financial data, identify key revenue drivers, and incorporate relevant market trends into your projections.

## Context
**Company:** {{company-name}}
**Forecast period:** {{time-period}}
**Forecasting method:** {{forecasting-method}}
**Key metrics to include:** {{key-metrics}}

## Process
1. Analyze available historical data and identify primary revenue drivers
2. Apply the specified forecasting method to project future revenue
3. Consider external factors: market conditions, competitive landscape, industry trends, and seasonality
4. Calculate all requested key metrics for each period in the forecast
5. Identify risks and opportunities that could impact the forecast

## Output
Present your revenue forecast as a markdown table with:
- Time periods as columns (quarters, years, or months as appropriate)
- Each key metric as a row
- Clear numerical values with appropriate units (currency, percentages, growth rates)

Following the table, provide:
- **Metric Explanations:** Brief definition and significance of each key metric in the table
- **Forecast Assumptions:** Core assumptions underlying your projections
- **Risk Factors:** Potential negative impacts on the forecast
- **Upside Scenarios:** Opportunities that could drive revenue above projections

Ensure all analysis is data-driven, professionally formatted, and actionable for executive decision-making.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-name}}、{{forecasting-method}}、{{key-metrics}}、{{time-period}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Revenue Forecasting Prompt for Financial Analysis is a free AI prompt that builds detailed revenue project…
