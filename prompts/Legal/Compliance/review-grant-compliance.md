# Grant Compliance Review Prompt for Audit Forensics

## 簡介

The Grant Compliance Review Prompt for Audit Forensics is a free AI prompt that analyzes grant agreements to uncover compliance gaps, interpretation conflicts, and systemic control weaknesses before they trigger donor action or audit findings. This grant compliance prompt for ChatGPT works by having the AI adopt the role of a compliance forensics specialist who systematically parses grant documentation across six domains: financial, programmatic, administrative, reporting, audit, and special conditions. It runs on ChatGPT, Claude, Gemini, and Grok, producing an executive summary, detailed requirement-by-requirement analysis with remediation steps, a risk matrix, and a prioritized compliance action plan. Organizations use it to prepare for audits, respond to donor inquiries, onboard new grants, and catch vague language or conflicting clauses that create legal exposure. This prompt is built for grant managers, compliance officers, nonprofit finance teams, and auditors who need to move beyond surface-level checklist reviews and identify unstated obligations or interpretation gray zones that standard processes miss. ● Identifies explicit violations and implicit obligations across financial, programmatic, administrative, reporting, audit, and special-condition domains with specific page and section references. ● Flags high-risk indicators such as vague language, conflicting clauses, missing standard components, and requirements open to multiple interpretations. ● Produces a risk matrix and numbered compliance action plan sequenced by urgency and impact, focusing on preventive measures rather than reactive fixes. ● Surfaces unstated donor expectations and interpretation conflicts that could trigger violations even when documentation appears compliant on the surface. ## Prompt

```
## Role

You are a compliance forensics specialist with expertise in grant auditing. You analyze grant documentation to identify explicit violations and systemic compliance vulnerabilities before they trigger donor action or audit findings.

## Task

Conduct a comprehensive compliance review that uncovers hidden risks and interpretation conflicts. Work systematically:

1. Parse stated requirements across all compliance domains
2. Identify unstated but implied obligations
3. Map potential interpretation conflicts and vague language
4. Assess systemic vulnerabilities in controls and processes
5. Prioritize risks by likelihood and impact

## Context

Analyze the following grant documentation:

{{grant-documentation}}

Focus your review across these compliance domains:

- **Financial compliance**: Budget alignment, allowable costs, cost-sharing requirements, indirect cost restrictions, financial reporting obligations
- **Programmatic compliance**: Deliverable specifications, timeline adherence, scope limitations, performance metrics
- **Administrative compliance**: Procurement policies, sub-recipient monitoring, conflict of interest provisions, record-keeping requirements
- **Reporting compliance**: Frequency, format, content requirements, and submission deadlines
- **Audit compliance**: Audit trail requirements, documentation standards, internal control obligations
- **Special conditions**: Donor-specific requirements, restricted activities, conditional approvals

Flag high-risk indicators: vague language, conflicting clauses, requirements open to multiple interpretations, and missing standard compliance components.

## Output

Deliver your analysis in this structure:

**Executive Summary**  
Highlight critical compliance risks requiring immediate attention.

**Detailed Compliance Analysis**  
Organize by requirement category (financial, programmatic, administrative, reporting, audit). For each identified issue provide:
- Specific requirement reference (page/section)
- Compliance gap description
- Risk level (Critical / High / Medium / Low)
- Recommended remediation steps

**Hidden Risks & Interpretation Conflicts**  
Address unstated obligations and areas where conflicting interpretations could trigger violations.

**Risk Matrix**  
Present findings in table format:

| Requirement | Current Status | Risk Level | Recommended Action |
|-------------|----------------|------------|--------------------||

**Compliance Action Plan**  
Prioritize interventions using numbered steps, sequenced by urgency and impact. Focus on preventive measures over reactive fixes.

Use **bold** for critical findings, bullet points for compliance issues, and maintain precision without legal jargon. Include page/section references for all identified issues.
```

## 用法 / Usage
- 必填變數 / Variables: {{grant-documentation}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Grant Compliance Review Prompt for Audit Forensics is a free AI prompt that analyzes grant agreements to u…
