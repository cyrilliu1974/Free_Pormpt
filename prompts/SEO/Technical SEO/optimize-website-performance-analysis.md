# Website Performance Analysis Prompt for ChatGPT

## 簡介

The Website Performance Analysis Prompt for ChatGPT is a free AI prompt that conducts technical performance audits for websites on both mobile and desktop devices. This website performance analysis prompt for ChatGPT guides the AI to act as an expert performance analyst, measuring core metrics such as load time, first contentful paint, largest contentful paint, and time to interactive. It produces a structured report complete with comparison tables showing measured values against optimal ranges, a prioritized list of performance issues, and specific optimization recommendations tailored to the analyzed site. The prompt runs on ChatGPT, Claude, and Gemini and is ideal for Technical SEO workflows. Real use cases include auditing client websites before optimization work, diagnosing page speed problems that affect search rankings, and benchmarking performance improvements after code or infrastructure changes. Reach for this prompt when you need a systematic, data-driven performance audit that goes beyond generic advice and delivers recommendations specific to a particular website URL. ● Produces side-by-side mobile and desktop performance metric tables with status indicators (good, needs improvement, poor) for quick diagnostics. ● Identifies key performance issues ranked by impact, avoiding generic checklists in favor of findings specific to the analyzed website. ● Delivers concrete optimization recommendations tied directly to the metrics and issues found, not boilerplate speed tips. ● Includes curated additional resources relevant to the identified issues, giving users a clear path to implementation. ## Prompt

```
## Role
You are an expert website performance analyst with deep knowledge of web performance optimization techniques and testing tools.

## Task
Conduct a comprehensive performance analysis of the provided website URL for both mobile and desktop devices. Identify key performance issues, gather detailed metrics using performance testing tools, and provide specific, actionable optimization recommendations tailored to this website. Avoid generic advice.

## Context
Website URL: {{website-url}}

## Output
Deliver your analysis as follows:

**Website Performance Analysis Report for {{website-url}}**

**Mobile Performance Metrics:**

| Metric | Value | Optimal Range | Status |
|--------|-------|---------------|--------|
| [metric name] | [measured value] | [optimal range] | ✅/⚠️/❌ |

(Use ✅ for good, ⚠️ for needs improvement, ❌ for poor)

**Desktop Performance Metrics:**

| Metric | Value | Optimal Range | Status |
|--------|-------|---------------|--------|
| [metric name] | [measured value] | [optimal range] | ✅/⚠️/❌ |

**Key Performance Issues Identified:**
1. [Issue 1]
2. [Issue 2]
3. [Issue 3]
...

**Recommendations for Optimization:**
1. [Specific, actionable recommendation 1]
2. [Specific, actionable recommendation 2]
3. [Specific, actionable recommendation 3]
...

**Additional Resources:**
- [Relevant article or guide 1]
- [Relevant article or guide 2]
- [Relevant article or guide 3]
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Website Performance Analysis Prompt for ChatGPT is a free AI prompt that conducts technical performance au…
