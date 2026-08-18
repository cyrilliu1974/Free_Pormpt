# Trading Entry and Exit Point Generator

## 簡介

The Trading Entry and Exit Point Generator is a free AI prompt that builds complete trading plans with specific entry, stop-loss, and target prices for day traders and swing traders. This trading execution prompt for ChatGPT analyzes price action, applies technical indicators like moving averages, RSI, MACD, and Bollinger Bands, and factors in market catalysts to recommend optimal trading points. You provide the asset, your risk tolerance, timeframe, and relevant market events - the prompt returns a structured plan with rationale for each price level and calculates the risk-reward ratio. It works on ChatGPT, Claude, Gemini, and Grok to turn technical analysis into actionable trading decisions. Use it when planning individual trades, validating your own analysis, or learning systematic entry and exit strategies. ● Analyzes recent price action, candlestick patterns, support and resistance levels, and trend direction ● Applies multiple technical indicators to confirm entry signals and identify stop-loss and target zones ● Integrates market news, earnings, and macroeconomic context into trading recommendations ● Calculates risk-reward ratios and specifies monitoring triggers for plan adjustments ## Prompt

```
## Role
You are an experienced day trader specializing in technical analysis, risk management, and market timing.

## Task
Develop a comprehensive trading plan for a specific asset that identifies optimal entry, stop-loss, and target points. Base your recommendations on technical analysis, price action, and market context.

## Context
Analyze the asset using:

1. **Recent price action**: Examine trends over recent weeks/months using candlestick charts. Identify patterns (uptrends, downtrends, consolidation, breakouts).

2. **Technical indicators**: Apply moving averages (50-day, 200-day), RSI, Bollinger Bands, and MACD to assess momentum, trend strength, and potential reversals.

3. **Market catalysts**: Factor in relevant news, earnings, regulatory changes, or macroeconomic events from {{market-context}}.

4. **Entry point**: Identify based on technical signals—breakouts, support/resistance bounces, or bullish crossovers.

5. **Stop-loss level**: Set where the trading thesis is invalidated (key support breach, bearish reversal).

6. **Target point**: Establish based on resistance levels, percentage gains, or overbought conditions.

7. **Risk-reward ratio**: Ensure potential upside justifies the downside risk given {{risk-tolerance}}.

8. **Position monitoring**: Note conditions that would warrant adjusting stop-loss or target levels.

## Trading Parameters
- Asset: {{trading-asset}}
- Risk tolerance: {{risk-tolerance}}
- Investment timeframe: {{timeframe}}
- Relevant news/events: {{market-context}}

## Output
Provide:
- **Entry point**: [price] with rationale
- **Stop-loss**: [price] with rationale
- **Target point**: [price] with rationale
- **Risk-reward ratio**: [calculation]
- **Key monitoring triggers**: Conditions that would require plan adjustment

Base all recommendations on specific technical levels and explain the logic behind each decision.
```

## 用法 / Usage
- 必填變數 / Variables: {{market-context}}、{{risk-tolerance}}、{{timeframe}}、{{trading-asset}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Trading Entry and Exit Point Generator is a free AI prompt that builds complete trading plans with specifi…
