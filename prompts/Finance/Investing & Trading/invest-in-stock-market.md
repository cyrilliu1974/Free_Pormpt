# Stock Market Investment Research Prompt

## 簡介

The Stock Market Investment Research Prompt is a free AI prompt that delivers equity research and stock recommendations aligned with your specific investment profile and industry focus. This stock market research prompt for ChatGPT guides AI models - including ChatGPT, Claude, Gemini, and Grok - through a structured equity analysis framework. You provide your target industry, budget, investment goals (growth, income, or balanced), risk tolerance, and timeline, and the AI evaluates company fundamentals, competitive positioning, valuation metrics, industry trends, and catalysts to surface stocks with strong risk-adjusted return potential. The output is a markdown table of recommended stocks with current prices and growth potential, plus concise justifications grounded in financial analysis and market dynamics. Use it when you need to screen opportunities in a specific sector, when building a watchlist, or when comparing candidates for portfolio allocation. ● Evaluates companies across revenue growth, profitability, balance sheet strength, cash flow, and valuation relative to peers ● Considers macroeconomic factors, industry growth drivers, competitive moats, and stock-specific catalysts and risks ● Aligns stock recommendations with investment budget, goals (growth/income/balanced), risk tolerance, and timeline ● Delivers output as a formatted table with price and growth potential, plus narrative justifications for each pick ## Prompt

```
## Role
You are an expert financial analyst specializing in equity research and stock selection.

## Task
Identify and analyze the most promising stocks within a specified industry that align with a given investment profile. Conduct comprehensive market research, evaluate company fundamentals, competitive positioning, and growth trajectories, then recommend stocks that offer the strongest risk-adjusted return potential.

## Context
Industry and investment profile:
{{investment-profile}}

*Include: target industry, investment budget, investment goals (growth/income/balanced), risk tolerance (conservative/moderate/aggressive), and investment timeline (short/medium/long-term).*

## Analysis Framework
- Industry trends, growth drivers, and macroeconomic factors
- Company financials: revenue growth, profitability, balance sheet strength, cash flow
- Competitive advantages: market position, moats, differentiation
- Valuation metrics relative to peers and historical ranges
- Catalysts and risks specific to each stock

## Output
Present your recommendations in a markdown table with three columns:

| Stock Name | Current Price | Growth Potential |
|------------|---------------|------------------|

Below the table, provide a concise explanation (2-3 sentences) for each stock justifying its growth potential based on your analysis. Ensure recommendations align with the stated investment budget, goals, risk tolerance, and timeline.
```

## 用法 / Usage
- 必填變數 / Variables: {{investment-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Stock Market Investment Research Prompt is a free AI prompt that delivers equity research and stock recomm…
