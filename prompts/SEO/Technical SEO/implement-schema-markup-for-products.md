# Product Schema Markup Implementation Guide

## 簡介

The Product Schema Markup Implementation Guide is a free AI prompt that generates tailored, step-by-step instructions for adding structured data to e-commerce product pages. This product schema markup prompt for ChatGPT produces a complete implementation plan including annotated JSON-LD code templates, platform-specific integration instructions, property mapping guidance, and validation steps using Google's Rich Results Test. It adapts technical language and explanations to match your stated expertise level, whether you're a beginner adding your first schema or an experienced developer working across multiple platforms. The prompt works on ChatGPT, Claude, and Gemini, and covers essential Product schema properties such as name, price, availability, description, reviews, and ratings. Real use cases include optimizing Shopify stores for rich snippets, implementing structured data on custom WooCommerce builds, and ensuring BigCommerce product pages meet Google's guidelines for enhanced search result displays. ● Provides complete JSON-LD code templates with annotations explaining each required and recommended Product schema property ● Includes platform-specific integration steps for major e-commerce systems like Shopify, WooCommerce, BigCommerce, and custom builds ● Delivers validation instructions using Google's Rich Results Test and highlights common implementation errors to avoid ● Adapts technical explanations and code complexity based on stated expertise level, from beginner to advanced developer ## Prompt

```
## Role
You are an expert SEO specialist implementing Schema Markup for e-commerce products.

## Task
Provide a comprehensive, step-by-step guide to implement Product schema in JSON-LD format that improves search engine visibility and adheres to Google's structured data guidelines.

## Context
Website: {{website-url}}
E-commerce platform: {{ecommerce-platform}}
User technical level: {{technical-expertise-level}}

The implementation must cover:
- Product name, price, and availability
- Product description
- Customer reviews and ratings
- Proper placement in page HTML
- Validation steps
- Platform-specific integration notes

## Output
Deliver a numbered step-by-step implementation guide that includes:

1. **Setup overview** - where to place the schema code on product pages
2. **Complete JSON-LD code template** - annotated example showing all required and recommended Product schema properties
3. **Property mapping** - how to populate each field with actual product data
4. **Platform integration** - specific instructions for the stated e-commerce platform
5. **Testing** - how to validate using Google's Rich Results Test
6. **Common pitfalls** - errors to avoid based on the user's technical level

Provide working code snippets formatted in markdown code blocks. Explain technical concepts in language appropriate to the stated expertise level.
```

## 用法 / Usage
- 必填變數 / Variables: {{ecommerce-platform}}、{{technical-expertise-level}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Product Schema Markup Implementation Guide is a free AI prompt that generates tailored, step-by-step instr…
