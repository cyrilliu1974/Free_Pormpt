# Duplicate Content SEO Audit Report Generator

## 簡介

The Duplicate Content SEO Audit Report Generator is a free AI prompt that produces comprehensive technical SEO audits focused on identifying and resolving duplicate content problems across websites. This duplicate content SEO audit prompt for ChatGPT systematically crawls your site, documents every duplicate content issue, analyzes root causes like URL parameters or trailing slashes, and maps each problem to specific fixes such as canonical tags, 301 redirects, or parameter handling rules. It works on ChatGPT, Claude, and Gemini by taking your website URL, business context, and SEO focus as inputs and delivering a structured report with an executive summary, duplicate content inventory table, root cause breakdown, prioritized recommendations ranked by ranking impact, and a sequenced implementation roadmap with technical instructions. SEO professionals use it to audit client sites for search visibility issues, and in-house teams rely on it to diagnose why pages cannibalize each other in search results. ● Crawls and inventories all duplicate content instances with severity ratings and issue type classifications ● Identifies root causes grouped by pattern, including URL parameters, pagination, HTTP/HTTPS variations, and www/non-www duplication ● Maps each duplicate content issue to the correct technical solution, specifying canonical tags, 301 redirects, robots.txt rules, noindex directives, or content rewrites ● Prioritizes recommendations by potential ranking impact, factoring in search volume, business value, and current traffic loss ● Delivers a step-by-step implementation roadmap with timeline, resource requirements, and validation steps ## Prompt

```
## Role
You are an expert SEO analyst conducting a technical SEO audit focused on duplicate content issues.

## Task
Produce a comprehensive audit report that identifies duplicate content problems on {{website-url}} and provides actionable solutions prioritized by impact on search rankings.

## Context
Business type: {{business-context}}
Target audience and primary keywords: {{seo-focus}}

## Audit Process
1. **Crawl & Identify**: Document all pages with duplicate content across the site
2. **Analyze Impact**: Assess the severity of each duplication issue and its effect on search visibility
3. **Root Cause Analysis**: Determine why duplication occurs (URL parameters, pagination, thin product descriptions, session IDs, www vs non-www, HTTP vs HTTPS, trailing slashes, etc.)
4. **Solution Mapping**: For each issue, specify the fix—canonical tags, 301 redirects, parameter handling in robots.txt or Search Console, noindex directives, or content rewriting
5. **Prioritization**: Rank fixes by potential ranking impact (consider search volume, business value, and current traffic loss)
6. **Implementation Roadmap**: Provide a sequenced, step-by-step plan with technical instructions and resource requirements

## Output
Structure the report with:
- **Executive Summary** (key findings and estimated impact)
- **Duplicate Content Inventory** (table with URL, issue type, and severity)
- **Root Cause Breakdown** (grouped by pattern)
- **Prioritized Recommendations** (numbered list with rationale)
- **Implementation Plan** (timeline, owners, validation steps)

Use clear headings, subheadings, bullet points, and tables. Write concisely with each recommendation logically building on the diagnostic findings that precede it.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{seo-focus}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Skill_Structure_And_Refinement_Discipline
- 適用 / Use when: The Duplicate Content SEO Audit Report Generator is a free AI prompt that produces comprehensive technical SEO…
