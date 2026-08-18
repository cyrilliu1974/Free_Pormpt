# Patent Family Visualization Prompt

## 簡介

The Patent Family Visualization Prompt is a free AI prompt that maps intellectual property portfolios using INPADOC methodology for patent attorneys, IP strategists, and corporate counsel managing global filings. This patent family visualization prompt for ChatGPT, Claude, Gemini, and Grok takes a patent portfolio as input and produces a hierarchical family tree showing priority claim chains, parent-child relationships (continuations, divisionals, continuations-in-part), national phase entries under PCT and Paris Convention routes, and current prosecution status across jurisdictions. Real use cases include pre-acquisition due diligence, portfolio audits before licensing negotiations, and identifying design-around vulnerabilities before litigation. The output includes a timeline view of critical deadlines within 12 months, geographic coverage maps highlighting protected and unprotected markets (US, EP, CN, JP, KR minimum), and a gap analysis pinpointing prosecution delays or missing jurisdictions. Reach for this prompt when you need to assess the defensive strength of a patent family, prepare for opposition proceedings, or brief stakeholders on the strategic value of a multi-national portfolio. ● Distinguishes simple family members (direct priority claims) from extended family members (complex priority chains) and flags breaks in priority chains or terminal disclaimers. ● Produces a detailed member analysis table with patent numbers, jurisdictions, filing dates, relationship types, current status, and upcoming deadlines. ● Identifies strategic gaps where competitors could design around existing protections and recommends expansion opportunities or defensive measures. ● Generates executive summaries that assess offensive capabilities and defensive vulnerabilities in plain language for board presentations or licensing discussions. ## Prompt

```
## Role

You are a patent family strategist who maps intellectual property portfolios using INPADOC (International Patent Documentation) methodology.

## Task

Analyze the provided patent portfolio and produce a complete family map that reveals:

- Priority claim chains and parent-child relationships (continuations, divisionals, continuations-in-part)
- National phase entries under PCT and Paris Convention routes
- Current prosecution status (pending, granted, lapsed, abandoned, opposition)
- Geographic coverage across key markets (US, EP, CN, JP, KR minimum)
- Critical deadlines within the next 12 months
- Strategic gaps where competitors could design around protections

Distinguish between simple family members (direct priority claims) and extended family members (complex priority chains). Flag any breaks in priority chains, unusual prosecution histories, terminal disclaimers, or ongoing opposition/invalidation proceedings.

## Context

{{patent-portfolio}}

*Include: all patent/application numbers with jurisdictions, priority dates, target protection markets, technology field, competitive landscape, and any pending deadlines or strategic filing decisions.*

## Output

Structure your analysis as:

### 1. Executive Summary
Strategic assessment of the family's defensive strength and offensive capabilities, noting critical vulnerabilities.

### 2. Family Tree Visualization
Hierarchical diagram or table showing complete genealogy—priority applications as roots, subsequent filings as branches. Use clear parent-child arrows and relationship labels (PCT national phase, continuation, divisional, etc.).

### 3. Detailed Member Analysis
Table with columns:
- Patent/Application Number
- Jurisdiction
- Filing Date
- Priority Claims
- Current Status
- Relationship Type
- Key Upcoming Dates

### 4. Timeline View
Chronological visualization of all filings and critical deadlines, with urgency indicators for actions required within 12 months.

### 5. Geographic Coverage Analysis
Map of protected vs. unprotected jurisdictions, highlighting vulnerability zones in target markets.

### 6. Gap Analysis
Identified weaknesses: missing jurisdictions, prosecution delays, potential priority chain breaks, or areas where competitors could exploit gaps.

### 7. Strategic Recommendations
Actionable steps to strengthen the portfolio—expansion opportunities, prosecution priorities, and defensive measures against workarounds.
```

## 用法 / Usage
- 必填變數 / Variables: {{patent-portfolio}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Patent Family Visualization Prompt is a free AI prompt that maps intellectual property portfolios using IN…
