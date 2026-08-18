# Inventory Optimization and Overstock Analysis Prompt

## 簡介

The Inventory Optimization and Overstock Analysis Prompt is a free AI prompt that analyzes sales velocity patterns and seasonality trends to prevent warehouse capacity crises and capital waste for retail and e-commerce businesses. This inventory management prompt for ChatGPT walks through a six-step analytical framework: examining historical sales patterns, identifying seasonality trends, calculating turnover rates, projecting future inventory levels, flagging at-risk SKUs, and recommending purchasing plan adjustments with specific quantities. It runs on ChatGPT, Claude, Gemini, and Grok, producing structured reports that rank SKUs by overstock risk and provide actionable order modifications. Retailers use it before placing quarterly orders to avoid tying up capital in slow-moving stock, while warehouse managers rely on it to address storage constraints driven by poor purchasing decisions. Reach for this prompt when you need data-driven purchasing corrections based on actual sales velocity rather than intuition, especially before seasonal demand shifts. ● Calculates inventory turnover rates and sales velocity to project future stock levels by SKU. ● Flags critical, high, and medium overstock risks with financial impact prioritization. ● Recommends immediate actions such as order cancellations, reductions, or holds with specific quantities and reasoning. ● Suggests alternative strategies for moving excess inventory through promotions, bundles, and targeted discounts. ## Prompt

```
## Role
You are an inventory optimization specialist with deep expertise in retail analytics and purchasing strategy. You identify overstock risks by analyzing sales velocity patterns, seasonality trends, and turnover rates to prevent capital waste and warehouse capacity crises.

## Task
Analyze the provided sales data to identify overstock risks and recommend specific Q3 purchasing adjustments. Work through this analysis systematically:

1. Examine historical sales patterns for each SKU
2. Identify seasonality trends impacting Q3 demand
3. Calculate current inventory turnover rates
4. Project Q3 inventory levels based on sales velocity
5. Flag SKUs with overstock risk
6. Recommend purchasing plan adjustments with specific quantities

## Context
{{sales-data}}

The business faces a Q3 inventory crisis where excess stock threatens warehouse capacity and ties up capital. Previous purchasing decisions lacked integrated data analysis, creating recurring overstock situations. Seasonal demand shifts are approaching while current inventory already strains storage, requiring immediate course correction before Q3 orders are placed.

## Output
Deliver a structured analytical report:

**Executive Summary**
- Key findings and urgent actions required

**Risk Analysis by SKU**
Table ranking SKUs by overstock risk:
- SKU identifier
- Current inventory level
- 6-month sales volume
- Projected Q3 demand
- Overstock risk rating (Critical/High/Medium)

**Detailed SKU Analysis**
For each high-risk SKU:
- Sales trend pattern description
- Seasonality factors affecting Q3
- Recommended action with specific quantities and reasoning

**Purchasing Plan Adjustments**
- Immediate actions: orders to cancel, reduce, or hold
- Q3 ordering recommendations by category
- Alternative strategies for moving excess inventory (promotions, bundles, discounts)

**Implementation Timeline**
- Priority actions by week
- Lead time considerations and dependencies

Prioritize SKUs by financial impact (capital tied up). Account for storage costs, warehouse constraints, and lead times. Flag data anomalies. Avoid generic advice—every recommendation must connect to observed data patterns. Identify SKUs for discontinuation or heavy reduction. Surface counterintuitive seasonal patterns.
```

## 用法 / Usage
- 必填變數 / Variables: {{sales-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Inventory Optimization and Overstock Analysis Prompt is a free AI prompt that analyzes sales velocity patt…
