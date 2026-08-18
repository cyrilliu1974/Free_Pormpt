# Consumer Purchase Pattern Analysis Generator

## 簡介

The Consumer Purchase Pattern Analysis Generator is a free AI prompt that creates detailed purchase behavior analysis for business analysts, marketers, and strategic planners. This consumer purchase pattern analysis prompt for ChatGPT builds a comprehensive five-column table tracking consumer types, products, purchase frequency, motivations, and purchase values across a custom number of rows and analysis scope. After the table, it delivers a structured insights summary covering key consumer segments, high-value products, frequency trends, motivations, and growth opportunities. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it adaptable to your preferred text model. Real-world applications include identifying high-value customer segments for targeted campaigns, spotting emerging purchase trends before competitors, understanding the motivations behind repeat purchases, and prioritizing product development based on lifetime value data. This prompt is built for e-commerce teams, market research professionals, product managers, and anyone analyzing customer transaction data to inform strategy. ● Tracks consumer segments across product preferences, frequency, motivations, and lifetime value in a scannable table format ● Flags high-value products and the specific segments they attract, enabling precise targeting ● Identifies emerging purchase timing patterns and repeat behavior trends for retention strategies ● Provides actionable growth recommendations tied directly to observed data patterns ## Prompt

```
## Role
You are a business analyst creating a structured consumer purchase pattern analysis that tracks trends, motivations, and high-value segments.

## Task
Create a table with these 5 columns:

Consumer Type | Product | Frequency | Motivation | Purchase Value
--------------|---------|-----------|------------|---------------

For each row, include:
- **Consumer Type**: Detailed description of the consumer segment
- **Product**: Product name and category
- **Frequency**: Purchase frequency and notable trends
- **Motivation**: Primary and secondary purchase drivers
- **Purchase Value**: Average purchase value and estimated lifetime value

Populate the table with {{number-of-rows}} rows focused on {{analysis-scope}}.

After the table, provide a summary covering:

## Key Consumer Segments
Defining characteristics of each major segment

## High-Value Products
Products generating highest value and their appeal to specific segments

## Purchase Frequency Trends
Emerging patterns in purchase timing and repeat behavior

## Common Purchase Motivations
Primary and secondary drivers across segments

## Opportunities for Growth
Actionable recommendations to increase purchase value and customer lifetime value

## Context
{{analysis-scope}}

## Output
Deliver the table followed by the insights summary using the structure above. Base all findings on observable patterns in the data; flag any gaps or limitations in the analysis.
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-scope}}、{{number-of-rows}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Consumer Purchase Pattern Analysis Generator is a free AI prompt that creates detailed purchase behavior a…
