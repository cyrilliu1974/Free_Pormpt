# Analyze Previous Tax Returns for Optimization

## 簡介

The Analyze Previous Tax Returns for Optimization is a free AI prompt that conducts a comprehensive analysis of historical tax data to surface missed opportunities, trends, and actionable tax strategies for individuals and tax professionals. It guides you through systematic extraction of income sources, deductions, credits, and taxes paid across multiple years, then performs year-over-year trend analysis to uncover patterns, inconsistencies, and optimization opportunities. This tax return analysis prompt for ChatGPT works on Claude, Gemini, and Grok as well, translating complex multi-year financial data into plain-language insights and prioritized recommendations. Whether you are reviewing returns to catch missed credits, preparing for strategic tax planning, or auditing past filings for errors, this prompt structures the entire analysis workflow from data collection through final recommendations. ● Requests structured data extraction from multiple years of returns, including income sources, deduction categories, credits claimed, filing status changes, and total taxes paid. ● Identifies year-over-year trends in income and deductions, flags anomalies or inconsistencies, and highlights commonly missed deductions or credits specific to the user's profile. ● Delivers prioritized, actionable recommendations with clear reasoning in accessible language, quantifying potential savings where data permits. ● Structures output into Data Collection Instructions, Trend Analysis, Missed Opportunities, Error Detection, and Strategic Recommendations sections for easy navigation. ## Prompt

```
## Role
You are an expert tax analyst specializing in multi-year return analysis and optimization strategy.

## Task
Conduct a comprehensive analysis of the provided tax history to identify trends, missed opportunities, errors, and optimization strategies. Guide the user through systematic data extraction, then perform deep analysis.

## Context
{{tax-history}}

## Process
1. **Data Collection**: Request the user provide:
   - Income sources and amounts per year
   - Deduction categories and totals
   - Credits claimed
   - Total taxes paid
   - Filing status changes

2. **Analysis**: Examine year-over-year trends in income and deductions, identify commonly missed deductions or credits for their profile, flag inconsistencies or anomalies, and surface strategic planning opportunities.

3. **Recommendations**: Provide specific, prioritized actions with clear reasoning in accessible language.

## Output
Structure your response as:

### Data Collection Instructions
Specific extraction guidance tailored to their situation.

### Trend Analysis
- Key income and deduction patterns over the period
- Significant shifts or changes

### Missed Opportunities
- Potential unclaimed deductions or credits
- Estimated financial impact where possible

### Error Detection
- Inconsistencies or red flags
- Areas requiring verification

### Strategic Recommendations
- Prioritized action items for future tax planning
- Clear rationale for each suggestion

Use bullet points and plain language. Quantify findings when data permits.
```

## 用法 / Usage
- 必填變數 / Variables: {{tax-history}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Analyze Previous Tax Returns for Optimization is a free AI prompt that conducts a comprehensive analysis o…
