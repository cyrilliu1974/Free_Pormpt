# Site Architecture Analysis for SEO

## 簡介

The Site Architecture Analysis for SEO is a free AI prompt that conducts a comprehensive technical audit of website structure, crawlability, and on-page elements for businesses and SEO professionals. This site architecture prompt for ChatGPT works by systematically evaluating crawl structure, URL design, internal linking, navigation, mobile responsiveness, duplicate content, broken links, canonical tags, XML sitemaps, robots.txt, and header tag hierarchy. You provide your website URL, business context, and target keywords, and the prompt delivers 15-25 prioritized findings in a three-column markdown table mapping each issue to a specific URL and an actionable recommendation. It runs on ChatGPT, Claude, and Gemini, making it adaptable to your preferred text model. Reach for this prompt when you need a structured technical SEO audit that goes beyond surface-level checks and ties every issue to implementation guidance. ● Evaluates site hierarchy, URL structure, internal linking patterns, and navigation design for crawlability ● Identifies duplicate content, broken links, orphaned pages, and mobile responsiveness issues ● Audits canonical tags, XML sitemaps, robots.txt, header tags, meta descriptions, and title tags ● Outputs findings as a prioritized markdown table with URL, issue description, SEO impact, and actionable recommendation ## Prompt

```
## Role
You are an expert SEO analyst conducting a comprehensive technical site architecture audit.

## Task
Perform a systematic technical SEO audit covering:

- **Crawl & Structure**: Site hierarchy, URL structure, internal linking patterns
- **Technical Performance**: Navigation design, page load times, mobile responsiveness
- **Content Issues**: Duplicate content, broken links, orphaned pages
- **SEO Implementation**: Canonical tags, XML sitemaps, robots.txt configuration
- **On-Page Elements**: Header tag hierarchy, meta descriptions, title tag optimization

Work methodically through each area, identifying specific issues tied to URLs where possible.

## Context
**Website**: {{website-url}}  
**Business Context**: {{business-context}}  
**Target Keywords**: {{primary-keywords}}

## Output
Deliver your findings as a markdown table with three columns:

| URL | Issue | Recommendation |
|-----|-------|----------------|

Each row must contain:
- **URL**: Specific page affected (or "Site-wide" for global issues)
- **Issue**: Clear, concise description of the problem and its SEO impact
- **Recommendation**: Actionable solution with implementation guidance

Prioritize issues by SEO impact. Include 15-25 findings covering all audit areas above.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{primary-keywords}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Site Architecture Analysis for SEO is a free AI prompt that conducts a comprehensive technical audit of we…
