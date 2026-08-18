# Supply Chain Logistics Plan Builder for ChatGPT

## 簡介

The Supply Chain Logistics Plan Builder is a free AI prompt that creates end-to-end logistics optimization plans for businesses managing products, suppliers, and delivery operations. This supply chain logistics prompt for ChatGPT takes your business context - product types, supplier relationships, current transportation methods, and delivery locations - and outputs a structured four-column plan covering supplier management, inventory control, transportation routing, and last-mile delivery. It runs on ChatGPT, Claude, and Gemini, acting as an expert logistics coordinator to identify cost reduction opportunities, lead-time improvements, and customer satisfaction enhancements across every stage of your supply chain. Use it when you need to audit existing logistics, onboard new suppliers, redesign distribution networks, or prepare operational plans for stakeholders. ● Outputs a four-column markdown table (Suppliers | Inventory | Transportation | Delivery) with specific strategies for each stage ● Includes actionable implementation steps, cost-reduction methods, and quality measures for every component ● Covers supplier relationship management, inventory control systems, transportation mode selection, and last-mile delivery processes ● Tailors recommendations to your business type, products handled, current methods, and delivery locations ## Prompt

```
## Role
You are an expert logistics coordinator specializing in supply chain optimization.

## Task
Create a comprehensive logistics plan that minimizes costs, reduces lead times, and improves customer satisfaction across the entire supply chain.

## Context
Business and supply chain details:
{{supply-chain-context}}

(Include: business type, products/services handled, main suppliers, transportation methods currently used, and primary delivery locations)

## Output
Present your logistics plan as a markdown table with four columns:

| Suppliers | Inventory | Transportation | Delivery |
|-----------|-----------|----------------|----------|

Each column must contain:
- Specific optimization strategies for that supply chain component
- Actionable steps to implement improvements
- Methods to reduce costs and lead times
- Quality and reliability measures

Cover supplier relationship management, inventory control systems, transportation routing and mode selection, and last-mile delivery processes.
```

## 用法 / Usage
- 必填變數 / Variables: {{supply-chain-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Fact_Boundary_Audit
- 適用 / Use when: The Supply Chain Logistics Plan Builder is a free AI prompt that creates end-to-end logistics optimization pla…
