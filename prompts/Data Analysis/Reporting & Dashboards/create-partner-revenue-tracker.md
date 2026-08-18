# Partner Revenue Tracker Table Generator

## 簡介

The Partner Revenue Tracker Table Generator is a free AI prompt that creates structured revenue attribution tables for marketing teams managing partnership performance and campaign ROI. This partner revenue tracking prompt for ChatGPT produces a clean 6-column markdown table with partner names, campaigns, revenue figures, costs, calculated ROI percentages, and a notes column for performance insights. It automatically computes ROI as ((Revenue - Costs) / Costs) × 100% for each entry, ensuring consistent financial analysis across all partnership data. The prompt works on ChatGPT, Claude, Gemini, and Grok, accepting raw partnership data and transforming it into an organized table format that highlights which partners and campaigns deliver the strongest returns. Marketing analysts, partnership managers, and revenue operations teams use it to track attribution, compare campaign performance, and document key drivers behind revenue fluctuations. ● Outputs a markdown table with Partner, Campaign, Revenue, Costs, ROI, and Notes columns for clear financial oversight. ● Automatically calculates ROI percentages using the standard formula to ensure consistency across all entries. ● Includes a Notes column for documenting performance drivers, red flags, or strategic observations for each partner-campaign combination. ● Accepts flexible partnership data inputs and formats them into aligned, easy-to-read rows with proper dollar formatting. ## Prompt

```
## Role
You are a revenue tracking and analysis expert specializing in partnership performance, campaign attribution, cost analysis, and ROI optimization.

## Task
Create a comprehensive 6-column table to track and analyze partner revenue contribution:

**Columns:**
- Partner
- Campaign
- Revenue
- Costs
- ROI
- Notes

Provide clear column headers with example rows populated using the data below. Calculate ROI as ((Revenue - Costs) / Costs) × 100%. Include space for performance insights in the Notes column.

## Context
{{partnership-data}}

## Output
Deliver the table in markdown format:

```
| Partner | Campaign | Revenue | Costs | ROI | Notes |
|---------|----------|---------|-------|-----|-------|
| [Name] | [Campaign] | $XX,XXX | $X,XXX | XX% | [Performance insights] |
```

Ensure all revenue and cost figures align with the provided data, ROI calculations are accurate, and notes highlight key performance drivers or concerns for each partner/campaign combination.
```

## 用法 / Usage
- 必填變數 / Variables: {{partnership-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Partner Revenue Tracker Table Generator is a free AI prompt that creates structured revenue attribution ta…
