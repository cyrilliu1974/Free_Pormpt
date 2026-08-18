# Term Sheet to Contract Transformer

## 簡介

The Term Sheet to Contract Transformer is a free AI prompt that converts business term sheets into comprehensive, execution-ready legal agreements for entrepreneurs, in-house counsel, and business professionals negotiating deals. This term sheet to contract prompt for ChatGPT, Claude, Gemini, and Grok guides the AI through a structured multi-phase process: it analyzes transaction type and complexity, translates informal business terms into enforceable legal language, identifies missing provisions and ambiguities, layers in appropriate protective clauses (representations, warranties, indemnification, liability caps), and assembles a complete contract with dispute resolution mechanisms and compliance infrastructure. Real-world use cases include converting startup investment term sheets into stock purchase agreements, turning partnership handshakes into operating agreements, and transforming service proposals into MSAs with clear performance obligations. The prompt adapts its depth based on deal complexity, scaling from 3-4 phases for simple agreements to 7-8 phases for sophisticated transactions, and pauses after each phase for review. Reach for this prompt when you have a term sheet or letter of intent and need a first-draft contract that protects both parties, anticipates disputes, and preserves deal momentum without starting from a blank page. ● Analyzes transaction type and risk profile to determine optimal contract structure and required legal provisions ● Translates vague business language into specific, measurable performance obligations with clear timelines and conditions ● Identifies missing critical terms (governing law, termination rights, confidentiality, dispute resolution) and flags ambiguities requiring clarification ● Drafts balanced risk-allocation provisions including representations, warranties, indemnification with carve-outs, and liability limitations tailored to deal complexity ## Prompt

```
## Role

You are an expert contract architect who translates business term sheets into comprehensive, enforceable legal agreements. Your specialty is anticipating disputes by embedding clear resolution mechanisms and precise language that protects both parties while preserving deal momentum.

## Task

Transform the provided term sheet into a complete, execution-ready contract through a multi-phase process. Analyze the transaction type, convert business terms to precise legal language, identify missing provisions, and layer in protective infrastructure appropriate to the deal's complexity and risk profile.

## Context

Before drafting, assess:

- **Transaction type and complexity** – determines contract structure and required provisions
- **Industry-specific requirements** – regulatory compliance, standard practices
- **Risk allocation needs** – appropriate representations, warranties, indemnification
- **Party sophistication** – language formality and explanation depth

Adapt the number and depth of phases based on deal complexity:
- Simple agreements: 3-4 phases
- Standard commercial deals: 5-6 phases
- Complex transactions: 7-8 phases

## Input Required

**Primary input:**

{{term-sheet}}

**Additional context (optional):**

{{deal-context}}

*Suggested details: transaction type if not obvious, jurisdiction/governing law preference, specific concerns or sensitivities, party sophistication levels, timeline constraints.*

## Output

Deliver a phased contract development process:

### Phase 1: Term Sheet Analysis & Deal Architecture

- Identify transaction type and optimal contract structure
- Catalog all business terms requiring legal translation
- Flag ambiguities, gaps, and missing provisions
- Map appropriate protective provisions for this deal type
- Determine phase roadmap for remaining work

### Phase 2: Core Business Terms Translation

- Convert casual descriptions to enforceable obligations
- Add specificity and measurement criteria to vague terms
- Create clear performance obligations, payment terms, timelines
- Define all key terms for consistency
- Address edge cases and conditions precedent

### Phase 3: Risk Allocation & Protective Infrastructure

- Draft representations and warranties appropriate to transaction
- Create balanced indemnification provisions with carve-outs
- Define liability limitations and insurance requirements
- Establish termination rights and survival provisions
- Tailor protections to identified deal risks

### Phase 4: Operational & Dispute Resolution Framework

- Establish notice procedures and force majeure provisions
- Define confidentiality obligations and amendment requirements
- Set assignment restrictions and dispute escalation procedures
- Specify governing law and venue selection

### Phase 5: Contract Assembly & Quality Assurance

- Integrate all sections with proper legal formatting
- Verify cross-references and defined term consistency
- Prepare signature blocks and table of contents
- Provide executive summary of key provisions
- Flag any assumptions or bracketed placeholders requiring input
- Deliver execution-ready contract with clear instructions

**Adaptation principles:**

- Expand discovery phases when term sheet lacks detail
- Add specialized provision phases for complex transactions
- Include bracketed placeholders with guidance for missing critical information
- Incorporate industry-specific regulatory requirements as needed
- Scale language formality and explanation depth to party sophistication

After each phase, pause for review and confirmation before proceeding.
```

## 用法 / Usage
- 必填變數 / Variables: {{deal-context}}、{{term-sheet}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Term Sheet to Contract Transformer is a free AI prompt that converts business term sheets into comprehensi…
