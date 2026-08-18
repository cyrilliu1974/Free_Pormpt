# E-commerce Schema Markup Implementation Prompt

## 簡介

The E-commerce Schema Markup Implementation Prompt is a free AI prompt that generates schema.org-compliant JSON-LD structured data for product categories to improve search engine visibility and click-through rates. This schema markup prompt for ChatGPT analyzes product categories, identifies key attributes like name, description, price, availability, images, reviews, and SKUs, then produces complete JSON-LD code incorporating Product, Offer, AggregateRating, and Brand properties. It delivers platform-specific implementation instructions for WordPress, Shopify, custom CMS platforms, and other e-commerce systems, along with validation guidance using Google Rich Results Test and Schema Markup Validator. The prompt runs on ChatGPT, Claude, and Gemini to help SEO specialists and developers implement technical SEO enhancements that enable rich snippets in search results. Reach for this prompt when you need to add or update structured data for e-commerce product pages, ensure schema.org compliance, or implement technical SEO improvements that display product information directly in search engine results. ● Produces complete, working JSON-LD code snippets ready to copy and implement on your website ● Includes platform-specific instructions for WordPress, Shopify, and custom CMS environments ● Provides validation steps using Google Rich Results Test and Schema Markup Validator to confirm proper implementation ● Identifies category-specific schema opportunities and warns about common implementation mistakes ## Prompt

```
## Role
You are an SEO specialist implementing Schema Markup for e-commerce product categories to enhance search engine visibility and improve click-through rates.

## Task
Create accurate, schema.org-compliant JSON-LD structured data for the specified product categories. Deliver implementation instructions, working code snippets, and validation guidance.

## Context
Product categories and platform details:
{{product-context}}

Include: the product categories to be marked up, the website platform (WordPress, Shopify, custom CMS, etc.), and any existing schema implementation already in place.

## Process
1. Analyze the product categories and identify their key attributes (name, description, price, availability, images, reviews, SKUs, variants).
2. Develop JSON-LD schema incorporating essential properties: Product, Offer, AggregateRating, Brand, and category-specific attributes.
3. Ensure compliance with current schema.org vocabulary and search engine best practices.
4. Provide platform-specific implementation instructions with code placement guidance.
5. Include testing steps using Google Rich Results Test and Schema Markup Validator.

## Output
Deliver your response in this structure:

**Analysis**: Summary of category attributes and markup opportunities

**JSON-LD Code**: Complete, working code snippets ready to implement

**Implementation Steps**: Platform-specific instructions for adding the markup to the website

**Validation Process**: How to test the schema using official tools and interpret results

**Optimization Notes**: Any category-specific recommendations or common pitfalls to avoid
```

## 用法 / Usage
- 必填變數 / Variables: {{product-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The E-commerce Schema Markup Implementation Prompt is a free AI prompt that generates schema.org-compliant JSO…
