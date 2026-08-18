# Competitive Analysis Report Generator

## 簡介

The Competitive Analysis Report Generator is a free AI prompt that produces data-driven competitive intelligence reports for business owners, strategists, and product managers. By analyzing competitor URLs alongside your business context, it delivers structured insights tailored to your specific analysis objective - whether that's a SWOT analysis, SEO keyword research, user experience audit, market positioning review, or another strategic task. This competitive analysis prompt for ChatGPT works by having you provide competitor URLs, your business context, and the specific analysis task you need completed. The prompt guides ChatGPT, Claude, Gemini, or Grok to browse the competitor sites, extract relevant data, and synthesize findings into a three-part report: data-backed insights tied directly to your objective, 3-5 prioritized recommended actions, and optional notes on limitations or follow-up research opportunities. Real use cases include benchmarking competitor features before a product launch, identifying content gaps for SEO strategy, and mapping competitive positioning before entering a new market. This prompt is for entrepreneurs, marketing teams, and business analysts who need structured competitive intelligence without hiring a consulting firm. ● Structures findings into insights, recommended actions, and research notes for immediate strategic use ● Adapts to multiple analysis types: SWOT, SEO, UX audits, market positioning, pricing comparisons, and more ● Flags data limitations and assumptions so you understand the confidence level of each recommendation ● Delivers prioritized next steps grounded in the competitive landscape and your specific business context ## Prompt

```
## Role
You are an expert strategic analyst providing data-driven competitive intelligence and actionable recommendations.

## Task
Perform a comprehensive analysis based on the user's specified objective. Browse the provided competitor URLs to gather relevant data, then deliver insights directly applicable to the requested task type (SWOT analysis, SEO keyword research, user experience audit, market positioning, etc.).

Think step-by-step before formulating your response to ensure depth and accuracy.

## Context
**Competitors:**
{{competitor-urls}}

**Business context:**
{{business-context}}

**Analysis objective:**
{{analysis-task}}

## Output
Structure your response in three sections:

**Insights:** Present findings directly relevant to the analysis objective, grounded in the competitive data and business context provided.

**Recommended Actions:** List 3-5 prioritized next steps the business owner should take based on your analysis.

**Notes:** (Optional) Flag any data limitations, assumptions made, or suggestions for follow-up research to strengthen future analyses.
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-task}}、{{business-context}}、{{competitor-urls}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Competitive Analysis Report Generator is a free AI prompt that produces data-driven competitive intelligen…
