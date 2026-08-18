# Mobile SEO Error Audit and Fix Prompt

## 簡介

The Mobile SEO Error Audit and Fix Prompt is a free AI prompt that analyzes your website's mobile version and delivers a prioritized list of technical SEO issues with implementable solutions for webmasters and SEO professionals. This mobile SEO prompt for ChatGPT examines critical factors affecting mobile search rankings: page speed, Core Web Vitals, image optimization, viewport configuration, mobile usability, and mobile-first indexing compliance. It runs on ChatGPT, Claude, and Gemini, producing a structured markdown table that pairs each discovered error with both a clear description and a fix aligned with current best practices. Use it when launching a mobile site, diagnosing ranking drops, or preparing for a technical SEO audit - especially valuable for businesses targeting mobile audiences where user experience directly impacts conversion. ● Identifies slow loading times, render-blocking resources, and Core Web Vitals failures that harm mobile rankings ● Flags unoptimized images, incorrect viewport tags, and mobile usability errors blocking mobile-first indexing ● Prioritizes issues by search ranking impact and user engagement so you fix what matters first ● Outputs a three-column markdown table (Error, Description, Solution) ready to share with developers or clients ## Prompt

```
## Role
You are an expert mobile SEO specialist conducting a comprehensive technical audit.

## Task
Analyze the mobile version of {{website-url}} and identify critical mobile SEO issues including slow loading times, unoptimized images, poor mobile usability, incorrect viewport configuration, and mobile-specific technical errors. For each issue found, provide a clear description and an actionable solution aligned with current mobile SEO best practices.

## Context
Website: {{website-url}}
Business type: {{business-type}}
Target audience: {{target-audience}}

Focus your analysis on mobile user experience, Core Web Vitals, and mobile-first indexing requirements. Prioritize issues by their impact on search rankings and user engagement.

## Output
Present your findings in a markdown table with three columns:

| Error | Description | Solution |
|-------|-------------|----------|

Each row should address one specific mobile SEO issue with a comprehensive, implementable fix. Include 8-12 of the most impactful issues discovered.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-type}}、{{target-audience}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mobile SEO Error Audit and Fix Prompt is a free AI prompt that analyzes your website's mobile version and …
