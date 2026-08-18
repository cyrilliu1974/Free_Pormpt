# Supplier Research and Comparison Prompt for Procurement

## 簡介

The Supplier Research and Comparison Prompt for Procurement is a free AI prompt that helps procurement specialists identify and evaluate product material suppliers based on quality, cost, and sustainability criteria. This supplier research prompt for ChatGPT guides AI models (ChatGPT, Claude, Gemini, Grok) to act as an expert procurement specialist, researching vendors that match your product requirements, budget constraints, and location preferences. The prompt produces a structured markdown comparison table ranking suppliers alongside a detailed analysis of the top three options, complete with trade-off assessments and best-fit use cases. Real-world applications include strategic sourcing projects, vendor consolidation initiatives, RFP evaluation, and sustainability-focused procurement programs where teams need clear, actionable comparisons across multiple dimensions. This prompt is designed for procurement managers, supply chain analysts, purchasing agents, and anyone responsible for vendor selection who needs to balance competing priorities of quality, cost efficiency, and environmental impact. ● Produces markdown comparison tables with standardized columns for supplier name, material type, cost, quality rating, and sustainability score ● Delivers written analysis of the top three suppliers highlighting key strengths, weaknesses, and quality-cost-sustainability trade-offs ● Ranks suppliers by overall fit based on your specific product requirements, budget constraints, and geographic location ● Identifies best-fit scenarios and use cases for each recommended supplier to guide final sourcing decisions ## Prompt

```
## Role
You are an expert procurement specialist conducting supplier research and comparison.

## Task
Research and identify the best sources for product materials. Create a comprehensive supplier comparison evaluating quality, cost, and sustainability factors.

## Context
Product and requirements: {{product-and-requirements}}

Budget constraints: {{budget}}

Location: {{location}}

## Process
1. Research suppliers that offer the required materials
2. Evaluate each supplier on product quality, pricing structure, and sustainable practices
3. Identify trade-offs between quality, cost, and sustainability for each option
4. Rank suppliers based on overall fit

## Output
Deliver your findings as:

**Comparison Table** (markdown format with columns: Supplier | Material | Cost | Quality Rating | Sustainability Score)

**Analysis of Top 3 Options** — for each, explain:
- Key strengths and weaknesses
- Quality-cost-sustainability trade-offs
- Best-fit scenarios or use cases
```

## 用法 / Usage
- 必填變數 / Variables: {{budget}}、{{location}}、{{product-and-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Supplier Research and Comparison Prompt for Procurement is a free AI prompt that helps procurement special…
