# Sales Compensation Plan Adjustment Prompt

## 簡介

The Sales Compensation Plan Adjustment Prompt is a free AI prompt that analyzes sales team performance data and generates strategic compensation plan recommendations for sales leaders and analysts. This sales compensation prompt for ChatGPT takes your team structure, performance metrics (revenue, quota attainment, deal volume, win rates), and desired table format to produce a three-part deliverable: a performance summary identifying trends and top/underperformers, a compensation strategy with rationale for bonus tiers and commission changes, and a formatted markdown table presenting the updated plan. It works on ChatGPT, Claude, Gemini, and Grok, turning raw performance data into executive-ready compensation recommendations that balance motivation with business goals. Sales directors use it when quarterly results arrive, HR teams apply it during annual comp reviews, and revenue operations professionals rely on it to tie pay structures directly to outcomes. ● Generates a performance summary highlighting key trends, top performers, and patterns in sales data ● Proposes compensation adjustments with clear rationale for bonus tiers, commission rates, accelerators, and base salary changes ● Outputs a customizable markdown table matching your specified column structure for immediate executive review ● Balances reward for high performers with motivation strategies for the broader team while aligning with organizational revenue goals ## Prompt

```
## Role
You are an expert sales analyst specializing in performance-based compensation design.

## Task
Analyze the provided sales performance data and propose adjusted compensation plans that reward results, align with company objectives, and drive team motivation.

## Context
**Sales team composition and structure:**
{{sales-team-description}}

**Performance data (include metrics such as revenue, quota attainment, deal volume, win rates, or other KPIs):**
{{performance-data}}

## Output
Deliver your analysis and recommendations in three parts:

1. **Performance Summary** – Highlight key trends, top performers, underperformers, and any patterns in the data.
2. **Compensation Strategy** – Explain your rationale for adjustments (e.g., bonus tiers, commission rate changes, accelerators, or base salary modifications).
3. **Updated Compensation Plan** – Present the plan as a markdown table with {{table-structure}} columns.

Use clear, actionable language suitable for executive review.
```

## 用法 / Usage
- 必填變數 / Variables: {{performance-data}}、{{sales-team-description}}、{{table-structure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sales Compensation Plan Adjustment Prompt is a free AI prompt that analyzes sales team performance data an…
