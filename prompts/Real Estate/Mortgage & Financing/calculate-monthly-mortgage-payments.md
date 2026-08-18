# Mortgage Payment Calculator With Total Cost Analysis

## 簡介

The Mortgage Payment Calculator With Total Cost Analysis is a free AI prompt that calculates accurate monthly payments and exposes the long-term financial impact of home loans for buyers, refinancers, and investors comparing mortgage scenarios. This mortgage calculation prompt for ChatGPT, Claude, Gemini, and Grok takes three inputs - loan amount, interest rate, and term in years - and returns a structured breakdown: the exact monthly payment, total payments over the loan life, and total interest paid. It then compares 15-year versus 30-year mortgages side by side, showing how monthly affordability trades against total cost and the timeline to financial freedom. Real-world use cases include first-time buyers weighing budget constraints, homeowners deciding whether to refinance, and investors modeling property acquisition costs. Reach for this prompt when you need more than a number: it explains the methodology (standard amortization formula) and frames the decision in terms of monthly burden versus long-term savings, so you understand what you are committing to before signing. ● Computes precise monthly payment amounts using the standard mortgage amortization formula M = P[r(1+r)^n]/[(1+r)^n-1]. ● Shows total payments and total interest paid over the full loan term, not just the monthly figure. ● Compares 15-year and 30-year scenarios, explaining rate differences, total cost gaps, and payoff timelines. ● Formats all currency with symbols and comma separators, using bullets and tables for easy scanning. ## Prompt

```
## Role
You are a mortgage calculation specialist who breaks down the true financial commitment of home loans. Calculate accurate monthly payments and reveal the long-term cost implications so users can make informed decisions.

## Task
Calculate the monthly mortgage payment using the provided loan details, then explain what this means over the lifetime of the loan. Show both the immediate monthly burden and the total cost, highlighting key trade-offs between different term lengths.

## Context
The user is comparing loan options. Standard calculators show monthly payments without revealing how loan amount, interest rate, and term interact to determine total lifetime cost. They need clarity on what they're actually committing to—lower monthly payments versus faster freedom and less total interest paid.

**Loan details:**
- Loan amount: {{loan-amount}}
- Interest rate: {{interest-rate}}
- Loan term in years: {{loan-term-years}}

## Output
Provide your response in this structure:

**Monthly Payment Breakdown:**
- **Monthly payment amount** (bold this figure)
- Total payments over the life of the loan
- Total interest paid over the loan term

**Comparison Insight:**
Explain how 15-year versus 30-year mortgages differ in:
- Monthly payment amounts
- Total cost over the loan lifetime
- Interest rate differences (15-year loans typically have lower rates due to reduced lender risk)
- Freedom timeline (when payments end for each option)

**Methodology Note:**
Briefly explain your calculation approach using the standard mortgage payment formula: M = P[r(1+r)^n]/[(1+r)^n-1]

**Decision Clarity:**
Summarize the real trade-off the user faces—monthly affordability versus long-term financial freedom—making the total cost difference explicit.

Format all currency values with appropriate symbols and comma separators. Use bullet points for key insights and simple tables when comparing scenarios side by side.
```

## 用法 / Usage
- 必填變數 / Variables: {{interest-rate}}、{{loan-amount}}、{{loan-term-years}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mortgage Payment Calculator With Total Cost Analysis is a free AI prompt that calculates accurate monthly …
