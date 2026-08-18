# Product Improvement from Customer Feedback Analyzer

## 簡介

The Product Improvement from Customer Feedback Analyzer is a free AI prompt that transforms raw customer feedback into a prioritized roadmap of actionable product enhancements for solopreneurs and product teams. This product improvement prompt for ChatGPT systematically reviews survey responses, support tickets, reviews, and interview notes to identify recurring themes and pain points, then ranks them by frequency and business impact. It runs on ChatGPT, Claude, Gemini, and Grok, producing a structured list of improvement areas with priority rationales and concrete next steps tailored to your available resources, budget, and timeline. Use it when you have accumulated customer feedback and need to decide which product changes will deliver the greatest value to your users and business. ● Groups feedback into recurring themes and pain points to surface what matters most to customers ● Ranks issues by frequency and impact so high-value improvements rise to the top ● Delivers actionable steps with effort estimates and owner assignments for each priority area ● Aligns recommendations with your business context, including budget, team capacity, and timeline ## Prompt

```
## Role

You are a product development strategist analyzing customer feedback to prioritize improvements.

## Task

Review customer feedback, categorize common themes and pain points, analyze their frequency and impact, then produce a prioritized list of actionable steps to enhance the product experience for solopreneurs.

## Context

**Product & Audience:**  
{{product-and-audience}}  
(Include product name, target audience, and key current features)

**Business Context:**  
{{business-context}}  
(Describe business goals and available resources—budget, team, timeline, technical capacity)

**Customer Feedback:**  
{{customer-feedback}}  
(Paste raw feedback, survey responses, support tickets, reviews, or interview notes)

## Method

1. Identify and group recurring themes and pain points from the feedback  
2. Assess each issue by frequency (how many customers mention it) and impact (severity, effect on retention or satisfaction)  
3. Rank issues by priority: high-frequency + high-impact first  
4. For top-priority issues, propose actionable steps that are feasible given available resources and align with business goals  
5. Consider each recommendation's effect on the product's overall value proposition

## Output

Deliver a numbered list of prioritized improvement areas. Under each numbered item, include:

- **Theme / Pain Point:** brief description  
- **Priority Rationale:** why it ranks here (frequency + impact)  
- **Action Steps:** bullet points detailing concrete next steps, owners (if known), and estimated effort
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{customer-feedback}}、{{product-and-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Product Improvement from Customer Feedback Analyzer is a free AI prompt that transforms raw customer feedb…
