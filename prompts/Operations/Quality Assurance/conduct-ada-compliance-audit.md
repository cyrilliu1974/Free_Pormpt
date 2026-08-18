# ADA Compliance Audit Report Generator

## 簡介

The ADA Compliance Audit Report Generator is a free AI prompt that produces detailed accessibility audit reports for websites, helping businesses identify and fix compliance issues. This ADA compliance audit prompt for ChatGPT works by evaluating your website against WCAG 2.1 success criteria, Section 508 standards, and location-specific regulations. It identifies barriers preventing users with disabilities from accessing content, assigns severity ratings to each issue, and delivers clear remediation steps prioritized by impact and effort. The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing a complete audit report with methodology, compliance overview, issue breakdown, remediation roadmap, training recommendations, and an ongoing monitoring plan. Use it when you need to assess website accessibility, prepare for compliance reviews, or develop a systematic plan to improve usability for visitors with disabilities. ● Evaluates conformance to WCAG 2.1 Level A, AA, and AAA standards plus Section 508 requirements ● Categorizes issues by severity (High, Medium, Low) with specific remediation steps for each finding ● Produces a three-tier remediation roadmap separating critical, important, and minor fixes ● Includes training recommendations and ongoing monitoring plans to maintain accessibility over time ## Prompt

```
## Role
You are an expert web accessibility consultant specializing in ADA compliance audits.

## Task
Perform a comprehensive accessibility audit on {{website-url}}, focusing on adherence to ADA regulations and best practices for {{location}}. Identify accessibility issues, provide clear remediation recommendations, and deliver an actionable report to help improve the website's accessibility and compliance.

## Audit Criteria
- Evaluate against WCAG 2.1 success criteria, Section 508 standards, and relevant local regulations for {{location}}
- Identify accessibility barriers that prevent users with disabilities from accessing content or functionality
- Provide clear, actionable recommendations for remediating identified issues
- Prioritize issues based on their impact on accessibility and the effort required to address them
- Avoid technical jargon; ensure the report is understandable by non-technical stakeholders

## Output
Deliver your audit as a structured report:

### Executive Summary
Outline the overall state of the website's accessibility and compliance.

### Accessibility Audit Methodology
Describe the methodology used to assess the website.

### Compliance Overview
- **WCAG 2.1 Conformance Level**: Assess Level A, AA, or AAA conformance
- **Section 508 Compliance**: Evaluate adherence to federal standards
- **Local Regulations Adherence**: Address {{location}}-specific requirements

### Accessibility Issues
For each issue identified, provide:
- Description: What the issue is
- Severity: High, Medium, or Low
- Recommendations: How to remediate

### Remediation Roadmap
- **Priority 1**: Critical issues to be addressed immediately
- **Priority 2**: Important issues to be addressed in the near future
- **Priority 3**: Minor issues to be addressed over time

### Accessibility Training Recommendations
Suggest training programs for the client's team to maintain accessibility standards.

### Ongoing Monitoring Plan
Outline a plan to ensure continued accessibility and compliance.
```

## 用法 / Usage
- 必填變數 / Variables: {{location}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The ADA Compliance Audit Report Generator is a free AI prompt that produces detailed accessibility audit repor…
