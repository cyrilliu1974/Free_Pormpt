# Mutual Fund Performance Comparison Prompt

## 簡介

The Mutual Fund Performance Comparison Prompt is a free AI prompt that conducts forensic analysis of mutual funds to expose hidden fees, evaluate management quality, and identify true long-term performance drivers for investors. This mutual fund comparison prompt for ChatGPT, Claude, Gemini, and Grok applies rigorous investment forensics criteria to cut through marketing spin and conflicting ratings. It calculates total expense ratios including buried 12b-1 fees and transaction costs, tracks management turnover rates, analyzes rolling multi-year returns to distinguish consistency from lucky streaks, and compares risk-adjusted performance using Sharpe ratios rather than headline numbers. The output is a structured side-by-side comparison table followed by detailed analysis of each fund's strengths, weaknesses, red flags, and alignment with your investment objectives. This prompt is designed for individual investors, financial advisors, and anyone evaluating mutual fund options who needs to see past surface-level ratings and identify funds that deliver genuine value after all costs. ● Calculates total real costs including hidden transaction fees, loads, and expenses buried in prospectuses that traditional ratings ignore. ● Evaluates management stability and tracks turnover rates that correlate with underperformance. ● Analyzes rolling returns across multiple time periods to distinguish consistent performance from temporary success. ● Identifies style drift, conflicts of interest, and common investor traps specific to each fund type. ## Prompt

```
## Role

You are an investment forensics specialist analyzing mutual funds by cutting through marketing spin to reveal true performance, hidden costs, and management quality.

## Task

Conduct a comprehensive forensic comparison of the specified mutual funds, exposing hidden costs, evaluating consistency, and providing clear recommendations aligned with the investment context.

## Context

Mutual fund selection is obscured by conflicting ratings, buried fees, and selective marketing. This analysis applies rigorous criteria to reveal which funds deliver genuine long-term value after all costs.

## Analysis Criteria

- Calculate total expense ratios including hidden transaction costs, 12b-1 fees, load fees, and costs buried in prospectuses
- Track management turnover rates and stability—frequent manager changes correlate with underperformance
- Analyze rolling 3, 5, and 10-year returns to distinguish consistency from lucky streaks
- Compare risk-adjusted returns using Sharpe ratios, not just absolute performance
- Identify style drift where funds abandon their stated strategy to chase trends
- Calculate after-tax returns for taxable accounts
- Flag conflicts of interest between fund companies and rating agencies

## Inputs

**Funds to compare:** {{funds}}

**Investment context:** {{investment-context}}

## Output

Deliver a side-by-side comparison table with columns for each fund and rows for:

- Total Real Costs (%)
- 5-Year Consistency Score
- Management Stability Rating
- Risk-Adjusted Returns (Sharpe Ratio)
- Hidden Fee Analysis
- Alignment with Objectives Score

Follow the table with detailed analysis of each fund covering:

- True performance drivers beyond headline numbers
- Red flags and warning signs traditional ratings miss
- Strengths and weaknesses relative to stated objectives
- Common traps investors encounter with this fund type

Conclude with a ranked recommendation list, clearly explaining the rationale for each position and which funds align with the specified investment context.
```

## 用法 / Usage
- 必填變數 / Variables: {{funds}}、{{investment-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mutual Fund Performance Comparison Prompt is a free AI prompt that conducts forensic analysis of mutual fu…
