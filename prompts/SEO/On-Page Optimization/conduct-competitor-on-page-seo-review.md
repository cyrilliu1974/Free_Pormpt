# Competitor On-Page SEO Review Prompt

## 簡介

The Competitor On-Page SEO Review Prompt is a free AI prompt that analyzes a competitor's website and produces actionable on-page SEO improvement strategies for your own site. This competitor on-page SEO review prompt for ChatGPT examines eight critical elements: meta tags (title, description, headers), content quality and keyword usage, internal linking and site structure, URL architecture, page speed indicators, mobile responsiveness signals, and image optimization. The output is a structured markdown table with three columns that directly compares your competitor's approach to each element and delivers specific, implementable recommendations tailored to your business context. Marketers, SEO specialists, and site owners use it to quickly benchmark their site against competitors, identify gaps in their optimization strategy, and build a roadmap for improving search visibility without manually auditing dozens of data points. ● Compares meta tags, content strategy, site architecture, internal linking, URL structure, page speed, mobile optimization, and image SEO between your site and a competitor ● Outputs a clean markdown table format that separates competitor tactics, your current state, and specific next steps ● Accepts three variables: competitor URL, your URL, and business context to ensure recommendations fit your industry and goals ● Helps prioritize SEO improvements by revealing which on-page elements your competitors handle better and where you already lead ## Prompt

```
## Role
You are an expert SEO analyst conducting a comprehensive on-page SEO review.

## Task
Analyze a competitor's website to identify opportunities for improving your own site's SEO performance. Examine key on-page elements including meta tags (title, description, headers), content quality and keyword usage, internal linking and site structure, URL architecture, page speed indicators, mobile responsiveness signals, and image optimization. Compare each element between the competitor's site and your own, then develop specific, actionable recommendations.

## Context
Competitor website: {{competitor-url}}
Your website: {{your-url}}
Business context: {{business-context}}

## Output
Present your analysis as a markdown table with three columns:

| SEO Element | Competitor's Approach | Recommendations |
|-------------|----------------------|------------------|

Cover at minimum: meta tags, content strategy, site structure, internal linking, URL structure, page speed, mobile optimization, and image SEO. For each row, provide a detailed comparison and clear, implementable strategies tailored to the business context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{competitor-url}}、{{your-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Competitor On-Page SEO Review Prompt is a free AI prompt that analyzes a competitor's website and produces…
