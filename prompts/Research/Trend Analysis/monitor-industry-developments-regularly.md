# Industry Development Monitoring Prompt

## 簡介

The Industry Development Monitoring Prompt is a free AI prompt that scans market news, reports, and trends to deliver actionable strategic intelligence for business analysts and market researchers. This industry development monitoring prompt for ChatGPT systematically evaluates recent market events within a defined timeframe and focus area, then outputs a prioritized markdown table with three columns: Date, Development, and Potential Impact. Each finding is assessed for its strategic relevance - whether it represents an opportunity or threat - and categorized by priority level (high, medium, or low). Use it to track competitive shifts, regulatory changes, technology launches, or customer behavior patterns that could affect market position or sales outlook. The prompt works across ChatGPT, Claude, Gemini, and Grok, adapting to any industry vertical or analysis window you specify. This prompt is built for industry analysts, competitive intelligence teams, sales strategists, and business development professionals who need to stay current on market dynamics without manually sifting through scattered news sources. ● Scans and synthesizes news, reports, and trends for a custom company, industry, and timeframe ● Delivers findings in a clean three-column markdown table (Date, Development, Potential Impact) ● Categorizes each development as opportunity or threat with high/medium/low priority labels ● Configurable focus areas and number of findings to match your research scope ## Prompt

```
## Role
You are an expert industry analyst monitoring market developments to identify opportunities and threats.

## Task
Scan industry news, reports, and trends relevant to {{company-and-industry}}, then deliver a structured analysis of key developments and their strategic implications. Evaluate each finding's potential impact on market position, competitive advantage, and sales outlook.

## Context
Focus your analysis on: {{focus-areas}}

Timeframe: {{timeframe}}

Deliver your {{number-of-findings}} most significant findings, prioritizing developments with the highest strategic relevance.

## Output
Present your analysis as a markdown table with three columns:

| Date | Development | Potential Impact |
|------|-------------|------------------|

For each row:
- **Date**: When the development occurred or was announced
- **Development**: Clear description of the market event, trend, or news item
- **Potential Impact**: Actionable assessment of how this affects strategy, categorized by significance (opportunity/threat, high/medium/low priority)
```

## 用法 / Usage
- 必填變數 / Variables: {{company-and-industry}}、{{focus-areas}}、{{number-of-findings}}、{{timeframe}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Industry Development Monitoring Prompt is a free AI prompt that scans market news, reports, and trends to …
