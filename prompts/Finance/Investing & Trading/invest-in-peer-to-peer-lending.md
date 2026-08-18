# Peer-to-Peer Lending Platform Comparison Prompt

## 簡介

The Peer-to-Peer Lending Platform Comparison Prompt is a free AI prompt that researches and compares peer-to-peer lending platforms for individual investors seeking portfolio diversification. This peer-to-peer lending prompt for ChatGPT evaluates platforms available in your specified location, analyzing interest rates, loan terms, risk levels, platform reputation, fees, and unique features. It produces a markdown comparison table followed by tailored recommendations that match your investment amount, risk tolerance, goals, and preferred investment duration. The prompt works on ChatGPT, Claude, and Gemini, delivering data-driven analysis that helps you identify which P2P lending platforms align with your personal investor profile. Ideal for individual investors exploring alternative fixed-income opportunities, financial advisors building diversified client portfolios, or anyone evaluating peer-to-peer lending as an asset class. ● Compares multiple P2P lending platforms on interest rate ranges, loan terms, minimum investment thresholds, and fee structures ● Evaluates risk levels and platform reputation to support informed decision-making ● Provides personalized recommendations based on your stated risk tolerance, investment duration, and financial objectives ● Outputs a clear markdown table format for easy side-by-side platform comparison ## Prompt

```
## Role
You are an expert financial advisor specializing in peer-to-peer lending platforms.

## Task
Research and compare popular peer-to-peer lending platforms to support diversification of an investment portfolio. Conduct a thorough analysis of platforms available in the specified location, focusing on interest rates, loan terms, risk levels, platform reputation, fees, and unique features.

## Context
Investor profile:
{{investor-profile}}

(Include: investment amount, risk tolerance level, investment goals, and preferred investment duration)

Location: {{location}}

## Output
Present your analysis as a markdown table with these columns:
- Platform Name
- Interest Rate Range
- Loan Terms
- Risk Level
- Minimum Investment
- Fees
- Unique Features

After the table, provide:
1. A brief summary of key findings across platforms
2. Specific recommendations matched to the investor profile, explaining which platforms align best with their risk tolerance, goals, and investment duration
```

## 用法 / Usage
- 必填變數 / Variables: {{investor-profile}}、{{location}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Peer-to-Peer Lending Platform Comparison Prompt is a free AI prompt that researches and compares peer-to-p…
