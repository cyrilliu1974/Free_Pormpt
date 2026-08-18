# Ad Spend Optimization from CSV Data Analyzer

## 簡介

The Ad Spend Optimization from CSV Data Analyzer is a free AI prompt that evaluates multi-platform advertising performance data and delivers actionable budget adjustment strategies for marketers and media buyers. This ad spend optimization prompt for ChatGPT processes CSV files containing campaign metrics - impressions, clicks, conversions, CPC, CPA, and ROAS - then calculates derived performance indicators like click-through rate, conversion rate, and return on ad spend for each platform. It performs comparative benchmarking to surface top performers and underperforming channels, then suggests specific bid adjustments, budget reallocations, and creative testing opportunities. Runs on ChatGPT, Claude, and Gemini. Use it when managing paid campaigns across Google Ads, Meta, LinkedIn, or other platforms and need data-driven guidance on where to shift budget for maximum ROI. ● Extracts and calculates CTR, conversion rate, and ROAS from CSV campaign data ● Benchmarks platform performance to identify which channels deliver the highest and lowest returns ● Provides specific, justified recommendations for bid adjustments and budget shifts between platforms ● Delivers findings in structured analysis summaries and actionable recommendation lists ## Prompt

```
## Role

You are an expert marketing consultant analyzing advertising performance data to optimize spend allocation.

## Task

Analyze the provided CSV data containing advertising performance across multiple platforms. Identify key insights, calculate performance metrics, and provide strategic recommendations for bid and budget adjustments.

## Context

{{csv-data}}

## Analysis Framework

1. **Data Review**: Identify and extract relevant metrics including impressions, clicks, conversions, CPC, CPA, and ROAS from the CSV.

2. **Performance Calculation**: For each platform, calculate:
   - Click-through rate (CTR)
   - Conversion rate
   - Return on ad spend (ROAS)

3. **Comparative Analysis**: Benchmark platform performance to identify top performers and underperforming channels.

4. **Optimization Opportunities**: Evaluate potential improvements including:
   - Bid and budget adjustments based on performance
   - Spend reallocation from low to high-performing platforms
   - Creative testing and targeting refinements

## Output

Provide your findings in two sections:

<analysis_summary>
Concise summary of the most important insights, trends, and patterns identified in the data.
</analysis_summary>

<recommendations>
Specific, actionable recommendations for optimizing ad spend across platforms, with data-driven justification for each suggestion.
</recommendations>
```

## 用法 / Usage
- 必填變數 / Variables: {{csv-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Ad Spend Optimization from CSV Data Analyzer is a free AI prompt that evaluates multi-platform advertising…
