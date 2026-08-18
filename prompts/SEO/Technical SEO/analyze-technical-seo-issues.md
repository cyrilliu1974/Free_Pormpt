# Technical SEO Audit Roadmap Generator

## 簡介

The Technical SEO Audit Roadmap Generator is a free AI prompt that produces prioritized technical SEO remediation plans for websites of any size and platform. This technical SEO prompt for ChatGPT, Claude, Gemini, and Grok analyzes your site context - platform architecture, crawlability barriers, performance bottlenecks, and technical debt - then structures findings into High, Medium, and Low Urgency tiers. Each recommendation includes specific fixes, step-by-step implementation guidance, expected impact, realistic timelines, success metrics, and potential risks. SEO professionals use it to balance impact against implementation cost, ensure fixes are tailored to platform constraints, and avoid common pitfalls that can worsen organic visibility. Reach for this prompt when you need an actionable audit that accounts for development resources, site size, and business model rather than a generic checklist. ● Diagnoses crawlability barriers, performance bottlenecks, and platform-specific technical debt based on your site context. ● Structures all findings into a three-tier priority system that balances organic visibility impact against implementation complexity. ● Provides step-by-step implementation guidance, realistic timelines, and success metrics for each recommended fix. ● Identifies potential risks and pitfalls to prevent improper execution that could harm search rankings. ## Prompt

```
## Role
You are a technical SEO specialist with expertise in diagnosing site-level issues, understanding platform constraints, and creating actionable remediation plans that balance impact against implementation cost.

## Task
Analyze the provided site context and produce a comprehensive technical SEO audit roadmap. Structure all findings into a three-tier priority system (High, Medium, Low Urgency) that accounts for resource constraints and technical capacity.

## Context
{{site-context}}

Technical SEO fixes can dramatically improve organic visibility when implemented correctly, but improper execution often causes more harm than the original issue. Consider platform architecture, crawlability barriers, performance bottlenecks, and current technical debt.

## Output
For each priority tier, deliver recommendations in this format:

**High Urgency**
- **Fix**: [specific issue and solution]
- **Implementation**: [step-by-step guidance]
- **Expected impact**: [measurable outcome]
- **Timeline**: [realistic estimate]
- **Success metrics**: [KPIs to track]
- **Risks**: [potential pitfalls during implementation]

**Medium Urgency**
[same structure]

**Low Urgency**
[same structure]

Prioritize fixes that deliver maximum impact relative to implementation complexity. Tailor all guidance to the platform, site size, development resources, and business model described in the site context.
```

## 用法 / Usage
- 必填變數 / Variables: {{site-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Technical SEO Audit Roadmap Generator is a free AI prompt that produces prioritized technical SEO remediat…
