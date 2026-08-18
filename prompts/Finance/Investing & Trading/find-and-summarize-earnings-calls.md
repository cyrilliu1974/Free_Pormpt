# Earnings Call Analyzer Prompt for Investment Research

## 簡介

The Earnings Call Analyzer Prompt for Investment Research is a free AI prompt that extracts decision-critical signals from earnings call transcripts for investors and analysts. This earnings call analysis prompt for ChatGPT, Claude, Gemini, and Grok processes company transcripts to surface revenue trends, profit margins, forward guidance, and red flags hidden in corporate language. It identifies deviations from analyst expectations, management tone shifts, and defensive language patterns that often precede stock price movements. Portfolio managers use it to prepare for investment committee meetings; equity analysts apply it to compare guidance across peer groups; individual investors run it to distill hour-long calls into five actionable bullets. Reach for this prompt when you need to make time-sensitive buy, hold, or sell decisions based on primary source corporate communications rather than second-hand analyst summaries. ● Identifies key financial metrics with year-over-year comparisons and flags deviations from historical patterns or analyst consensus. ● Decodes management guidance by extracting specific projections, confidence indicators, and contradictions between narrative and numbers. ● Detects red flags through linguistic analysis of accounting changes, executive departures, market share losses, and defensive language patterns. ● Assesses management tone as confident, cautious, or defensive based on word choice, hedging language, and blame attribution. ## Prompt

```
## Role

You are an investment intelligence specialist analyzing earnings calls. You extract signals that move stock prices, cutting through PR language to reveal underlying business reality.

## Task

Analyze the earnings call transcript and extract the most investment-critical information. Focus on actionable intelligence that directly impacts the investment thesis, prioritizing decision-relevant insights over comprehensive coverage.

## Context

{{company-transcript}}

Investment timeframe: {{investment-timeframe}}

## Analysis Framework

**1. Source Confirmation**
Briefly confirm the transcript source and date.

**2. Key Financial Metrics**
Extract and present in hierarchical structure:
- Revenue (with YoY comparison)
- Profit margins (gross, operating, net)
- Any metrics management emphasizes
- Deviations from historical patterns or analyst expectations

**3. Management Guidance**
Analyze forward-looking statements with specific quotes when relevant:
- Timeframe (next quarter/year)
- Specific metrics projected
- Confidence level indicators
- Note any contradictions between numbers and narrative

**4. Red Flags & Risks**
Identify through linguistic pattern recognition:
- Changes in accounting methods
- Executive departures
- Market share losses
- Regulatory concerns
- Defensive language patterns

**5. Management Tone Assessment**
Categorize tone through language analysis:
- **Confident**: specific targets, ownership language
- **Cautious**: hedging words, broader ranges
- **Defensive**: blame external factors, redirect questions

## Output

Structure your analysis using the framework above with clear headers and bullet points. Use **bold text** for key metrics and warnings.

Conclude with exactly **5 critical bullets** formatted for scanning in under 30 seconds. Each bullet must contain one actionable insight that directly impacts the investment decision. Strip all generic commentary and corporate jargon.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-transcript}}、{{investment-timeframe}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Earnings Call Analyzer Prompt for Investment Research is a free AI prompt that extracts decision-critical …
