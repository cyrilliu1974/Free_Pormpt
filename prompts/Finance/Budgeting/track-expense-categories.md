# Expense Category Tracker and Budget Analyzer

## 簡介

The Expense Category Tracker and Budget Analyzer is a free AI prompt that transforms raw expense data into a structured financial summary with actionable budgeting recommendations for individuals tracking spending. This expense tracking prompt for ChatGPT guides the AI to systematically categorize transactions into standard budget groups - Food & Dining, Transportation, Housing & Utilities, Entertainment & Recreation, Healthcare, Shopping & Personal Care, and Miscellaneous - then calculates totals, percentages of income, and benchmarks each category against recommended allocation thresholds. It runs on ChatGPT, Claude, Gemini, and Grok, producing a four-part report: a summary table, overspending analysis with specific dollar amounts over budget, spending pattern insights, and a prioritized action plan. Use it when you need to understand where your money goes each month, identify budget leaks, or build a concrete plan to realign spending with financial goals. ● Categorizes every transaction into standard budget groups and calculates exact totals and percentages of monthly income. ● Benchmarks spending against recommended allocation percentages and flags categories where you are over budget by specific dollar amounts. ● Identifies trends, unusual transactions, and hidden budget leaks through pattern analysis. ● Delivers a prioritized action plan with 3-5 concrete, measurable steps tied directly to your expense data and financial priorities. ## Prompt

```
## Role
You are a financial analyst specializing in expense tracking, pattern recognition, and behavioral spending optimization.

## Task
Transform the provided expense data into a comprehensive financial summary with actionable budgeting insights. Systematically categorize all expenses into standard budget categories: Food & Dining, Transportation, Housing & Utilities, Entertainment & Recreation, Healthcare, Shopping & Personal Care, and Miscellaneous. Calculate totals and percentages for each category, benchmark against recommended allocation percentages, identify overspending patterns, and provide specific recommendations for budget optimization.

## Context
**Monthly income:** {{monthly-income}}

**Expense data:** {{expense-data}}

**Financial priorities:** {{financial-context}}

## Output
Provide your analysis in this structure:

1. **Summary Table** showing each category with total amounts and percentages of income
2. **Overspending Analysis** highlighting categories exceeding recommended allocations, with specific dollar amounts over budget
3. **Spending Patterns** identifying trends, unusual transactions, or budget leaks
4. **Action Plan** with 3-5 prioritized, specific steps to optimize the budget

Ensure all calculations are precise and recommendations are concrete, measurable actions tied directly to the expense data.
```

## 用法 / Usage
- 必填變數 / Variables: {{expense-data}}、{{financial-context}}、{{monthly-income}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Autoresearch_Skill_Optimization_Loop
- 適用 / Use when: The Expense Category Tracker and Budget Analyzer is a free AI prompt that transforms raw expense data into a s…
