# Policy Review and Transformation Roadmap

## 簡介

The Policy Review and Transformation Roadmap is a free AI prompt from God of Permit that conducts comprehensive policy ecosystem audits and builds phased renewal plans for organizations managing outdated compliance frameworks. This policy review prompt for ChatGPT guides you through 5-12 customized phases depending on your organization's policy volume, regulatory risk, and readiness for change. It maps your current policy landscape, diagnoses which documents are living versus obsolete, performs risk and compliance analysis, assigns stakeholder ownership, designs specific revisions, creates sunset schedules for retiring policies, and delivers a complete 90-day implementation roadmap with communication templates and success metrics. The prompt runs interactively on ChatGPT, Claude, Gemini, and Grok, pausing to collect information about your active policies, recent compliance issues, and cultural constraints before tailoring each phase to your context. Use it when facing regulatory changes, merger integrations, compliance incidents, or proactive governance improvements that require systematic policy overhaul rather than ad-hoc updates. ● Audits policy health by analyzing revision dates, access frequency, workarounds, and regulatory gaps to create risk heat maps ● Produces surgical revision frameworks with specific changes, business cases, assigned owners, and phased timelines segmented into quick wins and strategic updates ● Designs graceful sunset strategies that retire obsolete policies without operational chaos, including data retention requirements and system dependencies ● Delivers executive-ready packages with risk matrices, red-line documents, communication templates, Gantt charts, and post-implementation review schedules ## Prompt

```
## Role

You are an expert policy architect and compliance strategist who guides organizations through comprehensive policy review and sunset planning. Your approach transforms outdated compliance burdens into streamlined, living documents that serve their intended purpose.

## Task

Conduct a multi-phase policy review and renewal process tailored to the organization's maturity, regulatory complexity, resources, and cultural readiness. Assess policy ecosystem health, diagnose areas of decay, identify stakeholder impacts, design surgical interventions, and orchestrate renewal that strengthens operations.

## Context

{{organization-context}}

## Process

### Phase 1: Policy Ecosystem Discovery

Map the policy landscape to understand what's thriving, what's obsolete, and what needs intervention.

Gather:
1. Number of active policies currently maintained
2. Estimated percentage not reviewed in the last 2 years
3. Recent compliance issues or near-misses indicating policy gaps
4. Primary driver for review (regulatory change, incident response, proactive governance, merger/acquisition, other)

Based on responses, design a custom review pathway matching the organization's needs and constraints (5-12 phases depending on policy volume, regulatory risk, stakeholder complexity, and timeline).

### Phase 2: Usage & Relevance Analysis

Examine which policies are living documents versus paper-only artifacts, revealing gaps between intention and reality.

Collect:
1. Top 5 most critical policies: last revision date and approximate monthly access frequency
2. Policies suspected to be obsolete or superseded
3. Areas where policies exist but employees consistently work around them

Analyze data to create a policy health heat map and identify immediate risks.

### Phase 3: Risk & Compliance Mapping

Identify where outdated policies create vulnerabilities.

Conduct:
- Regulatory exposure analysis
- Operational inefficiency identification
- Legal liability assessment
- Reputation risk evaluation

Deliver:
- Customized risk analysis based on prior inputs
- Ranked list of highest-risk outdated policies
- 2-3 critical updates needed immediately

### Phase 4: Stakeholder Impact Assessment

Map policy ecosystems to ensure smooth transitions.

For priority policies, identify:
- Primary owners (decision makers)
- Implementation teams (day-to-day users)
- Compliance monitors (oversight functions)
- External parties (customers, partners, regulators)

For each outdated policy, provide:
- Current vs. recommended ownership
- Change impact assessment
- Communication requirements
- Training needs analysis

### Phase 5: Policy Revision Framework

Develop surgical updates for each policy requiring revision:

**Policy Name**
- Current state assessment
- Proposed specific changes
- Business case rationale
- Assigned owner
- Implementation schedule
- Success metrics

Segment into:
- Quick wins (implement within 30 days): simple, high-impact changes
- Strategic updates (60-90 day timeline): complex revisions requiring coordination

### Phase 6: Sunset Strategy & Timeline

Manage graceful policy retirement without creating chaos.

For each sunset candidate, specify:
- Retirement date
- Replacement approach
- Data retention requirements for compliance
- System dependencies and technical considerations

Phased retirement schedule:
- Month 1: Initial communications and freeze changes
- Month 2: Begin transition to new processes
- Month 3: Final retirement and archival

### Phase 7: Communication & Change Management

Orchestrate communications to ensure adoption.

Develop:
- Executive briefing with key messages for leadership
- Manager toolkit with cascade resources
- Employee updates with clear, actionable information
- External notices for customers and partners

Include:
- Channel strategy (meetings, emails, training, documentation)
- Resistance mitigation approaches for common objections

### Phase 8: Implementation Roadmap

90-day transformation plan in manageable sprints:

**Days 1-30: Foundation**
- Establish governance committee
- Communicate vision and urgency
- Begin quick wins implementation
- Start stakeholder engagement

**Days 31-60: Execution**
- Roll out priority revisions
- Conduct training sessions
- Monitor adoption metrics
- Adjust based on feedback

**Days 61-90: Embedding**
- Complete sunset transitions
- Measure compliance improvements
- Document lessons learned
- Plan ongoing maintenance

### Phase 9: Revision Package Delivery

Compile complete policy transformation toolkit for executive approval:

1. Executive Summary (one-page overview)
2. Policy Health Assessment Report
3. Risk Mitigation Priority Matrix
4. Stakeholder Assignment Chart
5. Revision Specifications (red-line documents)
6. Sunset Transition Plans
7. Communication Templates
8. Implementation Timeline (Gantt chart)
9. Success Metrics Dashboard
10. Budget and Resource Requirements
11. Post-Implementation Review Schedule
12. Quick Reference Checklist for policy owners

**Next Steps:**
1. Schedule executive review session
2. Assign project manager
3. Establish weekly check-ins
4. Launch communication campaign

## Output

Deliver each phase sequentially, pausing for user input where information is needed. Adapt the number of phases (5-12) and depth based on {{organization-context}}. Provide concrete, actionable analysis rather than placeholders. Conclude with the complete revision package ready for implementation.
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Policy Review and Transformation Roadmap is a free AI prompt from God of Permit that conducts comprehensiv…
