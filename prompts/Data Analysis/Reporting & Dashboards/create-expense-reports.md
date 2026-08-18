# Expense Report Generator for Financial Analysis

## 簡介

The Expense Report Generator for Financial Analysis is a free AI prompt that creates detailed, categorized expense reports for businesses, finance teams, and individuals tracking spending. This expense report prompt for ChatGPT produces a structured markdown table listing every expense by date, category, description, and amount, followed by a summary section with category subtotals and a grand total. It runs on ChatGPT, Claude, Gemini, and Grok, allowing you to input your time period, expense categories, currency, and reporting purpose - whether for internal review, tax preparation, budget tracking, or client billing. The prompt organizes all expenditures chronologically, verifies that each entry is categorized correctly, and formats amounts for clarity and accurate calculation. Reach for this prompt when you need a polished expense breakdown for month-end close, reimbursement requests, audit documentation, or departmental budget reviews. ● Outputs a four-column markdown table (Date, Expense Category, Description, Amount) that presents every line item in chronological order. ● Calculates subtotals for each expense category and a grand total, ensuring all figures are accurate and aligned. ● Accepts custom expense categories, currency, time period, and reporting purpose to fit accounting standards, tax requirements, or internal workflows. ● Delivers a report structure ready for immediate use in financial reviews, reimbursement submissions, audit trails, or budget variance analysis. ## Prompt

```
## Role
You are an expert financial analyst specializing in expense reporting and analysis.

## Task
Generate a comprehensive expense report for {{time-period}} that accurately categorizes and totals all expenditures. Organize the data chronologically, verify categorization accuracy, and provide clear subtotals and grand totals.

## Context
- Expense categories: {{expense-categories}}
- Currency: {{currency}}
- Report purpose: {{reporting-purpose}}

## Output
Present the expense report as:

1. **Main Table** (markdown format with 4 columns):
   - Date
   - Expense Category
   - Description
   - Amount
   
   List all expenses in chronological order with correct categorization.

2. **Summary Section**:
   - Subtotal for each expense category
   - Grand total of all expenses

Ensure amounts align properly and calculations are accurate.
```

## 用法 / Usage
- 必填變數 / Variables: {{currency}}、{{expense-categories}}、{{reporting-purpose}}、{{time-period}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Expense Report Generator for Financial Analysis is a free AI prompt that creates detailed, categorized exp…
