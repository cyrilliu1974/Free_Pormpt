# Mobile Sitemap Configuration for SEO

## 簡介

The Mobile Sitemap Configuration for SEO is a free AI prompt that builds XML-compliant mobile sitemap tables for SEO specialists and webmasters seeking better search engine indexing. This mobile sitemap prompt for ChatGPT analyzes your website structure, identifies mobile-friendly pages, and outputs a three-column markdown table (URL, Last Modified Date, Change Frequency) along with deployment instructions tailored to your target search engines. It runs on ChatGPT, Claude, Gemini, and Grok, accepting four key variables: your website URL, content type, typical update frequency, and which search engines you want to target (Google, Bing, Yandex, or others). The prompt follows XML sitemap protocol standards and delivers actionable guidance for submitting the sitemap to search consoles. Reach for this prompt when launching a mobile site, auditing existing sitemaps, or ensuring your mobile pages are properly discoverable by search crawlers. ● Produces a structured three-column table mapping mobile URLs, last modified dates, and recommended change frequencies based on content patterns ● Ensures compliance with XML sitemap protocol standards recognized by major search engines ● Includes step-by-step implementation guidance for deploying the sitemap file and submitting it to Google Search Console, Bing Webmaster Tools, and other platforms ● Adapts change frequency recommendations to your content type and actual update cadence, avoiding generic one-size-fits-all intervals ## Prompt

```
## Role
You are an SEO specialist configuring mobile sitemaps for optimal search engine visibility and rankings.

## Task
Create a mobile sitemap table for the provided website following XML sitemap protocol standards. Deliver a structured table with three columns: URL, Last Modified Date, and Change Frequency.

## Process
1. Analyze the website structure and identify all mobile-friendly pages
2. Determine appropriate update frequency for each page based on content type and update patterns
3. Populate the table with accurate information for each mobile page
4. Ensure compliance with XML sitemap protocol standards
5. Include implementation guidance for submitting to search engines

## Context
- Website: {{website-url}}
- Primary content type: {{content-type}}
- Typical update frequency: {{update-frequency}}
- Target search engines: {{target-search-engines}}

## Output
Provide your response as a markdown table with three columns: URL | Last Modified Date | Change Frequency. Follow with brief implementation instructions for deploying the sitemap and submitting it to the specified search engines.
```

## 用法 / Usage
- 必填變數 / Variables: {{content-type}}、{{target-search-engines}}、{{update-frequency}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mobile Sitemap Configuration for SEO is a free AI prompt that builds XML-compliant mobile sitemap tables f…
