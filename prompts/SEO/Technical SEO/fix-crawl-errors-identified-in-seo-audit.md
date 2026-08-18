# SEO Crawl Error Fix and Technical Audit Action Plan

## 簡介

The SEO Crawl Error Fix and Technical Audit Action Plan is a free AI prompt that transforms SEO audit reports into prioritized, actionable remediation plans for webmasters and technical SEO specialists. This technical SEO prompt for ChatGPT takes your audit findings and website context - including your CMS, target keywords, and current rankings - and outputs a structured markdown table that categorizes every crawl error, indexability problem, and technical issue by priority (High, Medium, Low) alongside clear, implementable fixes. It runs on ChatGPT, Claude, Gemini, and Grok, delivering solutions tailored to your specific content management system and technical environment. Whether you're facing broken links, duplicate content, slow page speeds, or mobile usability problems, the prompt applies current SEO best practices to each identified issue. Reach for this prompt when you need to convert a long list of audit findings into a strategic roadmap that focuses effort where it matters most - on the critical issues blocking crawlers or harming core ranking factors. ● Categorizes every issue by impact level - High for critical indexability and crawlability problems, Medium for ranking and UX concerns, Low for minor optimizations. ● Provides CMS-specific fixes so you can implement solutions in WordPress, Shopify, custom builds, or any platform you specify. ● Outputs a clean markdown table format that's easy to share with developers, clients, or stakeholders. ● Aligns every recommendation with current SEO standards, ensuring fixes improve both search visibility and user experience. ## Prompt

```
## Role
You are an expert SEO analyst specializing in technical SEO audits and remediation.

## Task
Analyze the provided SEO audit report and create a prioritized action plan. Review the issues identified, assess their impact on search engine rankings and user experience, then provide clear, actionable solutions aligned with current SEO best practices.

## Context
**SEO Audit Report:** {{seo-audit-report}}

**Website & Technical Details:** {{website-context}}
(Include: website URL, content management system, primary target keywords, current search engine rankings)

## Output
Deliver your analysis as a markdown table with three columns:

| Issue | Priority | Fix |
|-------|----------|-----|

**Priority levels:**
- **High:** Critical impact on indexability, crawlability, or core ranking factors
- **Medium:** Moderate impact on rankings or user experience
- **Low:** Minor optimization opportunities

For each issue, provide specific, implementable solutions tailored to the CMS and technical environment described.
```

## 用法 / Usage
- 必填變數 / Variables: {{seo-audit-report}}、{{website-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The SEO Crawl Error Fix and Technical Audit Action Plan is a free AI prompt that transforms SEO audit reports …
