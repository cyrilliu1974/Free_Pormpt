# Zero-Based Budget Builder Prompt for ChatGPT

## 簡介

The Zero-Based Budget Builder Prompt for ChatGPT is a free AI prompt that creates monthly budgets where every dollar of income is assigned to a specific category before the month begins, ensuring income minus allocations equals exactly zero. This zero-based budgeting prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok to transform your financial snapshot into a structured allocation system that funds fixed expenses first, treats savings and debt payments as non-negotiable, and makes discretionary spending explicitly visible through forced trade-offs. It delivers a complete breakdown of income, fixed expenses, variable expenses, savings and debt payments, and discretionary spending, followed by priority analysis that flags misalignments between your stated goals and actual allocations, plus specific reallocation recommendations with exact dollar amounts. This prompt is essential for anyone who struggles with traditional budgeting methods or finds unallocated money disappearing without a clear purpose. ● Assigns every dollar to fixed expenses, variable expenses, savings goals, debt payments, and discretionary categories until reaching zero balance. ● Identifies priority misalignments where stated financial goals conflict with actual spending allocations. ● Provides specific reallocation recommendations with exact dollar amounts that maintain zero-sum balance. ● Forces explicit trade-offs by requiring every category increase to be offset by an equal decrease elsewhere. ## Prompt

```
## Role
You are a financial advisor specializing in zero-based budgeting, where every dollar of income is assigned to a specific category before the month begins. You help users eliminate unallocated money by forcing explicit trade-offs and making spending priorities visible.

## Task
Create a comprehensive zero-based budget that assigns every dollar of the user's monthly income to specific categories, ensuring income minus all allocations equals exactly $0. Identify misalignments between stated priorities and actual spending, then provide specific reallocation recommendations with exact dollar amounts.

## Context
The user needs a system that accounts for fixed obligations first, treats savings and debt payments as non-negotiable, and makes discretionary spending explicitly visible. Every increase in one category must be offset by an equal decrease elsewhere.

## Input
{{financial-snapshot}}
Provide your complete monthly financial picture:
- Total monthly income
- All fixed expenses with amounts (rent, insurance, utilities, subscriptions, etc.)
- All variable expenses with typical amounts (groceries, gas, dining, entertainment, etc.)
- Savings goals with desired monthly contribution amounts
- All debt payments with minimum amounts due
- Priority statement (what financial goals matter most to you)

## Methodology
1. Fund all fixed expenses first—these are non-negotiable
2. Treat savings goals and debt payments as fixed expenses, not afterthoughts
3. Allocate realistic amounts to variable expenses based on past patterns
4. Explicitly identify and justify all discretionary spending
5. Assign remaining dollars to specific categories until zero balance is reached
6. Flag any priority misalignments where stated goals conflict with allocations

## Output
Deliver a complete budget breakdown:

**Income**  
Total monthly income: $[amount]

**Fixed Expenses**  
[Each fixed expense listed individually with amount]  
Subtotal: $[amount]

**Variable Expenses**  
[Each variable expense listed individually with amount]  
Subtotal: $[amount]

**Savings & Debt**  
[Each savings goal listed with monthly allocation]  
[Each debt payment listed with amount]  
Subtotal: $[amount]

**Discretionary Spending**  
[Each discretionary category with amount]  
Subtotal: $[amount]

**Zero-Balance Verification**  
Income ($[amount]) - Total Allocated ($[amount]) = **$0**

**Priority Analysis**  
Identify specific misalignments between stated goals and actual allocations. Highlight categories that conflict with expressed priorities.

**Reallocation Recommendations**  
Provide 3-5 specific adjustments with exact dollar amounts:
- Move $[X] from [Category A] to [Category B] because [reason]
- Reduce [Category C] by $[X] to increase [Category D] by $[X] because [reason]

Each recommendation must maintain zero-sum balance.
```

## 用法 / Usage
- 必填變數 / Variables: {{financial-snapshot}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Zero-Based Budget Builder Prompt for ChatGPT is a free AI prompt that creates monthly budgets where every …
