# Cash Flow Outflow Analysis Prompt

## 簡介

The Cash Flow Outflow Analysis Prompt is a free AI prompt that identifies timing mismatches, hidden cost drivers, and working capital stress points for finance teams and business operators. This cash flow analysis prompt for ChatGPT, Claude, Gemini, and Grok takes your expense data and produces a forensic report that categorizes outflows as recurring, variable, or one-time, ranks cost drivers by impact, detects temporal patterns like spikes misaligned with revenue cycles, and surfaces hidden aggregates - small expenses that compound into significant drains. Unlike traditional budget reviews that focus only on totals, it exposes timing problems and distinguishes necessary expenses from financial waste, then delivers immediate (0–30 days), short-term (1–3 months), and structural (3–6 months) optimization strategies. Use it when you need visibility into true cost drivers before the next budget cycle locks in unsustainable spending, or when working capital stress signals that something beneath the surface is wrong. ● Classifies expenses into recurring, variable, and one-time buckets so you see which costs are predictable and which are eroding liquidity. ● Ranks cost drivers by absolute size and relative impact on working capital, not just percentage of budget. ● Detects temporal anomalies - expense spikes that don't align with revenue cycles, seasonal variations, and payment term opportunities - to prevent unnecessary borrowing costs. ● Delivers a three-tier optimization strategy: immediate quick wins (vendor term renegotiations, discretionary cuts), short-term improvements, and structural changes that protect operational capacity while improving cash position. ## Prompt

```
## Role
You are a cash flow forensics specialist identifying timing mismatches, hidden cost drivers, and warning signs that create working capital stress.

## Task
Analyze the provided expense data to expose cash flow leaks, timing problems, and cost patterns that erode working capital. Distinguish necessary expenses from financial waste. Deliver actionable strategies that improve cash position within 30 days while protecting operational capacity.

## Context
The organization lacks visibility into true cost drivers. Previous reviews focused on totals rather than timing, missing critical patterns. Surface these issues before the next budget cycle locks in unsustainable spending.

Request the user's expense categories, then:

1. **Classify outflows** into recurring (predictable intervals), variable (fluctuating but necessary), and one-time (non-recurring/discretionary)
2. **Rank cost drivers** by absolute size and relative impact on cash position
3. **Identify temporal patterns**: expense spikes misaligned with revenue cycles, seasonal variations, payment term opportunities
4. **Surface hidden aggregates**: small expenses that compound to significant amounts, discretionary spending disguised as essential costs
5. **Distinguish** growth investments from wasteful spending

## Input
{{expense-data}}

## Output
Structure your analysis with these sections:

**Executive Summary**  
Key findings in 3-4 sentences.

**Categorized Expense Breakdown**  
- Recurring costs  
- Variable costs  
- One-time costs  

**Cost Driver Analysis**  
Ranked by impact, with specific metrics.

**Anomaly Detection**  
Unusual patterns, spikes, timing mismatches that create unnecessary borrowing costs.

**Cash Flow Optimization Strategy**  
- Immediate actions (0-30 days): quick wins, vendor term renegotiations  
- Short-term improvements (1-3 months)  
- Structural changes (3-6 months)  

Use bullet points for actionable items.

**Risk Assessment**  
Consequences of current spending patterns if unaddressed.
```

## 用法 / Usage
- 必填變數 / Variables: {{expense-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Skill_Orchestration&Assembly · Skill_Selection_Gate_And_Binding
- 適用 / Use when: The Cash Flow Outflow Analysis Prompt is a free AI prompt that identifies timing mismatches, hidden cost drive…
