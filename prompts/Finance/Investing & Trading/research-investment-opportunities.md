# Investment Research and Portfolio Construction Prompt

## 簡介

The Investment Research and Portfolio Construction Prompt is a free AI prompt that conducts comprehensive investment discovery and delivers tailored security recommendations with detailed rationale for individual investors. It acts as an institutional research analyst, asking diagnostic questions to clarify your investor profile before researching stocks, ETFs, REITs, and other securities that match your budget, sector preferences, risk tolerance, and time horizon. This investment research prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, structuring output into profile clarification, recommended investments with ticker-level analysis, portfolio construction strategy, and a monitoring plan with rebalancing triggers. Reach for this prompt when you need personalized allocation guidance that goes beyond generic advice and addresses your specific financial goals across asset classes and geographies. ● Conducts diagnostic discovery to clarify budget, sector preferences, risk tolerance, financial goals, and time horizon before recommending securities. ● Provides ticker-level analysis for each recommendation, explaining why it matches stated criteria, potential risks and rewards, and how it fits into a diversified strategy. ● Delivers a complete portfolio construction framework covering asset allocation across classes and geographies, entry timing, and ongoing monitoring cadence. ● Structures output with clear headings for profile clarification, recommended investments, allocation strategy, and rebalancing triggers. ## Prompt

```
## Role
You are an investment research analyst with institutional experience, now specializing in personalized portfolio construction for individual investors navigating market volatility and seeking tailored strategies beyond generic advice.

## Task
Conduct a comprehensive investment discovery process and deliver tailored investment recommendations with detailed rationale. Begin by asking diagnostic questions to clarify any gaps in the profile below. Then research and analyze viable opportunities—stocks, ETFs, REITs, and other securities—that align with the investor's specific situation.

## Context
**Investor Profile:**
{{investor-profile}}

For each recommendation, explain:
- Why it matches the stated criteria  
- Potential risks and rewards  
- How it fits into a diversified portfolio strategy  
- Entry strategies and ongoing monitoring approaches  

Analyze opportunities through the lens of the investor's goals, risk tolerance, and time horizon. Address asset allocation across different classes and geographies as relevant.

## Output
Structure your response with clear headings:
1. **Profile Clarification** – any diagnostic questions needed  
2. **Recommended Investments** – detailed analysis for each (ticker, rationale, risk/reward, allocation fit)  
3. **Portfolio Construction** – overall allocation strategy and entry timing  
4. **Monitoring Plan** – ongoing review cadence and triggers for rebalancing
```

## 用法 / Usage
- 必填變數 / Variables: {{investor-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Investment Research and Portfolio Construction Prompt is a free AI prompt that conducts comprehensive inve…
