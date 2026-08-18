# WCAG Compliance Checklist Generator for Websites

## 簡介

The WCAG Compliance Checklist Generator for Websites is a free AI prompt that creates a detailed accessibility audit framework for any website URL based on the latest Web Content Accessibility Guidelines. This WCAG compliance prompt for ChatGPT produces a structured, five-category checklist that mirrors the core WCAG principles: Perceivable (text alternatives, multimedia, adaptable content), Operable (keyboard access, timing, navigation), Understandable (readable text, predictable behavior), Robust (compatibility with assistive technologies), and Testing with Assistive Technologies (screen reader and keyboard verification). Each criterion includes fields to document the issue found, assign severity (High, Medium, Low), and record a recommended fix. The prompt runs on ChatGPT, Claude, and Gemini, delivering output in plain language that both technical teams and non-expert stakeholders can act on. Use it to prepare for accessibility audits, document remediation workflows, meet ADA or Section 508 requirements, or establish an internal quality-assurance baseline for inclusive design. ● Organizes criteria by the five WCAG principles so auditors can systematically review every guideline area ● Provides checkbox format with issue description, severity rating, and fix recommendation fields for clear documentation ● Uses plain language accessible to designers, developers, and compliance officers without specialized accessibility training ● Adapts to any website URL, making it reusable across multiple projects and client sites ## Prompt

```
## Role
You are an expert web accessibility specialist with deep knowledge of WCAG standards and best practices for ensuring accessible, inclusive websites.

## Task
Generate a comprehensive web accessibility compliance checklist for auditing {{website-url}} against the latest WCAG guidelines.

## Structure
Organize the checklist into five categories based on WCAG principles:

1. **Perceivable** – Information and UI components must be presentable to users in ways they can perceive
2. **Operable** – UI components and navigation must be operable by all users
3. **Understandable** – Information and UI operation must be understandable
4. **Robust** – Content must be robust enough to work with current and future technologies
5. **Testing with Assistive Technologies** – Verification using screen readers, keyboard navigation, and other assistive tools

Under each category, list specific criteria to evaluate. For each criterion, provide a checkbox format that allows documenting:
- Issue Found (description of the problem)
- Severity (High, Medium, or Low)
- Recommended Fix (actionable solution)

## Output
Format the checklist as follows:

**Web Accessibility Compliance Checklist for {{website-url}}**

### Perceivable
- [ ] Criterion description
  - Issue Found: [Describe issue]
  - Severity: High | Medium | Low
  - Recommended Fix: [Explain fix]
- [ ] Criterion description
  - Issue Found:
  - Severity:
  - Recommended Fix:

### Operable
- [ ] Criterion description
  - Issue Found:
  - Severity:
  - Recommended Fix:

### Understandable
- [ ] Criterion description
  - Issue Found:
  - Severity:
  - Recommended Fix:

### Robust
- [ ] Criterion description
  - Issue Found:
  - Severity:
  - Recommended Fix:

### Testing with Assistive Technologies
- [ ] Criterion description
  - Issue Found:
  - Severity:
  - Recommended Fix:

Ensure the checklist is comprehensive, uses plain language accessible to non-experts, and prioritizes the most critical accessibility issues in each category.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The WCAG Compliance Checklist Generator for Websites is a free AI prompt that creates a detailed accessibility…
