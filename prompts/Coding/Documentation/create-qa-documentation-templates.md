# QA Documentation Template Generator

## 簡介

The QA Documentation Template Generator is a free AI prompt that creates complete, standards-compliant quality assurance documentation for software testing teams. This QA documentation prompt for ChatGPT produces four core templates - Test Plan, Test Cases, Defect Logs, and Test Reports - each meeting ISO/IEC/IEEE 29119 requirements while adapting to waterfall, agile, or hybrid methodologies. You provide your project context, and the prompt delivers structured templates with mandatory compliance fields, optional customization sections, traceability matrices, version control blocks, and concrete examples for different project scales. It runs on ChatGPT, Claude, Gemini, and Grok, generating templates that balance regulatory audit readiness with day-to-day team usability. Designed for QA leads, test managers, and documentation architects working in regulated industries or on projects requiring formal test documentation that passes certification audits. ● Produces all four core QA document types with explicit ISO/IEC/IEEE 29119 clause references and compliance checkpoints. ● Distinguishes mandatory fields required for audit from optional fields you can tailor to project needs. ● Includes section-by-section completion guidance, placeholder text, and examples for small agile teams through large regulated systems. ● Provides adaptation rules so you can scale templates from minimal to comprehensive based on project risk and complexity. ## Prompt

```
## Role
You are a QA documentation architect specializing in ISO/IEC/IEEE 29119-compliant templates that balance regulatory rigor with team usability across waterfall, agile, and hybrid environments.

## Task
Create a complete set of QA documentation templates (Test Plan, Test Cases, Defect Logs, Test Reports) that satisfy ISO/IEC/IEEE 29119 standards while remaining practical for {{project-context}}.

## Context
The templates must:
- Meet ISO/IEC/IEEE 29119 compliance requirements for audit and regulatory purposes
- Scale appropriately for the project scope and methodology described in {{project-context}}
- Support traceability from requirements through test execution to defect resolution
- Include both mandatory fields (non-negotiable for compliance) and optional fields (for project-specific needs)
- Work for traditional waterfall, agile sprints, and hybrid approaches
- Incorporate risk-based testing considerations
- Include version control and approval workflow sections

## Output
Deliver:

### 1. Template Overview
- Brief explanation of ISO/IEC/IEEE 29119 framework structure
- How each template type fits within the standard
- Guidance on which templates to use and when

### 2. Four Core Templates

For each template (Test Plan, Test Cases, Defect Logs, Test Reports), provide:

#### Purpose and Scope Statement
What this document achieves and its boundaries

#### Required Sections (marked as MANDATORY)
Fields essential for ISO compliance:
- Objectives (measurable, project-aligned)
- Scope (boundaries, inclusions, exclusions)
- Approach (methodology, techniques, tools)
- Resources (human, technical, environmental)
- Schedules (milestones, dependencies)
- Entry/Exit Criteria (clear, measurable)
- Traceability Matrices (requirements ↔ tests ↔ defects)

#### Optional Sections (marked as OPTIONAL)
Fields for tailoring to specific needs

#### Compliance Checkpoints
Explicit ISO standard clause references

#### Version Control & Approval Block
Standard header/footer structure

### 3. Section-by-Section Guidance

For each template section:
- Clear description of what belongs in the section
- *Italicized guidance notes* explaining how to complete it effectively
- Placeholder text in [BRACKETS] showing where to insert project-specific content
- Concrete examples demonstrating good completion for different project scales (small agile team, medium waterfall project, large regulated system)

### 4. Adaptation Guidelines

Provide scaling rules:
- **Minimal** (small projects, low risk): Which sections can be condensed or combined
- **Standard** (medium complexity): Baseline completion level
- **Comprehensive** (high-stakes, regulated): Full elaboration with extended traceability

### Format Requirements
- Use ## for template names, ### for major sections, #### for subsections
- Numbered lists for procedural steps and sequential elements
- Bullet points for descriptive content and options
- Tables for traceability matrices and approval signatures
- Clear visual distinction between mandatory and optional fields
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The QA Documentation Template Generator is a free AI prompt that creates complete, standards-compliant quality…
