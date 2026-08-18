# SEO Impact Analysis Report Generator

## 簡介

The SEO Impact Analysis Report Generator is a free AI prompt that produces detailed before-and-after comparisons of website traffic and keyword performance for SEO professionals and marketers. This SEO analysis prompt for ChatGPT walks through a 60-day evaluation window - 30 days before and 30 days after a specified implementation date - to measure how specific SEO changes affected organic traffic volume and the rankings of your top five keywords. It structures the output into clear sections: baseline metrics, post-change metrics, percentage shifts, ranking position movements, and a prioritized list of next-step recommendations. Real use cases include auditing technical SEO fixes, evaluating content refreshes, and reporting campaign ROI to stakeholders. The prompt runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt whenever you need to quantify the results of an SEO initiative and translate raw analytics into a client-ready or internal strategy document. ● Compares organic traffic and keyword rankings across a standardized 30-day pre- and post-implementation window. ● Outputs visual tables and charts to highlight traffic trends and ranking shifts. ● Delivers a prioritized action plan based on which changes drove the most impact. ● Saves hours of manual spreadsheet work by automating the report structure and analysis narrative. ## Prompt

```
## Role
You are an expert SEO analyst specializing in Google Analytics and keyword tracking.

## Task
Analyze the impact of recent SEO changes on website performance by comparing organic traffic and keyword rankings before and after implementation.

## Context
Website: {{website-url}}
SEO changes implemented: {{seo-changes}}
Date of implementation: {{implementation-date}}

## Method
1. Compare data from 30 days before and 30 days after the implementation date
2. Track organic traffic volume and percentage change
3. Monitor ranking shifts for the top 5 keywords
4. Visualize trends using tables and charts where helpful
5. Identify what worked, what didn't, and why

## Output
Provide a structured report:

**Before SEO Changes** (30 days prior)
- Organic traffic: [volume]
- Top 5 keyword rankings: [list with keyword and position]

**After SEO Changes** (30 days after)
- Organic traffic: [volume]
- Top 5 keyword rankings: [list with keyword and position]

**Impact Summary**
- Traffic change: [percentage and direction]
- Keyword ranking changes: [position shifts for each keyword]
- Visual comparison: [chart or table format]

**Analysis & Recommendations**
- What the data reveals about the changes' effectiveness
- Specific, actionable recommendations for further optimization
- Priority order for next steps based on impact potential
```

## 用法 / Usage
- 必填變數 / Variables: {{implementation-date}}、{{seo-changes}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The SEO Impact Analysis Report Generator is a free AI prompt that produces detailed before-and-after compariso…
