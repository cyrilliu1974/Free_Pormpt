# Site Speed & UX Optimization Audit Prompt

## 簡介

The Site Speed & UX Optimization Audit Prompt is a free AI prompt that analyzes website performance and delivers actionable recommendations for e-commerce businesses looking to improve user experience and search rankings. This site speed optimization prompt for ChatGPT evaluates four critical dimensions: page load speed (resource optimization, caching, compression), mobile responsiveness (viewport handling, touch targets, adaptive layouts), content optimization (keyword strategy, metadata, internal linking), and technical SEO (crawlability, schema markup, Core Web Vitals). It structures recommendations using dependency grammar, where each main strategy branches into specific implementation steps and expected metric improvements. The output prioritizes quick wins alongside foundational changes, making it practical for teams to execute incrementally. Compatible with ChatGPT, Claude, Gemini, and Grok, it transforms a website URL and business profile into a concrete optimization roadmap. Reach for this prompt when you need a structured performance audit that connects technical fixes to business outcomes, whether you're preparing for a site redesign, troubleshooting bounce rates, or building an SEO improvement plan. ● Evaluates page load speed, mobile responsiveness, content quality, and technical SEO in a single analysis ● Uses dependency grammar to show how implementation steps connect to strategy and expected outcomes ● Prioritizes recommendations by impact on user satisfaction and search visibility ● Outputs actionable, tool-specific guidance rather than generic best practices ## Prompt

```
## Role
You are an expert website optimization specialist focused on e-commerce performance, user experience, and search engine rankings.

## Task
Analyze the provided website and deliver a prioritized optimization plan. Structure your analysis using dependency grammar: each main recommendation should branch into specific sub-points that explain implementation details.

## Context
**Website:** {{website-url}}

**Business profile:** {{business-profile}}
(Include target audience, primary products/services, current search engine rankings, and known performance issues)

## Analysis Framework
Evaluate across four dimensions:
- **Page load speed** – resource optimization, caching, compression
- **Mobile responsiveness** – viewport handling, touch targets, adaptive layouts
- **Content optimization** – keyword strategy, metadata, internal linking, product descriptions
- **Technical SEO** – crawlability, schema markup, sitemap health, Core Web Vitals

## Output
Deliver your recommendations as a bullet-point list using dependency grammar structure:
- Main optimization strategy
  - Supporting technique or implementation step
    - Specific action or tool
  - Expected impact or metric improvement

Prioritize strategies by potential impact on both user satisfaction and search visibility. Begin with quick wins, then move to foundational improvements.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-profile}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Site Speed & UX Optimization Audit Prompt is a free AI prompt that analyzes website performance and delive…
