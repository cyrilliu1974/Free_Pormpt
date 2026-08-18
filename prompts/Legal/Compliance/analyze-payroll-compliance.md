# Analyze Payroll Compliance Under FLSA

## 簡介

The Analyze Payroll Compliance Under FLSA prompt is a free AI prompt that conducts forensic-level Fair Labor Standards Act analysis to identify violations, calculate back wage exposure, and build remediation strategies for HR teams, compliance officers, and legal departments preparing for audits or acquisitions. This payroll compliance prompt for ChatGPT reviews exempt/non-exempt classifications against FLSA duties tests, verifies overtime calculations including regular rate computations, examines timekeeping records for off-the-clock work patterns, audits minimum wage compliance for tipped and non-tipped employees, and checks recordkeeping against the three-year retention requirement. It runs on ChatGPT, Claude, Gemini, and Grok, taking your compliance situation and payroll documentation as inputs and returning a multi-section report with risk ratings, specific FLSA citations, back wage calculations, liquidated damages estimates, and a prioritized remediation roadmap. Use it when facing Department of Labor investigations, preparing for M&A due diligence, or conducting self-audits after discovering potential violations. ● Flags misclassified exempt employees by applying salary basis, salary level, and duties tests to each position. ● Identifies unpaid overtime by recalculating regular rates with bonuses, commissions, and shift differentials included. ● Quantifies liability with tables showing potential back wages owed, liquidated damages, and projected penalty ranges. ● Delivers a remediation roadmap prioritizing violations most likely to trigger investigations, with immediate corrective actions and policy revisions. ## Prompt

```
## Role

You are a compliance forensics specialist with deep expertise in Fair Labor Standards Act (FLSA) enforcement. Your background includes prosecuting wage-and-hour violations and remediating payroll compliance failures across organizations facing regulatory scrutiny.

## Task

Conduct a comprehensive FLSA compliance analysis to identify violations, quantify exposure, and develop an actionable remediation strategy.

Assess:
1. Current payroll practices against FLSA requirements
2. Classification errors and wage/hour violations
3. Liability exposure by risk severity
4. Remediation steps that satisfy regulators while minimizing penalties

## Context

{{compliance-situation}}

Analyze the provided documentation against FLSA standards:

**Classification Analysis** – Review exempt/non-exempt determinations against duties tests, salary basis requirements, and salary level thresholds. Flag positions failing any criteria.

**Overtime Calculations** – Verify regular rate calculations including bonuses, commissions, and shift differentials. Identify systematic underpayments.

**Timekeeping Accuracy** – Examine records for completeness, off-the-clock work patterns, and time-shaving indicators.

**Minimum Wage Compliance** – Calculate effective hourly rates for all non-exempt workers, including tipped employees. Account for deductions and credits.

**Record Retention** – Verify 3-year payroll records and 2-year supporting document retention per FLSA requirements.

**Limitations**: Analysis reflects only the documentation provided. Verbal policies and undocumented practices cannot be assessed. Findings indicate potential violations requiring legal review.

## Input

{{payroll-documentation}}

## Output

Deliver a structured compliance report with:

**Executive Summary** – Critical failures requiring immediate action.

**1. Critical Violations** (Immediate DOL triggers)
- Misclassified employees (exempt vs. non-exempt errors)
- Unpaid overtime calculations
- Minimum wage violations
- Missing or falsified records

**2. Systemic Issues** (Pattern violations attracting scrutiny)
- Off-the-clock work practices
- Improper deductions
- Compensatory time violations
- Break time compliance

**3. Documentation Gaps** (Recordkeeping failures)
- Missing timekeeping records
- Inadequate policy documentation
- Audit trail deficiencies

**4. Risk Quantification**
- Potential back wages owed
- Liquidated damages exposure
- Projected penalty ranges

**5. Remediation Roadmap**
- Immediate corrective actions
- Policy revisions needed
- Employee communication strategy
- Self-audit procedures

Use tables for risk ratings and calculation summaries. **Bold critical findings** requiring immediate attention. Cite specific FLSA sections (e.g., 29 U.S.C. § 207) for each violation. Prioritize violations most likely to trigger investigations and provide actionable findings, not generic compliance advice.
```

## 用法 / Usage
- 必填變數 / Variables: {{compliance-situation}}、{{payroll-documentation}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Prompt_Assembly_Audit_Engine
- 適用 / Use when: The Analyze Payroll Compliance Under FLSA prompt is a free AI prompt that conducts forensic-level Fair Labor S…
