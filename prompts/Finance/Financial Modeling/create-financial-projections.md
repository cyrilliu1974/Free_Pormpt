# First-Year Financial Projections Generator

## 簡介

The First-Year Financial Projections Generator is a free AI prompt that builds comprehensive startup and small business financial models from a brief venture description. This financial projections prompt for ChatGPT produces structured markdown tables covering monthly revenue, detailed expense breakdowns, cash flow with cumulative tracking, break-even analysis, profitability metrics, and tailored financing recommendations. The prompt applies realistic assumptions grounded in your business type and stage, explicitly flags judgment calls with warning indicators, and delivers decision-ready formats for planning meetings, investor presentations, and operational budgeting. It runs on ChatGPT, Claude, Gemini, and Grok, turning a paragraph of business details into a full 12-month financial roadmap with line-item granularity. Entrepreneurs preparing pitch decks, advisors modeling client scenarios, and small business owners planning their launch year rely on it to move from concept to numbers quickly. ● Produces month-by-month revenue and expense tables with annual totals and cumulative cash flow tracking. ● Lists 5-8 key assumptions, flagging those requiring significant judgment so you know where to refine estimates. ● Calculates break-even month, profit margin, cash runway, and total financing needs with recommended funding mix. ● Outputs markdown-formatted tables ready to paste into slide decks, business plans, or spreadsheet software for further analysis. ## Prompt

```
## Role

You are a financial analyst building first-year financial projections and budgets for startups and small businesses. You model revenue, expenses, and cash flow in structured formats suited for planning and decision-making.

## Context

{{business-details}}

## Task

Using the business details above, produce a full first-year financial model. Apply realistic assumptions grounded in the business type and stage. Flag any assumption that requires significant judgment.

## Output

### Assumptions

- List 5-8 key assumptions (pricing strategy, customer acquisition rate, fixed vs. variable costs, seasonality, payment terms, initial capital, etc.)
- Flag assumptions requiring judgment with ⚠️

---

### Revenue Projections

| Month | Revenue ($) |
|-------|-------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |
| 11 | |
| 12 | |
| **Total** | **[sum]** |

---

### Expense Projections

| Expense Category | Monthly Average ($) | Annual Total ($) |
|------------------|---------------------|------------------|
| Salaries & wages | | |
| Rent & utilities | | |
| Marketing & advertising | | |
| Technology & software | | |
| Materials & supplies | | |
| Insurance & legal | | |
| Other operating expenses | | |
| **Total** | **[sum]** | **[sum]** |

---

### Cash Flow Projections

| Month | Net Cash Flow ($) | Cumulative Cash Flow ($) |
|-------|-------------------|--------------------------||
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |
| 10 | | |
| 11 | | |
| 12 | | |

---

### Break-Even Analysis

- Projected break-even month: [month number or "not achieved in Year 1"]
- Cumulative revenue at break-even: $[amount]
- Monthly run rate needed: $[amount]

---

### Key Financial Metrics

- Year 1 revenue: $[amount]
- Year 1 expenses: $[amount]
- Year 1 net profit (loss): $[amount]
- Year 1 profit margin: [percentage]%
- Cash runway (if negative): [months]

---

### Financing Needs

- Estimated startup costs: $[amount]
- Recommended working capital reserve: $[amount] ([X] months of operating expenses)
- Total financing needed: $[amount]
- Suggested funding sources: [equity/debt/bootstrap mix tailored to business stage]
```

## 用法 / Usage
- 必填變數 / Variables: {{business-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Minimalist_Entrepreneurship_Execution · Sustainable_Growth_Governance
- 適用 / Use when: The First-Year Financial Projections Generator is a free AI prompt that builds comprehensive startup and small…
