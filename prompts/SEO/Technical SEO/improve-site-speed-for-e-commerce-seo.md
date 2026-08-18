# E-commerce Site Speed Optimization Plan Generator

## 簡介

The E-commerce Site Speed Optimization Plan Generator is a free AI prompt that creates tailored, actionable speed improvement plans for online stores and e-commerce platforms. This e-commerce site speed prompt for ChatGPT analyzes your platform details and produces a numbered optimization roadmap organized into image optimization, CSS and JavaScript minification, browser caching configuration, and additional performance techniques like CDN implementation and database tuning. Each recommendation includes implementation steps, expected load-time impact, and e-commerce-specific trade-offs for product pages and checkout flows. It runs on ChatGPT, Claude, Gemini, and Grok, delivering technical guidance matched to your development team's expertise level. Reach for this prompt when you need to diagnose performance bottlenecks and build a prioritized fix list that balances conversion design with page speed. ● Produces category-organized plans covering image formats and lazy loading, code minification, caching rules, and server response tuning ● Estimates load-time impact and implementation difficulty for each recommendation, enabling teams to prioritize high-ROI fixes ● Addresses e-commerce-specific concerns like product image quality, dynamic inventory content, and checkout page responsiveness ● Adapts technical depth to match your team's skill level, from beginner-friendly steps to advanced rendering path optimization ## Prompt

```
## Role
You are an expert web developer and SEO specialist focused on website performance optimization.

## Task
Create a comprehensive, step-by-step optimization plan to improve loading speed for an e-commerce platform. The plan must enhance both SEO performance and user experience while maintaining visual appeal.

## Context
{{platform-details}}

Analyze the current website structure, identify performance bottlenecks, and recommend actionable improvements. Tailor all recommendations to e-commerce requirements, balancing conversion-optimized design with speed.

## Output
Deliver a numbered optimization plan organized under clear category headings:

1. **Image Optimization** – compression techniques, format selection, lazy loading
2. **Code Minification** – CSS and JavaScript optimization strategies
3. **Browser Caching** – implementation approach and configuration
4. **Additional Performance Techniques** – CDN usage, database optimization, server response improvements, critical rendering path optimization

For each category:
- Explain the specific technique
- Provide implementation steps matched to the technical expertise level
- Estimate the expected impact on load time
- Note any trade-offs or considerations for e-commerce (product images, checkout flow, dynamic content)

Prioritize recommendations by impact and implementation difficulty.
```

## 用法 / Usage
- 必填變數 / Variables: {{platform-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The E-commerce Site Speed Optimization Plan Generator is a free AI prompt that creates tailored, actionable sp…
