# Anonymous Meeting Notes Generator

## 簡介

The Anonymous Meeting Notes Generator is a free AI prompt that systematically anonymizes meeting documentation for compliance teams, HR professionals, and organizations handling sensitive discussions. This meeting notes prompt for ChatGPT works by identifying and replacing all personally identifiable information - names, job titles, company details, project names, dates, locations, and unique numerical data - with neutral placeholders while maintaining the document's logical flow and business utility. It runs on ChatGPT, Claude, and Gemini, following a structured nine-step process that preserves meeting structure, key decisions, discussion points, and action items. Organizations use it to share internal meeting summaries across departments, archive discussions for future reference without privacy risk, and prepare materials for external audits or legal review. Reach for this prompt when you need to distribute meeting notes while complying with GDPR, CCPA, or internal data protection policies, or when sharing discussions that reference employees, clients, or proprietary information. ● Replaces personal names, job titles, company names, and identifying details with systematic placeholders ● Preserves the original meeting structure including agenda items, decisions, and action items ● Generalizes dates, locations, and numerical data while maintaining relevance and context ● Ensures the anonymized output remains coherent, actionable, and compliant with data protection policies ## Prompt

```
## Role
You are an expert in data privacy and document anonymization.

## Task
Anonymize the provided meeting notes by identifying and replacing all information that could lead to identification of individuals, companies, or sensitive business details—including names, job titles, specific locations, unique company jargon, numerical data that could be identifying, project names, and dates—while maintaining the document's utility and logical flow.

## Process
1. Read the entire document to understand context, key discussions, and decisions
2. Replace personal names with neutral placeholders (Participant 1, Speaker A, etc.)
3. Change specific job titles to generic equivalents (Department Head, Team Leader, etc.)
4. Replace company names, products, and services with generic descriptors (Company A, Product X, Service B)
5. Identify and generalize indirect identifiers: unique project names, uncommon jargon, technical terms
6. Alter unique numerical data or statistics while preserving relevance
7. Generalize dates and locations ("in Q2", "at regional office")
8. Preserve meeting structure: agenda, discussion points, decisions, and action items
9. Review the anonymized document for logical flow and completeness

## Context
{{meeting-notes}}

## Output
Provide the fully anonymized meeting notes in the same format as the original. Retain all crucial business insights, decisions, and action items. Ensure the document is compliant with data protection policies while remaining coherent and actionable.
```

## 用法 / Usage
- 必填變數 / Variables: {{meeting-notes}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Anonymous Meeting Notes Generator is a free AI prompt that systematically anonymizes meeting documentation…
