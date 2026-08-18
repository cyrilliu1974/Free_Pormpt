# Mobile SEO Audit and Usability Analysis Prompt

## 簡介

The Mobile SEO Audit and Usability Analysis Prompt is a free AI prompt that conducts detailed mobile usability testing and SEO analysis to improve mobile search rankings for websites and digital properties. This mobile SEO analysis prompt for ChatGPT guides UX researchers and SEO specialists through a structured audit covering navigation patterns, keyword optimization, page load performance, and mobile-friendliness. It produces a comprehensive report with executive summaries, methodology breakdowns, detailed findings organized by category, and prioritized next steps. The prompt runs on ChatGPT, Claude, and Gemini, combining user experience metrics like task completion rates and time-on-task with technical SEO data from tools like Google Search Console, PageSpeed Insights, and Mobile-Friendly Test. Real use cases include pre-launch mobile audits, quarterly SEO reviews, and diagnosing mobile traffic declines. This prompt is for SEO specialists, UX researchers, and digital marketers who need to identify and fix mobile search performance issues with data-driven recommendations. ● Structures mobile audits around navigation flow, keyword optimization, page speed, and responsiveness with severity ratings for each issue ● Combines qualitative usability testing data with quantitative SEO metrics from industry-standard tools ● Produces executive summaries, detailed findings tables, keyword gap analysis, and prioritized action plans in a single report ● Customizable test parameters including participant demographics, device types, usability metrics, and SEO tool selection ## Prompt

```
## Role
You are a UX researcher and SEO specialist conducting a comprehensive mobile usability audit to identify SEO improvements for better mobile search rankings.

## Task
Analyze the provided website's mobile experience and compile a detailed report covering navigation, keyword optimization, page performance, and mobile-friendliness. Identify actionable improvements prioritized by impact on mobile search performance.

## Context
{{website-url}}

{{test-parameters}}
Include: number of participants, demographics, devices tested, usability metrics tracked (task completion rate, time-on-task, error rate, etc.), and SEO analysis tools used (Google Search Console, PageSpeed Insights, Mobile-Friendly Test, etc.).

## Output
Deliver a structured report with these sections:

**Executive Summary**
- Key findings (3-5 bullet points)
- Primary recommendations (2-3 bullet points)

**Methodology**
- User testing parameters
- Usability metrics tracked
- SEO analysis tools used

**Detailed Findings**

1. **Navigation and User Flow**
   - Issue: [description]
     - Severity: High/Medium/Low
     - Recommendation: [solution]
   - (Repeat for each issue found)

2. **Mobile Keyword Optimization**
   - Current keyword rankings (table format)
   - Keyword gaps and opportunities with current → target positions
   - On-page optimization recommendations

3. **Page Load Speed and Performance**
   - Current mobile page load time
   - Performance issues identified
   - Optimization recommendations

4. **Mobile-Friendliness and Responsiveness**
   - Mobile usability score (/100)
   - Responsiveness issues
   - Recommendations for improvement

**Next Steps and Prioritization**
1. High priority action item
2. Medium priority action item
3. Lower priority action item

Use clear headings, bullet points, and tables. No XML tags.
```

## 用法 / Usage
- 必填變數 / Variables: {{test-parameters}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Mobile SEO Audit and Usability Analysis Prompt is a free AI prompt that conducts detailed mobile usability…
