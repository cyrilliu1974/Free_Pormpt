# Business Systems Integration Plan Generator

## 簡介

The Business Systems Integration Plan Generator is a free AI prompt that produces detailed integration roadmaps for connecting disparate business systems and streamlining operational processes. This business systems integration prompt for ChatGPT walks you through five core planning phases: current state analysis of both systems, integration architecture design with API specifications and data transformation logic, a phased implementation roadmap with dependencies and contingencies, a testing and validation strategy covering unit through user acceptance testing, and an efficiency measurement plan tied to baseline metrics. It runs on ChatGPT, Claude, Gemini, and Grok. Use it when merging CRM and ERP platforms, connecting e-commerce systems to inventory management, or linking any two business applications where data exchange and process automation are critical. ● Maps existing system capabilities, data models, and integration touchpoints before defining connection requirements ● Specifies API endpoints, authentication methods, middleware needs, and data transformation logic with attention to rate limits and error handling ● Breaks implementation into phased milestones with clear dependencies, rollback steps, and timeline alignment ● Establishes post-integration KPIs, monitoring dashboards, and success thresholds tied directly to your baseline efficiency metrics ## Prompt

```
## Role
You are an expert systems integration specialist.

## Task
Create a comprehensive integration plan that connects two business systems, streamlines the target process, and improves measurable efficiency.

## Context
**Systems to integrate:** {{systems-and-process}}

**Current baseline:** {{efficiency-metrics}}

**Target timeline:** {{timeline}}

## Output
Deliver a structured integration plan organized under these headings:

### 1. Current State Analysis
- Map each system's capabilities, data models, and existing interfaces
- Identify integration touchpoints and data exchange requirements
- Flag compatibility gaps or technical constraints

### 2. Integration Architecture
- Define data flow direction and transformation logic
- Specify API endpoints, authentication methods, and middleware requirements
- Anticipate technical challenges (rate limits, data format mismatches, error handling)

### 3. Implementation Roadmap
- Break the integration into phased milestones aligned with the timeline
- Assign dependencies between tasks
- Include rollback and contingency steps

### 4. Testing & Validation Strategy
- Unit testing for individual connectors
- End-to-end process testing with realistic data volumes
- User acceptance criteria and sign-off gates

### 5. Efficiency Measurement Plan
- Define post-integration KPIs that map to the baseline metrics
- Recommend monitoring dashboards and reporting cadence
- Establish success thresholds and review intervals

Use bullet points and numbered steps throughout to maintain clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{efficiency-metrics}}、{{systems-and-process}}、{{timeline}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Business Systems Integration Plan Generator is a free AI prompt that produces detailed integration roadmap…
