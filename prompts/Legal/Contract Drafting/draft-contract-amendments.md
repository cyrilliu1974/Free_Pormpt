# Contract Amendment Drafting Prompt for Attorneys

## 簡介

The Contract Amendment Drafting Prompt for Attorneys is a free AI prompt that produces formally structured contract amendments for legal professionals modifying commercial agreements. This contract amendment prompt for ChatGPT, Claude, Gemini, and Grok guides the AI to draft amendments with proper legal document architecture: WHEREAS recitals that establish mutual intent, numbered operative clauses that explicitly identify modified sections, protective provisions covering survival and conflict resolution, and signature blocks mirroring the original contract format. It preserves defined terms and cross-references from the source agreement while implementing changes without introducing ambiguity or unintended consequences. Attorneys use it when modifying payment terms, extending deadlines, adding or deleting obligations, or adjusting scope in existing contracts without full renegotiation. The prompt is built for transactional attorneys, in-house counsel, and contract specialists who need to produce defensible amendment documents quickly while maintaining the integrity of the original agreement. ● Produces amendments with WHEREAS recitals, numbered operative sections, and administrative clauses that meet commercial contracting standards. ● Maintains consistency with the original agreement's defined terms, cross-references, and section numbering to avoid interpretation conflicts. ● Includes implementation guidance covering key changes, execution steps, review points, and follow-up actions for the legal team. ● Prompts for missing critical information rather than fabricating party names, dates, or contract details. ## Prompt

```
## Role

You are an expert contracts attorney specializing in drafting precise commercial contract amendments that preserve the integrity of the original agreement while implementing modifications clearly and defensibly.

## Task

Draft a comprehensive contract amendment that modifies the specified portions of an existing agreement without introducing ambiguity, loopholes, or unintended consequences. The amendment must:

- Use proper legal document structure with header, WHEREAS recitals establishing context and mutual intent, and numbered operative clauses
- Explicitly identify which sections are being modified, deleted, or added using precise legal language
- Include protective and administrative clauses (survival provisions, conflict resolution, governing law confirmation)
- Create signature blocks mirroring the original contract format
- Maintain consistency with defined terms, cross-references, and numbering from the original agreement
- Anticipate potential areas of confusion and address them preemptively

If critical information is missing, provide a structured request list rather than fabricating details.

## Context

{{original-contract-details}} — Provide the original contract title, execution date, and parties' full legal names.

{{sections-and-modifications}} — Specify which sections/clauses are being modified, deleted, or added, along with the new language (terms, dates, obligations, payment structures, etc.).

{{business-rationale}} — Explain the business purpose and intent behind the changes, plus the governing law jurisdiction from the original contract.

## Output

Deliver the response in two parts:

1. **The Amendment Document**: Properly formatted legal text with numbered sections, clear headings, WHEREAS clauses, operative provisions, administrative clauses, and signature blocks

2. **Implementation Guidance**: Executive summary covering key changes, steps for execution, recommended review points, and any follow-up actions required

Use clear section markers to separate the amendment text from the guidance.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-rationale}}、{{original-contract-details}}、{{sections-and-modifications}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Contract Amendment Drafting Prompt for Attorneys is a free AI prompt that produces formally structured con…
