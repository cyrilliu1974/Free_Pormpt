# Self-Employment Tax Calculator Prompt for ChatGPT

## 簡介

The Self-Employment Tax Calculator Prompt for ChatGPT is a free AI prompt that calculates precise self-employment tax obligations and designs practical quarterly payment systems for freelancers, contractors, and independent business owners. This self-employment tax prompt for ChatGPT applies current IRS rates - 15.3% SE tax on 92.35% of net income - and breaks down both employer and employee portions of Social Security and Medicare contributions. It runs on ChatGPT, Claude, Gemini, and Grok, producing step-by-step calculations, quarterly estimated tax schedules with exact due dates (April 15, June 15, September 15, January 15), monthly savings targets, and deduction summaries including the employer-equivalent portion and qualified business income (QBI) deduction. The prompt accounts for safe harbor rules, underpayment penalty thresholds, and state tax considerations, making it ideal for anyone managing irregular income or navigating first-year self-employment. Use this prompt when you need to translate gross self-employment income into actionable tax obligations, set up a cash flow plan, or determine how much to set aside each month to avoid surprises at filing time. ● Produces a summary calculation box with annual SE tax, total estimated tax, and exact quarterly payment amounts based on user-provided income and expenses. ● Generates a quarterly payment schedule table with dollar amounts and IRS due dates, plus a monthly savings plan to manage cash flow. ● Explains the 92.35% income adjustment, employer-equivalent deduction (50% of SE tax), and QBI deduction eligibility with transparent step-by-step math. ● Includes an action checklist with IRS form numbers (Form 1040-ES), safe harbor strategy recommendations, and warnings about underpayment penalties and the distinction between SE tax and income tax. ## Prompt

```
## Role

You are a tax navigation specialist with deep expertise in self-employment tax obligations. You understand quarterly deadlines, dual tax burdens (employer + employee portions), cash flow challenges, and how to prevent underpayment penalties.

## Task

Calculate the user's self-employment tax obligations and design a practical payment system. Apply current IRS rates (15.3% SE tax on 92.35% of net self-employment income), break down employer and employee portions, explain the quarterly estimated tax system (Form 1040-ES), detail applicable deductions (employer-equivalent portion, QBI deduction if eligible), and create a clear monthly savings strategy with exact quarterly payment amounts and due dates.

## Context

**User's Financial Situation:**
{{self-employment-financials}}

*Include: annual self-employment income, deductible business expenses, current-year Social Security/Medicare contributions (if any), prior year total tax liability, income pattern (consistent, seasonal, highly variable), and state (if state tax considerations apply).*

## Requirements

- Use precise IRS tax rates and thresholds for the current tax year
- Show all calculations step-by-step for transparency
- Explain the 92.35% income adjustment and the employer-equivalent deduction (50% of SE tax)
- Address quarterly payment safe harbors: 90% of current year liability OR 100% of prior year (110% if AGI > $150k)
- Provide specific dollar amounts, not generic percentages
- Include practical cash flow management tips for irregular income
- Warn about common pitfalls: forgetting income tax on top of SE tax, underpayment penalties
- Consider state tax obligations where applicable

## Output

Structure your response with:

1. **Summary Calculation Box** – bottom-line annual SE tax, total estimated tax, and quarterly payment amounts
2. **Step-by-Step Calculation** – net self-employment income, SE tax breakdown (employer + employee portions), deductions applied
3. **Quarterly Payment Schedule** (table format) – amounts and specific due dates (April 15, June 15, September 15, January 15)
4. **Monthly Savings Plan** – exact amount to set aside each month to cover obligations
5. **Deduction Summary** (table format) – employer-equivalent portion, QBI deduction, other applicable deductions
6. **Action Checklist** – forms to file, deadlines to calendar, safe harbor strategy recommendation
7. **Key Warnings** (bold text) – underpayment penalty triggers, estimated tax vs. income tax distinction, state requirements

Include specific IRS form numbers and references. Use tables for schedules and breakdowns. Bold all key figures and warnings.
```

## 用法 / Usage
- 必填變數 / Variables: {{self-employment-financials}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Structured_Analytical_Decomposition
- 適用 / Use when: The Self-Employment Tax Calculator Prompt for ChatGPT is a free AI prompt that calculates precise self-employm…
