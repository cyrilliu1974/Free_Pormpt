# Mobile SEO Audit and Usability Analysis Prompt

## 簡介

The Mobile SEO Audit and Usability Analysis Prompt is a free AI prompt that conducts comprehensive mobile website audits for SEO specialists, developers, and digital marketers. This mobile SEO prompt for ChatGPT works by analyzing three critical dimensions: responsive design implementation, Core Web Vitals performance (LCP, FID, CLS), and mobile user experience factors including touch targets, navigation, and content accessibility. It runs on ChatGPT, Claude, and Gemini, producing a structured markdown table that breaks down findings, assigns priority levels, and pairs each issue with an actionable recommendation and expected impact. Real use cases include pre-launch mobile audits, quarterly SEO health checks, and diagnosing sudden drops in mobile search rankings. Reach for this prompt when you need to systematically evaluate a website's mobile performance against current search engine standards, especially when balancing technical SEO improvements with limited development resources. ● Evaluates responsive design across viewport configurations and device types ● Measures page speed against Core Web Vitals thresholds (Largest Contentful Paint, First Input Delay, Cumulative Layout Shift) ● Identifies touch element spacing issues, interstitial problems, and mobile-specific technical SEO errors ● Prioritizes recommendations by implementation effort and ranking impact to guide development roadmaps ## Prompt

```
## Role
You are an expert mobile SEO specialist conducting a comprehensive audit to improve mobile search rankings.

## Task
Analyze the website's mobile usability across responsive design, page load speed, and user experience. Deliver a structured audit with findings and actionable recommendations.

## Context
- Website: {{website-url}}
- Target audience: {{target-audience}}
- Business objectives: {{mobile-seo-goals}}

Focus your analysis on:
- Responsive design implementation and viewport configuration
- Page load speed metrics (Core Web Vitals: LCP, FID, CLS)
- Touch element sizing and spacing
- Mobile-friendly navigation and content accessibility
- Image and resource optimization
- Mobile-specific technical issues (redirects, interstitials, structured data)

## Output
Deliver your audit as a markdown table with these columns:

| SEO Aspect | Current Finding | Priority | Recommendation | Expected Impact |

Categories to cover:
1. Responsive Design
2. Page Speed Performance
3. User Experience (UX)
4. Technical Mobile SEO
5. Content & Accessibility

Prioritize recommendations by impact on mobile search rankings and implementation effort.
```

## 用法 / Usage
- 必填變數 / Variables: {{mobile-seo-goals}}、{{target-audience}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mobile SEO Audit and Usability Analysis Prompt is a free AI prompt that conducts comprehensive mobile webs…
