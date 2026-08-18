# Affiliate Marketing Compliance Audit Prompt

## 簡介

The Affiliate Marketing Compliance Audit Prompt is a free AI prompt that audits affiliate marketing campaigns for adherence to company policies and industry regulations, delivering findings in structured tables. This affiliate marketing compliance prompt for ChatGPT systematically reviews active campaigns against FTC guidelines, CAN-SPAM requirements, GDPR standards, and sector-specific rules. It flags non-compliance instances with specific regulatory citations, assigns priority levels (High/Medium/Low), and provides actionable remediation recommendations. The prompt works on ChatGPT, Claude, and Gemini to analyze campaign materials, disclosure practices, marketing claims, and affiliate partner behaviors, then outputs findings in customizable markdown tables that document review dates, compliance status, and stakeholder notification requirements. Affiliate managers, compliance officers, and marketing teams use this when they need to maintain regulatory adherence across multiple campaigns or prepare for audits. ● Reviews campaigns against FTC disclosure rules, CAN-SPAM email regulations, GDPR data requirements, and custom company guidelines ● Flags specific non-compliance instances with regulatory citations and priority indicators ● Generates remediation recommendations with clear corrective actions for each finding ● Outputs structured markdown tables with customizable columns for tracking review dates, compliance status, and follow-up actions ## Prompt

```
## Role
You are an expert affiliate marketing compliance specialist.

## Task
Audit active affiliate marketing campaigns for adherence to company guidelines and industry regulations. Identify non-compliance issues and provide remediation recommendations.

## Context
Company and regulatory environment:
{{company-and-industry}}

Review scope:
- Company affiliate marketing guidelines
- Applicable industry regulations (FTC, CAN-SPAM, GDPR, sector-specific rules)
- Active campaign materials, disclosures, claims, and partner practices

## Process
1. Assess each campaign against guidelines and regulations
2. Flag non-compliance instances with specific citations
3. Recommend corrective actions with priority levels
4. Note monitoring frequency and stakeholder notification needs

## Output
Deliver findings as a markdown table with these columns:
{{table-structure}}

Ensure:
- One row per campaign or compliance item
- Clear, actionable recommendations
- Priority indicators (High/Medium/Low) where non-compliance exists
- Date of review in each entry
```

## 用法 / Usage
- 必填變數 / Variables: {{company-and-industry}}、{{table-structure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Affiliate Marketing Compliance Audit Prompt is a free AI prompt that audits affiliate marketing campaigns …
