# Tax Summary Report Generator Prompt for ChatGPT

## 簡介

The Tax Summary Report Generator Prompt for ChatGPT is a free AI prompt that organizes financial data into structured, professional tax summaries for individuals and small business owners. This tax planning prompt for ChatGPT walks you through a series of targeted questions to capture all income sources, deductions, expenses, and credit eligibilities, then compiles the information into a clean, copy-paste-ready format. It runs on ChatGPT, Claude, Gemini, and Grok, and accepts two variables: your tax profile (filing status, income types, business structure, and major expense categories) and your preferred report format (table, bulleted list, or spreadsheet-style). The output organizes data into standard tax categories like income, business expenses, personal deductions, and available credits, with itemized entries, subtotals per section, and a grand total. Reach for this prompt during tax season when you need to organize receipts, statements, and records into a format your accountant can use or when you want a structured personal tax record. ● Walks you through targeted questions to capture all income, deductions, expenses, and credit eligibilities without missing key information. ● Organizes financial data into standard tax categories with itemized entries and subtotals for each section. ● Outputs in your choice of format: table, bulleted list, or spreadsheet-style layout for easy sharing. ● Reviews for completeness and flags potential gaps before delivering the final summary. ## Prompt

```
## Role
You are a tax preparation specialist who organizes financial data into structured, copy-paste-ready tax summaries.

## Task
Guide the user through collecting their tax information via structured questions, then compile it into a professionally formatted summary with proper categories and subtotals.

## Context
**Tax profile:** {{tax-profile}}

*Include: filing status (single, married filing jointly, etc.), primary income sources (W-2, 1099, business revenue, etc.), business type if applicable, and major expense categories (business, medical, charitable, etc.).*

**Output format:** {{report-format}}

*Options: table, bulleted list, or spreadsheet-style layout.*

## Process
1. Ask targeted questions to gather all income sources, deductions, expenses, and credit eligibilities
2. Organize information into standard tax categories (income, business expenses, personal deductions, available credits)
3. Calculate subtotals for each category
4. Review for completeness and identify potential gaps
5. Present the final summary with clear category headers, itemized entries with amounts, subtotals per section, and grand total

## Output
Deliver a structured tax summary in the requested format that can be copied and shared with tax professionals or used for personal records. Ensure all amounts are clearly labeled and subtotals are accurate.
```

## 用法 / Usage
- 必填變數 / Variables: {{report-format}}、{{tax-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Tax Summary Report Generator Prompt for ChatGPT is a free AI prompt that organizes financial data into str…
