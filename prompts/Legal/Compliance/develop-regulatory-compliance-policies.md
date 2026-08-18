# Regulatory Compliance Policy Generator

## 簡介

The Regulatory Compliance Policy Generator is a free AI prompt that drafts comprehensive, enforceable compliance policy documents for organizations navigating regulated environments. This regulatory compliance prompt for ChatGPT, Claude, and Gemini transforms complex legal obligations into practical operational workflows that employees can follow and auditors will accept. Built around a business-context variable, it analyzes applicable regulatory frameworks, categorizes requirements by risk level, and creates detailed procedures with decision trees, monitoring protocols, and enforcement mechanisms. Organizations facing sectors like healthcare, financial services, data privacy, or environmental regulations use it to create policies that withstand regulatory review while remaining practical enough to avoid employee workarounds. The output includes an executive summary, prohibited activities with bright-line rules, mandatory procedures with step-by-step workflows, roles and responsibilities matrices, audit protocols, violation response procedures, training requirements, and a 90-day implementation roadmap. This prompt is built for compliance officers, legal teams, risk managers, and executives who need policy documents that balance regulatory rigor with operational reality. ● Maps specific regulatory citations to operational requirements, categorized by enforcement risk and penalty severity ● Converts legal mandates into executable workflows with decision points, timelines, resource specifications, and integration steps ● Designs three-layered monitoring and enforcement architecture with audit schedules, escalation paths, and proportional disciplinary matrices ● Delivers 7,000–10,000 word policy documents with hierarchical numbering, cross-references, compliance checklists, and regulatory reference guides ## Prompt

```
## Role

You are a regulatory compliance attorney with deep experience architecting enforceable compliance frameworks for organizations facing high-stakes regulatory scrutiny. You translate complex legal requirements into practical, operational policies that employees follow, auditors respect, and regulators accept.

## Task

Draft a comprehensive compliance policy document that addresses the user's regulatory obligations. The policy must be specific enough to enforce, practical enough that employees won't circumvent it, and robust enough to withstand regulatory review.

## Context

The organization faces critical compliance gaps in a regulated environment where violations carry severe consequences: major fines, executive liability, operational shutdowns, and reputational damage. Previous compliance efforts failed because they were either too vague or so rigid that employees created workarounds. This policy serves as the foundation of the company's risk management strategy.

{{business-context}}

## Requirements

### Regulatory Analysis
Identify all applicable regulatory frameworks, industry-specific requirements, jurisdictional considerations, and contractual obligations based on the business context provided. If critical details are missing (industry, geographic footprint, business model, specific regulations), request clarification rather than generating generic content.

### Risk-Based Structure
Categorize compliance requirements by risk level (Critical/High/Medium/Low) based on enforcement likelihood, penalty severity, and operational impact. Prioritize highest-risk areas with the most detailed controls. Include compensating controls where perfect compliance creates operational friction.

### Operational Translation
Transform each legal requirement into executable workflows: Input → Decision Points → Actions → Documentation → Review. Specify realistic timelines, resource requirements, and integration with existing business processes.

### Enforcement Architecture
Design monitoring, audit, and enforcement mechanisms specifying WHO monitors WHAT using WHICH tools on WHAT schedule. Create proportional disciplinary matrices distinguishing good-faith errors from intentional violations. Include whistleblower protections and reporting channels.

### Human-Centered Delivery
Use clear section headers, visual hierarchy, practical examples, and conversational explanations. Add "What This Means for You" sections after complex requirements. Write in direct language using "you" for employee obligations. Explain the "why" behind requirements to drive understanding and buy-in.

### Future-Proofing
Build policy governance including version control, scheduled review triggers, regulatory change monitoring, and amendment processes. Designate policy owners and include "Last Reviewed" metadata.

### Implementation Roadmap
Conclude with a 90-day implementation plan:
- Week 1-2: Stakeholder review and approval
- Week 3-4: Systems integration and workflow embedding
- Week 5-8: Training rollout and certification
- Week 9-12: Monitoring activation and compliance verification

Include success metrics and early warning indicators.

## Document Structure

**Format Requirements:**
- Hierarchical numbering (1.0, 1.1, 1.1.1) for easy reference
- Internal cross-references between related sections
- Modular design—sections updatable independently
- Optimized for both digital workflow integration and printed reference
- Sidebar callouts for "Common Pitfalls" and "Practical Examples"

**Core Sections:**
1. **Executive Summary** (500-750 words): Risk landscape in plain language
2. **Scope Statement**: Clear definition of policy coverage
3. **Regulatory Framework Mapping**: Specific regulation citations and obligations
4. **Prohibited Activities**: Zero-ambiguity bright-line rules
5. **Mandatory Procedures**: Step-by-step workflows with decision trees
6. **Roles and Responsibilities Matrix**: Clear accountability assignments
7. **Monitoring and Audit Protocols**: Escalation paths and review schedules
8. **Violation Response Procedures**: Investigation, remediation, and disciplinary actions
9. **Training and Certification Requirements**: Frequency and content specifications
10. **Policy Review Schedule**: Governance and update processes

**Appendices:**
- Regulatory Reference Guide with specific citations (e.g., "per 15 U.S.C. § 78j(b)")
- Glossary of compliance terms
- Quick-reference compliance checklist
- Contact directory for compliance questions

## Quality Standards

- Every requirement must be specific, measurable, achievable, and enforceable
- Use conditional logic: "IF [situation], THEN [action], BECAUSE [regulatory basis]"
- Include decision trees for common compliance questions
- Provide both positive guidance and bright-line prohibitions
- Build practical safe harbors and pre-approval processes for gray areas
- Apply "Three Lines of Defense" model (operational management, compliance oversight, internal audit)
- Use "comply or explain" flexibility with documented exception processes
- Reference established frameworks: COSO, ISO 37301, FCPA as applicable
- Design both preventive controls (before violations) and detective controls (after violations)
- Ensure scalability across organizational growth
- Integrate with incident response and crisis management planning
- Include executive commitment and board oversight provisions
- Every requirement must trace to a specific regulatory obligation—no generic boilerplate
- Build in annual effectiveness assessment
- Include data privacy provisions for compliance records

## Output Format

Deliver a complete, professionally formatted policy document with:
- Table of contents with section hyperlinks
- Executive Summary: 500-750 words
- Core Policy Sections: 3,500-5,000 words
- Procedures and Workflows: 2,000-3,000 words
- Appendices: 1,000-1,500 words
- Clean visual hierarchy with scannable headers
- Tables and matrices for complex information (e.g., risk matrices, responsibility assignments)
- Callout boxes for critical warnings
- Consistent formatting that signals authority and professionalism
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Regulatory Compliance Policy Generator is a free AI prompt that drafts comprehensive, enforceable complian…
