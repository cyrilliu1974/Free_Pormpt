# Sales Pipeline Bottleneck Analysis Prompt

## 簡介

The Sales Pipeline Bottleneck Analysis Prompt is a free AI prompt that helps sales teams and revenue leaders diagnose friction points slowing conversions and costing revenue. This sales pipeline analysis prompt for ChatGPT takes your pipeline data and produces a structured table identifying the stages where deals stall, the underlying causes, an impact score (1-10) reflecting severity on conversion and revenue, a priority rating (High/Medium/Low), and actionable solutions for each bottleneck. It works on ChatGPT, Claude, Gemini, and Grok, turning raw pipeline metrics into a clear diagnostic roadmap. Sales operations teams use it to spot drop-off zones between lead qualification and close, revenue leaders use it to prioritize where optimization efforts will yield the highest ROI, and sales strategists use it to present data-backed improvement plans to leadership. Reach for this prompt when conversion rates plateau, when deal velocity slows, or when you need to justify where to invest time fixing your funnel. ● Identifies the exact pipeline stages where deals are leaking or stalling, with clear descriptions of each bottleneck. ● Assigns a 1-10 impact score to quantify how severely each bottleneck affects conversion rates and revenue. ● Delivers priority rankings (High/Medium/Low) so teams know which fixes to tackle first for maximum ROI. ● Provides specific, actionable solutions tailored to the root cause of each identified bottleneck, not generic advice. ## Prompt

```
## Role
You are a sales strategist specializing in pipeline optimization and revenue generation.

## Task
Analyze the provided sales pipeline data to identify bottlenecks, diagnose root causes, assess their impact on conversion rates and revenue, and recommend prioritized solutions.

## Context
Sales pipeline data to analyze:
{{pipeline-data}}

## Output
Deliver your analysis as a table with these columns:

| Bottleneck Stage | Description | Root Cause | Impact Score (1-10) | Priority Level | Recommended Solutions |
|------------------|-------------|------------|---------------------|----------------|----------------------|
| [stage]          | [desc]      | [cause]    | [score]             | [priority]     | [solutions]          |

**Impact Score Legend:**
- 1-3: Minor impact on conversion rates and revenue
- 4-7: Moderate impact on conversion rates and revenue
- 8-10: Severe impact on conversion rates and revenue

**Priority Level Legend:**
- High: Requires immediate attention and resolution
- Medium: Needs to be addressed in the near future
- Low: Can be addressed as part of long-term optimization efforts

**Requirements:**
- Focus on the most critical bottlenecks with greatest impact on conversion and revenue
- Provide clear, specific descriptions of each bottleneck and its root cause
- Assign accurate impact scores and priority levels based on severity
- Offer practical, actionable solutions directly addressing each identified bottleneck
```

## 用法 / Usage
- 必填變數 / Variables: {{pipeline-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Sales Pipeline Bottleneck Analysis Prompt is a free AI prompt that helps sales teams and revenue leaders d…
