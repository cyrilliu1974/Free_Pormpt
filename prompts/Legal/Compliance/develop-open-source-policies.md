# Open-Source Software Compliance Policy Generator

## 簡介

The Open-Source Software Compliance Policy Generator is a free AI prompt that creates actionable OSS licensing policies for organizations managing software development and distribution. It analyzes your software stack, classifies licenses by copyleft strength (permissive, weak copyleft, strong copyleft), and builds approval workflows tailored to internal tools, customer-facing products, and embedded systems. This open-source compliance prompt for ChatGPT works with Claude, Gemini, and Grok to produce professional policy documents that prevent license violations, forced code disclosure, and legal disputes. The prompt is designed for engineering teams, legal departments, and compliance officers who need structured guidance on OSS license management across SaaS, on-premise, and embedded distribution models. ● Classifies all licenses in your software inventory by copyleft strength with specific usage guidelines for MIT, Apache 2.0, LGPL, MPL, GPL, and AGPL. ● Builds approval workflows that account for different distribution scenarios including SaaS deployments, on-premise installations, and embedded systems. ● Defines compliance obligations and audit procedures for ongoing license monitoring, compatibility conflict resolution, and future technology adoption. ● Outputs a structured policy document with executive summary, license matrix, decision trees, implementation timeline, and role-specific responsibilities. ## Prompt

```
## Role
You are an open-source compliance specialist with expertise in software licensing, enterprise policy development, and the Linux Foundation's Open Source Compliance framework.

## Task
Draft a comprehensive Open-Source Use Policy that categorizes licenses by copyleft strength, establishes clear approval workflows, and creates robust compliance procedures. The policy must be actionable for both technical teams and legal stakeholders while preventing license compliance failures that can result in legal disputes, forced code disclosure, or product recalls.

## Context
Organization profile and software details:
{{organization-profile}}

Current open-source landscape:
{{oss-inventory}}

## Process
1. Analyze the provided software stack and categorize all OSS licenses by copyleft strength: permissive (MIT, Apache 2.0), weak copyleft (LGPL, MPL), and strong copyleft (GPL, AGPL)
2. Create detailed approval workflows accounting for different use cases: internal tools, customer-facing products, and embedded systems
3. Establish compliance requirements specific to each distribution scenario (SaaS, on-premise, embedded)
4. Develop audit procedures for ongoing license monitoring
5. Address potential license compatibility conflicts proactively
6. Ensure the policy accommodates future technology adoption

## Output
Structure the policy document with these sections:

- **Executive Summary**: Business rationale and compliance objectives
- **License Classification Matrix**: All licenses categorized by copyleft strength with usage guidelines
- **Approval Workflows**: Decision trees and authorization paths for each use case
- **Compliance Requirements**: Obligations by distribution method and license type
- **Audit Procedures**: Ongoing monitoring, tooling, and review cadence
- **Implementation Timeline**: Phased rollout with milestones and ownership

Format as a professional policy document with clear, actionable guidelines ready for immediate implementation.
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-profile}}、{{oss-inventory}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Non_Copyable_Direction_Card_Generator
- 適用 / Use when: The Open-Source Software Compliance Policy Generator is a free AI prompt that creates actionable OSS licensing…
