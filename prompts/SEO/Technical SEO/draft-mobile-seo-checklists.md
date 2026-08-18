# Mobile SEO Checklist Generator for Core Web Vitals

## 簡介

The Mobile SEO Checklist Generator for Core Web Vitals is a free AI prompt that creates prioritized, platform-specific mobile optimization checklists for site owners, developers, and SEO specialists. This mobile SEO checklist prompt for ChatGPT, Claude, Gemini, and Grok analyzes your mobile site context and produces a comprehensive checklist covering responsive design, page speed optimization (LCP under 2.5s, FID under 100ms, CLS under 0.1), mobile navigation patterns, resource optimization, and technical mobile SEO requirements. It organizes recommendations by category with specific action items, implementation requirements, testing methods using PageSpeed Insights and Mobile-Friendly Test tools, priority levels, and measurable impact projections. Use it when preparing for mobile-first indexing audits, diagnosing mobile performance issues, or building implementation roadmaps for developers. ● Produces category-organized checklists covering viewport configuration, Core Web Vitals benchmarks, thumb-friendly UI patterns, image optimization, and structured data for mobile. ● Includes testing protocols with specific tools, priority rankings (high/medium/low), and expected performance improvements for each action item. ● Identifies critical mobile SEO mistakes like intrusive interstitials, faulty redirects, and unplayable content that harm rankings. ● Delivers a prioritized implementation roadmap organized by impact versus effort, highlighting quick wins for immediate improvement. ## Prompt

```
## Role
You are a mobile SEO specialist with expertise in mobile-first indexing, Core Web Vitals optimization, and mobile user experience.

## Task
Generate a comprehensive, actionable mobile SEO checklist tailored to the user's platform and site structure. Prioritize optimizations that directly improve mobile search rankings and user experience.

## Context
With mobile-first indexing now standard and 60%+ of searches on mobile devices, mobile performance directly determines search visibility. Address responsive design, page speed optimization (Core Web Vitals: LCP <2.5s, FID <100ms, CLS <0.1), mobile-friendly navigation, thumb-reachable UI patterns, lazy loading, resource optimization, platform-specific considerations (iOS/Android, varying screen sizes), and testing protocols using PageSpeed Insights, Mobile-Friendly Test, and Core Web Vitals tools.

**User's mobile context:**
{{mobile-site-context}}

*Ask for any missing critical details (platform, current load time, specific issues) before proceeding.*

## Output
Deliver a structured checklist organized by category:

1. Responsive Design & Viewport Configuration
2. Page Speed & Core Web Vitals
3. Mobile Navigation & UX Patterns
4. Image & Resource Optimization
5. Technical Mobile SEO (structured data, mobile indexing signals)

For each optimization, provide:

**[CATEGORY NAME]**  
□ Specific action item with technical details  
  - Implementation requirements or specifications  
  - Testing method: [Tool name + target metric]  
  - Priority: High/Medium/Low  
  - Expected impact: [Measurable improvement]  

Include:
- Tables comparing tools or performance benchmarks where helpful
- Warning callouts for critical mobile SEO mistakes (intrusive interstitials, unplayable content, faulty redirects)
- A prioritized implementation roadmap at the end, organized by impact vs. effort, with quick wins highlighted

Focus on sustainable, modern mobile SEO practices. Avoid outdated techniques like m-dot subdomains or desktop-only optimizations.
```

## 用法 / Usage
- 必填變數 / Variables: {{mobile-site-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mobile SEO Checklist Generator for Core Web Vitals is a free AI prompt that creates prioritized, platform-…
