# Sales Incentive Tracker Table Generator

## 簡介

The Sales Incentive Tracker Table Generator is a free AI prompt that creates customizable tracking tables for monitoring sales team performance and incentive progress. This sales incentive tracking prompt for ChatGPT takes your company name and team incentive structure as input, then outputs a formatted markdown table with columns for salesperson names, incentive descriptions, target amounts, and visual progress bars built from filled and empty Unicode blocks. The table includes a key for interpreting achievement percentages and a reference list of common incentive types - cash bonuses, PTO rewards, gift cards, sales retreats, and commission multipliers - customized to match your actual compensation program. Sales managers use it to create clear, at-a-glance dashboards that show where each team member stands against quota and what rewards they are working toward. The prompt runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need a simple, shareable format to communicate incentive performance to your sales team or leadership, or when building quarterly sales reports. ● Outputs markdown tables that render in Slack, Notion, Confluence, GitHub, and most documentation platforms ● Includes visual progress bars using Unicode block characters, making achievement status immediately clear ● Generates a reference list of incentive types tailored to your company's actual rewards program ● Provides usage instructions so team members can update achievement percentages as sales progress ## Prompt

```
## Role
You are an expert sales incentive program designer with deep knowledge of compensation structures that drive sales performance.

## Task
Create a comprehensive sales incentive tracking table that allows easy monitoring of each salesperson's progress toward targets and the incentives they can earn. Provide a clear, visually intuitive format that sales managers can use to optimize team performance.

## Input
Company name: {{company-name}}

Sales team and incentive structure: {{team-and-incentives}}
(Include: salesperson names, their assigned incentive types, target amounts or quotas, and current achievement percentages)

## Output
Generate a markdown table with these columns:
- **Salesperson** – team member name
- **Incentive** – reward description
- **Target** – goal amount or quantity
- **Achievement** – progress bar showing percentage of target achieved using filled blocks (▓) and empty blocks (░)

Include a **Key** explaining the progress bar scale (100% = ▓▓▓▓▓▓, 0% = ░░░░░░).

Provide an **Incentive Types** reference list with examples:
- Cash Bonus: $X for reaching Y% of target
- Additional PTO: X days for reaching Y% of target
- Gift Card: $X for [retailer] for reaching Y% of target
- Sales Retreat: All-expenses-paid trip for top X% of team
- Commission Multiplier: X% boost on commissions for exceeding target by Y%

Customize all examples to match the company's actual rewards program. Include brief usage instructions for updating and interpreting the table.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-name}}、{{team-and-incentives}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sales Incentive Tracker Table Generator is a free AI prompt that creates customizable tracking tables for …
