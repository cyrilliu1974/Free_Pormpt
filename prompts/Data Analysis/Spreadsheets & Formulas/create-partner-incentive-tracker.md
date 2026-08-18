# Partner Incentive Tracker Spreadsheet Builder

## 簡介

The Partner Incentive Tracker Spreadsheet Builder is a free AI prompt that generates a formatted tracking table for businesses managing partner incentive programs. This partner incentive tracker prompt for ChatGPT builds a five-column spreadsheet structure that captures partner names, incentive types (discounts, rebates, promotional items), program start and end dates, and three key performance metrics: sales volume, new customer acquisition counts, and revenue growth percentages. The prompt automatically applies conditional formatting rules that highlight upcoming program dates in blue, expiring or past deadlines in red, and results that meet or exceed your custom thresholds in green. It runs on ChatGPT, Claude, and Gemini, delivering clean table structures ready for Google Sheets, Excel, or Airtable. Reach for this prompt when you need to monitor multiple partner programs simultaneously, compare incentive effectiveness across different partners, or quickly identify which programs require attention based on approaching deadlines or performance metrics. ● Tracks five essential data points per partner program: name, incentive type, start date, end date, and three-metric results ● Applies color-coded conditional formatting that flags programs starting soon (blue), ending soon (red), and hitting targets (green) ● Accepts custom thresholds for sales volume, new customer count, and revenue growth percentage to match your business goals ● Outputs clean table structures with explicit formatting rules you can implement in any spreadsheet platform ## Prompt

```
## Role
You are a spreadsheet specialist designing data tracking solutions for business operations.

## Task
Create a partner incentive tracking table with these columns:

1. **Partner Name**: Organization or individual partner
2. **Incentive Type**: Type of incentive (discount, rebate, promotional item, etc.)
3. **Start Date**: Program start date (YYYY-MM-DD format)
4. **End Date**: Program end date (YYYY-MM-DD format)
5. **Results**: Three metrics:
   - Sales volume (total units/revenue during incentive period)
   - New customers acquired (count during incentive period)
   - Revenue growth (percentage increase vs. previous period)

## Conditional Formatting Rules
- **Start Date**: Highlight blue if within next 30 days
- **End Date**: Highlight red if within next 7 days or already passed
- **Results**: Highlight green if meeting or exceeding these thresholds:
  - Sales volume: {{sales-volume-target}}
  - New customers: {{new-customer-target}}
  - Revenue growth: {{revenue-growth-target}}

## Output
Deliver the table structure with column headers and formatting rules applied. Include no additional explanations.
```

## 用法 / Usage
- 必填變數 / Variables: {{new-customer-target}}、{{revenue-growth-target}}、{{sales-volume-target}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Prompt_Assembly_Audit_Engine
- 適用 / Use when: The Partner Incentive Tracker Spreadsheet Builder is a free AI prompt that generates a formatted tracking tabl…
