# Trial Exhibit List Generator for Litigation

## 簡介

The Trial Exhibit List Generator for Litigation is a free AI prompt that builds professional, court-ready exhibit lists organizing depositions, contracts, emails, photographs, expert reports, and demonstrative exhibits for attorneys preparing complex trials. This trial exhibit list prompt for ChatGPT takes your case context and document inventory and outputs a formatted table with exhibit numbers, document descriptions, Bates ranges, page counts, witness assignments, purpose notes, and anticipated objections. It works on ChatGPT, Claude, Gemini, and Grok, producing both the primary exhibit table required by local court rules and supplemental tools like witness-based cross-indexes and strategic trial management recommendations. Attorneys use it to transform scattered discovery into a filing that serves dual purposes: satisfying case management orders and enabling rapid document retrieval during witness examination. Reach for this prompt when you need to organize hundreds of documents for trial, ensure Federal Rules of Evidence compliance, or create a coherent narrative structure that supports your theory of the case. ● Outputs complete exhibit tables with all standard columns: exhibit identifiers, dates, descriptions, authors, Bates ranges, page counts, witness ties, trial purpose, admission status, and foundation notes. ● Creates witness-based cross-indexes showing which exhibits support each witness's testimony, streamlining examination flow. ● Flags special handling requirements for video, audio, physical objects, voluminous records, and electronic evidence needing authentication. ● Applies jurisdiction-appropriate exhibit numbering conventions and ensures descriptions use neutral, accessible language for judges and juries. ## Prompt

```
## Role

You are an experienced trial attorney specializing in exhibit organization and trial presentation strategy.

## Task

Create a comprehensive, court-compliant Exhibit List that organizes trial documents for strategic presentation. The list must serve as both a legal filing and a practical trial tool—enabling quick document retrieval, supporting witness examination, and projecting professionalism to the court.

## Context

{{case-context}} should include: case name and number, court, party you represent, applicable local rules or case management order requirements, and your preferred organizational structure (chronological, witness-based, by document type, by issue/claim, or hybrid).

{{documents}} should describe or list all evidence to be included: contracts, emails, photographs, videos, deposition transcripts, expert reports, business records, demonstrative exhibits, electronic evidence, and any non-standard materials requiring special handling.

## Output

Deliver a professionally formatted exhibit list with:

**Header section** containing the complete case caption per court rules.

**Primary exhibit table** with these columns:
- Exhibit Number/Letter (following jurisdiction-appropriate conventions)
- Document Date
- Document Description (clear, specific, neutral language accessible to non-lawyers)
- Author/Source
- Bates Range
- Page Count
- Witness (if tied to specific testimony)
- Purpose/Use at trial
- Status (admitted, pending, withdrawn)
- Notes (foundation requirements, objections anticipated, special handling)

**Supplemental tools**:
- Witness-based exhibit index cross-referencing which exhibits support each witness
- Strategic recommendations for exhibit management during trial
- Special handling notes for video, audio, physical objects, or voluminous records

Ensure Federal Rules of Evidence compliance for authentication and foundation. Maintain consistent formatting throughout. Group and sequence exhibits to tell a coherent story aligned with your theory of the case.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-context}}、{{documents}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Trial Exhibit List Generator for Litigation is a free AI prompt that builds professional, court-ready exhi…
