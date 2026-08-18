# Site Speed Optimization Audit Prompt for ChatGPT

## 簡介

The Site Speed Optimization Audit Prompt for ChatGPT is a free AI prompt that analyzes website performance bottlenecks and produces prioritized recommendations for improving load times, Core Web Vitals, and search engine rankings. This site speed optimization prompt for ChatGPT systematically evaluates server response time, resource optimization, mobile responsiveness, caching, and compression to pinpoint critical issues affecting SEO and user experience. It runs on ChatGPT, Claude, and Gemini, requiring only your website URL and business context (target audience, competitors, current load time). The output is a markdown table listing issues by severity, their impact on rankings and engagement, and specific implementation steps tied to measurable performance gains. Web developers, SEO specialists, and site owners use it to diagnose technical debt, prepare for algorithm updates, or troubleshoot declining organic traffic caused by slow pages. ● Evaluates server response time, page load speed, Core Web Vitals, and hosting infrastructure in one audit ● Identifies resource optimization opportunities for images, CSS, JavaScript, and fonts ● Assesses mobile responsiveness, caching, compression, and content delivery configuration ● Prioritizes issues by their direct impact on search rankings and user experience, not arbitrary checklists ## Prompt

```
## Role
You are an expert SEO and web performance analyst conducting a comprehensive site speed optimization audit.

## Task
Analyze the provided website to identify performance bottlenecks, assess their impact on SEO and user experience, and deliver prioritized, actionable recommendations. Systematically evaluate:

- Server response time and hosting infrastructure
- Page load speed and Core Web Vitals
- Resource optimization (images, CSS, JavaScript, fonts)
- Mobile responsiveness and adaptive performance
- Caching, compression, and delivery optimization

Prioritize issues by severity and their effect on search engine rankings and user experience.

## Context
**Website:** {{website-url}}

**Business context:** {{business-context}}
(Include target audience, business type, primary competitors, and current average page load time)

## Output
Present your findings in a markdown table with three columns: **Issue**, **Impact**, and **Recommendation**.

List issues in priority order, with the most critical performance problems first. Ensure all recommendations are specific, implementable, and tied to measurable performance improvements.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Site Speed Optimization Audit Prompt for ChatGPT is a free AI prompt that analyzes website performance bot…
