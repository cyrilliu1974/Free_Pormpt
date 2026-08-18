# Secure Communication Protocol Builder

## 簡介

The Secure Communication Protocol Builder is a free AI prompt that creates a complete confidential information handling framework for organizations managing sensitive data across multiple communication channels. This secure communication protocol prompt for ChatGPT generates a structured document that covers data classification tiers, channel-specific encryption and access controls, incident response workflows, employee training programs, third-party agreements, and maintenance schedules. It translates complex security requirements into clear, actionable policies accessible to technical and non-technical stakeholders alike. Organizations use it to establish consistent data handling standards across email, messaging platforms, file sharing, video conferencing, and other channels. The prompt runs on ChatGPT, Claude, Gemini, and Grok, adapting to your existing security context including current communication tools, classification systems, and retention policies. Reach for this prompt when you need to formalize data security practices, satisfy compliance requirements, onboard employees to confidential information policies, or audit and strengthen existing protocols. ● Defines 3-4 data classification levels with clear handling criteria for each sensitivity tier ● Specifies access controls, encryption methods, and retention policies tailored to each communication channel in use ● Provides a five-stage incident response plan from detection through post-incident review ● Outlines employee training frequency, core topics, and third-party NDA provisions ● Includes a protocol maintenance schedule with review frequency and stakeholder roles ## Prompt

```
## Role

You are a communications security expert specializing in confidential information handling protocols. Design a comprehensive framework that ensures data security and integrity across all communication channels and throughout the information lifecycle.

## Task

Create a complete protocol document covering data classification, channel-specific security measures, incident response, training requirements, third-party management, and ongoing review processes. Address potential vulnerabilities with actionable mitigation steps. Write in clear, non-technical language accessible to all stakeholders.

## Context

{{organizational-security-context}}

Include: communication channels in use (email, messaging platforms, file sharing, video conferencing, etc.), existing data classification categories (if any), and current data retention policies.

## Output

Structure the protocol as follows:

**1. Data Classification**
- Define 3-4 categories of confidential information with clear criteria for each level
- Include handling requirements per category

**2. Communication Channel Security**

For each channel in use, specify:
- Access controls (authentication, authorization, role-based permissions)
- Encryption methods (in-transit and at-rest)
- Data retention policy (storage duration, deletion procedures)

**3. Incident Response Plan**
- Detection: Monitoring methods and alert triggers
- Containment: Immediate isolation steps
- Investigation: Evidence gathering and analysis process
- Recovery: System restoration and data integrity verification
- Post-incident review: Lessons learned and protocol updates

**4. Employee Training Program**
- Frequency: Initial onboarding plus recurring intervals
- Core topics: data classification, secure communication practices, incident reporting, social engineering awareness, compliance requirements

**5. Third-Party Agreements**
- NDA requirements and scope
- Data handling provisions and restrictions
- Audit rights and compliance verification

**6. Protocol Maintenance**
- Review frequency (recommended: quarterly or semi-annually)
- Stakeholders involved (IT security, legal, compliance, department heads)
- Update process and change management procedures
```

## 用法 / Usage
- 必填變數 / Variables: {{organizational-security-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Secure Communication Protocol Builder is a free AI prompt that creates a complete confidential information…
