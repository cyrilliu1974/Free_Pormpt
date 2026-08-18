# Duplicate Content SEO Audit and Canonical Tag Strategy

## 簡介

The Duplicate Content SEO Audit and Canonical Tag Strategy is a free AI prompt that builds a systematic plan to eliminate duplicate content issues and optimize site architecture for SEO professionals and website owners. This duplicate content SEO prompt for ChatGPT produces a detailed four-phase roadmap that walks you through crawling your site, categorizing duplication issues (www vs non-www, HTTP vs HTTPS, URL parameters, pagination), implementing canonical tags, restructuring internal links into a logical hierarchy, and setting up ongoing monitoring in Google Search Console. It runs on ChatGPT, Claude, Gemini, and Grok, accepting your website URL and specific SEO parameters to tailor the output. Real use cases include resolving indexing problems after a site migration, cleaning up e-commerce product variant URLs, and fixing pagination-related duplication. This prompt is ideal for technical SEO specialists managing large sites, digital marketers tasked with improving organic search performance, and web developers who need a clear action plan to consolidate link equity and prevent search engine penalties. ● Crawls and categorizes duplicate content by type, then prioritizes fixes based on SEO impact ● Provides step-by-step canonical tag implementation and XML sitemap update instructions ● Designs a four-tier internal linking hierarchy to keep all pages within optimal click depth ● Includes weekly and monthly tracking routines to monitor crawl errors, rankings, and new duplication ## Prompt

```
## Role
You are an expert SEO strategist and website architect specializing in site structure optimization and duplicate content elimination.

## Task
Develop a comprehensive plan to identify and resolve duplicate content issues on the user's website through canonical tag implementation and internal linking restructuring. Present the plan as a detailed roadmap diagram.

## Context
{{website-url}}

{{seo-parameters}}

## Output
Present the plan as a four-phase roadmap:

### 1. Duplicate Content Audit
- Crawl the entire website using the specified crawler tool
- Analyze crawl results to detect duplicate or near-duplicate pages based on the similarity threshold
- Categorize duplicate content issues by type (e.g., www vs non-www, HTTP vs HTTPS, parameter variations, paginated content, printer-friendly versions)
- Prioritize resolution starting with the top priority category

### 2. Canonical Tag Implementation
- For each set of duplicate pages, determine the canonical URL to retain
- Implement canonical tags on all duplicate pages pointing to the canonical URL
- Update the XML sitemap to include only canonical URLs
- Submit the updated sitemap to Google Search Console

### 3. Internal Link Optimization
- Identify main navigation pages
- Build a hierarchical internal linking structure:
  - **Top level:** Navigation pages
  - **2nd level:** Category pages
  - **3rd level:** Subcategory pages
  - **4th level:** Product/Article pages
- Update all internal links to point to canonical URLs
- Ensure no canonical URL exceeds the maximum click depth from the home page

### 4. Tracking and Monitoring
- Monitor crawl errors and 404 pages in Search Console weekly
- Track improvements in organic search impressions, clicks, and rankings
- Re-crawl the website monthly to detect new duplicate content
- Continuously optimize canonical URLs and internal linking based on findings

Provide clear, actionable steps without technical jargon.
```

## 用法 / Usage
- 必填變數 / Variables: {{seo-parameters}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Duplicate Content SEO Audit and Canonical Tag Strategy is a free AI prompt that builds a systematic plan t…
