# HR Policy Risk Analysis Prompt

## 簡介

The HR Policy Risk Analysis Prompt is a free AI prompt that identifies dangerous language patterns in workplace policies and delivers legally safer alternatives for HR teams and employment counsel. This HR policy risk analysis prompt for ChatGPT, Claude, Gemini, and Grok takes your organization context and surfaces phrases that sound reasonable but create unintended contractual obligations, discriminatory impact, procedural violations, or regulatory non-compliance. It explains the specific legal vulnerability each phrase introduces and why courts or agencies view it unfavorably, then offers replacement language that accomplishes the same policy goal without the exposure. HR professionals use it before publishing new policies, during compliance audits, and when preparing for regulatory review. Reach for this prompt when drafting employee handbooks, revising discipline procedures, or conducting risk assessments of existing HR documentation. ● Surfaces overly broad policy statements that create enforceable promises the organization cannot keep or do not intend to honor ● Flags language with discriminatory implications that appear neutral but produce disparate impact under Title VII or ADA scrutiny ● Identifies unclear procedural language that violates due process expectations or invites wrongful termination claims ● Provides jurisdiction-aware alternative phrasing tailored to your organization's legal environment and compliance concerns ## Prompt

```
## Role

You are an expert employment law attorney and HR compliance specialist with deep experience defending organizations against workplace litigation and regulatory violations.

## Task

Identify high-risk language patterns in HR policies that create legal vulnerabilities and provide safer alternative phrasing. Analyze common policy language that creates unintended legal exposure through overly broad statements, discriminatory implications, unclear procedures, or promises the organization cannot keep.

## Context

Poorly worded policies become evidence in discrimination lawsuits, wrongful termination claims, and regulatory audits. Focus on phrases that sound reasonable to HR professionals but create liability traps when scrutinized by opposing counsel or regulatory agencies.

Examine language that inadvertently creates contractual obligations, discriminatory impact, procedural due process violations, or regulatory non-compliance. Consider how seemingly innocent phrases can be weaponized in legal proceedings.

**Organization profile:**
{{organization-context}}

## Output

Provide a numbered list where each entry contains:

1. **Problematic phrase** – the exact language that creates risk
2. **Legal risk** – the specific vulnerability it creates and why courts or agencies view it unfavorably
3. **Recommended alternative** – safer phrasing that accomplishes the policy goal without the legal exposure

Format each entry clearly with these three components. Focus on the most common and dangerous patterns first.
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The HR Policy Risk Analysis Prompt is a free AI prompt that identifies dangerous language patterns in workplac…
