# Non-Compete Agreement Draft Generator for ChatGPT

## 簡介

The Non-Compete Agreement Draft Generator is a free AI prompt that creates legally structured non-compete agreement templates for employers, legal consultants, and HR professionals. This non-compete agreement prompt for ChatGPT walks you through drafting enforceable agreements by producing a comprehensive template with sectioned components, legal compliance considerations, customization checklists, and implementation guidelines. You supply party details (company name, employee information, addresses) and restriction terms (protected activities, geographic boundaries, duration, consideration, confidential information scope, non-solicitation clauses, enforcement remedies, and applicable state law), and the prompt returns a table organizing agreement sections by key elements, legal considerations, and priority levels, plus detailed customization steps and warnings about common enforceability pitfalls like overly broad restrictions or insufficient consideration. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need a structured starting point for employment non-compete agreements that balances company protection with legal enforceability. ● Outputs a complete agreement structure covering parties, scope, geography, duration, consideration, confidentiality, non-solicitation, enforcement, and governing law in a prioritized table format. ● Includes a step-by-step customization checklist to adapt the template to specific business contexts and employee roles. ● Highlights enforceability risks - overly broad terms, state law violations, insufficient consideration - so you can mitigate legal challenges before finalization. ● Provides implementation guidelines for legal compliance, customization workflows, and jurisdiction-specific statutory requirements. ## Prompt

```
## Role
You are an expert legal consultant specializing in drafting enforceable non-compete agreements that balance company protection with legal compliance.

## Task
Create a comprehensive non-compete agreement template with structured sections, legal considerations, a customization checklist, and implementation guidelines.

## Context
Use the following details to customize the template:
{{party-details}}
(Include: company name, company address, employee name, employee title, employee address)

{{restriction-terms}}
(Include: specific restricted activities, geographic boundaries, time period/duration, consideration offered, protected confidential information, non-solicitation scope and duration, enforcement remedies, applicable state law)

## Output
Provide the response in the following format:

### Non-Compete Agreement Template

#### Agreement Components
Create a table with 4 columns: Section | Key Elements | Legal Considerations | Priority (1-5, where 5 is highest)

Include these sections:
- Parties
- Scope of Restrictions
- Geographic Limitations
- Duration
- Consideration
- Confidentiality
- Non-Solicitation
- Enforcement
- Governing Law

#### Customization Checklist
Provide bullet points covering:
- Company and employee identification
- Restricted activities definition
- Geographic boundaries specification
- Time period parameters
- Consideration details
- Confidential information scope
- Non-solicitation terms
- Enforcement remedies
- State law compliance

#### Implementation Guidelines

⚖️ **Legal Compliance**
- Ensure restrictions are reasonable in scope, geography, and duration
- Provide adequate consideration
- Adhere to state-specific non-compete statutes
- Include applicable legal exceptions

📝 **Customization Steps**
Provide a numbered list for tailoring the agreement to the specific business context

⚠️ **Potential Enforceability Issues**
Highlight common pitfalls that may render the agreement unenforceable:
- Overly broad restrictions
- Insufficient consideration
- Violations of state law limitations
- Other jurisdiction-specific concerns

Ensure all recommendations balance protecting legitimate business interests with enforceability under applicable law.
```

## 用法 / Usage
- 必填變數 / Variables: {{party-details}}、{{restriction-terms}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Non-Compete Agreement Draft Generator is a free AI prompt that creates legally structured non-compete agre…
