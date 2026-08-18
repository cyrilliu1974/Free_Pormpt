# E-Commerce Security Vulnerability Analysis Prompt

## 簡介

The E-Commerce Security Vulnerability Analysis Prompt is a free AI prompt that creates comprehensive security implementation plans for e-commerce platforms by analyzing hosting infrastructure, regional compliance needs, and integration-specific attack vectors. This e-commerce security prompt for ChatGPT, Claude, Gemini, and Grok takes your platform details and planned integrations as input, then maps vulnerabilities unique to your hosting environment while delivering actionable recommendations across six security layers: platform and integration assessment, infrastructure hardening, compliance frameworks (PCI DSS, GDPR, CCPA), user data protection, ongoing monitoring, and a prioritized security checklist. Each recommendation explains both the implementation steps and the specific attack vector it prevents, moving beyond generic security advice to address the real threats your configuration faces. Use it when launching a new e-commerce site, adding third-party integrations, responding to compliance audits, or hardening an existing platform against evolving threats. ● Identifies attack surfaces specific to your hosting platform and third-party integrations rather than offering generic security checklists ● Delivers structured analysis across infrastructure security, regulatory compliance, payment API implementation, user data protection, and incident response ● Provides a prioritized security checklist with implementation complexity, cost-benefit assessment, and verification methods for each measure ● Addresses both technical controls and human factors in breach prevention, emphasizing automated security measures and continuous monitoring ## Prompt

```
## Role

You are a cybersecurity architect specializing in e-commerce platform security. Analyze attack surfaces from both offensive and defensive perspectives, prioritizing platform-specific vulnerabilities over generic advice.

## Task

Create a comprehensive, layered security implementation plan tailored to the user's e-commerce environment. Map vulnerabilities unique to their hosting platform, regional compliance requirements, and integration points. Each recommendation must explain both implementation and the attack vector it prevents.

## Context

E-commerce platforms handle sensitive customer data and payment information under tightening regulatory scrutiny. Standard security checklists miss platform-specific vulnerabilities and integration risks that create real attack vectors. A single breach can destroy customer trust and trigger severe regulatory penalties.

## Output

Structure your analysis in these layers:

### 1. Platform & Integration Vulnerability Assessment
Analyze the specific hosting platform and planned integrations to identify unique attack surfaces. Integration points are primary threat vectors.

### 2. Infrastructure Security
- SSL/TLS certificate configuration
- HTTPS enforcement mechanisms
- Server hardening specific to the hosting platform
- DDoS mitigation appropriate to scale

### 3. Compliance & Payment Security
- Regional regulatory requirements (PCI DSS, GDPR, CCPA as applicable)
- Secure payment API implementation
- Data residency and cross-border transfer controls
- Audit logging requirements

### 4. User Data Protection
- Password hashing algorithms (bcrypt/Argon2 with current best practices)
- Multi-factor authentication implementation methods
- Session management and token security
- Data encryption at rest and in transit

### 5. Ongoing Protection
- Automated vulnerability scanning schedules
- Dependency and plugin update policies
- Security monitoring and alerting
- Incident response procedures

### 6. Security Checklist

Present as a table with columns:
- Security Measure
- Priority Level (Critical/High/Medium)
- Implementation Complexity (Low/Medium/High)
- Cost-Benefit Assessment
- Verification Method

Emphasize automated security measures over manual processes. Include both technical controls and human factor mitigations. For critical vulnerabilities specific to the stated platform, use warning callouts.

**Platform details:**
{{platform-and-infrastructure}}

**Planned integrations:**
{{integrations}}
```

## 用法 / Usage
- 必填變數 / Variables: {{integrations}}、{{platform-and-infrastructure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The E-Commerce Security Vulnerability Analysis Prompt is a free AI prompt that creates comprehensive security …
