# Site Speed Optimization Strategy for SEO Rankings

## 簡介

The Site Speed Optimization Strategy for SEO Rankings is a free AI prompt that analyzes website performance and creates actionable speed improvement plans tailored to your CMS and performance goals. This site speed optimization prompt for ChatGPT analyzes Core Web Vitals like FCP, LCP, TTI, CLS, and TBT, then delivers prioritized recommendations across image optimization, code minification, caching strategies, server response times, critical rendering path fixes, and third-party script management. Each recommendation includes CMS-specific implementation instructions, code snippets, expected SEO impact, and priority ratings based on effort versus performance gain. The prompt works on ChatGPT, Claude, and Gemini, making it adaptable to your preferred text model. Web performance specialists use it to turn PageSpeed Insights data into executable roadmaps, addressing both quick wins and structural improvements that reduce page load times and boost search visibility. ● Benchmarks current load times against target metrics and identifies the highest-impact bottlenecks affecting Core Web Vitals ● Categorizes every recommendation by priority level (High/Medium/Low) with clear rationale tied to SEO impact and implementation difficulty ● Provides step-by-step technical instructions, including code examples and configuration settings, specific to WordPress, Shopify, Webflow, or other CMS platforms ● Structures a phased rollout plan with estimated timelines and task dependencies so teams know what to tackle first, next, and long-term ## Prompt

```
## Role
You are an expert SEO and web performance specialist.

## Task
Develop a comprehensive site speed optimization strategy that improves SEO rankings and user experience. Analyze current performance, identify bottlenecks, and deliver actionable recommendations prioritized by impact and implementation difficulty.

## Context
Website: {{website-url}}
Current page load time: {{current-load-time}}
Target page load time: {{target-load-time}}
CMS: {{cms}}

## Output
Structure your optimization strategy using these main categories:

### Performance Analysis
- Current bottlenecks and their impact
- Key metrics (FCP, LCP, TTI, CLS, TBT)
- Quick wins vs. long-term improvements

### Optimization Recommendations
For each recommendation, provide:
- **What**: The optimization technique
- **Why**: Expected impact on performance and SEO
- **How**: Step-by-step implementation for the specified CMS
- **Priority**: High/Medium/Low based on impact vs. effort
- **Technical details**: Code snippets, configuration examples, or tool recommendations where applicable

Cover these optimization areas:
- Image and media optimization
- Code minification and bundling (CSS, JavaScript, HTML)
- Caching strategies (browser, CDN, server-side)
- Server response time and hosting
- Critical rendering path optimization
- Third-party script management
- Mobile performance

### Implementation Roadmap
Sequence the recommendations into a phased rollout plan with estimated timelines and dependencies between tasks.
```

## 用法 / Usage
- 必填變數 / Variables: {{cms}}、{{current-load-time}}、{{target-load-time}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Site Speed Optimization Strategy for SEO Rankings is a free AI prompt that analyzes website performance an…
