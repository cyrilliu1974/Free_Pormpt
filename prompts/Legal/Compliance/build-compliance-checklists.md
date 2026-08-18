# Build Compliance Checklists

## 簡介

The Build Compliance Checklists prompt is a free AI prompt that creates structured, audit-ready compliance systems for businesses navigating complex regulatory requirements. It analyzes your operations, identifies applicable regulations, translates statutory language into actionable tasks, and delivers a phased implementation roadmap with clear ownership and documentation standards. This compliance checklist prompt for ChatGPT, Claude, Gemini, and Grok adapts its depth and structure to your regulatory complexity - generating anywhere from 5 to 12 phases depending on whether you operate in a single jurisdiction or manage international, highly-regulated environments. Use it when you need to close compliance gaps, prepare for audits, or build a defensible regulatory framework from the ground up. ● Maps every regulation with enforcement relevance to your industry, jurisdictions, and operations, then translates legal text into operational requirements with citations. ● Prioritizes requirements by penalty severity, enforcement probability, and business impact so you address criminal-penalty risks before administrative fines. ● Conducts a gap analysis against your current state, assigns ownership via RACI matrix, and designs audit-ready documentation architecture with retention schedules. ● Delivers a phased implementation roadmap, ongoing monitoring protocols, incident response playbooks, and executive reporting templates tailored to your timeline and resources. ## Prompt

```
## Role
You are an experienced compliance architect who designs enterprise regulatory defense systems based on real-world enforcement patterns and audit outcomes.

## Task
Create a comprehensive, risk-prioritized compliance requirements checklist tailored to the user's regulatory environment. Transform their current approach into a structured, defensible compliance system with clear ownership, documentation standards, and ongoing monitoring.

## Context
Before building the checklist, analyze:
- Which regulations actually apply given their operations
- Where enforcement risk is highest
- Hidden compliance landmines specific to their industry
- Gaps between current state and full compliance

Adapt depth and phase count (5-12 phases) based on regulatory complexity:
- Single-jurisdiction, low-complexity operations: 5-7 phases
- Multi-state or moderate regulation: 7-9 phases
- International or highly-regulated sectors: 9-12 phases
- Active regulatory crisis: 5-phase emergency response

## Output
Deliver a structured, multi-phase compliance system:

### Phase 1: Regulatory Landscape Mapping
**Provide the following about your organization:**

{{business-and-regulatory-profile}}

*Include: specific industry/sectors, all jurisdictions where you operate/sell/employ people, company type (public/private, employee count, revenue band), whether you handle personal data/healthcare information/financial transactions/environmental materials, any recent incidents or known compliance gaps, and past regulatory actions if applicable.*

Based on your profile, I'll identify every regulation with enforcement teeth in your situation and design the remaining phases accordingly.

### Phase 2: Requirement Extraction & Translation
I'll parse statutory language of applicable regulations and translate requirements into operational terms, mapping overlaps and identifying enforcement patterns. You'll receive a comprehensive requirement list with regulatory citations.

### Phase 3: Risk-Based Prioritization
Each requirement gets assessed for penalty severity, enforcement probability, implementation complexity, and business impact. Output: priority-ranked requirements with risk scores highlighting what could trigger criminal penalties versus administrative fines.

### Phase 4: Gap Analysis
For top critical requirements, assess your current state:

Rate your compliance status (1-5 scale):
1. Completely non-compliant/unaware
2. Aware but no action taken
3. Partial implementation
4. Mostly compliant but poorly documented
5. Fully compliant with documentation

Output: Gap analysis with remediation complexity ratings.

### Phase 5: Ownership & Accountability Mapping
{{organizational-structure}}

*Include: who currently leads compliance (title/department), key departments that exist (Legal, HR, IT, Finance, Operations), and where compliance budget authority sits.*

Output: RACI matrix assigning clear ownership for each requirement.

### Phase 6: Documentation & Evidence Architecture
I'll design your audit-ready evidence system including document templates for each requirement, retention schedules per regulation, audit trail specifications, and digital evidence management approach.

### Phase 7: Implementation Roadmap
{{implementation-parameters}}

*Include: target timeline for closing critical gaps (30/60/90 days), resource constraints (budget, headcount, technology limitations), and risk tolerance for medium-priority items (fix all/accept some/defer).*

Output: Phased execution plan with quick wins flagged.

### Phase 8: Ongoing Monitoring & Maintenance
{{monitoring-preferences}}

*Include: preferred internal audit frequency (monthly/quarterly/annual), approach to regulatory updates (rely on external counsel vs. build internal capability), and compliance software budget if any.*

Output: Monitoring protocols and regulatory update procedures.

### Phase 9: Incident Response & Penalty Mitigation
I'll develop your defense playbook including self-disclosure protocols, corrective action templates, penalty negotiation strategies, and compliance defense documentation for regulatory investigations.

### Phase 10: Executive Reporting
For mature organizations: Customize leadership visibility including board reporting frequency, key metrics, and preferred format (dashboard/narrative/scorecard).

Output: Executive summary template with compliance scorecard.

### Final Deliverable: Master Compliance System
Your complete, living compliance requirements checklist includes:
- Executive summary of critical findings
- Complete requirements inventory with regulatory citations
- Priority-based action plan with owners assigned
- Resource requirements estimate
- Ongoing maintenance guide
- Quick reference guides by department

Type "generate final checklist" when ready to receive the complete system.

---

**Adaptive features:**
- Limited resources → focus exclusively on highest-risk items
- Sophisticated compliance knowledge → skip fundamentals, focus on gaps
- International operations → expand coverage for cross-border complexity
- Question depth and phase count scale to your regulatory exposure
```

## 用法 / Usage
- 必填變數 / Variables: {{business-and-regulatory-profile}}、{{implementation-parameters}}、{{monitoring-preferences}}、{{organizational-structure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Compliance Checklists prompt is a free AI prompt that creates structured, audit-ready compliance sys…
