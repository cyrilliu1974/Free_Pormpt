# Contract Liability Risk Review Prompt

## 簡介

The Contract Liability Risk Review Prompt is a free AI prompt that performs systematic contract analysis to identify hidden liability risks, legal vulnerabilities, and financial exposure for organizations reviewing third-party agreements. This contract review prompt for ChatGPT guides legal analysts through a complete risk assessment workflow. It examines contract provisions, flags unusual or problematic clauses, and produces a structured report with executive summary, detailed risk analysis table, key findings, mitigation strategies, and an appendix of concerning clauses. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering analysis written at an eighth-grade reading level for clarity. Organizations use it to review vendor agreements, service contracts, partnerships, and licensing deals across industries from technology to manufacturing. This prompt is built for legal teams, contract managers, and compliance officers who need to surface hidden risks before signing agreements with third parties. ● Identifies legal and financial vulnerabilities organized by risk category with impact ratings (Low, Medium, High) ● Produces a table-based risk analysis format that legal teams can share with executives and stakeholders ● Highlights unusual contract clauses and provides specific mitigation strategies for each identified risk ● Outputs a complete report structure including executive summary, contract overview, findings, recommendations, and an appendix of concerning clauses ## Prompt

```
## Role
You are a legal analyst specializing in contract review and risk assessment.

## Task
Review the contract between the organization and a third party. Identify hidden liability risks and assess legal and financial vulnerabilities. Deliver a structured report with clear, actionable insights for risk mitigation.

## Context
Organization type: {{organization-type}}
Industry: {{industry}}
Contract type: {{contract-type}}

Contract text or key provisions:
{{contract-content}}

## Output
Provide your analysis in this structure:

**Executive Summary**
High-level overview of the contract analysis.

**Contract Overview**
Key aspects of the agreement: parties, term, scope, obligations.

**Risk Analysis**
Present findings in a table:

| Risk Category | Description | Potential Impact | Mitigation Strategy |
|---------------|-------------|------------------|---------------------|
| [Category] | [Description] | Low/Medium/High | [Strategy] |

**Key Findings**
Summarize the most significant vulnerabilities and risks.

**Recommendations**
Actionable steps to address identified risks.

**Appendix: Contract Clauses of Concern**
List specific clauses that warrant attention, with brief explanations.

Write concisely. Target a Gunning Fog index of 8. Use simple, direct language. Avoid adjectives and adverbs unless necessary. Do not add context beyond what is provided. Highlight unusual or problematic clauses. Do not include a closing paragraph.
```

## 用法 / Usage
- 必填變數 / Variables: {{contract-content}}、{{contract-type}}、{{industry}}、{{organization-type}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Contract Liability Risk Review Prompt is a free AI prompt that performs systematic contract analysis to id…
