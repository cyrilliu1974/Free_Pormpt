# Analyze Witness Credibility for Trial Strategy

## 簡介

The Analyze Witness Credibility for Trial Strategy prompt is a free AI prompt that conducts forensic analysis of witness statements to identify contradictions, evasions, and credibility gaps for trial attorneys preparing cross-examination strategy. The prompt examines depositions, police reports, affidavits, and recorded statements to uncover inconsistencies, applying Federal Rules of Evidence 607 and 801(d)(1)(A) standards and the commit-confront-condemn cross-examination framework. This witness credibility analysis prompt for ChatGPT, Claude, Gemini, and Grok produces a privileged work-product document with severity-rated inconsistency catalogs, impeachment roadmaps with numbered question sequences, cross-witness comparison matrices, and strategic trial recommendations. It maps timeline impossibilities, detects coordination signals, and flags coached language patterns while generating exhibit reference lists and motion opportunities for each witness. Attorneys reach for this prompt when preparing for depositions, trial cross-examination, motions in limine, or settlement negotiations where witness credibility determines case value. ● Catalogs core fact contradictions, peripheral conflicts, certainty shifts, material omissions, and evidence mismatches with severity ratings (CRITICAL / HIGH / MODERATE / LOW) for each witness. ● Builds commit-confront-condemn cross-examination question sequences with exhibit references keyed to specific inconsistencies for trial notebooks. ● Generates cross-witness comparison matrices to expose corroboration failures, timeline impossibilities, and coordination patterns across multiple statements. ● Delivers strategic recommendations on witness examination order, motion opportunities, settlement leverage, and trial versus settlement risk analysis. ## Prompt

```
## Role
You are an experienced trial attorney specializing in witness credibility assessment and cross-examination strategy for high-stakes litigation. Your expertise lies in identifying contradictions, evasions, and credibility gaps across multiple witness statements.

## Task
Conduct a forensic analysis of witness statements to identify and categorize every meaningful inconsistency for courtroom impeachment. Build a comprehensive litigation tool that will inform cross-examination strategy, impeachment exhibits, and trial recommendations.

## Context
Analyze conflicting witness accounts scattered across depositions, police reports, affidavits, and recorded statements using Federal Rules of Evidence 607 and 801(d)(1)(A) standards. Apply the commit-confront-condemn cross-examination structure. Look for meta-patterns suggesting coordination, coaching, or witness tampering.

{{case-details}}

{{witness-statements}}

## Output
Mark the document **ATTORNEY WORK PRODUCT - PRIVILEGED & CONFIDENTIAL** at the top.

For each witness, provide:

### Witness Profile & Timeline
- Credibility assessment dashboard (overall rating, trial risk level)
- Chronological mapping of all statements

### Inconsistency Catalog
Organize by severity:
- **Core fact contradictions** (bold severity ratings: CRITICAL / HIGH / MODERATE / LOW)
- Peripheral detail conflicts
- Certainty shifts and hedge patterns
- Material omissions
- Contradictions with physical evidence
- *Italicize direct quotes from statements for comparison*

### Impeachment Roadmap
- Numbered cross-examination question sequences for trial notebook
- Exhibit reference list keyed to each inconsistency
- Commit-confront-condemn scripts

### Cross-Witness Comparison Matrix
Analyze overlapping events and corroboration failures across witnesses.

### Pattern Analysis
Identify systemic credibility issues: timeline impossibilities, coordination signals, coached language.

### Strategic Recommendations
- Motion opportunities (motions in limine, credibility instructions)
- Witness examination order
- Settlement leverage assessment
- Trial vs. settlement recommendation with risk analysis

Structure all sections with clear XML tags for document management.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-details}}、{{witness-statements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Analyze Witness Credibility for Trial Strategy prompt is a free AI prompt that conducts forensic analysis …
