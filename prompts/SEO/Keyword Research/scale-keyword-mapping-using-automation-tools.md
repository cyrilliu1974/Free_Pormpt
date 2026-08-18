# Keyword Mapping Automation Strategy Builder

## 簡介

The Keyword Mapping Automation Strategy Builder is a free AI prompt that creates structured keyword-to-page alignment strategies with automation workflows for SEO professionals and content teams. This keyword mapping prompt for ChatGPT produces a three-column markdown table mapping target keywords to specific pages or URL patterns on your site, complete with step-by-step automation instructions tailored to your chosen SEO tool (Ahrefs, SEMrush, Screaming Frog, or custom scripts). It factors in search volume, keyword difficulty, user intent, and content relevance to ensure every keyword lands on the most appropriate page. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it adaptable to your existing workflow. Use cases include scaling keyword assignments across large e-commerce catalogs, programmatically organizing blog topic clusters, and auditing existing site structures for optimization opportunities. Reach for this prompt when you need a repeatable, data-driven framework to map hundreds or thousands of keywords without manual spreadsheet drudgery, or when onboarding a new automation platform into your SEO stack. ● Outputs a markdown table with Keywords, Pages, and Automation Steps columns for immediate implementation ● Accounts for search volume, keyword difficulty, user intent, and content relevance in every mapping decision ● Tailors automation instructions to your specified tool (Ahrefs, SEMrush, Python scripts, Google Sheets, or API workflows) ● Accepts your website URL, target audience, and current SEO context to generate audience-specific, competitive mappings ## Prompt

```
## Role
You are an expert SEO strategist specializing in programmatic keyword mapping and automation.

## Task
Create a comprehensive keyword mapping strategy for {{website-url}} that aligns target keywords with relevant pages and defines automation steps using {{automation-tool}}. The strategy must be scalable and account for search volume, keyword difficulty, user intent, and content relevance.

## Context
- Target audience: {{target-audience}}
- Current SEO performance and competitive landscape: {{seo-context}}

Develop a systematic approach that can be automated for efficiency at scale.

## Output
Provide your keyword mapping strategy as a markdown table with three columns:

| Keywords | Pages | Automation Steps |
|----------|-------|------------------|

Each row should map one or more related keywords to a specific page type or URL pattern, with clear instructions for automating the mapping process.
```

## 用法 / Usage
- 必填變數 / Variables: {{automation-tool}}、{{seo-context}}、{{target-audience}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Keyword Mapping Automation Strategy Builder is a free AI prompt that creates structured keyword-to-page al…
