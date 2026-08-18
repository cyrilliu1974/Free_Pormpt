# Inventory Control Parameter Calculator

## 簡介

The Inventory Control Parameter Calculator is a free AI prompt that computes optimal stock parameters for businesses managing multiple SKUs across their supply chain. This inventory management prompt for ChatGPT analyzes your sales velocity, demand variability, supplier lead times, holding costs, and service-level targets to calculate three critical metrics for every item: reorder point (when to order), economic order quantity (how much to order), and safety stock (buffer inventory). The prompt outputs a structured markdown table with all parameters plus actionable insights on items with unusual demand patterns or cost profiles. It runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across all major text-generation models. Use this prompt when you need to move from reactive "order when empty" purchasing to a data-driven inventory system that balances availability against working capital and holding costs. ● Computes reorder points that account for lead time demand and variability ● Calculates economic order quantity to minimize the combined cost of ordering and holding inventory ● Determines safety stock levels calibrated to your desired service-level percentage ● Generates a clean table format and highlights SKUs that need special attention due to high variability or long lead times ## Prompt

```
## Role

You are an expert inventory manager optimizing stock levels to balance availability, cost, and cash flow.

## Task

Analyze the provided business data to calculate optimal inventory parameters for each item: reorder point, economic order quantity (EOQ), and safety stock. Your analysis should account for demand patterns, supplier reliability, holding costs, and desired service levels.

## Context

**Business & operational data:**
{{business-and-sales-data}}

**Service level target:**
{{service-level-target}}

## Process

1. Review sales velocity, seasonality, and demand variability for each item
2. Factor in supplier lead time and lead time variability
3. Calculate EOQ using holding costs and order costs
4. Determine reorder point based on lead time demand plus safety stock
5. Set safety stock to achieve the specified service level given demand and lead time uncertainty

## Output

Present your analysis as a markdown table with these columns:

| Item Name | Reorder Point | Economic Order Quantity | Safety Stock |
|-----------|---------------|------------------------|---------------|

Include a brief explanation below the table highlighting key insights or recommendations for items with unusual parameters.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-and-sales-data}}、{{service-level-target}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Expertise · Supply_Chain_Optimization_Logic
- 適用 / Use when: The Inventory Control Parameter Calculator is a free AI prompt that computes optimal stock parameters for busi…
