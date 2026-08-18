# XML Sitemap Generator for E-commerce SEO

## 簡介

The XML Sitemap Generator for E-commerce SEO is a free AI prompt that creates structured sitemap plans to improve search engine crawling and indexing for online stores. This e-commerce SEO prompt for ChatGPT walks you through building a complete sitemap table that identifies all important URLs across your store - homepage, category pages, product pages, and static content - then assigns each a last modified date and appropriate change frequency value (hourly, daily, weekly, monthly, yearly, or never). The output is a markdown table with 10–20 representative URLs following XML sitemap protocol standards, making it easy to implement or hand off to your development team. It runs on ChatGPT, Claude, Gemini, and Grok, and is ideal for e-commerce managers, SEO specialists, and web developers who need to organize crawl priorities around traffic and conversion goals. ● Maps all major page types - homepage, categories, products, static pages - into a single crawl-optimized table. ● Assigns realistic change frequency values based on how often each section is updated, helping search engines allocate crawl budget efficiently. ● Outputs in markdown table format with URL, last modified date (YYYY-MM-DD), and frequency columns, ready for XML conversion. ● Adheres to official XML sitemap protocol standards, ensuring compatibility with Google Search Console, Bing Webmaster Tools, and other indexing platforms. ## Prompt

```
## Role
You are an SEO specialist creating an XML sitemap to improve search engine crawling and indexing.

## Task
Generate a comprehensive sitemap plan for an e-commerce website that identifies:
- All important URLs (homepage, category pages, product pages, static pages)
- Last modified dates for each page type
- Appropriate change frequency values (always, hourly, daily, weekly, monthly, yearly, never)

Adhere to XML sitemap protocol standards and prioritize pages that drive traffic and conversions.

## Context
{{website-details}}

*Include: site name, primary product categories, structure (depth, number of products, key sections), and how often content is typically updated.*

## Output
Deliver a markdown table with three columns:

| URL | Last Modified Date | Change Frequency |
|-----|-------------------|------------------|

Include 10–20 representative URLs covering all major page types. Use YYYY-MM-DD format for dates and standard sitemap frequency values.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The XML Sitemap Generator for E-commerce SEO is a free AI prompt that creates structured sitemap plans to impr…
