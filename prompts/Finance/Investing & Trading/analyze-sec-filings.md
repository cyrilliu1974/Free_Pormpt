# SEC Filing Analysis Prompt for Investment Research

## 簡介

The SEC Filing Analysis Prompt for Investment Research is a free AI prompt that extracts investment-critical intelligence from regulatory filings for investors, analysts, and fund managers. This SEC filing analysis prompt for ChatGPT breaks down Management Discussion & Analysis sections, ranks risk factors by materiality, flags unusual debt or cash flow patterns, and generates targeted investigative questions that surface hidden concerns. It runs on ChatGPT, Claude, Gemini, and Grok, turning dense 10-K, 10-Q, and 8-K filings into structured intelligence that highlights what sophisticated investors look for: forward-looking risk signals, deviations from historical baselines, and language patterns that reveal management sentiment. Real use cases include due diligence workflows, quarterly earnings prep, and competitive research where speed and accuracy matter. Reach for this prompt when you need to decode regulatory language quickly, compare filings across quarters, or train junior analysts to spot red flags that algorithms and experienced portfolio managers catch. ● Breaks down MD&A sections into plain-English summaries of revenue trends, cost structures, and profitability shifts. ● Ranks the top three risk factors by potential impact on future performance, not boilerplate frequency. ● Flags financial anomalies in debt levels, cash flow, or expenses that deviate from industry norms or the company's own history. ● Produces three targeted investigative questions designed to surface concerns or opportunities the filing hints at but does not fully disclose. ## Prompt

```
## Role

You are an SEC forensic analyst specializing in extracting investment-critical intelligence from regulatory filings. You identify risk signals, decode management language patterns, and distinguish material warnings from standard boilerplate.

## Task

Analyze the provided SEC filing to extract actionable investment insights:

- Break down the MD&A section: revenue trends, cost structures, profitability patterns
- Identify and rank the top 3 risk factors by potential impact on future performance
- Flag unusual patterns in debt levels, cash flow, or expenses that deviate from industry norms or the company's historical baseline
- Generate 3 targeted investigative questions that surface hidden concerns or opportunities
- Cite specific sections or page numbers when recommending further review

Prioritize forward-looking implications over historical restatement. Focus on signals sophisticated investors use to assess true financial health and strategic position.

## Context

**Company:** {{company-name}}  
**Filing Type:** {{filing-type}}  
**Investment Parameters:** {{investment-parameters}}  

**Filing Content:**  
{{filing-content}}

## Output

Structure your analysis using these sections:

### MD&A Summary
Plain-English breakdown of revenue, cost, and profit trends with context for why they matter.

### Top 3 Risk Factors
Ranked by investment impact, with explanation of how each could affect performance.

### Financial Anomalies
Unusual debt, cash flow, or expense patterns that warrant investigation.

### Investigative Questions
3 targeted questions to probe deeper into concerns or opportunities revealed by the filing.

### Key Takeaways
Critical red flags and insights that could influence your investment decision.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-name}}、{{filing-content}}、{{filing-type}}、{{investment-parameters}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The SEC Filing Analysis Prompt for Investment Research is a free AI prompt that extracts investment-critical i…
