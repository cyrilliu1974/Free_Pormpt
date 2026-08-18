# Design Ticket Prioritization Scoring Systems

## 簡介

The Design Ticket Prioritization Scoring Systems prompt is a free AI prompt that builds a complete, objective ticket prioritization framework for customer support teams struggling with manual triage at scale. This ticket prioritization prompt for ChatGPT guides you through designing a 0-100 scoring system based on 6-8 weighted criteria - customer tier, issue severity, scope, time sensitivity, sentiment signals, and ticket age - all measurable by your support platform. It outputs five components: a scoring criteria table with measurement methods and rationale, a four-tier priority mapping (P1-P4) with response and resolution SLAs, dynamic adjustment rules including age-based escalation and re-open penalties, a plain-language implementation specification with complete formulas for developers, and a monthly calibration checklist to prevent score inflation. The system runs on ChatGPT, Claude, Gemini, and Grok, and accepts variables for your business context and support platform to tailor the framework to your team's workflow. Reach for this prompt when manual prioritization creates inconsistency, biases toward loud customers, or collapses under volume, or when you need an objective, repeatable system that small teams can implement without dedicated triage roles. ● Produces 6-8 weighted criteria with objective measurement methods tied to data your support platform already captures ● Maps scores to four priority levels with target response and resolution times, ensuring no more than 20% of tickets fall into P1 ● Includes dynamic adjustment formulas for ticket age, re-opens, repeat contacts, and VIP overrides with specific threshold values ● Delivers a developer-ready implementation spec with complete scoring formulas, required data fields, automation triggers, and worked examples ● Provides a monthly calibration process with metrics to review, decision criteria, and thresholds that indicate the system needs retuning ## Prompt

```
## Role
You are an expert support operations analyst and systems architect specializing in ticket prioritization frameworks for high-volume customer support teams.

## Task
Design a complete, mathematically sound ticket prioritization scoring system that automatically assigns numerical priority scores to incoming support tickets based on weighted, measurable criteria.

## Context
Manual prioritization collapses under volume, creates inconsistency, and biases toward loud customers rather than actual urgency. Effective prioritization requires objective criteria, clear weighting rationale, dynamic adjustments over time, and calibration mechanisms to prevent score inflation.

**Business context:**
{{business-context}}

Support channels: email, live chat, and in-app messaging
Current method: manual triage by the first available agent
Team structure: small support team without dedicated triage or escalation roles

## Output
Deliver five components:

### 1. Scoring Criteria
Define 6-8 scoring criteria with assigned weights totaling 100%. Include customer tier/account value, issue severity, issue scope, time sensitivity, customer sentiment signals, and ticket age. Present as a markdown table:

| Criterion | Weight (%) | Measurement Method | Rationale |
|-----------|------------|-------------------|------------|

Ensure criteria are objectively measurable using data automatically captured by {{support-platform}}. Differentiate weights meaningfully rather than distributing equally.

### 2. Priority Level Mapping
Create a 0-100 scoring scale mapped to four priority levels. Present as a markdown table:

| Priority Level | Score Range | Target Response Time | Target Resolution Time |
|----------------|-------------|---------------------|------------------------|
| P1 Critical | | | |
| P2 High | | | |
| P3 Medium | | | |
| P4 Low | | | |

Ensure no more than 20% of tickets fall into P1 based on the score distribution.

### 3. Dynamic Score Adjustment Rules
Provide numbered rules including:
- Age-based escalation formula (how score increases as ticket remains open)
- Re-open penalty (score adjustment when ticket is reopened)
- Repeat contact bonus (score adjustment for multiple contacts on same issue)
- VIP override conditions that trigger automatic priority changes

Include specific formulas and threshold values for each rule.

### 4. Implementation Specification
Write a plain-language specification developers can use to build this system. Include:
- Complete scoring formula in a code block
- Required data fields from {{support-platform}}
- Automation triggers
- Update frequency
- Calculation examples with sample values

### 5. Monthly Calibration Process
Define a calibration process including:
- Specific metrics to review
- Questions to ask
- Decision criteria for adjusting weights based on actual outcomes
- Thresholds that indicate the system needs retuning

Format as a structured checklist or numbered procedure.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{support-platform}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Design Ticket Prioritization Scoring Systems prompt is a free AI prompt that builds a complete, objective …
