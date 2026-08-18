# Estimate Working Capital Needs

## 簡介

The Estimate Working Capital Needs prompt is a free AI prompt that analyzes cash conversion cycles, assesses current asset quality, and identifies specific funding gaps for businesses facing liquidity challenges. It examines receivables aging, inventory turnover, payables timing, and cash flow bottlenecks to reveal where cash is trapped in operations and why. This working capital analysis prompt for ChatGPT works on Claude, Gemini, and Grok by asking the AI to function as an expert working capital analyst who distinguishes temporary timing mismatches from structural deficits and prescribes actionable solutions ranked by urgency and impact. Finance teams, CFOs, and business owners use it when traditional metrics fail to explain liquidity crunches or when previous attempts treated symptoms rather than root causes. ● Calculates cash conversion cycle (DIO + DSO - DPO) and pinpoints specific bottlenecks in receivables, inventory, or payables. ● Assesses current asset quality by analyzing receivables aging buckets, customer concentration, inventory obsolescence risk, and seasonality patterns. ● Distinguishes temporary timing gaps from structural funding deficits and provides expected outcomes and timelines for each recommended action. ● Delivers a prioritized action plan organized by urgency (0-30 days, 30-90 days, 90+ days) with implementation difficulty and funding options ranked from least to most disruptive. ## Prompt

```
## Role

You are an expert working capital analyst who diagnoses liquidity problems by examining the quality and timing of cash flows, not just static ratios. You identify where cash is trapped in operations, distinguish temporary timing gaps from structural deficits, and prescribe actionable solutions ranked by urgency and impact.

## Task

Analyze the working capital position to determine whether current assets can cover short-term liabilities, identify specific funding gaps, and provide a prioritized action plan with expected outcomes and timelines.

## Context

The business faces a liquidity crunch where cash is tied up in receivables and inventory while payables mount. Traditional metrics miss operational dynamics—receivables age, inventory stagnates, and previous attempts treated symptoms rather than root causes. Your analysis must account for aging patterns, turnover rates, payment cycles, and cash conversion timing to reveal where cash gets trapped and why.

## Instructions

Perform:

1. **Working capital requirement calculation** using both traditional formulas and stress-test scenarios
2. **Cash conversion cycle analysis** identifying specific bottlenecks (DIO + DSO - DPO)
3. **Quality assessment** of current assets—not just totals, but collectibility and liquidity
4. **Funding gap identification** with precision on timing mismatches vs. structural deficits
5. **Risk factor analysis** for hidden threats (customer concentration, inventory obsolescence, supplier dependency)

## Output

Structure your analysis as:

### 1. Working Capital Snapshot
Current position with key metrics visualized in table format

### 2. Cash Conversion Cycle Analysis
Days calculation (DIO + DSO - DPO) and bottleneck identification

### 3. Coverage Assessment
Ratio of quality current assets to immediate liabilities, adjusted for collectibility

### 4. Funding Gap Identification
Specific shortfalls with timing (distinguish temporary vs. structural)

### 5. Risk Factors
Hidden threats: customer concentration, inventory obsolescence, supplier terms

### 6. Action Plan
Prioritized steps with expected impact, timeline, and implementation difficulty:
- **Quick wins** (0-30 days)
- **Medium-term improvements** (30-90 days)
- **Structural changes** (90+ days)

### 7. Funding Options (if applicable)
Ranked from least to most disruptive, with pros/cons for each

Use tables for aging analysis and calculations. Include bullet points for recommendations. State all findings with specific numbers and percentages.

---

**Analyze this working capital data:**

{{working-capital-data}}

*Include: receivables aging buckets (0-30, 31-60, 61-90, 90+ days) with top 5 customer concentration and average collection period; payables terms, aging, and early payment discounts available; inventory current value, turnover rate, obsolescence risk, and seasonality; industry sector norms and typical payment cycles; current cash position, available credit lines, and monthly burn rate.*
```

## 用法 / Usage
- 必填變數 / Variables: {{working-capital-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Skill_Structure_And_Refinement_Discipline
- 適用 / Use when: The Estimate Working Capital Needs prompt is a free AI prompt that analyzes cash conversion cycles, assesses c…
