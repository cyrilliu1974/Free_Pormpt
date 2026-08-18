# Mobile Usability Audit & Fix Recommendations

## 簡介

The Mobile Usability Audit & Fix Recommendations is a free AI prompt that conducts technical audits of mobile websites and delivers prioritized, actionable fixes for SEO professionals and web developers. This mobile usability prompt for ChatGPT analyzes page load speed, Core Web Vitals, responsive design breakpoints, touch target sizing, viewport configuration, and mobile-specific SEO signals. It runs on ChatGPT, Claude, Gemini, and Grok, producing a structured markdown table that maps each identified issue to specific implementation guidance. Use it to diagnose layout shifts, optimize images for mobile, fix interstitials that harm rankings, ensure thumb-zone navigation, and improve mobile crawlability for Google's mobile-first index. Reach for this prompt when preparing for a mobile SEO audit, troubleshooting Core Web Vitals failures, or addressing Google Search Console mobile usability warnings. ● Evaluates Core Web Vitals (LCP, FID, CLS) and page load performance with optimization paths ● Checks touch target dimensions, spacing, and thumb-zone placement for mobile interaction ● Identifies responsive design failures, viewport misconfigurations, and layout shift triggers ● Audits mobile-specific factors like interstitials, font scaling, lazy loading, and crawlability signals ## Prompt

```
## Role
You are an expert SEO and mobile usability analyst conducting a technical audit to improve search performance and mobile user experience.

## Task
Audit the mobile version of the provided website, identify usability and performance issues, then deliver specific, actionable recommendations to enhance mobile UX and search engine rankings.

## Context
Website to audit: {{website-url}}

Focus your analysis on:
- Page load speed and Core Web Vitals
- Responsive design breakpoints and layout shifts
- Touch target sizing and spacing (minimum 48×48px)
- Mobile-specific content optimization and readability
- Navigation patterns and thumb-zone accessibility
- Form usability and input types
- Viewport configuration and font scaling
- Image optimization and lazy loading
- Interstitial and pop-up interference
- Mobile crawlability and indexing signals

{{audit-parameters}}

## Output
Deliver your findings as a markdown table with the structure and columns specified in the audit parameters above. Each row should contain one specific issue or recommendation with clear, implementable guidance. Prioritize issues by SEO and UX impact.
```

## 用法 / Usage
- 必填變數 / Variables: {{audit-parameters}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mobile Usability Audit & Fix Recommendations is a free AI prompt that conducts technical audits of mobile …
