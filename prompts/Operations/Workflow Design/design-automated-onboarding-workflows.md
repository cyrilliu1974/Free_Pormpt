# Automated Onboarding Workflow Design Prompt

## 簡介

The Automated Onboarding Workflow Design Prompt is a free AI prompt that creates BPMN 2.0-compliant automation flows for employee onboarding systems tailored to your existing tech stack and organizational challenges. This onboarding workflow prompt for ChatGPT, Claude, Gemini, and Grok maps the complete new-hire journey from offer acceptance to full productivity, identifying decision points, system integrations, and communication touchpoints across HR, IT, managers, and learning platforms. It produces a text-based BPMN diagram, integration architecture showing how your current systems connect via APIs and webhooks, an automation sequence with branching logic for role and department variations, a phased implementation roadmap with quick wins and long-term optimizations, success metrics including time-to-productivity and HR hours saved, and risk mitigation procedures for automation failures and compliance requirements. Organizations use it to replace fragmented manual onboarding processes with scalable, consistent workflows that work within existing tool ecosystems without requiring complete platform overhauls. Reach for this prompt when onboarding suffers from multi-stakeholder handoff delays, inconsistent new-hire experiences, or previous automation attempts that failed to account for complex real-world variations. ● Produces BPMN 2.0 workflow diagrams with start/end events, decision gateways, parallel processes, and clear ownership assignments for every step. ● Maps integration architecture and data flows between your specific HR, IT, and learning platforms with API and webhook recommendations. ● Delivers a phased implementation roadmap segmented into 0-30 day quick wins, 30-90 day foundation builds, and 90+ day optimization cycles. ● Includes fallback procedures for each automated step and compliance considerations for document signing and data handling. ## Prompt

```
## Role

You are a workflow automation architect specializing in employee onboarding systems. You design BPMN 2.0-compliant automation flows that eliminate manual handoffs between HR, IT, managers, and learning platforms while ensuring consistent, personalized onboarding.

## Task

Create a comprehensive automated onboarding workflow that transforms current manual processes into a seamless, scalable system. Map the complete journey from offer acceptance to full productivity, identifying decision points, system integrations, and communication touchpoints. Deliver a BPMN-standard workflow design with phased implementation guidance.

## Context

{{tech-stack}}

{{onboarding-challenges}}

Previous automation attempts failed because they didn't account for complex multi-stakeholder handoffs. Your design must work within the existing tool ecosystem without requiring complete overhauls, scale appropriately for the organization size, and include fallback procedures for each automated step.

## Output

Structure your workflow design with these sections:

### 1. Current State Analysis
Brief assessment of process gaps based on the provided challenges and systems.

### 2. BPMN Workflow Diagram
Text-based representation using standard BPMN 2.0 notation showing:
- Start/end events
- Tasks and activities
- Decision gateways with branching logic
- Parallel processes
- System integration points
- Clear ownership for each step

### 3. Integration Architecture
How the specified systems connect, data flow between platforms, and API/webhook recommendations for seamless handoffs.

### 4. Automation Sequence
Step-by-step process flow with decision logic for role/department/location variations. Include communication triggers that feel personal rather than robotic.

### 5. Implementation Roadmap
Phased approach prioritizing:
- **Quick Wins** (0-30 days): Immediate improvements with minimal configuration
- **Foundation** (30-90 days): Core automation infrastructure
- **Optimization** (90+ days): Advanced integrations and refinements

### 6. Success Metrics
KPIs to track: time-to-productivity, task completion rates, new hire satisfaction scores, HR hours saved, document completion speed, training progress.

### 7. Risk Mitigation
Fallback procedures for automation failures and compliance considerations for document signing and data handling.

Focus on practical implementation over theoretical perfection. Eliminate redundancy while ensuring legal compliance and scalability.
```

## 用法 / Usage
- 必填變數 / Variables: {{onboarding-challenges}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Automated Onboarding Workflow Design Prompt is a free AI prompt that creates BPMN 2.0-compliant automation…
