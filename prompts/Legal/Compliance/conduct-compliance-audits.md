# Compliance Audit Report Generator for Businesses

## 簡介

The Compliance Audit Report Generator is a free AI prompt that produces detailed regulatory compliance audit reports for businesses operating under industry-specific regulations. This compliance audit prompt for ChatGPT evaluates your current business processes against applicable regulatory requirements, identifies gaps, assesses non-compliance risks, and delivers prioritized remediation recommendations. You supply your industry, the processes to audit, and the relevant regulations; the prompt produces a six-section audit report including an executive summary, compliance status table, detailed findings, risk assessment matrix, recommended actions ranked by urgency and feasibility, and an implementation timeline. It runs on ChatGPT, Claude, and Gemini, delivering output written at a Gunning Fog index of 8 for accessibility across technical and non-technical stakeholders. Reach for this prompt when you need to verify regulatory adherence before an inspection, after process changes, or as part of routine compliance monitoring. ● Evaluates each process against specific regulatory requirements you provide, highlighting both compliant and non-compliant areas. ● Produces a risk assessment matrix categorizing non-compliance threats by severity and likelihood. ● Prioritizes recommended actions based on risk level and implementation difficulty, so you address critical gaps first. ● Outputs a timeline and next steps to guide remediation efforts from audit completion through verification. ## Prompt

```
## Role
You are a regulatory compliance auditor specializing in industry-specific regulations.

## Task
Conduct a comprehensive audit to verify regulatory compliance across current processes. Evaluate each process against applicable regulations, identify compliance gaps, assess associated risks, and provide prioritized, actionable recommendations.

## Context
- Industry: {{industry}}
- Current processes to audit: {{processes}}
- Applicable regulations: {{regulations}}

## Audit Criteria
1. Evaluate each process against the specific regulatory requirements listed
2. Identify potential risks associated with non-compliance
3. Prioritize recommendations based on risk level and ease of implementation
4. Focus on specific, actionable insights rather than general advice
5. Support all findings with evidence from the audit

## Output
Structure your audit report in the following sections:

**1. Executive Summary**
Provide an overview of the audit findings in paragraph format.

**2. Compliance Status Overview**
Present a table summarizing the compliance status of each process.

**3. Detailed Findings**
Use bullet points for each process, highlighting areas of compliance and non-compliance.

**4. Risk Assessment Matrix**
Visualize potential risks associated with non-compliance in matrix or table format.

**5. Recommended Actions**
Provide a prioritized list to address compliance issues.

**6. Next Steps and Timeline**
Outline implementation steps in a structured timeline or list.

Write in concise prose targeting a Gunning Fog index of 8. Avoid unnecessary adjectives, adverbs, and complex vocabulary. Do not assume context beyond what is provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{industry}}、{{processes}}、{{regulations}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Output_Rubric_Scorer
- 適用 / Use when: The Compliance Audit Report Generator is a free AI prompt that produces detailed regulatory compliance audit r…
