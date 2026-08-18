# Long-Duration Bond Investment Recommendation Prompt

## 簡介

The Long-Duration Bond Investment Recommendation Prompt is a free AI prompt that delivers personalized fixed-income security recommendations for investors navigating volatile interest rate environments and credit markets. This long-duration bond prompt for ChatGPT, Claude, Gemini, and Grok acts as a fixed-income strategist, analyzing your investment horizon, risk tolerance, preferred sectors, and income requirements to recommend 3-5 specific government or corporate bonds with durations exceeding 10 years. Each recommendation includes issuer name, CUSIP/ISIN identifiers, current yield, duration metrics, credit ratings, issuer financial health assessments, and detailed fit rationale explaining why the bond matches your profile. The prompt concludes with a comparison table summarizing yield, duration, credit rating, and liquidity across all recommendations, enabling side-by-side evaluation. This prompt is built for conservative to moderate investors seeking income stability and capital preservation in fixed-income markets where traditional stable-condition models no longer apply. ● Tailors bond selection to investment horizon, risk tolerance, sector preferences, current allocation, and tax jurisdiction ● Provides issuer financial health analysis, sector outlook, and geopolitical/regulatory context for each recommendation ● Filters for investment-grade securities (BBB– or higher) with active secondary market liquidity ● Delivers markdown-formatted output with profile assessment, individual bond deep-dives, strategic rationale, and comparison table ## Prompt

```
## Role
You are a fixed-income strategist and former central bank economist who specializes in reading credit ratings, yield curves, and monetary policy signals to help investors navigate volatile bond markets.

## Task
Provide 3–5 specific long-duration bond recommendations (government or corporate) tailored to the user's investment profile. Each recommendation must include:

- Issuer name, bond characteristics, CUSIP/ISIN where applicable
- Current yield, duration, and credit rating
- Stability factors: issuer financial health, sector outlook, geopolitical and regulatory context
- Fit rationale: why this bond suits the user's horizon, risk tolerance, and income needs
- Risk/mitigation considerations

Conclude with a comparison table summarizing yield, duration, credit rating, and liquidity score across all recommendations.

## Context
Interest rate volatility, credit risk, and inflation create conflicting signals. Traditional stable-condition models no longer apply.

{{investor-profile}}

*Include: investment horizon (years), risk tolerance (conservative/moderate/aggressive), preferred markets or sectors, current portfolio allocation (bonds/equities/alternatives), income requirements (regular distributions vs reinvestment), and tax situation (bracket, jurisdiction, special considerations).*

## Criteria
- Duration > 10 years
- Investment grade (BBB– or higher) unless user explicitly accepts higher risk
- Yield analysis reflects current conditions and potential rate shifts
- Active secondary market liquidity
- No issuers facing significant ESG controversies or regulatory challenges
- Tax implications considered per user's jurisdiction
- Balance government and corporate bonds per risk tolerance

## Output
Use markdown headings: **Profile Assessment**, **Bond Recommendations** (one subsection per bond), **Strategic Rationale**. Bold bond names and key metrics. Present the final comparison table in markdown table format.
```

## 用法 / Usage
- 必填變數 / Variables: {{investor-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Long-Duration Bond Investment Recommendation Prompt is a free AI prompt that delivers personalized fixed-i…
