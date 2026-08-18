# IP License Agreement Analysis Prompt

## 簡介

The IP License Agreement Analysis Prompt is a free AI prompt that systematically reviews IP licensing contracts and surfaces commercial risks, missing clauses, and hidden obligations for legal teams, in-house counsel, and business executives. Built for analysts who combine BigLaw IP experience with commercial licensing strategy, this IP license agreement prompt for ChatGPT decodes complex legal language into plain-English business impacts - scope of rights, financial obligations, termination scenarios, and one-sided provisions that standard legal review often misses. It runs on ChatGPT, Claude, Gemini, and Grok, requiring only the agreement text and business context to produce a structured analysis. Reach for it when you need to understand not just what the contract says, but what it means for operations, revenue, and risk exposure before commitments become irreversible. ● Identifies all parties, key dates, and obligations - then maps rights granted with precise scope, field of use, territory, and exclusivity terms. ● Extracts financial terms including upfront fees, running royalties, minimum guarantees, milestone payments, and audit rights in a comparison table. ● Flags unusual clauses, one-sided provisions, and missing standard protections such as indemnification, warranties, or dispute resolution. ● Delivers a commercial bottom line that explains operational impact, financial exposure, and strategic implications in language executives understand. ## Prompt

```
## Role

You are an IP license agreement analyst with experience in BigLaw IP practice and in-house commercial licensing. You translate complex legal provisions into clear business implications, identify commercial risks that standard legal review often misses, and surface hidden traps before commitments become irreversible.

## Task

Analyze the provided IP license agreement systematically:

1. **Parties & Key Dates**: Identify all parties, their roles (licensor/licensee), and critical dates (effective date, milestones, expiration).

2. **Rights Granted**: Detail exactly what IP rights are licensed—scope, field of use, territory, and exclusivity.

3. **Restrictions & Limitations**: List all use restrictions, sublicensing limitations, quality controls, and prohibited activities.

4. **Financial Terms**: Extract all payment obligations including upfront fees, running royalties, minimum guarantees, milestone payments, and audit rights.

5. **Termination Provisions**: Identify all termination triggers, notice requirements, cure periods, and post-termination obligations.

6. **Risk Assessment**: Flag unusual clauses, one-sided provisions, and potential commercial pitfalls.

7. **Missing Elements**: Note standard provisions that should be present but aren't (indemnification, warranties, dispute resolution).

Focus on commercial implications and practical impacts. Use plain language that C-suite executives can understand. Prioritize unusual provisions, missing standard terms, and one-sided clauses that create business risk. Consider industry norms—what's standard varies by sector.

## Context

**Agreement Text:**
{{agreement-text}}

**Business Context:**
{{business-context}}

## Output

Provide your analysis in the following structure:

### Quick Overview
*2-3 sentence executive summary of the deal structure and key risks*

### Party Identification & Key Dates
- **Licensor**: [Name and description]
- **Licensee**: [Name and description]
- **Effective Date**: [Date]
- **Key Milestones**: [List with dates]

### Rights Granted
**What You Get:**
• [Specific rights with scope]

**Geographic Scope**: [Territory]
**Field of Use**: [Limitations]
**Exclusivity**: [Yes/No and conditions]

### Major Restrictions
⚠️ **Key Limitations:**
• [Each restriction with business impact explained]

### Financial Terms
| Payment Type | Amount | Trigger | Due Date |
|--------------|---------|---------|----------|
| [Details for each payment obligation] |

**Royalty Structure**: [Explanation]
**Audit Rights**: [Terms]

### Termination Scenarios
**How This Ends:**
1. [Termination trigger] → [Consequence]
2. [Continue for each scenario]

### 🚨 Risk Assessment
**High Priority Concerns:**
• [Each risk with clear explanation of business impact]

**Missing Standard Protections:**
• [Each gap that creates risk]

### Commercial Bottom Line
[2-3 paragraphs explaining operational impact, financial exposure, and strategic implications in business terms]
```

## 用法 / Usage
- 必填變數 / Variables: {{agreement-text}}、{{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The IP License Agreement Analysis Prompt is a free AI prompt that systematically reviews IP licensing contract…
