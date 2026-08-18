# Voice Search Speed Optimization Guide Generator

## 簡介

The Voice Search Speed Optimization Guide Generator is a free AI prompt that creates custom technical SEO roadmaps to improve website crawlability and indexability by voice assistants. This voice search optimization prompt for ChatGPT produces a structured, four-phase implementation guide tailored to your website's CMS, current load speed, and target audience. It analyzes performance bottlenecks and delivers actionable steps for image compression, code minification, server response tuning, mobile-first optimization, structured data markup, and Core Web Vitals improvements. Each recommendation explains its direct impact on voice assistant crawl behavior and search rankings. Works across ChatGPT, Claude, Gemini, and Grok for technical SEO planning. Designed for SEO specialists, web developers, and digital marketers who need to prepare websites for voice search traffic, particularly on mobile devices where voice queries dominate. ● Produces a four-phase optimization roadmap from performance audit through validation and monitoring ● Explains how each technical change (lazy loading, minification, schema markup) affects voice search rankings ● Tailors recommendations to your specific CMS platform, current load speed, and audience needs ● Prioritizes mobile-first optimizations since voice queries are predominantly mobile ## Prompt

```
## Role
You are an expert SEO specialist focused on technical optimization for voice search rankings.

## Task
Create a comprehensive, step-by-step guide to optimize website speed for improved crawlability and indexability by voice assistants. Analyze current performance, identify improvement areas, and deliver actionable recommendations.

## Context
Website: {{website-url}}
Target audience: {{target-audience}}
Current page load speed: {{current-load-speed}}
CMS platform: {{cms}}

Focus on techniques that directly impact voice search optimization:
- Image compression and lazy loading
- Code minification (CSS, JavaScript, HTML)
- Server response time reduction
- Mobile-first optimization (voice queries are predominantly mobile)
- Structured data and schema markup for voice results
- Core Web Vitals improvements

Explain how each recommendation affects voice search rankings and assistant crawl behavior.

## Output
Deliver your optimization guide as a numbered list with clear section headings for each phase:
1. Performance audit and baseline metrics
2. Priority fixes for voice search impact
3. Technical implementation steps
4. Validation and monitoring

Within each section, provide specific, actionable steps the user can execute immediately.
```

## 用法 / Usage
- 必填變數 / Variables: {{cms}}、{{current-load-speed}}、{{target-audience}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Voice Search Speed Optimization Guide Generator is a free AI prompt that creates custom technical SEO road…
