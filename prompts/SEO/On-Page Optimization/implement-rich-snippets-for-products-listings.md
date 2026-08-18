# Rich Snippets Implementation Guide for Product Listings

## 簡介

The Rich Snippets Implementation Guide for Product Listings is a free AI prompt that creates detailed, actionable plans for adding structured data markup to e-commerce product pages. This structured data prompt for ChatGPT analyzes your current product listing architecture, identifies the correct schema.org vocabulary, and outputs JSON-LD code templates for marking up product name, price, availability, and review data. It runs on ChatGPT, Claude, Gemini, and Grok, delivering numbered implementation steps that include validation procedures using Google's Rich Results Test tool, common error patterns to avoid, and metrics for tracking SERP performance improvements. Use this prompt when you need to enhance product visibility in search results by displaying star ratings, pricing, and stock status directly in the SERPs. ● Produces schema.org Product markup templates in JSON-LD format following current search engine guidelines ● Includes validation steps with Google's Rich Results Test and troubleshooting for typical markup errors ● Covers core product properties including offers, aggregateRating, availability, and brand ● Provides metrics frameworks for measuring Rich Snippet appearance rates and CTR impact in search results ## Prompt

```
## Role
You are an expert SEO specialist implementing Rich Snippets structured data markup for e-commerce product listings.

## Task
Create a comprehensive step-by-step guide to implement schema.org product markup that improves search visibility and click-through rates. Cover:

1. Analyzing current product listing structure
2. Identifying appropriate schema.org vocabulary for products
3. Creating a structured data template for product listings
4. Implementing markup for product name, price, availability, and reviews
5. Testing implementation using Google's Rich Results Test tool
6. Monitoring SERP impact and making adjustments

## Context
{{platform-and-products}}

{{technical-setup}}

## Output
Deliver a numbered list with clear subsections for each implementation step. Include:

- Specific schema.org properties and types to use
- Code examples in JSON-LD format
- Validation steps and common errors to avoid
- Metrics to track for measuring impact
- Troubleshooting guidance for typical issues

Ensure all markup follows current schema.org standards and search engine best practices.
```

## 用法 / Usage
- 必填變數 / Variables: {{platform-and-products}}、{{technical-setup}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Rich Snippets Implementation Guide for Product Listings is a free AI prompt that creates detailed, actiona…
