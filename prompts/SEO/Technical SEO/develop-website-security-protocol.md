# Website Security Audit Protocol for Third-Party Scripts

## 簡介

The Website Security Audit Protocol for Third-Party Scripts is a free AI prompt that produces a structured security audit framework for evaluating and managing third-party scripts on any website. This website security protocol prompt for ChatGPT creates a six-part audit report that inventories every third-party script, assesses performance impact using a visual rating system, evaluates security risks from each provider, analyzes SEO consequences, establishes governance policies for ongoing script management, and delivers a prioritized implementation roadmap. It runs on ChatGPT, Claude, Gemini, and Grok, transforming a website URL into an actionable security review that cybersecurity consultants, technical SEO specialists, and web development teams can use to identify vulnerabilities from analytics trackers, advertising pixels, chat widgets, and other external JavaScript. The protocol is designed for organizations that need to systematically audit third-party dependencies and reduce attack surface while maintaining site performance. ● Inventories all third-party scripts with provider details, loading methods, and page locations in a structured table format ● Rates performance impact of each script using a color-coded system and provides optimization recommendations ● Classifies security risk levels and outlines specific mitigation strategies for vulnerabilities ● Evaluates SEO impact against a checklist of best practices including crawl accessibility and page speed ● Defines a governance framework with approval processes, auditing schedules, and role assignments ● Delivers a step-by-step implementation plan prioritized by risk level with timelines and success metrics ## Prompt

```
## Role
You are an expert cybersecurity consultant specializing in website security audits and third-party script management.

## Task
Develop a comprehensive security audit protocol for third-party scripts on {{website-url}}, addressing security vulnerabilities, performance impacts, and SEO risks.

## Output
Deliver a structured audit report containing:

### 1. Third-Party Script Inventory
Create a complete inventory table with these columns:
- Script Name
- Script Provider
- Script Purpose
- Script Location (header, body, footer)
- Script Loading Method (async, defer, or blocking)

### 2. Performance Impact Assessment
Rate each script using this emoji system:
- 🟢 Minimal impact
- 🟡 Moderate impact
- 🔴 Significant impact

Provide optimization recommendations for script loading and performance.

### 3. Security Risk Evaluation
Classify each script by risk level:
- **Low Risk**: Trusted provider, no known vulnerabilities
- **Medium Risk**: Less-established provider or minor vulnerabilities
- **High Risk**: Known security issues or untrusted source

Outline specific mitigation strategies for each identified risk.

### 4. SEO Impact Analysis
Evaluate each script against this checklist:
- ✅ Does not block search engine crawlers
- ✅ Does not generate duplicate content
- ✅ Does not slow page load times excessively
- ❌ Violates one or more SEO best practices

Provide actionable recommendations for any SEO issues found.

### 5. Governance Policy
Define a management framework including:
- Approval process for adding new scripts
- Regular auditing and monitoring schedule
- Procedures for removing outdated or insecure scripts
- Roles and responsibilities for script inventory maintenance

### 6. Implementation Plan
Outline a step-by-step roadmap with:
- Task prioritization based on risk level and performance impact
- Timeline for completing each audit phase
- Required tools and resources for ongoing monitoring
- Success metrics for measuring implemented changes

Format the response using markdown with tables, bullet points, and the specified emoji systems.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Website Security Audit Protocol for Third-Party Scripts is a free AI prompt that produces a structured sec…
