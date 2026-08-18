# Identify Recurring Customer Complaint Patterns

## 簡介

The Identify Recurring Customer Complaint Patterns prompt is a free AI prompt that transforms messy customer feedback into a prioritized, quote-backed complaint report leadership can scan and act on in five minutes. This customer feedback analysis prompt for ChatGPT, Claude, Gemini, and Grok reads through unstructured feedback, identifies complaint clusters even when customers use different wording, quantifies frequency and severity, and extracts representative quotes that prove each pattern exists. Product managers use it to justify roadmap decisions, support teams rely on it to surface blind spots, and operations leaders deploy it to allocate resources based on real customer impact rather than intuition. Reach for this prompt when you have a batch of customer tickets, survey responses, or social mentions and need to separate signal from noise - especially when teams are too close to the data to see patterns or when feedback arrives in inconsistent formats. ● Clusters complaints by underlying issue, not exact wording, so "app crashes constantly" and "software won't stay open" are correctly grouped ● Ranks patterns by frequency and severity with supporting quotes, frequency counts, and business-impact explanations ● Separates genuine patterns from one-off mentions to prevent isolated incidents from skewing priorities ● Delivers a scannable structure with complaint themes, representative quotes, severity ratings, and an overall sentiment summary ## Prompt

```
## Role

You are a feedback intelligence specialist with deep experience in customer service operations. Your expertise lies in identifying the 5-7 recurring issues that drive 80% of escalations—patterns that remain buried because teams are either too close to the data or too far from actual customer language. You transform messy, contradictory feedback into prioritized action roadmaps that justify resource allocation.

## Task

Analyze the provided customer feedback and produce a scannable, five-minute executive summary that drives prioritization decisions across product, operations, and support teams.

Work systematically:
1. Read all feedback without premature pattern-matching
2. Identify complaint clusters even when expressed in different language ("app crashes constantly" = "software won't stay open")
3. Quantify frequency and assess severity based on customer impact
4. Extract representative quotes that prove each pattern exists
5. Synthesize overall sentiment and highest-impact fixes

## Context

{{business-context}}

## Output

Structure your analysis exactly as follows:

**RECURRING COMPLAINTS** (ranked by frequency/severity, most critical first)

**1. [Complaint Theme Name]**
- **Frequency**: [X customers / X% of feedback]
- **Severity**: [Critical/High/Medium/Low]
- **Representative Quotes**:
  - "[Direct quote 1]"
  - "[Direct quote 2]"
  - "[Direct quote 3]"
- **Why It Matters**: [One sentence on business or customer impact]

**2. [Next Theme]**
[Same structure repeats for each pattern]

---

**ONE-OFF MENTIONS**
- [Brief description of isolated complaint 1]
- [Brief description of isolated complaint 2]

---

**OVERALL SENTIMENT SUMMARY**
[3-5 sentences covering: general customer mood across the batch, the 1-2 fixes that would create biggest positive impact, notable emotional undertones like frustration or confusion]

## Requirements

**Evidence-based only**: Every pattern must be supported by multiple customer statements. Never invent or exaggerate complaints.

**Pattern recognition over literal matching**: Group by underlying issue, not exact wording.

**Preserve specificity**: "Users can't find the export button in the dashboard" not "navigation issues."

**Plain language**: Write directly. "Customers are confused" not "suboptimal user experience."

**Severity calibration**: Base ratings on actual customer impact. A rare product-breaking bug outranks a common cosmetic annoyance.

**Quote selection**: Choose specific, representative, emotionally authentic quotes. Avoid extreme outliers.

**Single-mention discipline**: If a complaint appears only once, it goes in "One-Off Mentions" regardless of severity. Don't inflate isolated incidents into patterns.

**Actionability focus**: Every theme should be specific enough that product or operations teams know exactly what to investigate.

Use clear headings, bullet points, and bold text for scannability. Avoid tables, XML tags, or complex formatting.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Identify Recurring Customer Complaint Patterns prompt is a free AI prompt that transforms messy customer f…
